#!/bin/bash
# Sets kernel config options required for Docker for the Shadowrun World project.
# Single-container use case -- skips swarm, Kubernetes, overlay networks, IP_VS etc.
#
# Usage:  sudo bash docker-kernel-config.sh [/path/to/kernel/source]
# Default kernel source: /usr/src/linux (symlink to active source on Gentoo)
#
# After running, rebuild your kernel:
#   cd /usr/src/linux
#   make olddefconfig
#   make -j$(nproc)
#   make modules_install && make install
#   grub-mkconfig -o /boot/grub/grub.cfg   # or your bootloader equivalent

set -euo pipefail

KDIR="${1:-/usr/src/linux}"
CONFIG="${KDIR}/.config"
SCRIPTS_CONFIG="${KDIR}/scripts/config"

# -- Preflight checks ---------------------------------------------------------

if [[ $EUID -ne 0 ]]; then
  echo "ERROR: Run this script as root." >&2
  exit 1
fi

if [[ ! -f "$CONFIG" ]]; then
  echo "ERROR: Kernel config not found at ${CONFIG}" >&2
  echo "       Pass the kernel source directory as an argument, e.g.:" >&2
  echo "       sudo bash $0 /usr/src/linux-6.18.12-gentoo" >&2
  exit 1
fi

if [[ ! -x "$SCRIPTS_CONFIG" ]]; then
  echo "ERROR: scripts/config not found or not executable at ${SCRIPTS_CONFIG}" >&2
  exit 1
fi

echo "==> Kernel source: ${KDIR}"
echo "==> Config file:   ${CONFIG}"
echo ""

# -- Helper -------------------------------------------------------------------

CHANGED=0
ALREADY_SET=0
ERRORS=0

set_option() {
  local opt="$1"   # CONFIG_FOO
  local desc="$2"  # human description

  local before after

  # Read current state (may be =y, =m, is not set, or absent)
  before=$(grep -E "^(${opt}=|# ${opt} is not set)" "$CONFIG" || echo "absent")

  "${SCRIPTS_CONFIG}" --file "$CONFIG" --enable "$opt"

  after=$(grep -E "^${opt}=" "$CONFIG" || echo "absent")

  if [[ "$after" == "${opt}=y" ]]; then
    if echo "$before" | grep -q "^${opt}=y"; then
      echo "  [already y]  ${opt}  (${desc})"
      ((ALREADY_SET++)) || true
    else
      echo "  [SET   -> y] ${opt}  (${desc})"
      ((CHANGED++)) || true
    fi
  else
    echo "  [FAILED]     ${opt}  (${desc})  -- current: ${after}"
    ((ERRORS++)) || true
  fi
}

# Use set_module for options that MUST be loadable .ko files.
# iptables-legacy userspace calls modprobe by name -- =y (built-in) won't work.
set_module() {
  local opt="$1"
  local desc="$2"

  local before after

  before=$(grep -E "^(${opt}=|# ${opt} is not set)" "$CONFIG" || echo "absent")

  "${SCRIPTS_CONFIG}" --file "$CONFIG" --module "$opt"

  after=$(grep -E "^${opt}=" "$CONFIG" || echo "absent")

  if [[ "$after" == "${opt}=m" ]]; then
    if echo "$before" | grep -q "^${opt}=m"; then
      echo "  [already m]  ${opt}  (${desc})"
      ((ALREADY_SET++)) || true
    else
      echo "  [SET   -> m] ${opt}  (${desc})"
      ((CHANGED++)) || true
    fi
  else
    echo "  [FAILED]     ${opt}  (${desc})  -- current: ${after}"
    ((ERRORS++)) || true
  fi
}

# -- Generally Necessary (missing from your check-config output) ---------------

echo "--- cgroup controllers ---"
set_option CONFIG_CGROUP_DEVICE    "container device access control"
set_option CONFIG_MEMCG            "memory cgroup controller"
set_option CONFIG_CGROUP_BPF       "BPF programs attached to cgroups"

