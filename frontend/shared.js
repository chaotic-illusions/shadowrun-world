// Shared UI helpers — included by world-state.html and manage-runs.html

// Heat tier → CSS class name
function heatClass(h) {
  if (h <= 0) return 'heat-neutral';
  if (h <= 2) return 'heat-noticed';
  if (h <= 4) return 'heat-flagged';
  if (h <= 6) return 'heat-wanted';
  if (h <= 8) return 'heat-hot';
  return 'heat-nova-hot';
}

// Heat tier → label string
function heatLabelStr(h) {
  if (h <= 0) return 'Neutral';
  if (h <= 2) return 'Noticed';
  if (h <= 4) return 'Flagged';
  if (h <= 6) return 'Wanted';
  if (h <= 8) return 'Hot';
  return 'Nova Hot';
}

// Heat tier → inline CSS color string (for dynamic styling)
function heatColorStyle(heat) {
  if (heat <= 0) return '';
  if (heat <= 2) return 'color:#cccc44;';
  if (heat <= 4) return 'color:#ffaa22;';
  if (heat <= 6) return 'color:#ff7700;';
  if (heat <= 8) return 'color:#ff4422;';
  return 'color:#ff1111;text-shadow:0 0 8px #ff111188;';
}

// Net rep (0–40, neutral=20) → inline CSS color string
function repColorStyle(net_rep) {
  const delta = net_rep - 20;
  if (delta === 0) return '';
  if (delta > 0) {
    const pct = Math.min(1, delta / 20);
    const g = Math.round(160 + 95 * pct);
    return `color:rgba(0,${g},65,${0.7 + 0.3 * pct});`;
  } else {
    const pct = Math.min(1, Math.abs(delta) / 20);
    const opacity = 0.5 + 0.5 * pct;
    return `color:rgba(255,${Math.round(51 * (1 - pct))},${Math.round(51 * (1 - pct))},${opacity});`;
  }
}
