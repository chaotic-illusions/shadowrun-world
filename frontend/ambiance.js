/* =====================================================================
   ambiance.js -- shared canvas ambiance engine for Shadowrun World Engine.

   One module, many scenes. A page opts in with two lines before </body>:

       <script src="ambiance.js"></script>
       <script>Ambiance.start('corp');</script>

   The module self-injects the canvas (plus optional sky + vignette layers
   and the FX toggle chip) and the CSS it needs, runs a throttled (~60fps)
   render loop, honours prefers-reduced-motion, and persists the on/off
   choice (localStorage key sr_wsfx, shared with the original world-state
   toggle). Scenes register their own init/resize/frame; shared draw helpers
   (skyline, heat glow, twinkle) live here so multiple pages reuse them.

   The world-state skyline (#ambScene) and the deck-workshop (#fxPackets)
   effects have been migrated into this engine as the cityscape and deckgrid
   scenes; the corp scene reuses the same shared skyline renderer.
   ===================================================================== */
(function (global) {
  'use strict';

  // -- math + colour helpers ---------------------------------------------
  function lerp(a, b, t) { return a + (b - a) * t; }
  function mix(c1, c2, t) {
    return [lerp(c1[0], c2[0], t), lerp(c1[1], c2[1], t), lerp(c1[2], c2[2], t)];
  }
  function rgb(c) { return Math.round(c[0]) + ',' + Math.round(c[1]) + ',' + Math.round(c[2]); }

  // -- scene registry -----------------------------------------------------
  var scenes = {};
  function scene(name, def) { scenes[name] = def; }

  // -- shared CSS (injected once) ----------------------------------------
  function injectCss() {
    if (document.getElementById('amb-css')) return;
    var s = document.createElement('style');
    s.id = 'amb-css';
    s.textContent = [
      '.amb-sky{position:fixed;inset:0;z-index:-2;pointer-events:none;}',
      '#ambScene{position:fixed;inset:0;z-index:-1;pointer-events:none;}',
      '.amb-vig{position:fixed;inset:0;z-index:-1;pointer-events:none;',
      'background:radial-gradient(120% 82% at 50% 2%,transparent 56%,rgba(0,0,0,.55) 100%);}',
      'body.no-amb .amb-sky,body.no-amb #ambScene,body.no-amb .amb-vig{display:none;}',
      '#wsFxToggle{position:fixed;left:14px;bottom:12px;z-index:200;font-family:var(--font);',
      'font-size:0.6rem;letter-spacing:2px;color:var(--green-dim);background:#070707;',
      'border:1px solid var(--green-dark);padding:5px 10px;cursor:pointer;text-transform:uppercase;',
      'opacity:.55;transition:opacity .2s;}',
      '#wsFxToggle:hover{opacity:1;}',
      '#wsFxToggle.off{color:var(--text-dim);border-color:#222;}'
    ].join('');
    document.head.appendChild(s);
  }

  // -- shared draw helper: a parallax building skyline (offscreen) --------
  // Draws faceless towers across the full width into ctx `g`, returning the
  // lit-window coordinates so a scene can twinkle them. Palette via opts.
  function drawBuildings(g, W, H, o) {
    o = o || {};
    var fill = o.fill || '#080d12';
    var edge = o.edge || 'rgba(0,75,100,0.30)';
    var winRGB = o.winRGB || '255,200,130';
    var winChance = (o.winChance == null) ? 0.42 : o.winChance;
    var minH = (o.minH == null) ? 0.15 : o.minH;
    var varH = (o.varH == null) ? 0.27 : o.varH;
    var coords = [];
    var x = -20;
    while (x < W + 20) {
      var bw = 40 + Math.random() * 95;
      var bh = (minH + Math.random() * varH) * H;
      var bx = x, by = H - bh;
      g.fillStyle = fill;
      g.fillRect(bx, by, bw, bh);
      g.fillStyle = edge;
      g.fillRect(bx, by, bw, 1.5);
      for (var wy = by + 8; wy < H - 5; wy += 9) {
        for (var wx = bx + 6; wx < bx + bw - 4; wx += 8) {
          if (Math.random() < winChance) {
            g.fillStyle = 'rgba(' + winRGB + ',' + (0.12 + Math.random() * 0.32).toFixed(3) + ')';
            g.fillRect(wx, wy, 3, 3);
            coords.push([wx, wy]);
          }
        }
      }
      x += bw + 5 + Math.random() * 28;
    }
    return coords;
  }

  // -- shared draw helper: the Aztechnology pyramid ----------------------
  // A black-glass step-pyramid seen corner-on (front ridge facing the
  // viewer). Lit tier windows + glowing edges baked into the offscreen
  // bitmap; returns the apex point so the live loop can pulse a beacon.
  function drawPyramid(g, cx, baseY, h, heatT) {
    var apexY = baseY - h;
    var halfW = h * 0.64;                 // base half-width
    var leftX = cx - halfW, rightX = cx + halfW;
    var ridgeDip = function (frac) { return (halfW * frac) * 0.14; };  // front corner dips toward us
    var hot = Math.max(0, Math.min(1, heatT));   // Aztechnology teal at rest -> warning red when hot

    // faint backlight + ground bleed so the mass reads against the night.
    // The radial glow reaches r=0.9h around a centre at apexY+0.4h, so its top
    // edge is apexY-0.5h. The fill rect MUST start at/above that (here
    // apexY-0.55h) or the gradient gets clipped while still ~10% opaque and
    // bakes a hard horizontal line above the pyramid (the cut-off bug). Keep
    // the rect bounds and the gradient radius in sync.
    var haloC = mix([0, 128, 128], [182, 44, 24], hot);
    var halo = g.createRadialGradient(cx, apexY + h * 0.4, h * 0.05, cx, apexY + h * 0.4, h * 0.9);
    halo.addColorStop(0, 'rgba(' + rgb(haloC) + ',0.12)');
    halo.addColorStop(1, 'rgba(' + rgb(haloC) + ',0)');
    g.fillStyle = halo;
    g.fillRect(cx - h, apexY - h * 0.55, h * 2, h * 1.9);

    // two glass faces meeting at the front ridge (cx). Dark teal glass, left darker.
    g.fillStyle = '#061414';
    g.beginPath();
    g.moveTo(cx, apexY); g.lineTo(leftX, baseY); g.lineTo(cx, baseY + ridgeDip(1)); g.closePath(); g.fill();
    g.fillStyle = '#0a2020';
    g.beginPath();
    g.moveTo(cx, apexY); g.lineTo(rightX, baseY); g.lineTo(cx, baseY + ridgeDip(1)); g.closePath(); g.fill();

    // window colour eases teal -> blood-red with heat
    var winR = mix([64, 208, 208], [255, 78, 50], hot);
    var wc = 'rgba(' + rgb(winR) + ',';
    var tiers = 13;
    for (var i = 1; i < tiers; i++) {
      var f = i / tiers;                  // 0 (apex) -> 1 (base)
      var ty = apexY + (baseY - apexY) * f;
      var tHalf = halfW * f;
      var dip = ridgeDip(f);
      // tier shadow groove (chevron: side -> dipped ridge -> side)
      g.strokeStyle = 'rgba(0,0,0,0.45)'; g.lineWidth = 1;
      g.beginPath();
      g.moveTo(cx - tHalf, ty); g.lineTo(cx, ty + dip); g.lineTo(cx + tHalf, ty);
      g.stroke();
      // lit windows scattered along the tier
      var rowY = ty - 3;
      for (var k = -tHalf + 7; k < tHalf - 4; k += 11) {
        if (Math.random() < 0.5) continue;
        var t01 = (k + tHalf) / (2 * tHalf);
        var wyy = rowY + dip * Math.sin(t01 * Math.PI);   // ride the chevron
        g.fillStyle = wc + (0.34 + Math.random() * 0.4).toFixed(3) + ')';
        g.fillRect(cx + k, wyy, 2, 3);
      }
    }

    // glowing edges (left edge, right edge, front ridge) -- baked once.
    var edgeC = mix([0, 160, 160], [255, 100, 52], hot);
    var edgeS = mix([96, 224, 224], [255, 150, 96], hot);
    g.shadowColor = 'rgba(' + rgb(edgeC) + ',0.72)'; g.shadowBlur = 5;
    g.strokeStyle = 'rgba(' + rgb(edgeS) + ',0.68)'; g.lineWidth = 1.8;
    g.beginPath();
    g.moveTo(cx, apexY); g.lineTo(leftX, baseY);
    g.moveTo(cx, apexY); g.lineTo(rightX, baseY);
    g.stroke();
    g.strokeStyle = 'rgba(' + rgb(edgeS) + ',0.56)'; g.lineWidth = 1.6;
    g.beginPath();
    g.moveTo(cx, apexY); g.lineTo(cx, baseY + ridgeDip(1));
    g.stroke();
    g.shadowBlur = 0;

    // corporate signage: AZTECHNOLOGY climbing the right face, parallel to the
    // right edge and inset onto the glass so it reads as painted-on neon.
    drawPyramidSign(g, cx, apexY, rightX, baseY, h, heatT);

    return { x: cx, y: apexY };
  }

  // -- AZTECHNOLOGY wordmark running up the pyramid's right face ----------
  // Uses the app's themed display font ('Shadowrun') and stays teal #008080 so
  // it reads as the corp wordmark regardless of party heat.
  function drawPyramidSign(g, ax, ay, bx, by, h, heatT) {
    var word = 'AZTECHNOLOGY';
    var ex = bx - ax, ey = by - ay;              // apex -> right base corner
    var elen = Math.sqrt(ex * ex + ey * ey);
    if (elen < 40) return;
    var ux = ex / elen, uy = ey / elen;          // unit vector, downhill to base
    var nx = -uy, ny = ux;                        // inward normal (onto the face)
    var inset = h * 0.078;
    var ang = Math.atan2(uy, ux);
    g.save();
    g.translate(ax + nx * inset, ay + ny * inset);
    g.rotate(ang);
    var fs = Math.round(h * 0.058);
    g.font = '700 ' + fs + "px 'Shadowrun', 'Share Tech Mono', monospace";
    g.textAlign = 'center';
    g.textBaseline = 'middle';
    var t0 = elen * 0.15, t1 = elen * 0.93;       // span most of the edge
    var n = word.length;
    // neon-tube look: a saturated-teal bloom built up over several blur passes,
    // finished with a near-white hot core so the letters glow like lit glass.
    // Stays teal regardless of party heat (the wordmark never reddens).
    g.shadowColor = 'rgba(0,224,224,0.95)';
    function neonPass(blur, fill) {
      g.shadowBlur = blur;
      g.fillStyle = fill;
      for (var i = 0; i < n; i++) {
        var lx = t0 + (n > 1 ? (i / (n - 1)) : 0) * (t1 - t0);
        g.fillText(word.charAt(i), lx, 0);
      }
    }
    neonPass(fs * 0.95, 'rgba(0,190,190,0.75)');   // wide outer halo
    neonPass(fs * 0.55, 'rgba(40,224,224,0.90)');  // mid bloom
    neonPass(fs * 0.26, 'rgba(150,255,255,1)');    // bright inner edge
    neonPass(fs * 0.12, 'rgba(228,255,255,1)');    // near-white tube core
    g.restore();
    g.shadowBlur = 0;
  }

  // -- shared draw helper: ambient window twinkle ------------------------
  // A few lights ease on/off across the supplied coords. State is kept on
  // env.store so a scene just calls twinkle(env, coords, rgbStr, dt).
  function twinkle(env, coords, rgbStr, dt) {
    if (!coords || !coords.length) return;
    var st = env.store;
    if (!st._tw) { st._tw = []; st._twSpawn = 0; }
    st._twSpawn -= dt;
    if (st._twSpawn <= 0) {
      var w = coords[(Math.random() * coords.length) | 0];
      st._tw.push({ x: w[0], y: w[1], t: 0, dur: 0.9 + Math.random() * 1.4, dim: Math.random() < 0.5 });
      st._twSpawn = 0.18 + Math.random() * 0.35;
    }
    var ctx = env.ctx;
    for (var i = st._tw.length - 1; i >= 0; i--) {
      var tw = st._tw[i]; tw.t += dt;
      if (tw.t >= tw.dur) { st._tw.splice(i, 1); continue; }
      var k = Math.sin((tw.t / tw.dur) * Math.PI);
      ctx.fillStyle = tw.dim
        ? 'rgba(0,0,0,' + (0.42 * k).toFixed(3) + ')'
        : 'rgba(' + rgbStr + ',' + (0.5 * k).toFixed(3) + ')';
      ctx.fillRect(tw.x, tw.y, 3, 3);
    }
  }

  // =====================================================================
  // SCENE: corp -- Aztechnology pyramid over a cold corp-tower skyline
  // =====================================================================
  // corp scene paints the skyline + pyramid into an offscreen bitmap (baked
  // once per resize, and again when the display font finishes loading so the
  // AZTECHNOLOGY wordmark renders in 'Shadowrun' rather than the fallback).
  function corp_paint(env) {
    var W = env.W, H = env.H, st = env.store, g = st.sctx;
    st.sky.width = W; st.sky.height = H;
    g.clearRect(0, 0, W, H);
    // muted, faceless corp towers so the amber pyramid reads as the hero
    st.coords = drawBuildings(g, W, H, {
      fill: '#0c0a08', edge: 'rgba(120,98,64,0.24)',
      winRGB: '224,196,150', winChance: 0.34, minH: 0.12, varH: 0.26
    });
    // hero: the pyramid, anchored into the RIGHT margin beside the table.
    // SAMPLE (taller variant): the top now reaches 50% of the view height. The
    // horizontal CENTRE is deliberately kept where the shorter 0.26 build put it
    // (anchorHalf still uses 0.26), so the pyramid does NOT shift left as it
    // grows -- instead its wider right side runs off the right edge of the
    // screen, which is acceptable here. Drawn SOLID (no globalAlpha) so the
    // towers never show through it.
    var pyH = H * 0.50;                         // top at 50% of view height (from bottom)
    var anchorHalf = (H * 0.26) * 0.64;         // keep the SAME centre x as the 0.26 build
    var pyCx = Math.max(W * 0.55, W - anchorHalf - 16);
    st.apex = drawPyramid(g, pyCx, H, pyH, env.heatT);
  }
  // always-on turquoise city-glow rising from the horizon so the upper sky
  // never reads as a dead black void above the pyramid (cached per size).
  function corp_haze(env) {
    var ctx = env.ctx, W = env.W, H = env.H, st = env.store, key = W + 'x' + H;
    if (!st.haze || st.hazeKey !== key) {
      // warm amber city-glow that keeps a faint wash all the way to the top
      // (top stop stays > 0) so the upper sky never reads as a dead black band
      var grd = ctx.createLinearGradient(0, H, 0, 0);
      grd.addColorStop(0.00, 'rgba(102,66,28,0.32)');
      grd.addColorStop(0.32, 'rgba(82,52,24,0.20)');
      grd.addColorStop(0.64, 'rgba(58,40,22,0.10)');
      grd.addColorStop(1.00, 'rgba(38,28,18,0.035)');
      st.haze = grd; st.hazeKey = key;
    }
    ctx.fillStyle = st.haze; ctx.fillRect(0, 0, W, H);
  }
  scene('corp', {
    sky: 'linear-gradient(180deg,#0b0805 0%,#0e0a07 52%,#14100a 100%)',
    vignette: true,
    heat: true,
    init: function (env) {
      var st = env.store;
      st.sky = document.createElement('canvas');
      st.sctx = st.sky.getContext('2d');
      st.craft = []; st.spawnIn = 2.0;          // drifting aircraft (reuses ws_drawCraft)
      st.drops = []; st.speckles = [];          // rainy-Seattle theme (reuses ws_drawRain)
      // re-bake once the display font is ready so AZTECHNOLOGY uses it
      if (global.document && document.fonts && document.fonts.load) {
        document.fonts.load("700 40px 'Shadowrun'").then(function () {
          if (st._env) corp_paint(st._env);
        }).catch(function () {});
      }
    },
    resize: function (env) {
      env.store._env = env; corp_paint(env);
      ws_buildRain(env);
      ws_buildBokeh(env, [[255, 196, 140], [120, 200, 210], [255, 150, 90]]);
    },
    frame: function (env, t, dt) {
      var ctx = env.ctx, W = env.W, H = env.H, st = env.store;
      ctx.clearRect(0, 0, W, H);
      corp_haze(env);
      // horizon light-pollution: amber at rest, washing red as heat climbs
      env.heatGlow([[60, 40, 18], [92, 46, 18], [104, 22, 16]]);
      ctx.drawImage(st.sky, 0, 0);
      twinkle(env, st.coords, '224,196,150', dt);
      ws_drawCraft(env, dt);                     // aircraft + police lightbars, like world-state
      // pulsing apex beacon: teal at rest -> red warning when hot
      if (st.apex) {
        var a = st.apex, pulse = 0.5 + 0.5 * Math.sin(t / 420);
        var bc = mix([64, 216, 216], [255, 40, 36], env.heatT);
        ctx.fillStyle = 'rgba(' + rgb(bc) + ',0.82)';
        ctx.shadowColor = 'rgb(' + rgb(bc) + ')'; ctx.shadowBlur = 6 + 6 * pulse;
        ctx.fillRect(a.x - 1.5, a.y - 1.5, 3, 3);
        ctx.shadowBlur = 0;
      }
      ws_drawBokeh(env, t, dt);                  // soft wet-lens light blooms
      ws_drawRain(env, dt);                      // rainy-Seattle streaks, in front
    }
  });

  // =====================================================================
  // SCENE: cityscape -- rain-streaked Seattle sprawl (the world-state look)
  // Ported from world-state.html so the flagship ambiance lives in one place.
  // =====================================================================
  function ws_sampleWin(st, x, y) {
    // reservoir sample so the twinkle pool is even across the whole skyline
    st.winSeen++;
    if (st.winCoords.length < 600) { st.winCoords.push([x, y]); return; }
    var j = (Math.random() * st.winSeen) | 0;
    if (j < 600) st.winCoords[j] = [x, y];
  }
  function ws_paintNeedle(env, cx, baseY, s) {
    var g = env.store.sctx, st = env.store;
    var sil = '#0f1822';
    // Render the Space Needle as a hardcoded wireframe silhouette (traced from
    // an approved SVG, now inlined as the PX/PY path coords below) in the
    // world-state style: dark fill + cyan edge glow + lit window bands +
    // red beacon. The needle spans y 22..986 in a 300-wide viewBox; PX/PY
    // map those coords into canvas space, preserving the SVG aspect ratio.
    var SVG_BOT = 986, SVG_SPAN = 964;          // 986 - 22 (beacon to ground)
    var k = s / SVG_SPAN;                        // SVG-unit -> px
    function PX(x) { return cx + (x - 150) * k; }
    function PY(y) { return baseY - (SVG_BOT - y) * k; }
    var spireTopY = PY(22);                      // antenna tip (red light)

    // soft turquoise back-glow behind the tophouse
    var glowY = PY(171);
    var bg = g.createRadialGradient(cx, glowY, s * 0.02, cx, glowY, s * 0.30);
    bg.addColorStop(0, 'rgba(35,110,140,0.30)');
    bg.addColorStop(1, 'rgba(35,110,140,0)');
    g.fillStyle = bg; g.fillRect(cx - s * 0.30, glowY - s * 0.30, s * 0.60, s * 0.60);

    g.fillStyle = sil;

    // central elevator core (reads as the third leg up the middle)
    g.beginPath();
    g.moveTo(PX(145), PY(204)); g.lineTo(PX(155), PY(204));
    g.lineTo(PX(153), PY(950)); g.lineTo(PX(147), PY(950));
    g.closePath(); g.fill();

    // two wineglass legs: wide at the base, pinched to a high waist (~75% up)
    // where they nearly meet the core, then flared back out to the saucer.
    g.beginPath();
    g.moveTo(PX(124), PY(206));
    g.bezierCurveTo(PX(126), PY(290), PX(131), PY(340), PX(131), PY(394));
    g.bezierCurveTo(PX(131), PY(490), PX(95), PY(870), PX(66), PY(956));
    g.lineTo(PX(78), PY(956));
    g.bezierCurveTo(PX(107), PY(870), PX(143), PY(490), PX(143), PY(394));
    g.bezierCurveTo(PX(143), PY(340), PX(138), PY(290), PX(136), PY(206));
    g.closePath(); g.fill();
    g.beginPath();
    g.moveTo(PX(176), PY(206));
    g.bezierCurveTo(PX(174), PY(290), PX(169), PY(340), PX(169), PY(394));
    g.bezierCurveTo(PX(169), PY(490), PX(205), PY(870), PX(234), PY(956));
    g.lineTo(PX(222), PY(956));
    g.bezierCurveTo(PX(193), PY(870), PX(157), PY(490), PX(157), PY(394));
    g.bezierCurveTo(PX(157), PY(340), PX(162), PY(290), PX(164), PY(206));
    g.closePath(); g.fill();

    // splayed feet to the ground
    g.beginPath();
    g.moveTo(PX(66), PY(956)); g.lineTo(PX(62), PY(986));
    g.lineTo(PX(80), PY(986)); g.lineTo(PX(78), PY(956));
    g.closePath(); g.fill();
    g.beginPath();
    g.moveTo(PX(234), PY(956)); g.lineTo(PX(238), PY(986));
    g.lineTo(PX(220), PY(986)); g.lineTo(PX(222), PY(956));
    g.closePath(); g.fill();

    // tophouse silhouette: pedestal + straight roof + upper windows +
    // overhanging pancake + lower windows + vaned neck
    g.beginPath();
    g.moveTo(PX(135), PY(120));
    g.lineTo(PX(165), PY(120)); g.lineTo(PX(165), PY(131));
    g.lineTo(PX(215), PY(147)); g.lineTo(PX(215), PY(163));
    g.lineTo(PX(234), PY(166)); g.lineTo(PX(234), PY(177));
    g.lineTo(PX(215), PY(180)); g.lineTo(PX(215), PY(196));
    g.lineTo(PX(169), PY(204)); g.lineTo(PX(131), PY(204));
    g.lineTo(PX(85), PY(196)); g.lineTo(PX(85), PY(180));
    g.lineTo(PX(66), PY(177)); g.lineTo(PX(66), PY(166));
    g.lineTo(PX(85), PY(163)); g.lineTo(PX(85), PY(147));
    g.lineTo(PX(135), PY(131));
    g.closePath(); g.fill();

    // antenna mast
    var mastW = Math.max(1, k * 2);
    g.fillRect(cx - mastW / 2, PY(26), mastW, PY(120) - PY(26));

    // cyan edge highlights: leg outlines, core sides, antenna, and the full
    // tophouse outline (pedestal + roof + window-band sides + pancake + vanes)
    // so the saucer reads as wireframe structure, not just floating windows.
    g.strokeStyle = 'rgba(95,185,220,0.72)'; g.lineWidth = Math.max(1, k * 1.3);
    g.shadowColor = 'rgba(90,200,235,0.6)'; g.shadowBlur = 4;
    g.beginPath();
    g.moveTo(PX(124), PY(206));
    g.bezierCurveTo(PX(126), PY(290), PX(131), PY(340), PX(131), PY(394));
    g.bezierCurveTo(PX(131), PY(490), PX(95), PY(870), PX(66), PY(956));
    g.moveTo(PX(176), PY(206));
    g.bezierCurveTo(PX(174), PY(290), PX(169), PY(340), PX(169), PY(394));
    g.bezierCurveTo(PX(169), PY(490), PX(205), PY(870), PX(234), PY(956));
    g.moveTo(PX(145), PY(204)); g.lineTo(PX(147), PY(950));
    g.moveTo(PX(155), PY(204)); g.lineTo(PX(153), PY(950));
    g.moveTo(cx, PY(120)); g.lineTo(cx, PY(26));
    // tophouse outer silhouette (pedestal -> roof -> upper win -> pancake ->
    // lower win -> vanes -> neck and back up the left side)
    g.moveTo(PX(135), PY(120));
    g.lineTo(PX(165), PY(120)); g.lineTo(PX(165), PY(131));
    g.lineTo(PX(215), PY(147)); g.lineTo(PX(215), PY(163));
    g.lineTo(PX(234), PY(166)); g.lineTo(PX(234), PY(177));
    g.lineTo(PX(215), PY(180)); g.lineTo(PX(215), PY(196));
    g.lineTo(PX(169), PY(204)); g.lineTo(PX(131), PY(204));
    g.lineTo(PX(85), PY(196)); g.lineTo(PX(85), PY(180));
    g.lineTo(PX(66), PY(177)); g.lineTo(PX(66), PY(166));
    g.lineTo(PX(85), PY(163)); g.lineTo(PX(85), PY(147));
    g.lineTo(PX(135), PY(131)); g.closePath();
    // horizontal sills bounding the two window bands (separate them from the
    // roof, pancake and vanes)
    g.moveTo(PX(85), PY(147)); g.lineTo(PX(215), PY(147));
    g.moveTo(PX(85), PY(163)); g.lineTo(PX(215), PY(163));
    g.moveTo(PX(85), PY(180)); g.lineTo(PX(215), PY(180));
    g.moveTo(PX(85), PY(196)); g.lineTo(PX(215), PY(196));
    g.stroke();

    // bright lit edge on the pancake (the saucer's signature glow)
    g.strokeStyle = 'rgba(120,215,245,0.88)'; g.lineWidth = Math.max(1.2, k * 1.6);
    g.shadowColor = 'rgba(90,200,235,0.9)'; g.shadowBlur = 6;
    g.beginPath();
    g.moveTo(PX(85), PY(163)); g.lineTo(PX(66), PY(166));
    g.lineTo(PX(66), PY(177)); g.lineTo(PX(85), PY(180));
    g.moveTo(PX(215), PY(163)); g.lineTo(PX(234), PY(166));
    g.lineTo(PX(234), PY(177)); g.lineTo(PX(215), PY(180));
    g.stroke();
    g.shadowBlur = 0;

    // lit windows on both bands -- 7 individual panes per band (matches the
    // SVG's 7 window slots), sized well inside each band so the panes sit
    // cleanly within the SVG window rectangle, with clear dark gaps to the
    // roof / pancake / vanes above and below.
    var wc = 'rgba(' + Math.round(st.winWarm[0]) + ',' + Math.round(st.winWarm[1]) + ',' + Math.round(st.winWarm[2]) + ',';
    var winSlots = 7, winLo = 85, winHi = 215, slotW = (winHi - winLo) / winSlots;
    var paneW = slotW * 0.46;                      // pane width < slot -> side separation
    var paneWpx = Math.max(1.2, paneW * k);
    var bands = [[147, 163], [180, 196]];
    for (var b = 0; b < bands.length; b++) {
      var cyc = (bands[b][0] + bands[b][1]) * 0.5;       // band centre (SVG y)
      var halfH = (bands[b][1] - bands[b][0]) * 0.25;    // pane height = 50% of band, centred
      var wTop = PY(cyc - halfH), wH = PY(cyc + halfH) - wTop;
      for (var i = 0; i < winSlots; i++) {
        var wx = PX(winLo + (i + 0.5) * slotW - paneW * 0.5);
        g.fillStyle = wc + (0.5 + Math.random() * 0.5).toFixed(3) + ')';
        g.fillRect(wx, wTop, paneWpx, wH);
        ws_sampleWin(st, wx, wTop);
      }
    }

    // red aircraft-warning light at the antenna tip
    g.shadowColor = '#ff2828'; g.shadowBlur = 9;
    g.fillStyle = 'rgba(255,60,60,0.95)';
    var rb = Math.max(2, k * 3);
    g.fillRect(cx - rb / 2, spireTopY - rb / 2, rb, rb);
    g.shadowBlur = 0;
  }
  function ws_buildSkyline(env) {
    var W = env.W, H = env.H, st = env.store, sctx = st.sctx;
    st.sky.width = W; st.sky.height = H; st.winCoords = []; st.winSeen = 0;
    sctx.clearRect(0, 0, W, H);
    st.winWarm = mix([255, 200, 130], [255, 95, 60], env.heatT * 0.5);
    var wcs = 'rgba(' + Math.round(st.winWarm[0]) + ',' + Math.round(st.winWarm[1]) + ',' + Math.round(st.winWarm[2]) + ',';
    var x = -20;
    while (x < W + 20) {
      var bw = 40 + Math.random() * 95;
      var bh = (0.15 + Math.random() * 0.27) * H;
      var bx = x, by = H - bh;
      sctx.fillStyle = '#080d12';
      sctx.fillRect(bx, by, bw, bh);
      sctx.fillStyle = 'rgba(0,75,100,0.30)';
      sctx.fillRect(bx, by, bw, 1.5);
      for (var wy = by + 8; wy < H - 5; wy += 9) {
        for (var wx = bx + 6; wx < bx + bw - 4; wx += 8) {
          if (Math.random() < 0.42) {
            sctx.fillStyle = wcs + (0.12 + Math.random() * 0.32).toFixed(3) + ')';
            sctx.fillRect(wx, wy, 3, 3);
            ws_sampleWin(st, wx, wy);
          }
        }
      }
      x += bw + 5 + Math.random() * 28;
    }
    // Push the needle down by the un-outlined base height (the feet span SVG
    // y956..986 = 30 units, drawn fill-only) so the outlined leg bases sit at
    // the bottom edge and the un-outlined feet fall just below it.
    var _nS = H * 0.60;
    ws_paintNeedle(env, W * 0.87, H + _nS / 964 * 30, _nS);
  }
  function ws_newDrop(env, seed) {
    var W = env.W, H = env.H;
    return { x: Math.random() * (W + 60) - 30, y: seed ? Math.random() * H : -20,
      len: 8 + Math.random() * 16, spd: 470 + Math.random() * 470, a: 0.06 + Math.random() * 0.15 };
  }
  function ws_buildRain(env) {
    var W = env.W, H = env.H, st = env.store;
    st.drops = []; st.speckles = [];
    var n = Math.min(110, Math.round(W / 14));
    for (var i = 0; i < n; i++) st.drops.push(ws_newDrop(env, true));
    var sn = Math.min(24, Math.round(W / 75));
    for (var j = 0; j < sn; j++) st.speckles.push({ x: Math.random() * W, y: Math.random() * H,
      r: 1 + Math.random() * 2.1, slide: 5 + Math.random() * 15, vy: 0 });
  }
  function ws_drawCraft(env, dt) {
    var ctx = env.ctx, W = env.W, H = env.H, st = env.store, heatT = env.heatT;
    st.spawnIn -= dt;
    if (st.spawnIn <= 0) {
      var dir = Math.random() < 0.5 ? 1 : -1;
      st.craft.push({ dir: dir, x: dir > 0 ? -20 : W + 20, y: (0.13 + Math.random() * 0.44) * H,
        spd: 40 + Math.random() * 60, blink: Math.random(), police: Math.random() < (0.04 + heatT * 0.5),
        nav: Math.random() < 0.5 });
      st.spawnIn = lerp(4.5, 1.5, heatT) + Math.random() * lerp(5, 2, heatT);
    }
    for (var i = st.craft.length - 1; i >= 0; i--) {
      var c = st.craft[i];
      c.x += c.dir * c.spd * dt; c.blink += dt;
      ctx.fillStyle = 'rgba(20,26,32,0.65)';
      ctx.fillRect(c.x - 2, c.y - 1, 4, 2);
      var phase = (c.blink % 1) < 0.5;
      if (c.police) {
        ctx.fillStyle = phase ? 'rgba(255,40,40,0.95)' : 'rgba(50,95,255,0.95)';
        ctx.shadowColor = phase ? '#ff2828' : '#3060ff'; ctx.shadowBlur = 9;
        ctx.fillRect(c.x - 1, c.y - 1, 2, 2); ctx.shadowBlur = 0;
      } else if (phase) {
        ctx.fillStyle = c.nav ? 'rgba(255,60,60,0.9)' : 'rgba(60,255,90,0.9)';
        ctx.shadowColor = c.nav ? '#ff3030' : '#30ff50'; ctx.shadowBlur = 6;
        ctx.fillRect(c.x + (c.dir > 0 ? 2 : -3), c.y - 0.5, 1.5, 1.5); ctx.shadowBlur = 0;
      }
      if (c.x < -30 || c.x > W + 30) st.craft.splice(i, 1);
    }
  }
  function ws_drawRain(env, dt) {
    var ctx = env.ctx, W = env.W, H = env.H, st = env.store, heatT = env.heatT;
    var wind = lerp(26, 60, heatT), ang = wind / 600;
    ctx.lineWidth = 1;
    ctx.strokeStyle = 'rgba(175,215,255,0.13)';
    ctx.beginPath();
    for (var i = 0; i < st.drops.length; i++) {
      var d = st.drops[i];
      d.y += d.spd * dt; d.x += wind * dt;
      if (d.y > H + 20) { st.drops[i] = ws_newDrop(env, false); continue; }
      ctx.moveTo(d.x, d.y); ctx.lineTo(d.x - ang * d.len, d.y - d.len);
    }
    ctx.stroke();
    for (var s = 0; s < st.speckles.length; s++) {
      var p = st.speckles[s];
      p.slide -= dt;
      if (p.slide <= 0) {
        p.vy += 150 * dt; p.y += p.vy * dt;
        ctx.strokeStyle = 'rgba(160,205,255,0.09)'; ctx.lineWidth = p.r * 0.7;
        ctx.beginPath(); ctx.moveTo(p.x, p.y - p.r * 3); ctx.lineTo(p.x, p.y); ctx.stroke();
        ctx.lineWidth = 1;
        if (p.y > H + 6) { p.x = Math.random() * W; p.y = -4; p.vy = 0; p.slide = 6 + Math.random() * 16; }
      }
      ctx.fillStyle = 'rgba(190,220,255,0.15)';
      ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
    }
  }
  // Out-of-focus "bokeh" haze clouds: a few large, soft, slow-drifting light
  // blooms (additive, very low alpha) that read as wet-lens atmosphere behind
  // the rain. cols is a list of [r,g,b] tints to scatter through.
  function ws_buildBokeh(env, cols) {
    var W = env.W, H = env.H, st = env.store;
    st.bokeh = [];
    st.bokehCols = cols || [[120, 180, 255], [90, 210, 230], [255, 200, 140]];
    var n = Math.min(9, Math.max(5, Math.round(W / 240)));
    for (var i = 0; i < n; i++) {
      st.bokeh.push({
        x: Math.random() * W, y: Math.random() * H * 0.8,
        r: 38 + Math.random() * 92,
        col: st.bokehCols[(Math.random() * st.bokehCols.length) | 0],
        vx: (Math.random() - 0.5) * 7, vy: (Math.random() - 0.5) * 4.5,
        ph: Math.random() * 6.2832, base: 0.035 + Math.random() * 0.05
      });
    }
  }
  function ws_drawBokeh(env, t, dt) {
    var ctx = env.ctx, W = env.W, H = env.H, st = env.store;
    if (!st.bokeh) return;
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    for (var i = 0; i < st.bokeh.length; i++) {
      var b = st.bokeh[i];
      b.x += b.vx * dt; b.y += b.vy * dt;
      if (b.x < -b.r) b.x = W + b.r; else if (b.x > W + b.r) b.x = -b.r;
      if (b.y < -b.r) b.y = H + b.r; else if (b.y > H + b.r) b.y = -b.r;
      var a = b.base * (0.55 + 0.45 * Math.sin(t * 0.0006 + b.ph));
      if (a < 0.002) continue;
      var g = ctx.createRadialGradient(b.x, b.y, 0, b.x, b.y, b.r);
      g.addColorStop(0, 'rgba(' + rgb(b.col) + ',' + a.toFixed(3) + ')');
      g.addColorStop(0.55, 'rgba(' + rgb(b.col) + ',' + (a * 0.4).toFixed(3) + ')');
      g.addColorStop(1, 'rgba(' + rgb(b.col) + ',0)');
      ctx.fillStyle = g;
      ctx.beginPath(); ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2); ctx.fill();
    }
    ctx.restore();
  }
  function ws_updateTwinkle(env, dt) {
    var ctx = env.ctx, st = env.store;
    st.twSpawn -= dt;
    if (st.twSpawn <= 0 && st.winCoords.length) {
      var w = st.winCoords[(Math.random() * st.winCoords.length) | 0];
      st.twinkles.push({ x: w[0], y: w[1], t: 0, dur: 0.9 + Math.random() * 1.4, dim: Math.random() < 0.55 });
      st.twSpawn = 0.18 + Math.random() * 0.35;
    }
    for (var i = st.twinkles.length - 1; i >= 0; i--) {
      var tw = st.twinkles[i]; tw.t += dt;
      if (tw.t >= tw.dur) { st.twinkles.splice(i, 1); continue; }
      var k = Math.sin((tw.t / tw.dur) * Math.PI);
      ctx.fillStyle = tw.dim
        ? 'rgba(0,0,0,' + (0.42 * k).toFixed(3) + ')'
        : 'rgba(' + Math.round(st.winWarm[0]) + ',' + Math.round(st.winWarm[1]) + ',' + Math.round(st.winWarm[2]) + ',' + (0.5 * k).toFixed(3) + ')';
      ctx.fillRect(tw.x, tw.y, 3, 3);
    }
  }
  scene('cityscape', {
    sky: 'linear-gradient(180deg,#04060a 0%,#05080b 55%,#060a0e 100%)',
    vignette: true,
    heat: true,
    init: function (env) {
      var st = env.store;
      st.sky = document.createElement('canvas'); st.sctx = st.sky.getContext('2d');
      st.winWarm = [255, 200, 130]; st.winCoords = []; st.winSeen = 0;
      st.craft = []; st.spawnIn = 2.5;
      st.drops = []; st.speckles = [];
      st.twinkles = []; st.twSpawn = 0;
    },
    resize: function (env) {
      ws_buildSkyline(env); ws_buildRain(env);
      ws_buildBokeh(env, [[120, 180, 255], [80, 210, 225], [255, 196, 140]]);
    },
    frame: function (env, t, dt) {
      var ctx = env.ctx;
      ctx.clearRect(0, 0, env.W, env.H);
      env.heatGlow([[12, 46, 32], [74, 46, 14], [78, 16, 16]]);
      ctx.drawImage(env.store.sky, 0, 0);
      ws_updateTwinkle(env, dt);
      ws_drawCraft(env, dt);
      ws_drawBokeh(env, t, dt);
      ws_drawRain(env, dt);
    }
  });

  // =====================================================================
  // Shared grid helpers (used by the deck-workshop `deckgrid` scene): the 46px
  // blueprint grid metric, the weighted bit-colour palette, the colour picker,
  // and the grid-walk turn logic for bits riding the grid.
  // =====================================================================
  var PKT_GRID = 46;
  var PKT_COLORS = [
    { c: '0,255,65', w: 0.40 }, { c: '0,204,255', w: 0.30 },
    { c: '255,153,0', w: 0.16 }, { c: '153,102,255', w: 0.14 }
  ];
  function pkt_pickColor() {
    var r = Math.random(), acc = 0;
    for (var i = 0; i < PKT_COLORS.length; i++) { acc += PKT_COLORS[i].w; if (r <= acc) return PKT_COLORS[i].c; }
    return PKT_COLORS[0].c;
  }
  function pkt_decide(p) {
    if (p.jogLeft > 0) {
      p.jogLeft--;
      if (p.jogLeft === 0) { p.vx = p.pvx; p.vy = p.pvy; }
      return;
    }
    if (p.runLeft > 0) { p.runLeft--; return; }
    if (Math.random() < 0.38) {
      var side = Math.random() < 0.5 ? 1 : -1;
      if (p.pvx !== 0) { p.vx = 0; p.vy = side; }
      else { p.vy = 0; p.vx = side; }
      p.jogLeft = 1 + Math.floor(Math.random() * 3);
    }
    p.runLeft = 2 + Math.floor(Math.random() * 6);
  }

  // =====================================================================
  // SCENE: deckgrid -- the workbench as a LIVE CIRCUIT BOARD (deck-workshop).
  // The 46px blueprint grid becomes powered copper: solder-node junctions idle-
  // glow and periodically handshake, energize pulses race along the traces, and
  // the data bits ("bit chasers") spawn FROM nodes, ride the grid, flash a
  // handshake where two cross, get absorbed back into nodes, and every so often
  // a red ICE hunter prowls through with a targeting reticle. Host-driven:
  // started with { canvas:'fxPackets', toggle:false } so the workshop's own FX
  // chip drives it. Reuses the shared 46px grid metric + bit-colour palette.
  // =====================================================================
  var DG_GRID = PKT_GRID;            // 46 -- matches CSS .fx-grid + chaser step
  var DG_ICE = '255,51,51';
  function dg_key(cx, cy) { return cx + ',' + cy; }
  function dg_build(env) {
    var st = env.store, W = env.W, H = env.H, G = DG_GRID;
    st.cols = Math.max(2, Math.floor(W / G));
    st.rows = Math.max(2, Math.floor(H / G));
    // solder nodes on a sparse random subset of interior intersections
    st.nodes = []; st.nodeAt = {};
    for (var cy = 1; cy < st.rows; cy++) {
      for (var cx = 1; cx < st.cols; cx++) {
        if (Math.random() < 0.05) {
          st.nodeAt[dg_key(cx, cy)] = st.nodes.length;
          st.nodes.push({ cx: cx, cy: cy, x: cx * G, y: cy * G, ph: Math.random() * 6.2832, hand: 2 + Math.random() * 7, glow: 0 });
        }
      }
    }
    // bake static copper: faint solder pad + short trace stubs at each node
    st.map = st.map || document.createElement('canvas');
    st.map.width = W; st.map.height = H;
    var g = st.map.getContext('2d'), dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    g.clearRect(0, 0, W, H);
    for (var n = 0; n < st.nodes.length; n++) {
      var nd = st.nodes[n];
      g.strokeStyle = 'rgba(0,255,65,0.05)'; g.lineWidth = 1;
      for (var di = 0; di < dirs.length; di++) {
        var L = 1 + ((Math.random() * 2) | 0);
        g.beginPath(); g.moveTo(nd.x, nd.y);
        g.lineTo(nd.x + dirs[di][0] * G * L, nd.y + dirs[di][1] * G * L); g.stroke();
      }
      g.fillStyle = 'rgba(0,255,65,0.06)'; g.fillRect(nd.x - 3, nd.y - 3, 6, 6);
    }
    st.pulses = []; st.pulseIn = 0.2;
    st.packets = []; st.spawnIn = 0.3;
    st.flashes = []; st.iceIn = 12 + Math.random() * 12;
  }
  function dg_spawnPulse(env) {
    var st = env.store, W = env.W, H = env.H, G = DG_GRID;
    var horiz = Math.random() < 0.5, dir = Math.random() < 0.5 ? 1 : -1, col = pkt_pickColor();
    if (horiz) {
      var cy = 1 + ((Math.random() * (st.rows - 1)) | 0);
      st.pulses.push({ horiz: true, fixed: cy * G, pos: dir > 0 ? -G : W + G, dir: dir, len: G * (2 + Math.random() * 2.5), spd: 300 + Math.random() * 240, col: col });
    } else {
      var cx = 1 + ((Math.random() * (st.cols - 1)) | 0);
      st.pulses.push({ horiz: false, fixed: cx * G, pos: dir > 0 ? -G : H + G, dir: dir, len: G * (2 + Math.random() * 2.5), spd: 300 + Math.random() * 240, col: col });
    }
  }
  function dg_stepPulse(env, p, dt) {
    var st = env.store, ctx = env.ctx, G = DG_GRID;
    p.pos += p.dir * p.spd * dt;
    var head = p.pos, tail = p.pos - p.dir * p.len, x0, y0, x1, y1;
    if (p.horiz) { y0 = y1 = p.fixed; x0 = tail; x1 = head; }
    else { x0 = x1 = p.fixed; y0 = tail; y1 = head; }
    var grad = ctx.createLinearGradient(x0, y0, x1, y1);
    grad.addColorStop(0, 'rgba(' + p.col + ',0)');
    grad.addColorStop(0.72, 'rgba(' + p.col + ',0.14)');
    grad.addColorStop(1, 'rgba(' + p.col + ',0.55)');
    ctx.strokeStyle = grad; ctx.lineWidth = 1.6;
    ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();
    var hx = p.horiz ? head : p.fixed, hy = p.horiz ? p.fixed : head;
    ctx.fillStyle = 'rgba(' + p.col + ',0.85)';
    ctx.shadowColor = 'rgb(' + p.col + ')'; ctx.shadowBlur = 7;
    ctx.beginPath(); ctx.arc(hx, hy, 1.8, 0, 6.2832); ctx.fill(); ctx.shadowBlur = 0;
    // energize a node when the head passes its intersection
    var cAlong = Math.round(head / G), inter = cAlong * G;
    if (Math.abs(head - inter) < 7) {
      var cx = p.horiz ? cAlong : Math.round(p.fixed / G);
      var cy = p.horiz ? Math.round(p.fixed / G) : cAlong;
      var ni = st.nodeAt[dg_key(cx, cy)];
      if (ni != null) st.nodes[ni].glow = Math.max(st.nodes[ni].glow, 0.85);
    }
  }
  function dg_drawNodes(env, t, dt) {
    var st = env.store, ctx = env.ctx;
    for (var i = 0; i < st.nodes.length; i++) {
      var nd = st.nodes[i];
      nd.hand -= dt;
      if (nd.hand <= 0) { nd.glow = Math.max(nd.glow, 1); nd.hand = 4 + Math.random() * 8; }
      if (nd.glow > 0) nd.glow = Math.max(0, nd.glow - dt * 1.3);
      var a = Math.min(1, (0.18 + 0.12 * Math.sin(t / 700 + nd.ph)) + nd.glow);
      ctx.strokeStyle = 'rgba(0,255,65,' + (0.25 * a).toFixed(3) + ')'; ctx.lineWidth = 1;
      ctx.strokeRect(nd.x - 3, nd.y - 3, 6, 6);
      ctx.fillStyle = 'rgba(0,255,65,' + (0.5 * a).toFixed(3) + ')';
      ctx.shadowColor = 'rgba(0,255,65,' + a.toFixed(3) + ')'; ctx.shadowBlur = 6 * a;
      ctx.beginPath(); ctx.arc(nd.x, nd.y, 1.8, 0, 6.2832); ctx.fill(); ctx.shadowBlur = 0;
      if (nd.glow > 0.5) {
        var r = (1 - nd.glow) * 14 + 4;
        ctx.strokeStyle = 'rgba(0,255,65,' + (0.4 * nd.glow).toFixed(3) + ')'; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.arc(nd.x, nd.y, r, 0, 6.2832); ctx.stroke();
      }
    }
  }
  function dg_spawnPacket(env, ice) {
    var st = env.store;
    if (!st.nodes.length) return;
    var nd = st.nodes[(Math.random() * st.nodes.length) | 0];
    var dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]], d = dirs[(Math.random() * 4) | 0];
    st.packets.push({
      x: nd.x, y: nd.y, pvx: d[0], pvy: d[1], vx: d[0], vy: d[1], jogLeft: 0,
      runLeft: 2 + ((Math.random() * 5) | 0),
      speed: ice ? (240 + Math.random() * 120) : (170 + Math.random() * 150),
      color: ice ? DG_ICE : pkt_pickColor(),
      shape: ice ? 'diamond' : ['dot', 'dash', 'twin', 'diamond'][(Math.random() * 4) | 0],
      ice: !!ice, hops: 0, flashCd: 0,
      trail: [{ x: nd.x, y: nd.y }], trailMax: 120 + Math.random() * 120
    });
    nd.glow = Math.max(nd.glow, 1);   // birth flash at the node
  }
  function dg_drawPackets(env, t, dt) {
    var st = env.store, ctx = env.ctx, W = env.W, H = env.H, G = DG_GRID, i;
    for (i = st.packets.length - 1; i >= 0; i--) {
      var p = st.packets[i], dist = p.speed * dt, absorb = false;
      while (dist > 0) {
        var nextX = p.vx !== 0 ? (p.vx > 0 ? Math.floor(p.x / G + 1) : Math.ceil(p.x / G - 1)) * G : p.x;
        var nextY = p.vy !== 0 ? (p.vy > 0 ? Math.floor(p.y / G + 1) : Math.ceil(p.y / G - 1)) * G : p.y;
        var dToNode = p.vx !== 0 ? Math.abs(nextX - p.x) : Math.abs(nextY - p.y);
        if (dToNode <= 0.01) dToNode = G;
        var step = Math.min(dist, dToNode);
        p.x += p.vx * step; p.y += p.vy * step;
        p.trail.push({ x: p.x, y: p.y });
        dist -= step;
        if (step === dToNode) {
          pkt_decide(p); p.hops++;
          var ni = st.nodeAt[dg_key(Math.round(p.x / G), Math.round(p.y / G))];
          if (ni != null) {
            st.nodes[ni].glow = Math.max(st.nodes[ni].glow, 0.9);
            if (!p.ice && p.hops >= 3 && Math.random() < 0.22) { st.nodes[ni].glow = 1; absorb = true; break; }
          }
        }
      }
      var lenBudget = p.trailMax, kept = [p.trail[p.trail.length - 1]];
      for (var tt = p.trail.length - 2; tt >= 0 && lenBudget > 0; tt--) {
        var aa = p.trail[tt], bb = kept[kept.length - 1];
        lenBudget -= Math.abs(aa.x - bb.x) + Math.abs(aa.y - bb.y);
        kept.push(aa);
      }
      p.trail = kept.reverse();
      if (absorb) { st.packets.splice(i, 1); continue; }
      var m = p.trailMax + G * 2;
      if (p.x < -m || p.x > W + m || p.y < -m || p.y > H + m) { st.packets.splice(i, 1); continue; }
      var tw = p.ice ? 1.4 : 1;
      for (var s = 1; s < p.trail.length; s++) {
        var f = s / p.trail.length;
        ctx.strokeStyle = 'rgba(' + p.color + ',' + (f * f * (p.ice ? 0.6 : 0.55)).toFixed(3) + ')';
        ctx.lineWidth = tw + f * 1.2;
        ctx.beginPath(); ctx.moveTo(p.trail[s - 1].x, p.trail[s - 1].y); ctx.lineTo(p.trail[s].x, p.trail[s].y); ctx.stroke();
      }
      ctx.fillStyle = 'rgba(' + p.color + ',.95)';
      ctx.shadowColor = 'rgb(' + p.color + ')'; ctx.shadowBlur = p.ice ? 12 : 8;
      if (p.shape === 'dash') {
        if (p.vx !== 0) ctx.fillRect(p.x - 5, p.y - 1, 10, 2); else ctx.fillRect(p.x - 1, p.y - 5, 2, 10);
      } else if (p.shape === 'twin') {
        var ox = p.vx !== 0 ? 4 : 0, oy = p.vy !== 0 ? 4 : 0;
        ctx.fillRect(p.x - 1.5, p.y - 1.5, 3, 3); ctx.fillRect(p.x - 1.5 - ox, p.y - 1.5 - oy, 3, 3);
      } else if (p.shape === 'diamond') {
        var ds = p.ice ? 4.5 : 3.5;
        ctx.beginPath(); ctx.moveTo(p.x, p.y - ds); ctx.lineTo(p.x + ds, p.y); ctx.lineTo(p.x, p.y + ds); ctx.lineTo(p.x - ds, p.y); ctx.closePath(); ctx.fill();
      } else { ctx.fillRect(p.x - 1.5, p.y - 1.5, 3, 3); }
      ctx.shadowBlur = 0;
      if (p.ice) {
        var rp = 7 + 2 * Math.sin(t / 130 + i), ra = (0.35 + 0.25 * Math.sin(t / 130 + i)).toFixed(3);
        ctx.strokeStyle = 'rgba(' + DG_ICE + ',' + ra + ')'; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.arc(p.x, p.y, rp, 0, 6.2832); ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(p.x - rp - 2, p.y); ctx.lineTo(p.x - rp + 2, p.y);
        ctx.moveTo(p.x + rp - 2, p.y); ctx.lineTo(p.x + rp + 2, p.y);
        ctx.moveTo(p.x, p.y - rp - 2); ctx.lineTo(p.x, p.y - rp + 2);
        ctx.moveTo(p.x, p.y + rp - 2); ctx.lineTo(p.x, p.y + rp + 2);
        ctx.stroke();
      }
    }
    // handshake flashes where two chasers cross paths
    var thr = G * 0.45, thr2 = thr * thr;
    for (var a1 = 0; a1 < st.packets.length; a1++) {
      for (var b1 = a1 + 1; b1 < st.packets.length; b1++) {
        var pa = st.packets[a1], pb = st.packets[b1], dx = pa.x - pb.x, dy = pa.y - pb.y;
        if (dx * dx + dy * dy < thr2 && pa.flashCd <= 0 && pb.flashCd <= 0) {
          st.flashes.push({ x: (pa.x + pb.x) / 2, y: (pa.y + pb.y) / 2, life: 1, ice: pa.ice || pb.ice });
          pa.flashCd = 0.5; pb.flashCd = 0.5;
        }
      }
    }
    for (i = 0; i < st.packets.length; i++) { if (st.packets[i].flashCd > 0) st.packets[i].flashCd -= dt; }
  }
  function dg_drawFlashes(env, dt) {
    var st = env.store, ctx = env.ctx;
    for (var i = st.flashes.length - 1; i >= 0; i--) {
      var f = st.flashes[i]; f.life -= dt * 2.2;
      if (f.life <= 0) { st.flashes.splice(i, 1); continue; }
      var col = f.ice ? DG_ICE : '210,255,225', r = (1 - f.life) * 16 + 2;
      ctx.strokeStyle = 'rgba(' + col + ',' + (0.5 * f.life).toFixed(3) + ')'; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.arc(f.x, f.y, r, 0, 6.2832); ctx.stroke();
      ctx.fillStyle = 'rgba(' + col + ',' + (0.7 * f.life).toFixed(3) + ')';
      ctx.beginPath(); ctx.arc(f.x, f.y, 1.6, 0, 6.2832); ctx.fill();
    }
  }
  scene('deckgrid', {
    sky: false, vignette: false, heat: false,
    init: function (env) {
      var st = env.store;
      st.nodes = []; st.nodeAt = {}; st.pulses = []; st.packets = []; st.flashes = [];
      st.pulseIn = 0.2; st.spawnIn = 0.3; st.iceIn = 12 + Math.random() * 12;
    },
    resize: function (env) { dg_build(env); },
    frame: function (env, t, dt) {
      var st = env.store, ctx = env.ctx, pi;
      ctx.clearRect(0, 0, env.W, env.H);
      if (st.map) ctx.drawImage(st.map, 0, 0);
      st.pulseIn -= dt;
      if (st.pulseIn <= 0) { if (st.pulses.length < 7) dg_spawnPulse(env); st.pulseIn = 0.5 + Math.random() * 1.1; }
      for (pi = st.pulses.length - 1; pi >= 0; pi--) {
        var pu = st.pulses[pi]; dg_stepPulse(env, pu, dt);
        var lim = (pu.horiz ? env.W : env.H) + pu.len + DG_GRID;
        if (pu.pos < -pu.len - DG_GRID || pu.pos > lim) st.pulses.splice(pi, 1);
      }
      dg_drawNodes(env, t, dt);
      st.spawnIn -= dt;
      if (st.spawnIn <= 0) { if (st.packets.length < 6) dg_spawnPacket(env, false); st.spawnIn = 0.7 + Math.random() * 1.6; }
      st.iceIn -= dt;
      if (st.iceIn <= 0) { dg_spawnPacket(env, true); st.iceIn = 16 + Math.random() * 16; }
      dg_drawPackets(env, t, dt);
      dg_drawFlashes(env, dt);
    }
  });

  // =====================================================================
  // Shared ID helper: id_rand (used by several scenes).
  // =====================================================================
  function id_rand(n) { return (Math.random() * n) | 0; }

  // =====================================================================
  // SCENE: club -- a Shadowrunner nightclub (Club Penumbra / Underworld 93 /
  // Dante's Inferno), felt at the EDGES so it never fights the locations
  // table. Pieces: (1) a dancefloor underglow + faint perspective floor along
  // the bottom, pulsing to an implied beat; (1c) slow drifting haze; (1d)
  // sweeping club light beams spread across the bottom edge; (2) a row of
  // beat-synced equalizer bars hugging the bottom edge; (3) drifting neon
  // embers in the empty side gutters; (4) a STEADY (no-flicker) vertical neon
  // blade sign up the LEFT gutter. Identity (sign text + palette) is chosen
  // RANDOMLY on each page load by club_identity(). heat:false.
  // =====================================================================
  function club_identity() {
    var penumbra = {
      id: 'penumbra', name: 'CLUB PENUMBRA',
      washA: [255, 50, 152], washB: [64, 212, 255], washC: [150, 84, 255],
      neon: [255, 76, 184], glow: [124, 64, 255],
      sky: 'linear-gradient(180deg,#06040c 0%,#0a0614 55%,#0e0818 100%)'
    };
    var underworld = {
      id: 'underworld', name: 'UNDERWORLD 93',
      washA: [255, 140, 40], washB: [222, 48, 40], washC: [184, 98, 30],
      neon: [255, 150, 54], glow: [255, 92, 40],
      sky: 'linear-gradient(180deg,#0a0604 0%,#0d0805 55%,#120a06 100%)'
    };
    // Dante's Inferno -- the nine-circles-of-Hell club: fire & brimstone, a hot
    // RED-dominant hellfire palette (deeper/redder than U93's amber grunge).
    var dante = {
      id: 'dante', name: "DANTE'S INFERNO",
      washA: [255, 70, 16], washB: [170, 12, 22], washC: [255, 132, 28],
      neon: [255, 60, 30], glow: [235, 50, 12],
      sky: 'linear-gradient(180deg,#0c0301 0%,#140402 55%,#1a0503 100%)'
    };
    // randomly pick one each landing -- all three palettes are in rotation
    var pool = [penumbra, underworld, dante];
    return pool[Math.floor(Math.random() * pool.length)];
  }
  // smoothly cycle the 3 wash colours (period ~11s) so the dancefloor breathes
  function club_wash(idn, t) {
    var cols = [idn.washA, idn.washB, idn.washC];
    var p = ((t / 11000) % 1) * 3;
    var i = Math.floor(p), f = p - i;
    return mix(cols[i % 3], cols[(i + 1) % 3], f);
  }
  // steady vertical neon: name stacked top->bottom, centred on x, multi-pass
  // bloom (outer halo -> mid -> bright inner -> white core), NO flicker.
  function club_neonSign(g, name, x, y0, lineH, fs, neon, glow) {
    g.save();
    g.textAlign = 'center'; g.textBaseline = 'middle';
    g.font = '700 ' + fs + "px 'Shadowrun', 'Share Tech Mono', monospace";
    g.shadowColor = 'rgba(' + rgb(glow) + ',0.9)';
    var n = name.length;
    function pass(blur, fill) {
      g.shadowBlur = blur; g.fillStyle = fill;
      for (var i = 0; i < n; i++) {
        var ch = name.charAt(i);
        if (ch === ' ') continue;
        g.fillText(ch, x, y0 + i * lineH);
      }
    }
    pass(fs * 0.90, 'rgba(' + rgb(neon) + ',0.55)');
    pass(fs * 0.50, 'rgba(' + rgb(neon) + ',0.85)');
    pass(fs * 0.22, 'rgba(235,255,255,0.95)');
    pass(fs * 0.10, 'rgba(255,255,255,1)');
    g.shadowBlur = 0;
    g.restore();
  }
  // spawn one drifting neon ember in a side gutter (left or right). `seeded`
  // scatters it across the height for the first frame; otherwise it starts
  // just below the bottom edge and rises.
  function club_spawnEmber(st, W, H, seeded) {
    var left = Math.random() < 0.5;
    var gx = left ? 0 : W - st.gutterR;
    var gw = left ? st.gutterL : st.gutterR;
    return {
      x: gx + Math.random() * gw,
      y: seeded ? Math.random() * H : H + Math.random() * 40,
      r: 0.8 + Math.random() * 1.8,
      vy: 8 + Math.random() * 18,            // px/sec upward drift
      ph: Math.random() * 6.2832,
      sway: 6 + Math.random() * 14
    };
  }
  scene('club', {
    sky: 'linear-gradient(180deg,#06040c 0%,#0a0614 55%,#0e0818 100%)',
    vignette: true,
    heat: false,
    init: function (env) {
      var st = env.store, idn = club_identity();
      st.idn = idn;
      var sky = document.querySelector('.amb-sky');
      if (sky) sky.style.background = idn.sky;
    },
    resize: function (env) {
      var st = env.store, W = env.W, H = env.H;
      st.floorTop = Math.round(H * 0.70);          // dancefloor = bottom 30%
      st.vanX = W * 0.5;                            // perspective vanishing pt
      // empty side gutters (content is a centred ~max-1180 column) -- the neon
      // sign + drifting embers live here so the centre stays clean.
      var contentW = Math.min(1180, W * 0.92);
      st.gutterL = Math.max(28, (W - contentW) / 2);
      st.gutterR = st.gutterL;
      // equalizer bars hugging the bottom edge: per-bar phase + frequency so
      // the row reads like a spectrum (precomputed -> stable + cheap).
      st.eqN = Math.max(24, Math.round(W / 26));
      st.eq = [];
      for (var b = 0; b < st.eqN; b++) {
        st.eq.push({ ph: Math.random() * 6.2832, fr: 0.6 + Math.random() * 1.8 });
      }
      // drifting neon embers in the gutters (seeded across the height once)
      st.embers = [];
      for (var p = 0; p < 26; p++) st.embers.push(club_spawnEmber(st, W, H, true));
      // slow drifting haze puffs in the bottom band (large, faint, additive)
      var fh = H - st.floorTop, hazeTop = st.floorTop - fh * 0.1;
      st.haze = [];
      for (var hzI = 0; hzI < 5; hzI++) {
        st.haze.push({
          x: Math.random() * W,
          y: hazeTop + Math.random() * (H - hazeTop),
          r: (0.18 + Math.random() * 0.20) * W,
          vx: (Math.random() < 0.5 ? -1 : 1) * (4 + Math.random() * 7),
          ph: Math.random() * 6.2832,
          amp: 0.03 + Math.random() * 0.025
        });
      }
      // sweeping club light beams -- each rises from its OWN spot spread
      // across the bottom edge (not a single shared origin), sweeping side to
      // side. Brightest at the base (dance floor), fading before the table.
      st.beams = [];
      var nbeam = 4;
      for (var bmI = 0; bmI < nbeam; bmI++) {
        st.beams.push({
          ox: W * ((bmI + 0.5) / nbeam) + (Math.random() - 0.5) * W * 0.08,
          base: -Math.PI / 2 + (Math.random() - 0.5) * 0.5,
          swing: 0.30 + Math.random() * 0.16,
          spd: 0.00026 + Math.random() * 0.0002,
          ph: Math.random() * 6.2832,
          half: 0.05 + Math.random() * 0.02
        });
      }
      // steady vertical neon sign up the LEFT gutter
      st.signX = Math.min(st.gutterL * 0.5 + 14, 64);
      st.signFs = Math.max(14, Math.round(H * 0.026));
      st.signLineH = st.signFs * 1.18;
    },
    frame: function (env, t, dt) {
      var ctx = env.ctx, W = env.W, H = env.H, st = env.store, idn = st.idn;
      ctx.clearRect(0, 0, W, H);
      var floorTop = st.floorTop, fh = H - floorTop, vanX = st.vanX;
      var wash = club_wash(idn, t);
      var beat = 0.5 + 0.5 * Math.sin(t * Math.PI * 2 * 2.07 / 1000); // ~124 BPM
      var soft = 0.78 + 0.22 * beat;

      // (1) dancefloor underglow: wash rising from the bottom, fading to 0 at
      // floorTop so the top ~70% (where the table lives) stays clean.
      var grd = ctx.createLinearGradient(0, H, 0, floorTop);
      grd.addColorStop(0.00, 'rgba(' + rgb(wash) + ',' + (0.32 * soft).toFixed(3) + ')');
      grd.addColorStop(0.55, 'rgba(' + rgb(wash) + ',' + (0.11 * soft).toFixed(3) + ')');
      grd.addColorStop(1.00, 'rgba(' + rgb(wash) + ',0)');
      ctx.fillStyle = grd; ctx.fillRect(0, floorTop, W, fh);
      // a soft beat-pulsing bloom from the dancefloor centre
      var rgl = ctx.createRadialGradient(vanX, H, 0, vanX, H, fh * 1.15);
      rgl.addColorStop(0, 'rgba(' + rgb(wash) + ',' + (0.16 * beat).toFixed(3) + ')');
      rgl.addColorStop(1, 'rgba(' + rgb(wash) + ',0)');
      ctx.fillStyle = rgl; ctx.fillRect(0, floorTop, W, fh);

      // faint perspective floor grid (clipped to the band; fades up)
      ctx.save();
      ctx.beginPath(); ctx.rect(0, floorTop, W, fh); ctx.clip();
      ctx.lineWidth = 1;
      // A receding tiled PLANE. Depth z steps uniformly (z = 1 + row*gStep) and
      // every screen position scales by s = 1/z, so both the horizontal rows and
      // the ends of the vertical rails share the same compression. The plane goes
      // from the near edge (z=1, s=1, y=H, full width) back to the horizon row
      // (z=zFar, s=sFar, y=yFar). The rails STOP at that back row -- they never
      // pinch to a single point, and nothing sticks up above the topmost line.
      var gStep = 0.5, gRows = 8;
      var zFar = 1 + gRows * gStep, sFar = 1 / zFar;
      var yFar = floorTop + fh * sFar;              // back row = topmost line drawn
      // columns sized so the near cells read ~square
      var nearDy = (gStep / (1 + gStep)) * fh;
      var gCols = Math.max(8, Math.round(W / nearDy));
      // horizontal (constant-depth) rows -- bunch toward the horizon
      for (var gi = 0; gi <= gRows; gi++) {
        var si = 1 / (1 + gi * gStep);              // 1 (near) .. sFar (back)
        var gy = floorTop + fh * si;
        var ga = (0.05 + 0.17 * si) * soft;         // brighter near the viewer
        ctx.strokeStyle = 'rgba(' + rgb(wash) + ',' + ga.toFixed(3) + ')';
        ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke();
      }
      // vertical (depth) rails -- evenly spaced across the floor and continuing
      // PAST the screen sides so the compressed back row is still spanned all
      // the way across. A rail's near offset wx maps to screen x = vanX + wx*s;
      // at the back (s=sFar) the row must still reach both edges, so wx runs out
      // to +/-(W/2)/sFar. The extra outer rails start off-screen by the viewer
      // (clipped) and sweep inward toward the horizon.
      var railStep = W / gCols;                     // near spacing (square cells)
      var railMax = Math.ceil((W / 2 / sFar) / railStep);
      ctx.strokeStyle = 'rgba(' + rgb(wash) + ',' + (0.12 * soft).toFixed(3) + ')';
      for (var gc = -railMax; gc <= railMax; gc++) {
        var wx = gc * railStep;                      // floor offset from centre
        ctx.beginPath();
        ctx.moveTo(vanX + wx, H);
        ctx.lineTo(vanX + wx * sFar, yFar);
        ctx.stroke();
      }
      ctx.restore();

      // (1c) haze: slow drifting volumetric fog in the bottom band, additive
      // and very faint so the table above stays clean.
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';
      for (var hi = 0; hi < st.haze.length; hi++) {
        var hz = st.haze[hi];
        hz.x += hz.vx * dt;
        if (hz.x < -hz.r) hz.x = W + hz.r; else if (hz.x > W + hz.r) hz.x = -hz.r;
        var ha = hz.amp * (0.7 + 0.3 * Math.sin(t * 0.0004 + hz.ph)) * soft;
        var hg = ctx.createRadialGradient(hz.x, hz.y, 0, hz.x, hz.y, hz.r);
        hg.addColorStop(0, 'rgba(' + rgb(wash) + ',' + ha.toFixed(3) + ')');
        hg.addColorStop(1, 'rgba(' + rgb(wash) + ',0)');
        ctx.fillStyle = hg;
        ctx.fillRect(hz.x - hz.r, hz.y - hz.r, hz.r * 2, hz.r * 2);
      }
      ctx.restore();

      // (1d) club light beams: a few moving-head beams, each rising from its
      // own spot spread across the bottom edge, sweeping side to side.
      // Brightest at the base (dance floor), fading before the table. Additive.
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';
      var ay = H * 1.01, bl = H * 0.56;
      for (var bi = 0; bi < st.beams.length; bi++) {
        var bm = st.beams[bi];
        var ax = bm.ox;
        var ang = bm.base + Math.sin(t * bm.spd + bm.ph) * bm.swing;
        var dx = Math.cos(ang), dy = Math.sin(ang);
        var ex = ax + dx * bl, ey = ay + dy * bl;
        var px = -dy, py = dx, w1 = bl * bm.half + 28;
        ctx.beginPath();
        ctx.moveTo(ax + px * 5, ay + py * 5);
        ctx.lineTo(ex + px * w1, ey + py * w1);
        ctx.lineTo(ex - px * w1, ey - py * w1);
        ctx.lineTo(ax - px * 5, ay - py * 5);
        ctx.closePath();
        var lg = ctx.createLinearGradient(ax, ay, ex, ey);
        lg.addColorStop(0, 'rgba(' + rgb(idn.neon) + ',' + (0.09 * soft).toFixed(3) + ')');
        lg.addColorStop(1, 'rgba(' + rgb(idn.neon) + ',0)');
        ctx.fillStyle = lg;
        ctx.fill();
      }
      ctx.restore();

      // (2) equalizer bars hugging the bottom edge -- beat-synced "music" in
      // the cycling wash colour with a brighter neon cap. Bottom strip only,
      // modest alpha, so the table text above stays readable.
      var nb = st.eqN, barW = W / nb, gap = barW * 0.32, maxH = fh * 0.46;
      for (var b = 0; b < nb; b++) {
        var e = st.eq[b];
        var amp = 0.28 + 0.72 * Math.abs(Math.sin(t * 0.001 * e.fr + e.ph));
        var hgt = maxH * amp * (0.5 + 0.5 * beat);
        var ex0 = b * barW + gap * 0.5, ew = barW - gap;
        ctx.fillStyle = 'rgba(' + rgb(wash) + ',' + (0.16 * soft).toFixed(3) + ')';
        ctx.fillRect(ex0, H - hgt, ew, hgt);
        ctx.fillStyle = 'rgba(' + rgb(idn.neon) + ',' + (0.50 * soft).toFixed(3) + ')';
        ctx.fillRect(ex0, H - hgt, ew, 2);
      }

      // (3) drifting neon embers in the side gutters -- gentle organic motion
      // that fills the empty margins and never crosses the centre column.
      ctx.save();
      for (var p = 0; p < st.embers.length; p++) {
        var em = st.embers[p];
        em.y -= em.vy * dt;
        if (em.y < -4) { st.embers[p] = club_spawnEmber(st, W, H, false); continue; }
        var emx = em.x + Math.sin(t * 0.0006 + em.ph) * em.sway;
        var lifeA = Math.min(1, (H - em.y) / (H * 0.25)) * Math.min(1, em.y / (H * 0.4));
        var ea = 0.40 * lifeA;
        ctx.fillStyle = 'rgba(' + rgb(idn.neon) + ',' + ea.toFixed(3) + ')';
        ctx.shadowColor = 'rgba(' + rgb(idn.glow) + ',' + (ea * 0.8).toFixed(3) + ')';
        ctx.shadowBlur = 6;
        ctx.beginPath(); ctx.arc(emx, em.y, em.r, 0, 6.2832); ctx.fill();
      }
      ctx.shadowBlur = 0;
      ctx.restore();

      // (4) steady vertical neon blade sign up the LEFT gutter
      var fs = st.signFs, lineH = st.signLineH, name = idn.name;
      var totalH = (name.length - 1) * lineH;
      var y0 = Math.max(H * 0.15, (H - totalH) / 2);
      var bx0 = st.signX - fs * 0.66, bw = fs * 1.32;
      var by0 = y0 - lineH * 0.7, bh = totalH + lineH * 1.4;
      ctx.save();
      ctx.strokeStyle = 'rgba(' + rgb(idn.neon) + ',0.45)';
      ctx.shadowColor = 'rgba(' + rgb(idn.glow) + ',0.7)'; ctx.shadowBlur = 8;
      ctx.lineWidth = 1.5;
      if (ctx.roundRect) { ctx.beginPath(); ctx.roundRect(bx0, by0, bw, bh, 8); ctx.stroke(); }
      else { ctx.strokeRect(bx0, by0, bw, bh); }
      ctx.shadowBlur = 0;
      ctx.restore();
      club_neonSign(ctx, name, st.signX, y0, lineH, fs, idn.neon, idn.glow);
    }
  });

  // =====================================================================
  // Shared helper: gf_palette -- a cool->red datascape palette interpolated by
  // heat/alert level. Used by the RTG `meshgrid` scene.
  // =====================================================================
  function gf_palette(heatT) {
    return {
      grid: mix([40, 180, 200], [200, 60, 70], heatT),
      glow: mix([90, 230, 255], [255, 70, 80], heatT),
      node: mix([120, 245, 255], [255, 110, 100], heatT)
    };
  }

  // =====================================================================
  // SCENE: meshgrid -- the RTG as a SCULPTED SYSTEM (Shadowrun deck's-eye
  // view, not movie code-rain). Host constructs (SAN / CPU / SPU / DS / I-O /
  // ICE) are scattered EVENLY across the whole field as small neon wireframe
  // icons, wired together by datalines, with persona/packet pips routing
  // node-to-node and the occasional handshake ring. Full-bleed + uniform
  // density (no focal point, no centre void) so it underlays the table like
  // system fabric. Reddens with alert level (heat) via gf_palette.
  // Data hooks (set by the page):
  //   global.AMB_RTG_CODES      -- array of real grid codes (the part after
  //                                the '/'); each node gets a UNIQUE one (no
  //                                reuse) and shows it as its label.
  //   global.AMB_GET_FADE_RECT()-- returns {l,t,r,b} of the content table (in
  //                                viewport coords) or null; the mesh fades to
  //                                near-zero where it passes under that rect.
  // =====================================================================
  var MG_KINDS = ['SAN', 'CPU', 'SPU', 'DS', 'I-O', 'ICE'];
  function mg_icon(ctx, kind, x, y, r, col, a, lw) {
    ctx.strokeStyle = 'rgba(' + rgb(col) + ',' + a.toFixed(3) + ')';
    ctx.lineWidth = lw; ctx.beginPath();
    if (kind === 'CPU' || kind === 'SPU') {            // square
      ctx.rect(x - r, y - r, r * 2, r * 2);
    } else if (kind === 'DS') {                        // hexagon (datastore)
      for (var i = 0; i < 6; i++) {
        var ang = Math.PI / 6 + i * Math.PI / 3, px = x + Math.cos(ang) * r, py = y + Math.sin(ang) * r;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.closePath();
    } else if (kind === 'I-O') {                        // triangle (i/o port)
      ctx.moveTo(x, y - r); ctx.lineTo(x + r, y + r); ctx.lineTo(x - r, y + r); ctx.closePath();
    } else {                                            // diamond (SAN / ICE)
      ctx.moveTo(x, y - r); ctx.lineTo(x + r, y); ctx.lineTo(x, y + r); ctx.lineTo(x - r, y); ctx.closePath();
    }
    ctx.stroke();
  }
  // fade factor 1 (full) outside the table rect -> MG_DIM deep inside, with a
  // soft feather at the edges so the mesh dissolves smoothly under the table.
  var MG_DIM = 0.33, MG_FEATHER = 100;
  function mg_fade(x, y, tb) {
    if (!tb) return 1;
    var inside = Math.min(x - tb.l, tb.r - x, y - tb.t, tb.b - y);
    if (inside <= 0) return 1;
    if (inside >= MG_FEATHER) return MG_DIM;
    return 1 + (MG_DIM - 1) * (inside / MG_FEATHER);
  }
  function mg_codesKey() {
    var codes = global.AMB_RTG_CODES;
    if (!codes || !codes.length) return '';
    return codes.length + ':' + codes[0] + ':' + codes[codes.length - 1];
  }
  function mg_build(env) {
    var W = env.W, H = env.H, st = env.store;
    // even jittered-grid layout so coverage is uniform (no clusters / voids)
    var cols = Math.max(5, Math.round(W / 185));
    var rows = Math.max(3, Math.round(H / 165));
    var cw = W / cols, ch = H / rows;
    st.nodes = [];
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        st.nodes.push({
          x: (c + 0.20 + Math.random() * 0.60) * cw,
          y: (r + 0.20 + Math.random() * 0.60) * ch,
          kind: MG_KINDS[(Math.random() * MG_KINDS.length) | 0],
          r: 5 + Math.random() * 3, ph: Math.random() * 6.28,
          hand: Math.random() * 6, code: null
        });
      }
    }
    // assign real grid codes to every node, filling the whole field. Codes are
    // drawn from a shuffled pool; when it runs out we reshuffle and keep going,
    // so the mesh always covers the page even with more cells than codes.
    st.codesKey = mg_codesKey();
    var codes = global.AMB_RTG_CODES;
    if (codes && codes.length) {
      var pool = codes.slice(), pi = 0;
      var mg_shuffle = function () { for (var s = pool.length - 1; s > 0; s--) { var q = (Math.random() * (s + 1)) | 0, tmp = pool[s]; pool[s] = pool[q]; pool[q] = tmp; } };
      mg_shuffle();
      for (var nn = 0; nn < st.nodes.length; nn++) {
        if (pi >= pool.length) { mg_shuffle(); pi = 0; }
        st.nodes[nn].code = pool[pi++];
      }
    }
    // wire each node to its 2-3 nearest neighbours (datalines, deduped)
    st.links = [];
    for (var i = 0; i < st.nodes.length; i++) {
      var a = st.nodes[i], near = [];
      for (var j = 0; j < st.nodes.length; j++) {
        if (j === i) continue;
        var b = st.nodes[j];
        near.push({ j: j, d: Math.hypot(a.x - b.x, a.y - b.y) });
      }
      near.sort(function (p, q) { return p.d - q.d; });
      var deg = 2 + ((Math.random() * 2) | 0);
      for (var m = 0; m < deg && m < near.length; m++) {
        var k = near[m].j; if (i < k) st.links.push({ a: i, b: k, len: near[m].d });
      }
    }
    st.pips = []; st.pipIn = 0;
  }
  scene('meshgrid', {
    sky: 'linear-gradient(180deg,#020a08 0%,#03120d 50%,#01080a 100%)',
    vignette: true,
    heat: true,
    init: function (env) { env.store.pips = []; env.store.pipIn = 0; env.store.codesKey = '\u0000'; },
    resize: function (env) { mg_build(env); },
    frame: function (env, t, dt) {
      var ctx = env.ctx, W = env.W, H = env.H, st = env.store, pal = gf_palette(env.heatT);
      // rebuild once the page's real grid codes arrive (or change)
      if (mg_codesKey() !== st.codesKey) mg_build(env);
      var tb = (typeof global.AMB_GET_FADE_RECT === 'function') ? global.AMB_GET_FADE_RECT() : null;
      ctx.clearRect(0, 0, W, H);
      // datalines (faded per-segment where they pass under the table)
      ctx.lineWidth = 1;
      for (var l = 0; l < st.links.length; l++) {
        var L = st.links[l], a = st.nodes[L.a], b = st.nodes[L.b];
        var lf = mg_fade((a.x + b.x) / 2, (a.y + b.y) / 2, tb);
        ctx.strokeStyle = 'rgba(' + rgb(pal.grid) + ',' + (0.11 * lf).toFixed(3) + ')';
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
      }
      // persona / packet pips routing along datalines (more + faster)
      st.pipIn -= dt;
      if (st.pipIn <= 0 && st.links.length && st.pips.length < 60) {
        st.pipIn = 0.04 + Math.random() * 0.12;
        var li = (Math.random() * st.links.length) | 0;
        st.pips.push({ link: li, f: 0, spd: 0.9 + Math.random() * 1.3, rev: Math.random() < 0.5 });
      }
      for (var p = st.pips.length - 1; p >= 0; p--) {
        var P = st.pips[p]; P.f += P.spd * dt;
        if (P.f >= 1) { st.pips.splice(p, 1); continue; }
        var Lk = st.links[P.link]; if (!Lk) { st.pips.splice(p, 1); continue; }
        var na = st.nodes[Lk.a], nb = st.nodes[Lk.b], f = P.rev ? 1 - P.f : P.f;
        var px = na.x + (nb.x - na.x) * f, py = na.y + (nb.y - na.y) * f;
        var pf = mg_fade(px, py, tb);
        ctx.fillStyle = 'rgba(' + rgb(pal.node) + ',' + (0.9 * pf).toFixed(3) + ')';
        ctx.shadowColor = 'rgba(' + rgb(pal.node) + ',' + (0.9 * pf).toFixed(3) + ')'; ctx.shadowBlur = 6 * pf;
        ctx.beginPath(); ctx.arc(px, py, 1.8, 0, 6.2832); ctx.fill(); ctx.shadowBlur = 0;
      }
      // host constructs (wireframe icon + occasional handshake ring + grid tag)
      ctx.font = "9px 'Share Tech Mono', monospace";
      for (var n = 0; n < st.nodes.length; n++) {
        var nd = st.nodes[n], pulse = 0.5 + 0.5 * Math.sin(t / 600 + nd.ph);
        var nf = mg_fade(nd.x, nd.y, tb);
        nd.hand -= dt;
        if (nd.hand <= 0) nd.hand = 4 + Math.random() * 7;     // periodic handshake
        var hs = nd.hand < 0.6 ? nd.hand / 0.6 : 0;            // 1->0 ring flash at cycle end
        if (hs > 0) {
          ctx.strokeStyle = 'rgba(' + rgb(pal.glow) + ',' + (0.35 * hs * nf).toFixed(3) + ')'; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.arc(nd.x, nd.y, nd.r + 4 + (1 - hs) * 10, 0, 6.2832); ctx.stroke();
        }
        mg_icon(ctx, nd.kind, nd.x, nd.y, nd.r, pal.grid, (0.26 + 0.18 * pulse) * nf, 1);
        ctx.fillStyle = 'rgba(' + rgb(pal.node) + ',' + ((0.5 + 0.4 * pulse) * nf).toFixed(3) + ')';
        ctx.shadowColor = 'rgba(' + rgb(pal.glow) + ',' + (0.8 * nf).toFixed(3) + ')'; ctx.shadowBlur = (6 + pulse * 4) * nf;
        ctx.beginPath(); ctx.arc(nd.x, nd.y, 1.5, 0, 6.2832); ctx.fill(); ctx.shadowBlur = 0;
        if (nd.code) { ctx.fillStyle = 'rgba(' + rgb(pal.node) + ',' + (0.40 * nf).toFixed(3) + ')'; ctx.fillText(nd.code, nd.x + nd.r + 3, nd.y + 3); }
      }
    }
  });

  // =====================================================================
  // SCENE: cipher -- a faint key/cipher stream for the admin token vault.
  // Sparse columns of slow hex glyphs; occasionally a column 'resolves' into
  // a brighter decrypt run before fading. Deliberately subtle (utility page).
  // =====================================================================
  var CI_GLYPH = '0123456789ABCDEF<>/\\[]{}=+*#@$%&';
  function ci_ch() { return CI_GLYPH.charAt((Math.random() * CI_GLYPH.length) | 0); }
  scene('cipher', {
    sky: 'linear-gradient(180deg,#040806 0%,#050a07 60%,#030604 100%)',
    vignette: true,
    heat: false,
    init: function (env) { env.store.cols = []; env.store.keyIn = 1.5; },
    resize: function (env) {
      var st = env.store, W = env.W, H = env.H;
      st.cw = 16; st.rowH = 18; st.nrows = Math.ceil(H / st.rowH) + 2;
      var n = Math.floor(W / st.cw); st.cols = [];
      for (var i = 0; i < n; i++) {
        var chars = [];
        for (var r = 0; r < st.nrows; r++) chars.push(ci_ch());
        st.cols.push({ x: i * st.cw + 3, head: Math.random() * st.nrows, spd: 3 + Math.random() * 7, tail: 6 + (Math.random() * 10 | 0), chars: chars, decrypt: 0 });
      }
    },
    frame: function (env, t, dt) {
      var ctx = env.ctx, W = env.W, H = env.H, st = env.store;
      ctx.clearRect(0, 0, W, H);
      ctx.font = "13px 'Share Tech Mono', monospace";
      st.keyIn -= dt;
      if (st.keyIn <= 0 && st.cols.length) { st.keyIn = 2 + Math.random() * 4; st.cols[id_rand(st.cols.length)].decrypt = 1.4; }
      for (var i = 0; i < st.cols.length; i++) {
        var c = st.cols[i];
        c.head += c.spd * dt;
        if (c.head - c.tail > st.nrows) c.head = 0;
        if (Math.random() < 0.06) c.chars[(Math.random() * st.nrows) | 0] = ci_ch();
        var hot = c.decrypt > 0; if (hot) c.decrypt -= dt;
        var headI = Math.floor(c.head);
        for (var k = 0; k < c.tail; k++) {
          var rr = headI - k; if (rr < 0 || rr >= st.nrows) continue;
          var y = rr * st.rowH + 14, a = (k === 0) ? 0.55 : Math.max(0, 0.32 * (1 - k / c.tail));
          if (hot) ctx.fillStyle = 'rgba(150,255,200,' + Math.min(0.9, a + 0.4).toFixed(3) + ')';
          else ctx.fillStyle = (k === 0) ? 'rgba(140,235,170,' + a.toFixed(3) + ')' : 'rgba(60,160,90,' + a.toFixed(3) + ')';
          ctx.fillText(c.chars[rr], c.x, y);
        }
      }
    }
  });

  // =====================================================================
  // SCENE: noirhaze / violethaze -- a dark room, a key light, and slow
  // cigarette smoke curling up through the beam. Dust motes drift in the
  // light. A calm, low-clutter mood piece (no data, no heat, no scanlines).
  // noirhaze = warm amber (Characters); violethaze = violet/magenta (Runs).
  // One palette-parametrised factory (nh_make); palettes defined below.
  // =====================================================================
  function nh_puff(W, H, seeded) {
    return {
      x: Math.random() * W,
      y: H * (0.78 + Math.random() * 0.24),
      r0: 28 + Math.random() * 44,
      vy: 6 + Math.random() * 11,           // rises slowly
      drift: (Math.random() * 2 - 1) * 7,   // base horizontal lean
      sway: 10 + Math.random() * 16,        // curl amplitude
      freq: 0.2 + Math.random() * 0.3,
      age: seeded ? Math.random() * 5 : 0,
      life: 7 + Math.random() * 5,
      phase: Math.random() * 6.2832,
      warm: Math.random() < 0.5
    };
  }
  function nh_mote(W, H) {
    return { x: Math.random() * W, y: Math.random() * H, vy: 4 + Math.random() * 9,
      sway: Math.random() * 6.2832, swaySpd: 0.4 + Math.random() * 0.6, amp: 6 + Math.random() * 10,
      r: 0.6 + Math.random() * 1.0, tw: Math.random() * 6.2832 };
  }
  // -- palettes: warm amber (noirhaze, Characters) + violet/magenta
  // (violethaze, Runs). key = 3 radial-gradient stops 'r,g,b,a';
  // puff.warm/.cool = lit vs cooler smoke; mote = dust colour.
  var NH_WARM = {
    sky: 'linear-gradient(180deg,#070605 0%,#0a0807 55%,#050403 100%)',
    key: ['168,120,70,0.30', '108,80,50,0.11', '44,32,24,0'],
    puff: { warm: { c: '196,162,126', a: 0.15 }, cool: { c: '158,164,176', a: 0.12 } },
    mote: '200,175,140'
  };
  var NH_VIOLET = {
    sky: 'linear-gradient(180deg,#08060b 0%,#0b0710 55%,#050309 100%)',
    key: ['168,92,202,0.30', '112,62,142,0.11', '46,30,56,0'],
    puff: { warm: { c: '200,150,216', a: 0.15 }, cool: { c: '168,158,200', a: 0.12 } },
    mote: '206,168,224'
  };
  function nh_make(P) {
    return {
      sky: P.sky,
      vignette: true,
      heat: false,
      init: function (env) { env.store.puffs = null; env.store.motes = null; },
      resize: function (env) {
        var st = env.store, W = env.W, H = env.H;
        var np = Math.max(10, Math.min(20, Math.round(W / 110)));
        st.puffs = []; for (var i = 0; i < np; i++) st.puffs.push(nh_puff(W, H, true));
        var nm = Math.max(8, Math.min(18, Math.round(W / 130)));
        st.motes = []; for (var j = 0; j < nm; j++) st.motes.push(nh_mote(W, H));
        st.keyX = W * (0.30 + Math.random() * 0.16);   // key-light origin
      },
      frame: function (env, t, dt) {
        var ctx = env.ctx, W = env.W, H = env.H, st = env.store;
        ctx.clearRect(0, 0, W, H);
        // key light -- a soft glow from above (the noir backlight)
        var kx = st.keyX, ky = H * 0.12;
        var key = ctx.createRadialGradient(kx, ky, 10, kx, ky, H * 0.95);
        key.addColorStop(0, 'rgba(' + P.key[0] + ')');
        key.addColorStop(0.5, 'rgba(' + P.key[1] + ')');
        key.addColorStop(1, 'rgba(' + P.key[2] + ')');
        ctx.fillStyle = key; ctx.fillRect(0, 0, W, H);
        // smoke
        var puffs = st.puffs;
        for (var i = 0; i < puffs.length; i++) {
          var p = puffs[i]; p.age += dt;
          if (p.age >= p.life) { puffs[i] = nh_puff(W, H, false); continue; }
          var k = p.age / p.life, fin = Math.min(1, k / 0.22), fout = Math.min(1, (1 - k) / 0.45);
          var en = Math.min(fin, fout);
          var px = p.x + p.drift * p.age + Math.sin(p.age * p.freq * 6.2832 + p.phase) * p.sway;
          var py = p.y - p.vy * p.age;
          var r = p.r0 + p.age * 15;
          var a = (p.warm ? P.puff.warm.a : P.puff.cool.a) * en;
          var col = p.warm ? P.puff.warm.c : P.puff.cool.c;
          var g = ctx.createRadialGradient(px, py, 0, px, py, r);
          g.addColorStop(0, 'rgba(' + col + ',' + a.toFixed(3) + ')');
          g.addColorStop(1, 'rgba(' + col + ',0)');
          ctx.fillStyle = g;
          ctx.beginPath(); ctx.arc(px, py, r, 0, 6.2832); ctx.fill();
        }
        // dust motes drifting up, brighter as they pass through the key light
        var motes = st.motes;
        for (var mo = 0; mo < motes.length; mo++) {
          var d = motes[mo]; d.y -= d.vy * dt; d.tw += dt; d.sway += d.swaySpd * dt;
          if (d.y < -4) { d.y = H + 4; d.x = Math.random() * W; }
          var mx = d.x + Math.sin(d.sway) * d.amp;
          var lit = 0.10 + 0.16 * Math.max(0, 1 - Math.abs(mx - st.keyX) / (W * 0.5));
          var a2 = lit * (0.5 + 0.5 * Math.sin(d.tw * 2));
          ctx.fillStyle = 'rgba(' + P.mote + ',' + a2.toFixed(3) + ')';
          ctx.beginPath(); ctx.arc(mx, d.y, d.r, 0, 6.2832); ctx.fill();
        }
      }
    };
  }
  scene('noirhaze', nh_make(NH_WARM));
  scene('violethaze', nh_make(NH_VIOLET));

  // =====================================================================
  // SCENE: coolhaze -- a calm blue/teal/cyan neon bokeh haze for the downtime
  // page. Big out-of-focus light blooms drift slowly through a dark teal room
  // while a few smaller "in-focus" bokeh dots breathe. No data, no heat: a
  // relaxing between-runs lull that still reads as Shadowrun neon.
  // =====================================================================
  var CH_COLS = [[70, 225, 245], [55, 195, 195], [90, 150, 255], [80, 205, 230], [95, 235, 200], [120, 165, 250]];
  function ch_bloom(W, H, big) {
    var c = CH_COLS[(Math.random() * CH_COLS.length) | 0];
    return {
      x: Math.random() * W, y: Math.random() * H,
      r: big ? (90 + Math.random() * 150) : (10 + Math.random() * 26),
      col: c,
      vx: (Math.random() - 0.5) * (big ? 6 : 11),
      vy: -(big ? 3 : 6) - Math.random() * (big ? 5 : 9),
      ph: Math.random() * 6.2832, spd: 0.3 + Math.random() * 0.5,
      base: big ? (0.05 + Math.random() * 0.07) : (0.10 + Math.random() * 0.16)
    };
  }
  scene('coolhaze', {
    sky: 'linear-gradient(180deg,#03070b 0%,#040d12 45%,#02080c 100%)',
    vignette: true,
    heat: false,
    init: function (env) { env.store.big = null; env.store.dots = null; },
    resize: function (env) {
      var st = env.store, W = env.W, H = env.H, i;
      var nb = Math.max(7, Math.min(14, Math.round(W / 150)));
      st.big = []; for (i = 0; i < nb; i++) st.big.push(ch_bloom(W, H, true));
      var nd = Math.max(10, Math.min(22, Math.round(W / 95)));
      st.dots = []; for (i = 0; i < nd; i++) st.dots.push(ch_bloom(W, H, false));
    },
    frame: function (env, t, dt) {
      var ctx = env.ctx, W = env.W, H = env.H, st = env.store, i, b, a, g;
      ctx.clearRect(0, 0, W, H);
      // soft teal floor glow for depth
      var fl = ctx.createRadialGradient(W * 0.5, H * 1.02, H * 0.05, W * 0.5, H * 1.02, H * 0.9);
      fl.addColorStop(0, 'rgba(30,120,130,0.16)');
      fl.addColorStop(1, 'rgba(30,120,130,0)');
      ctx.fillStyle = fl; ctx.fillRect(0, 0, W, H);
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';
      // large out-of-focus blooms (drift up + wrap)
      for (i = 0; i < st.big.length; i++) {
        b = st.big[i];
        b.x += (b.vx + Math.sin(t * 0.0003 * b.spd + b.ph) * 4) * dt;
        b.y += b.vy * dt;
        if (b.y < -b.r) { b.y = H + b.r; b.x = Math.random() * W; }
        if (b.x < -b.r) b.x = W + b.r; else if (b.x > W + b.r) b.x = -b.r;
        a = b.base * (0.6 + 0.4 * Math.sin(t * 0.0005 + b.ph));
        if (a < 0.002) continue;
        g = ctx.createRadialGradient(b.x, b.y, 0, b.x, b.y, b.r);
        g.addColorStop(0, 'rgba(' + rgb(b.col) + ',' + a.toFixed(3) + ')');
        g.addColorStop(0.5, 'rgba(' + rgb(b.col) + ',' + (a * 0.42).toFixed(3) + ')');
        g.addColorStop(1, 'rgba(' + rgb(b.col) + ',0)');
        ctx.fillStyle = g;
        ctx.beginPath(); ctx.arc(b.x, b.y, b.r, 0, 6.2832); ctx.fill();
      }
      // smaller "in-focus" bokeh dots: brighter core, gentle twinkle
      for (i = 0; i < st.dots.length; i++) {
        b = st.dots[i];
        b.x += (b.vx + Math.sin(t * 0.0006 * b.spd + b.ph) * 6) * dt;
        b.y += b.vy * dt;
        if (b.y < -b.r) { b.y = H + b.r; b.x = Math.random() * W; }
        if (b.x < -b.r) b.x = W + b.r; else if (b.x > W + b.r) b.x = -b.r;
        a = b.base * (0.45 + 0.55 * Math.sin(t * 0.0011 + b.ph));
        if (a < 0.003) continue;
        g = ctx.createRadialGradient(b.x, b.y, 0, b.x, b.y, b.r);
        g.addColorStop(0, 'rgba(' + rgb(b.col) + ',' + a.toFixed(3) + ')');
        g.addColorStop(0.4, 'rgba(' + rgb(b.col) + ',' + (a * 0.6).toFixed(3) + ')');
        g.addColorStop(1, 'rgba(' + rgb(b.col) + ',0)');
        ctx.fillStyle = g;
        ctx.beginPath(); ctx.arc(b.x, b.y, b.r, 0, 6.2832); ctx.fill();
      }
      ctx.restore();
    }
  });

  // =====================================================================
  // SCENE: icevoid -- ICE SENTINELS in the deep void. A near-black datascape
  // where a handful of guardian constructs (slowly tumbling polyhedra -- d8
  // octahedra, d10 trapezohedra, d20 icosahedra) drift through the dark, each
  // sweeping a scan beam and pulsing red on alert, with faint data dust between
  // them. Faces are translucent (not bare wireframe) so the constructs read as
  // solid ICE crystals. Quiet, watched, menacing -- the lull while the IC
  // decides whether you belong. Fades under the page's main content.
  // =====================================================================
  var IV_ICE = [120, 222, 255], IV_RED = [255, 70, 70];
  function iv_proj(v, rx, ry) {
    var x = v[0], y = v[1], z = v[2];
    var cyA = Math.cos(ry), syA = Math.sin(ry);
    var x1 = x * cyA + z * syA, z1 = -x * syA + z * cyA;
    var cxA = Math.cos(rx), sxA = Math.sin(rx);
    var y1 = y * cxA - z1 * sxA, z2 = y * sxA + z1 * cxA;
    return { x: x1, y: y1, z: z2 };
  }
  // polyhedra as {v:[[x,y,z]...], f:[[vertex indices]...]} at ~unit radius.
  var IV_SHAPES = (function () {
    // d8 -- octahedron (8 triangular faces)
    var oct = {
      v: [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]],
      f: [[0, 2, 4], [2, 1, 4], [1, 3, 4], [3, 0, 4], [2, 0, 5], [1, 2, 5], [3, 1, 5], [0, 3, 5]]
    };
    // d10 -- pentagonal trapezohedron (10 kite faces, 2 apexes + 2 offset rings)
    var d10 = (function () {
      var v = [], f = [], i, a, c = 1.0, h = 0.30, r = 0.86;
      v.push([0, 0, c]); v.push([0, 0, -c]);                              // 0 top apex, 1 bottom apex
      for (i = 0; i < 5; i++) { a = i * 1.25664; v.push([Math.cos(a) * r, Math.sin(a) * r, h]); }            // 2..6 upper ring
      for (i = 0; i < 5; i++) { a = i * 1.25664 + 0.62832; v.push([Math.cos(a) * r, Math.sin(a) * r, -h]); } // 7..11 lower ring
      var U = function (k) { return 2 + (k % 5); }, L = function (k) { return 7 + (k % 5); };
      for (i = 0; i < 5; i++) f.push([0, U(i), L(i), U(i + 1)]);          // top kites
      for (i = 0; i < 5; i++) f.push([1, L(i), U(i + 1), L(i + 1)]);      // bottom kites
      return { v: v, f: f };
    })();
    // d20 -- icosahedron (20 triangular faces)
    var ico = (function () {
      var P = 1.61803, i, v = [
        [-1, P, 0], [1, P, 0], [-1, -P, 0], [1, -P, 0],
        [0, -1, P], [0, 1, P], [0, -1, -P], [0, 1, -P],
        [P, 0, -1], [P, 0, 1], [-P, 0, -1], [-P, 0, 1]
      ], Ln = Math.hypot(1, P, 0);
      for (i = 0; i < v.length; i++) v[i] = [v[i][0] / Ln, v[i][1] / Ln, v[i][2] / Ln];
      var f = [
        [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
        [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
        [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
        [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
      ];
      return { v: v, f: f };
    })();
    return { oct: oct, d10: d10, ico: ico };
  })();
  var IV_SHAPE_KEYS = ['oct', 'd10', 'ico'];
  function iv_build(env) {
    var W = env.W, H = env.H, st = env.store, i;
    // flank the content: stack sentinels down the left & right margins so they
    // stay visible (the centred panel hides whatever passes behind it). Fall
    // back to even thirds if the page exposes no content rect yet.
    var tb = (typeof global.AMB_GET_FADE_RECT === 'function') ? global.AMB_GET_FADE_RECT() : null;
    var lg = tb ? Math.max(60, tb.l) : W * 0.16;          // left gutter inner edge
    var rg = tb ? Math.min(W - 60, tb.r) : W * 0.84;      // right gutter inner edge
    var n = Math.max(4, Math.min(6, Math.round(H / 210)));
    // shuffle the shape keys so the mix is varied but every kind shows up
    var bag = IV_SHAPE_KEYS.slice();
    for (i = bag.length - 1; i > 0; i--) { var q = (Math.random() * (i + 1)) | 0, tm = bag[i]; bag[i] = bag[q]; bag[q] = tm; }
    st.sent = [];
    for (i = 0; i < n; i++) {
      var left = (i % 2 === 0);
      var gw = left ? lg : (W - rg);                       // this side's gutter width
      var x = left ? lg * (0.25 + Math.random() * 0.5) : rg + gw * (0.25 + Math.random() * 0.5);
      var y = (0.14 + 0.7 * ((i + 0.5) / n) + (Math.random() - 0.5) * 0.05) * H;
      st.sent.push({
        ax: x, ay: y,                                      // wander anchor
        x: x, y: y,                                        // live (wandered) centre
        wxA: Math.min(gw * 0.32, 70), wyA: 36 + Math.random() * 48,
        wxs: 0.00018 + Math.random() * 0.00022, wys: 0.00014 + Math.random() * 0.0002,
        wxp: Math.random() * 6.2832, wyp: Math.random() * 6.2832,
        shape: bag[i % bag.length],
        size: 30 + Math.random() * 26,
        rx: Math.random() * 6.2832, ry: Math.random() * 6.2832,
        vrx: (Math.random() - 0.5) * 0.45, vry: 0.16 + Math.random() * 0.28,
        scan: Math.random() * 6.2832, scanSpd: 0.45 + Math.random() * 0.5,
        alarm: 0, alarmIn: 4 + Math.random() * 9
      });
    }
    var nd = Math.max(50, Math.min(130, Math.round(W * H / 11000)));
    st.dust = [];
    for (i = 0; i < nd; i++) {
      st.dust.push({ x: Math.random() * W, y: Math.random() * H, r: 0.5 + Math.random() * 1.2, ph: Math.random() * 6.2832, vx: (Math.random() - 0.5) * 5, vy: (Math.random() - 0.5) * 5 });
    }
  }
  scene('icevoid', {
    sky: 'linear-gradient(180deg,#01030a 0%,#02060f 50%,#00020a 100%)',
    vignette: true, heat: false,
    init: function (env) { env.store.sent = null; env.store.dust = null; },
    resize: function (env) { iv_build(env); },
    frame: function (env, t, dt) {
      var ctx = env.ctx, W = env.W, H = env.H, st = env.store, i, j;
      if (!st.sent) iv_build(env);
      var tb = (typeof global.AMB_GET_FADE_RECT === 'function') ? global.AMB_GET_FADE_RECT() : null;
      ctx.clearRect(0, 0, W, H);
      // drifting data dust
      for (i = 0; i < st.dust.length; i++) {
        var d = st.dust[i];
        d.x += d.vx * dt; d.y += d.vy * dt;
        if (d.x < 0) d.x = W; else if (d.x > W) d.x = 0;
        if (d.y < 0) d.y = H; else if (d.y > H) d.y = 0;
        var df = mg_fade(d.x, d.y, tb), tw = 0.3 + 0.7 * (0.5 + 0.5 * Math.sin(t * 0.002 + d.ph));
        ctx.fillStyle = 'rgba(' + rgb(IV_ICE) + ',' + (0.22 * tw * df).toFixed(3) + ')';
        ctx.beginPath(); ctx.arc(d.x, d.y, d.r, 0, 6.2832); ctx.fill();
      }
      // sentinels
      for (i = 0; i < st.sent.length; i++) {
        var s = st.sent[i];
        s.rx += s.vrx * dt; s.ry += s.vry * dt; s.scan += s.scanSpd * dt;
        s.alarmIn -= dt;
        if (s.alarmIn <= 0) { s.alarm = 1; s.alarmIn = 6 + Math.random() * 11; }
        if (s.alarm > 0) s.alarm = Math.max(0, s.alarm - dt * 0.6);
        // gentle wander -- the construct drifts around its anchor, patrolling
        var sx = s.ax + Math.sin(t * s.wxs + s.wxp) * s.wxA + Math.sin(t * s.wxs * 0.41 + s.wxp * 1.7) * s.wxA * 0.35;
        var sy = s.ay + Math.sin(t * s.wys + s.wyp) * s.wyA + Math.sin(t * s.wys * 0.53 + s.wyp * 1.3) * s.wyA * 0.30;
        s.x = sx; s.y = sy;
        var sf = mg_fade(sx, sy, tb), col = mix(IV_ICE, IV_RED, s.alarm);
        // scan-beam wedge + bright sweep line
        var beamLen = s.size * 3.4, ba = s.scan, spread = 0.13;
        var gx = sx + Math.cos(ba) * beamLen, gy = sy + Math.sin(ba) * beamLen;
        var wg = ctx.createLinearGradient(sx, sy, gx, gy);
        wg.addColorStop(0, 'rgba(' + rgb(col) + ',' + (0.13 * sf).toFixed(3) + ')');
        wg.addColorStop(1, 'rgba(' + rgb(col) + ',0)');
        ctx.fillStyle = wg;
        ctx.beginPath(); ctx.moveTo(sx, sy);
        ctx.lineTo(sx + Math.cos(ba - spread) * beamLen, sy + Math.sin(ba - spread) * beamLen);
        ctx.lineTo(sx + Math.cos(ba + spread) * beamLen, sy + Math.sin(ba + spread) * beamLen);
        ctx.closePath(); ctx.fill();
        ctx.strokeStyle = 'rgba(' + rgb(col) + ',' + (0.3 * sf).toFixed(3) + ')'; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(gx, gy); ctx.stroke();
        // core glow (behind the body so translucent faces read on top)
        var core = ctx.createRadialGradient(sx, sy, 0, sx, sy, s.size * 0.95);
        core.addColorStop(0, 'rgba(' + rgb(col) + ',' + (0.30 * sf).toFixed(3) + ')');
        core.addColorStop(1, 'rgba(' + rgb(col) + ',0)');
        ctx.fillStyle = core;
        ctx.beginPath(); ctx.arc(sx, sy, s.size * 0.95, 0, 6.2832); ctx.fill();
        // solid ICE construct: depth-sorted translucent faces + edges
        var shp = IV_SHAPES[s.shape], P = [], minz = 1e9, maxz = -1e9;
        for (j = 0; j < shp.v.length; j++) P.push(iv_proj(shp.v[j], s.rx, s.ry));
        var faces = [];
        for (j = 0; j < shp.f.length; j++) {
          var fv = shp.f[j], cz = 0;
          for (var kk = 0; kk < fv.length; kk++) cz += P[fv[kk]].z;
          cz /= fv.length;
          if (cz < minz) minz = cz;
          if (cz > maxz) maxz = cz;
          faces.push({ fv: fv, z: cz });
        }
        faces.sort(function (a, b) { return a.z - b.z; });   // back -> front
        var zr = (maxz - minz) || 1;
        for (j = 0; j < faces.length; j++) {
          var F = faces[j], fr = (F.z - minz) / zr;           // 0 back .. 1 front
          ctx.beginPath();
          for (var kp = 0; kp < F.fv.length; kp++) {
            var vv = P[F.fv[kp]], px = sx + vv.x * s.size, py = sy + vv.y * s.size;
            if (kp === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
          }
          ctx.closePath();
          ctx.fillStyle = 'rgba(' + rgb(col) + ',' + ((0.08 + 0.22 * fr) * sf).toFixed(3) + ')';
          ctx.fill();
          ctx.strokeStyle = 'rgba(' + rgb(col) + ',' + ((0.16 + 0.5 * fr) * sf).toFixed(3) + ')';
          ctx.lineWidth = 1.1; ctx.stroke();
        }
        // front-vertex sparkle
        for (j = 0; j < P.length; j++) {
          var vp = P[j]; if (vp.z <= 0) continue;
          var vd = (vp.z + 1) / 2;
          ctx.fillStyle = 'rgba(' + rgb(col) + ',' + (0.55 * vd * sf).toFixed(3) + ')';
          ctx.beginPath(); ctx.arc(sx + vp.x * s.size, sy + vp.y * s.size, 1.7, 0, 6.2832); ctx.fill();
        }
        // alarm ring
        if (s.alarm > 0) {
          var rr = s.size * (1 + (1 - s.alarm) * 2.2);
          ctx.strokeStyle = 'rgba(' + rgb(IV_RED) + ',' + (0.5 * s.alarm * sf).toFixed(3) + ')'; ctx.lineWidth = 1.5;
          ctx.beginPath(); ctx.arc(sx, sy, rr, 0, 6.2832); ctx.stroke();
        }
      }
    }
  });

  // =====================================================================
  // ENGINE
  // =====================================================================
  function start(name, opts) {
    var def = scenes[name];
    if (!def) return;
    opts = opts || {};
    injectCss();
    var body = document.body;

    // Host-driven mode: draw on a page-owned canvas and let the page's own FX
    // control toggle the loop (deck-workshop). Default mode self-injects all.
    var providedCanvas = opts.canvas
      ? (typeof opts.canvas === 'string' ? document.getElementById(opts.canvas) : opts.canvas)
      : null;
    var manageToggle = opts.toggle !== false && !providedCanvas;

    // -- layers (created if absent) -------------------------------------
    var sky = null;
    if (def.sky && !providedCanvas) {
      sky = document.querySelector('.amb-sky');
      if (!sky) {
        sky = document.createElement('div');
        sky.className = 'amb-sky';
        sky.setAttribute('aria-hidden', 'true');
        sky.style.background = (typeof def.sky === 'string')
          ? def.sky
          : 'linear-gradient(180deg,#04060a 0%,#05080b 55%,#060a0e 100%)';
        body.insertBefore(sky, body.firstChild);
      }
    }
    var canvas = providedCanvas || document.getElementById('ambScene');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'ambScene';
      canvas.setAttribute('aria-hidden', 'true');
      body.insertBefore(canvas, sky ? sky.nextSibling : body.firstChild);
    }
    if (def.vignette && !providedCanvas && !document.querySelector('.amb-vig')) {
      var vig = document.createElement('div');
      vig.className = 'amb-vig';
      vig.setAttribute('aria-hidden', 'true');
      body.appendChild(vig);
    }

    var ctx = canvas.getContext('2d');
    var W = 0, H = 0;

    // -- heat easing (optional per scene) -------------------------------
    var heatT = 0, heatTarget = 0, heatTimer = null;
    var API_BASE = (typeof global.API !== 'undefined') ? global.API : '';
    function fetchHeat() {
      if (typeof global.apiFetch !== 'function') return;
      global.apiFetch(API_BASE + '/runs/party-stats').then(function (r) {
        if (!r.ok) return;
        return r.json();
      }).then(function (s) {
        if (s) heatTarget = Math.max(0, Math.min(1, (s.heat || 0) / 10));
      }).catch(function () {});
    }

    // -- cached heat-horizon glow (shared by scenes) --------------------
    var glowCache = null, glowKey = '';
    function heatGlow(palette) {
      var COLD = palette[0], WARM = palette[1], HOT = palette[2];
      var g = heatT <= 0.5 ? mix(COLD, WARM, heatT / 0.5) : mix(WARM, HOT, (heatT - 0.5) / 0.5);
      var key = Math.round(heatT * 50) + ':' + W + ':' + H;
      if (key !== glowKey) {
        var col = rgb(g);
        var grd = ctx.createRadialGradient(W / 2, H * 1.04, H * 0.04, W / 2, H * 1.04, H * 0.95);
        grd.addColorStop(0, 'rgba(' + col + ',1)');
        grd.addColorStop(1, 'rgba(' + col + ',0)');
        glowCache = grd; glowKey = key;
      }
      var baseA = lerp(0.16, 0.34, heatT);
      var pulse = heatT > 0.78 ? (0.82 + 0.18 * Math.sin(performance.now() / 360)) : 1;
      ctx.globalAlpha = baseA * pulse;
      ctx.fillStyle = glowCache;
      ctx.fillRect(0, 0, W, H);
      ctx.globalAlpha = 1;
    }

    // -- env handed to the scene ----------------------------------------
    var env = {
      ctx: ctx, W: 0, H: 0, heatT: 0,
      lerp: lerp, mix: mix, rgb: rgb,
      opts: opts, store: {},
      drawBuildings: drawBuildings, heatGlow: heatGlow
    };

    // -- loop / lifecycle -----------------------------------------------
    var rafId = null, running = false, lastRender = 0;
    var FRAME_MS = 1000 / 60;
    function loop(t) {
      rafId = requestAnimationFrame(loop);
      if (document.hidden) { lastRender = 0; return; }
      if (!lastRender) lastRender = t;
      if (t - lastRender < FRAME_MS) return;
      var dt = Math.min((t - lastRender) / 1000, 0.06);
      lastRender = t;
      env.W = W; env.H = H; env.heatT = heatT;
      if (def.frame) def.frame(env, t, dt);
      if (Math.abs(heatT - heatTarget) > 0.001) heatT += (heatTarget - heatT) * Math.min(1, dt * 0.6);
    }
    function sizeAndResize() {
      W = canvas.width = window.innerWidth;
      H = canvas.height = window.innerHeight;
      env.W = W; env.H = H; env.heatT = heatT;
      if (def.resize) def.resize(env);
    }
    function startLoop() { if (running) return; running = true; lastRender = 0; rafId = requestAnimationFrame(loop); }
    function stopLoop() { running = false; if (rafId) cancelAnimationFrame(rafId); rafId = null; if (ctx) ctx.clearRect(0, 0, W, H); }

    // size first so init/resize have real dimensions
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
    env.W = W; env.H = H;
    if (def.init) def.init(env);
    if (def.resize) def.resize(env);
    window.addEventListener('resize', sizeAndResize);

    // -- controller (used directly in host-driven mode) -----------------
    function ctrlStart() {
      startLoop();
      if (def.heat && !heatTimer) { fetchHeat(); heatTimer = setInterval(fetchHeat, 20000); }
    }
    function ctrlStop() {
      stopLoop();
      if (heatTimer) { clearInterval(heatTimer); heatTimer = null; }
    }

    // -- self-managed toggle (persisted) + reduced-motion default -------
    if (manageToggle) {
      var btn = document.getElementById('wsFxToggle');
      if (!btn) {
        btn = document.createElement('button');
        btn.id = 'wsFxToggle';
        btn.type = 'button';
        btn.title = 'Toggle background animation';
        btn.textContent = 'FX ON';
        body.appendChild(btn);
      }
      var pref = null; try { pref = localStorage.getItem('sr_wsfx'); } catch (e) {}
      var reduce = global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var off = pref ? (pref === 'off') : reduce;
      var apply = function () {
        if (off) {
          body.classList.add('no-amb');
          ctrlStop();
          btn.textContent = 'FX OFF'; btn.classList.add('off');
        } else {
          body.classList.remove('no-amb');
          ctrlStart();
          btn.textContent = 'FX ON'; btn.classList.remove('off');
        }
      };
      btn.addEventListener('click', function () {
        off = !off;
        try { localStorage.setItem('sr_wsfx', off ? 'off' : 'on'); } catch (e) {}
        apply();
      });
      apply();
    }

    return { start: ctrlStart, stop: ctrlStop, canvas: canvas, env: env };
  }

  global.Ambiance = { start: start, scene: scene, scenes: scenes };
})(window);
