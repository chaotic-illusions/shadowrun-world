#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DB_PATH="$SCRIPT_DIR/data/shadowrun.db"

wait_for_server() {
  echo "Waiting for server to be ready..."
  local RETRIES=0
  until curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/docs | grep -q "200"; do
    sleep 2
    RETRIES=$((RETRIES + 1))
    if [ $RETRIES -ge 30 ]; then
      echo "ERROR: Server did not become ready after 60 seconds"
      exit 1
    fi
  done
}

do_restart() {
  echo ""
  echo "[1/2] Rebuilding and restarting container..."
  docker compose -f "$SCRIPT_DIR/docker-compose.yml" up --build -d
  wait_for_server
  echo ""
  echo "[2/2] Done. Server is running at http://localhost:8000"
  echo ""
}

do_reseed() {
  echo ""
  echo "[1/5] Stopping container..."
  docker compose -f "$SCRIPT_DIR/docker-compose.yml" down

  echo ""
  echo "[2/5] Deleting database..."
  if [ -f "$DB_PATH" ]; then
    rm -f "$DB_PATH"
    echo "Deleted $DB_PATH"
  else
    echo "No existing database found, skipping."
  fi

  echo ""
  echo "[3/5] Rebuilding and starting container..."
  docker compose -f "$SCRIPT_DIR/docker-compose.yml" up --build -d
  wait_for_server

  echo ""
  echo "[4/5] Reseeding database..."
  cd "$SCRIPT_DIR"
  docker compose -f "$SCRIPT_DIR/docker-compose.yml" exec shadowrun-world python3 seed.py

  echo ""
  echo "[5/5] Cleaning up __pycache__..."
  find "$SCRIPT_DIR" -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
  echo "Cleaned."

  echo ""
  echo "Done. Server is running at http://localhost:8000"
  echo ""
}

echo ""
echo " Shadowrun World Engine"
echo " ----------------------"
echo " 1. Restart container (pick up backend/Python changes)"
echo " 2. Full reseed + rebuild (wipes database)"
echo ""
read -rp " Select option (1 or 2): " CHOICE

case "$CHOICE" in
  1) do_restart ;;
  2) do_reseed ;;
  *)
    echo "Invalid option. Exiting."
    exit 1
    ;;
esac