echo ""
echo "--- container networking ---"
set_option CONFIG_VETH             "virtual ethernet pairs (veth)"
set_option CONFIG_BRIDGE           "802.1d bridge"
set_option CONFIG_BRIDGE_NETFILTER "iptables/ip6tables over bridged traffic"

echo ""
echo "--- netfilter base ---"
set_option CONFIG_NETFILTER             "netfilter framework base"
# NF_CONNTRACK and XTABLES can be built-in; ip_tables.ko depends on them via Kconfig
set_option CONFIG_NETFILTER_XTABLES     "x_tables.ko base (xt_* match/target framework)"
set_option CONFIG_NF_CONNTRACK          "connection tracking"
set_option CONFIG_NF_NAT               "NAT core (nf_nat.ko)"

echo ""
echo "--- IPv4 netfilter (MUST be modules -- modprobe called by name at runtime) ---"
# Linux 6.x gates the entire legacy iptables path behind this flag.
# Without it, CONFIG_IP_NF_IPTABLES=m is ignored and ip_tables.ko never compiles.
set_option CONFIG_NETFILTER_XTABLES_LEGACY "enable legacy xtables path (required for ip_tables.ko)"
# CONFIG_IP_NF_IPTABLES builds ip_tables.ko -- this is what modprobe looks for
set_module CONFIG_IP_NF_IPTABLES         "ip_tables.ko (iptables-legacy core)"
set_module CONFIG_IP_NF_FILTER           "iptable_filter.ko"
set_module CONFIG_IP_NF_NAT             "iptable_nat.ko (Docker NAT chain lives here)"
set_module CONFIG_IP_NF_MANGLE           "iptable_mangle.ko"
set_module CONFIG_IP_NF_RAW              "iptable_raw.ko"
set_module CONFIG_IP_NF_TARGET_MASQUERADE "ipt_MASQUERADE.ko"

echo ""
echo "--- IPv6 netfilter ---"
set_module CONFIG_IP6_NF_IPTABLES         "ip6_tables.ko"
set_module CONFIG_IP6_NF_FILTER           "ip6table_filter.ko"
set_module CONFIG_IP6_NF_MANGLE           "ip6table_mangle.ko"
set_module CONFIG_IP6_NF_RAW              "ip6table_raw.ko"
set_module CONFIG_IP6_NF_NAT             "ip6table_nat.ko"
set_module CONFIG_IP6_NF_TARGET_MASQUERADE "ip6t_MASQUERADE.ko"

echo ""
echo "--- storage driver ---"
set_option CONFIG_OVERLAY_FS       "overlay filesystem (Docker default storage driver)"

echo ""
echo "--- pids cgroup (optional but useful) ---"
set_option CONFIG_CGROUP_PIDS      "pids cgroup controller"

# -- Summary -------------------------------------------------------------------

echo ""
echo "========================================"
echo "  Changed:     ${CHANGED}"
echo "  Already set: ${ALREADY_SET}"
echo "  Failed:      ${ERRORS}"
echo "========================================"

if [[ $ERRORS -gt 0 ]]; then
  echo ""
  echo "WARNING: ${ERRORS} option(s) could not be set."
  echo "These may depend on other options not yet enabled. Run 'make menuconfig'"
  echo "to find and enable their dependencies, then re-run this script."
fi

if [[ $CHANGED -gt 0 ]]; then
  echo ""
  echo "NEXT STEPS:"
  echo "  cd ${KDIR}"
  echo "  make olddefconfig        # resolve any new dependencies"
  echo "  make -j\$(nproc)         # compile"
  echo "  make modules_install && make install"
  echo "  grub-mkconfig -o /boot/grub/grub.cfg"
  echo ""
  echo "After rebooting into the new kernel, re-run check-config.sh to verify."
else
  echo ""
  echo "No changes needed -- all required options already enabled."
fi
