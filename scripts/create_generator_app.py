import json, os

assets_dir = r'C:\Users\Thoufeek\.gemini\antigravity\scratch\meme_page_project\assets'
with open(os.path.join(assets_dir, 'pfps_base64.json'), 'r') as f:
    pfps = json.load(f)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>@mrr.hamster — Instagram Meme & Tweet Post Studio</title>
  <style>
    :root {{
      --bg: #090a0f;
      --panel: #13151b;
      --card: #1c1e27;
      --border: #2b2e3b;
      --text: #f3f4f6;
      --muted: #9ca3af;
      --accent: #ff477e;
      --accent-hover: #ff2d6b;
      --accent-glow: rgba(255, 71, 126, 0.35);
      --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-family);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    header {{
      background: rgba(19, 21, 27, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 50;
    }}

    .logo {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 800;
      font-size: 1.15rem;
      letter-spacing: -0.3px;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, #ff477e, #ff8da1);
      color: #fff;
      padding: 4px 10px;
      border-radius: 8px;
      font-size: 0.8rem;
    }}

    .header-actions {{
      display: flex;
      gap: 10px;
    }}

    .btn {{
      padding: 9px 18px;
      border-radius: 9px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.18s ease;
      text-decoration: none;
    }}

    .btn-primary {{
      background: var(--accent);
      color: #fff;
      box-shadow: 0 4px 14px var(--accent-glow);
    }}
    .btn-primary:hover {{
      background: var(--accent-hover);
      transform: translateY(-1px);
    }}

    .btn-secondary {{
      background: #252834;
      color: var(--text);
      border-color: var(--border);
    }}
    .btn-secondary:hover {{
      background: #2f3342;
    }}

    .btn-sm {{
      padding: 6px 12px;
      font-size: 0.8rem;
      border-radius: 6px;
    }}

    /* Main Workspace Layout */
    .app-layout {{
      display: grid;
      grid-template-columns: 460px 1fr;
      flex: 1;
      overflow: hidden;
    }}

    @media (max-width: 980px) {{
      .app-layout {{
        grid-template-columns: 1fr;
        overflow: auto;
      }}
    }}

    /* Controls Panel */
    .controls-panel {{
      background: var(--panel);
      border-right: 1px solid var(--border);
      padding: 24px;
      overflow-y: auto;
      max-height: calc(100vh - 65px);
    }}

    .control-group {{
      margin-bottom: 22px;
    }}

    .group-label {{
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--muted);
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .input-field, .textarea-field, select {{
      width: 100%;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 9px;
      padding: 11px 14px;
      color: #fff;
      font-size: 0.95rem;
      font-family: inherit;
      outline: none;
      transition: border-color 0.15s;
    }}

    .input-field:focus, .textarea-field:focus, select:focus {{
      border-color: var(--accent);
    }}

    .textarea-field {{
      resize: vertical;
      min-height: 110px;
      line-height: 1.5;
    }}

    .field-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }}

    /* Preset quote chips */
    .chips-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }}

    .chip {{
      background: #232631;
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.75rem;
      color: #d1d5db;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .chip:hover {{
      background: #2e3240;
      border-color: var(--accent);
      color: #fff;
    }}

    /* PFP Selector Grid */
    .pfp-select-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-top: 8px;
    }}

    .pfp-thumb-option {{
      width: 100%;
      aspect-ratio: 1;
      border-radius: 12px;
      border: 2px solid var(--border);
      background: #fff;
      overflow: hidden;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
      position: relative;
    }}

    .pfp-thumb-option:hover {{
      transform: scale(1.05);
      border-color: var(--accent);
    }}

    .pfp-thumb-option.active {{
      border-color: var(--accent);
      box-shadow: 0 0 0 2px var(--accent-glow);
    }}

    .pfp-thumb-option img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      image-rendering: pixelated;
    }}

    /* Ratio & Align Buttons */
    .button-group {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
      gap: 8px;
    }}

    .btn-toggle {{
      padding: 8px 12px;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--muted);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
    }}
    .btn-toggle.active {{
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }}

    /* Image Attachment Box */
    .dropzone {{
      border: 2px dashed var(--border);
      border-radius: 10px;
      padding: 16px;
      text-align: center;
      cursor: pointer;
      background: var(--card);
      transition: border-color 0.15s;
    }}
    .dropzone:hover {{
      border-color: var(--accent);
    }}
    .dropzone p {{
      font-size: 0.85rem;
      color: var(--muted);
      margin-top: 4px;
    }}

    .attached-preview-wrapper {{
      margin-top: 10px;
      position: relative;
      border-radius: 8px;
      overflow: hidden;
      max-height: 140px;
      border: 1px solid var(--border);
    }}
    .attached-preview-wrapper img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .btn-remove-attachment {{
      position: absolute;
      top: 6px;
      right: 6px;
      background: rgba(0, 0, 0, 0.75);
      color: #ff5c8a;
      border: none;
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      cursor: pointer;
    }}

    /* Preview Stage */
    .preview-stage {{
      background: #08090d;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 30px;
      position: relative;
      overflow-y: auto;
    }}

    .canvas-container {{
      max-width: 520px;
      width: 100%;
      box-shadow: 0 20px 50px rgba(0,0,0,0.85);
      border-radius: 16px;
      overflow: hidden;
      border: 1px solid #222530;
      position: relative;
    }}

    canvas {{
      width: 100%;
      height: auto;
      display: block;
      background: #000000;
    }}

    .preview-footer {{
      margin-top: 18px;
      display: flex;
      gap: 12px;
      align-items: center;
    }}

    .toast {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #1f232e;
      border: 1px solid var(--accent);
      color: #fff;
      padding: 10px 20px;
      border-radius: 30px;
      font-size: 0.9rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.6);
      transition: transform 0.25s ease, opacity 0.25s ease;
      opacity: 0;
      pointer-events: none;
      z-index: 100;
    }}
    .toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>

  <header>
    <div class="logo">
      <span>🐹 @mrr.hamster</span>
      <span class="logo-badge">Post Studio</span>
    </div>
    <div class="header-actions">
      <button class="btn btn-secondary" id="btnCopy">
        📋 Copy to Clipboard
      </button>
      <button class="btn btn-primary" id="btnDownload">
        📥 Download for Instagram
      </button>
    </div>
  </header>

  <div class="app-layout">
    <!-- Controls Panel -->
    <div class="controls-panel">
      
      <!-- Text / Content -->
      <div class="control-group">
        <div class="group-label">
          <span>Meme Text / Quote</span>
          <span id="charCount" style="font-weight:400;">0 chars</span>
        </div>
        <textarea id="inputText" class="textarea-field" placeholder="Type your flirty, dark humor, or unhinged observation here...">flirting is easy until you have to flirt with someone you actually want.</textarea>
        
        <div class="chips-row">
          <span class="chip" data-text="i don't give mixed signals, you just have selective hearing">Mixed Signals</span>
          <span class="chip" data-text="flirting is easy until you have to flirt with someone you actually want.">Flirting Dilemma</span>
          <span class="chip" data-text="how do i explain to people that i can just slip into a nonverbal mood and it has absolutely nothing to do with them">Nonverbal Mood</span>
          <span class="chip" data-text="when the joke ended 20 minutes ago, but it keeps repeating in my head nonstop">20 Mins Ago</span>
          <span class="chip" data-text="i don't date for marriage i date to forget my ex like a normal person thank u">Dating Logic</span>
        </div>
      </div>

      <!-- Account Details -->
      <div class="control-group">
        <div class="group-label">Account Identity</div>
        <div class="field-row">
          <div>
            <label style="font-size:0.75rem; color:var(--muted); display:block; margin-bottom:4px;">Display Name</label>
            <input type="text" id="inputName" class="input-field" value="Mr. Hamster">
          </div>
          <div>
            <label style="font-size:0.75rem; color:var(--muted); display:block; margin-bottom:4px;">Instagram Handle</label>
            <input type="text" id="inputHandle" class="input-field" value="@mrr.hamster">
          </div>
        </div>
        <div style="margin-top:10px; display:flex; gap:16px;">
          <label style="font-size:0.85rem; display:flex; align-items:center; gap:6px; cursor:pointer;">
            <input type="checkbox" id="checkSparkle" checked> Show Sparkle ✨
          </label>
          <label style="font-size:0.85rem; display:flex; align-items:center; gap:6px; cursor:pointer;">
            <input type="checkbox" id="checkVerified"> Verified Check 🔵
          </label>
        </div>
      </div>

      <!-- PFP Selection & Background Styling -->
      <div class="control-group">
        <div class="group-label">Profile Avatar (PFP)</div>
        <div class="pfp-select-grid">
          <div class="pfp-thumb-option active" data-src="{pfps['pfp_mog_hamster.png']}" title="The Mog Hamster">
            <img src="{pfps['pfp_mog_hamster.png']}" alt="Mog">
          </div>
          <div class="pfp-thumb-option" data-src="{pfps['pfp_look_what_we_have.png']}" title="Look What We Have">
            <img src="{pfps['pfp_look_what_we_have.png']}" alt="Look">
          </div>
          <div class="pfp-thumb-option" data-src="{pfps['pfp_evil_flirty.png']}" title="Evil Flirty">
            <img src="{pfps['pfp_evil_flirty.png']}" alt="Evil">
          </div>
          <div class="pfp-thumb-option" data-src="{pfps['pfp_hamster_smirk.png']}" title="Hamster Smirk">
            <img src="{pfps['pfp_hamster_smirk.png']}" alt="Smirk">
          </div>
        </div>

        <div style="margin-top:12px;">
          <label style="font-size:0.75rem; color:var(--muted); display:block; margin-bottom:4px;">PFP Avatar Backdrop / Rim</label>
          <select id="selectPfpBg">
            <option value="white">Classic Pure White Circle</option>
            <option value="pink" selected>Aesthetic Soft Pink (#ffd1dc - Matches Nose)</option>
            <option value="charcoal">Sleek Dark Charcoal (#1f2128 with Border)</option>
            <option value="border">White with Hot Pink Border Ring</option>
          </select>
        </div>
      </div>

      <!-- Attached Reaction Meme Image -->
      <div class="control-group">
        <div class="group-label">Attach Reaction Meme Image (Optional)</div>
        <div class="dropzone" id="dropzone">
          <input type="file" id="inputAttach" accept="image/*" style="display:none;">
          <div style="font-size:1.4rem;">🖼️</div>
          <div style="font-size:0.88rem; font-weight:600; margin-top:4px;">Click or Drag Reaction Meme</div>
          <p>Pairs text with a reaction image below it</p>
        </div>
        <div class="attached-preview-wrapper" id="attachedPreview" style="display:none;">
          <img id="attachedImgElem" src="" alt="Attached">
          <button class="btn-remove-attachment" id="btnRemoveAttach">✕ Remove</button>
        </div>
      </div>

      <!-- Layout & Formatting -->
      <div class="control-group">
        <div class="group-label">Post Format (Canvas Ratio)</div>
        <div class="button-group">
          <button class="btn-toggle active" id="btnRatioPortrait" data-ratio="portrait">
            4:5 Feed Portrait<br><span style="font-size:0.7rem; opacity:0.7;">1080 × 1350 (Best)</span>
          </button>
          <button class="btn-toggle" id="btnRatioSquare" data-ratio="square">
            1:1 Square<br><span style="font-size:0.7rem; opacity:0.7;">1080 × 1080</span>
          </button>
        </div>
      </div>

      <!-- Typography Controls -->
      <div class="control-group">
        <div class="group-label">
          <span>Font Size</span>
          <span id="fontSizeDisplay">46px</span>
        </div>
        <input type="range" id="rangeFontSize" min="30" max="68" value="46" style="width:100%;">
        
        <div style="margin-top:12px; display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
          <div>
            <label style="font-size:0.75rem; color:var(--muted); display:block; margin-bottom:4px;">Vertical Align</label>
            <select id="selectVAlign">
              <option value="top">Top Aligned (Twitter/Threads)</option>
              <option value="center" selected>Centered on Post (High Focus)</option>
            </select>
          </div>
          <div>
            <label style="font-size:0.75rem; color:var(--muted); display:block; margin-bottom:4px;">Text Alignment</label>
            <select id="selectTextAlign">
              <option value="left" selected>Left Aligned</option>
              <option value="center">Center Aligned</option>
            </select>
          </div>
        </div>
      </div>

    </div>

    <!-- Preview Stage -->
    <div class="preview-stage">
      <div class="canvas-container">
        <canvas id="postCanvas" width="1080" height="1350"></canvas>
      </div>

      <div class="preview-footer">
        <span style="font-size:0.8rem; color:var(--muted);">
          Resolution: <strong id="resLabel" style="color:#fff;">1080 × 1350 px</strong> (OLED Dark Mode)
        </span>
      </div>
    </div>
  </div>

  <div class="toast" id="toastMessage">Copied image to clipboard!</div>

  <script>
    const canvas = document.getElementById('postCanvas');
    const ctx = canvas.getContext('2d');

    // State
    const state = {{
      text: document.getElementById('inputText').value,
      name: 'Mr. Hamster',
      handle: '@mrr.hamster',
      sparkle: true,
      verified: false,
      ratio: 'portrait', // 'portrait' (1080x1350) or 'square' (1080x1080)
      vAlign: 'center',
      textAlign: 'left',
      fontSize: 46,
      pfpBg: 'pink',
      pfpSrc: '{pfps['pfp_mog_hamster.png']}',
      attachedImg: null
    }};

    let loadedPfpImg = new Image();
    loadedPfpImg.onload = render;
    loadedPfpImg.src = state.pfpSrc;

    let loadedAttachedImg = null;

    function updateCanvasSize() {{
      if (state.ratio === 'portrait') {{
        canvas.width = 1080;
        canvas.height = 1350;
        document.getElementById('resLabel').textContent = '1080 × 1350 px (Instagram 4:5 Feed)';
      }} else {{
        canvas.width = 1080;
        canvas.height = 1080;
        document.getElementById('resLabel').textContent = '1080 × 1080 px (Instagram 1:1 Square)';
      }}
    }}

    // Text Wrapping Function for Canvas
    function getLines(ctx, text, maxWidth) {{
      const lines = [];
      const paragraphs = text.split('\\n');

      for (let p of paragraphs) {{
        if (p.trim() === '') {{
          lines.push('');
          continue;
        }}
        const words = p.split(' ');
        let currentLine = words[0];

        for (let i = 1; i < words.length; i++) {{
          const word = words[i];
          const width = ctx.measureText(currentLine + ' ' + word).width;
          if (width < maxWidth) {{
            currentLine += ' ' + word;
          }} else {{
            lines.push(currentLine);
            currentLine = word;
          }}
        }}
        lines.push(currentLine);
      }}
      return lines;
    }}

    function render() {{
      updateCanvasSize();
      const W = canvas.width;
      const H = canvas.height;

      // 1. Pure OLED Pitch Black Background
      ctx.fillStyle = '#000000';
      ctx.fillRect(0, 0, W, H);

      const marginX = 88;
      const contentWidth = W - marginX * 2;

      // 2. Measure content to compute vertical positioning
      const pfpSize = 92;
      const lineHeight = Math.round(state.fontSize * 1.48);
      ctx.font = `400 ${{state.fontSize}}px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`;
      
      const lines = getLines(ctx, state.text, contentWidth);
      const textBlockHeight = lines.length * lineHeight;
      const headerBlockHeight = pfpSize;
      const gapHeaderToText = 32;

      let attachedHeight = 0;
      let attachedWidth = contentWidth;
      const gapTextToAttach = 30;

      if (loadedAttachedImg) {{
        const aspect = loadedAttachedImg.width / loadedAttachedImg.height;
        // Limit max height to 620px
        attachedHeight = Math.min(620, Math.round(contentWidth / aspect));
      }}

      const totalContentHeight = headerBlockHeight + gapHeaderToText + textBlockHeight + (loadedAttachedImg ? (gapTextToAttach + attachedHeight) : 0);

      // Determine Start Y
      let startY = 110;
      if (state.vAlign === 'center') {{
        startY = Math.max(80, Math.round((H - totalContentHeight) / 2));
      }}

      // 3. Render Header (PFP + Name + Handle)
      const pfpX = marginX;
      const pfpY = startY;

      // Draw PFP Circular Background
      ctx.save();
      ctx.beginPath();
      ctx.arc(pfpX + pfpSize / 2, pfpY + pfpSize / 2, pfpSize / 2, 0, Math.PI * 2);
      ctx.closePath();
      ctx.clip();

      // PFP background color styling
      if (state.pfpBg === 'pink') {{
        ctx.fillStyle = '#ffd6e0';
      }} else if (state.pfpBg === 'charcoal') {{
        ctx.fillStyle = '#222530';
      }} else {{
        ctx.fillStyle = '#ffffff';
      }}
      ctx.fillRect(pfpX, pfpY, pfpSize, pfpSize);

      // Draw Hamster Image
      if (loadedPfpImg && loadedPfpImg.complete) {{
        ctx.drawImage(loadedPfpImg, pfpX, pfpY, pfpSize, pfpSize);
      }}
      ctx.restore();

      // PFP Border / Ring
      ctx.save();
      ctx.beginPath();
      ctx.arc(pfpX + pfpSize / 2, pfpY + pfpSize / 2, pfpSize / 2, 0, Math.PI * 2);
      if (state.pfpBg === 'border') {{
        ctx.strokeStyle = '#ff477e';
        ctx.lineWidth = 3;
      }} else if (state.pfpBg === 'charcoal') {{
        ctx.strokeStyle = '#383d4e';
        ctx.lineWidth = 2;
      }} else {{
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
        ctx.lineWidth = 1.5;
      }}
      ctx.stroke();
      ctx.restore();

      // Display Name & Handle
      const infoX = pfpX + pfpSize + 20;
      const nameY = pfpY + 34;

      ctx.textAlign = 'left';
      ctx.font = '700 32px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif';
      ctx.fillStyle = '#ffffff';
      
      let displayName = state.name;
      if (state.sparkle) displayName += ' ✨';
      ctx.fillText(displayName, infoX, nameY);

      // Verified Badge (optional)
      if (state.verified) {{
        const nameWidth = ctx.measureText(displayName).width;
        ctx.fillStyle = '#1d9bf0';
        ctx.beginPath();
        ctx.arc(infoX + nameWidth + 16, nameY - 8, 10, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#fff';
        ctx.font = '700 12px sans-serif';
        ctx.fillText('✓', infoX + nameWidth + 12.5, nameY - 4);
      }}

      // Handle
      ctx.font = '400 25px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif';
      ctx.fillStyle = '#71767b';
      ctx.fillText(state.handle, infoX, nameY + 34);

      // 4. Render Meme / Tweet Text
      let textCursorY = pfpY + headerBlockHeight + gapHeaderToText + state.fontSize;
      ctx.font = `400 ${{state.fontSize}}px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`;
      ctx.fillStyle = '#f7f9f9';
      ctx.textAlign = state.textAlign;

      for (let line of lines) {{
        const lineX = state.textAlign === 'center' ? (W / 2) : marginX;
        ctx.fillText(line, lineX, textCursorY);
        textCursorY += lineHeight;
      }}

      // 5. Render Attached Reaction Meme Image (if present)
      if (loadedAttachedImg && loadedAttachedImg.complete) {{
        const attachY = textCursorY - state.fontSize + gapTextToAttach;
        const cornerRadius = 24;

        ctx.save();
        ctx.beginPath();
        ctx.roundRect(marginX, attachY, attachedWidth, attachedHeight, cornerRadius);
        ctx.clip();
        ctx.drawImage(loadedAttachedImg, marginX, attachY, attachedWidth, attachedHeight);
        ctx.restore();

        // Rounded border for attachment
        ctx.save();
        ctx.beginPath();
        ctx.roundRect(marginX, attachY, attachedWidth, attachedHeight, cornerRadius);
        ctx.strokeStyle = '#2f3336';
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.restore();
      }}
    }}

    // Event Listeners
    document.getElementById('inputText').addEventListener('input', (e) => {{
      state.text = e.target.value;
      document.getElementById('charCount').textContent = `${{e.target.value.length}} chars`;
      render();
    }});

    document.getElementById('inputName').addEventListener('input', (e) => {{
      state.name = e.target.value;
      render();
    }});

    document.getElementById('inputHandle').addEventListener('input', (e) => {{
      state.handle = e.target.value;
      render();
    }});

    document.getElementById('checkSparkle').addEventListener('change', (e) => {{
      state.sparkle = e.target.checked;
      render();
    }});

    document.getElementById('checkVerified').addEventListener('change', (e) => {{
      state.verified = e.target.checked;
      render();
    }});

    document.getElementById('selectPfpBg').addEventListener('change', (e) => {{
      state.pfpBg = e.target.value;
      render();
    }});

    document.getElementById('rangeFontSize').addEventListener('input', (e) => {{
      state.fontSize = parseInt(e.target.value, 10);
      document.getElementById('fontSizeDisplay').textContent = `${{state.fontSize}}px`;
      render();
    }});

    document.getElementById('selectVAlign').addEventListener('change', (e) => {{
      state.vAlign = e.target.value;
      render();
    }});

    document.getElementById('selectTextAlign').addEventListener('change', (e) => {{
      state.textAlign = e.target.value;
      render();
    }});

    // Preset Quote Chips
    document.querySelectorAll('.chip').forEach(chip => {{
      chip.addEventListener('click', () => {{
        const text = chip.getAttribute('data-text');
        document.getElementById('inputText').value = text;
        state.text = text;
        document.getElementById('charCount').textContent = `${{text.length}} chars`;
        render();
      }});
    }});

    // PFP Selector
    document.querySelectorAll('.pfp-thumb-option').forEach(thumb => {{
      thumb.addEventListener('click', () => {{
        document.querySelectorAll('.pfp-thumb-option').forEach(t => t.classList.remove('active'));
        thumb.classList.add('active');
        const src = thumb.getAttribute('data-src');
        state.pfpSrc = src;
        loadedPfpImg = new Image();
        loadedPfpImg.onload = render;
        loadedPfpImg.src = src;
      }});
    }});

    // Ratio Toggle
    const btnPortrait = document.getElementById('btnRatioPortrait');
    const btnSquare = document.getElementById('btnRatioSquare');

    btnPortrait.addEventListener('click', () => {{
      btnPortrait.classList.add('active');
      btnSquare.classList.remove('active');
      state.ratio = 'portrait';
      render();
    }});

    btnSquare.addEventListener('click', () => {{
      btnSquare.classList.add('active');
      btnPortrait.classList.remove('active');
      state.ratio = 'square';
      render();
    }});

    // File Attachment Dropzone
    const dropzone = document.getElementById('dropzone');
    const inputAttach = document.getElementById('inputAttach');
    const attachedPreview = document.getElementById('attachedPreview');
    const attachedImgElem = document.getElementById('attachedImgElem');
    const btnRemoveAttach = document.getElementById('btnRemoveAttach');

    dropzone.addEventListener('click', () => inputAttach.click());

    dropzone.addEventListener('dragover', (e) => {{
      e.preventDefault();
      dropzone.style.borderColor = 'var(--accent)';
    }});

    dropzone.addEventListener('dragleave', () => {{
      dropzone.style.borderColor = 'var(--border)';
    }});

    dropzone.addEventListener('drop', (e) => {{
      e.preventDefault();
      dropzone.style.borderColor = 'var(--border)';
      if (e.dataTransfer.files && e.dataTransfer.files[0]) {{
        handleAttachedFile(e.dataTransfer.files[0]);
      }}
    }});

    inputAttach.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files[0]) {{
        handleAttachedFile(e.target.files[0]);
      }}
    }});

    function handleAttachedFile(file) {{
      const reader = new FileReader();
      reader.onload = (event) => {{
        const img = new Image();
        img.onload = () => {{
          loadedAttachedImg = img;
          attachedImgElem.src = event.target.result;
          attachedPreview.style.display = 'block';
          dropzone.style.display = 'none';
          render();
        }};
        img.src = event.target.result;
      }};
      reader.readAsDataURL(file);
    }}

    btnRemoveAttach.addEventListener('click', () => {{
      loadedAttachedImg = null;
      attachedPreview.style.display = 'none';
      dropzone.style.display = 'block';
      inputAttach.value = '';
      render();
    }});

    // Download Functionality
    document.getElementById('btnDownload').addEventListener('click', () => {{
      const link = document.createElement('a');
      const filename = `mrr_hamster_${{state.ratio}}_${{Date.now()}}.png`;
      link.download = filename;
      link.href = canvas.toDataURL('image/png', 1.0);
      link.click();
      showToast('Image downloaded! Ready for Instagram.');
    }});

    // Copy to Clipboard
    document.getElementById('btnCopy').addEventListener('click', async () => {{
      try {{
        canvas.toBlob(async (blob) => {{
          await navigator.clipboard.write([
            new ClipboardItem({{ 'image/png': blob }})
          ]);
          showToast('Copied post image to clipboard!');
        }});
      }} catch (err) {{
        console.error(err);
        showToast('Clipboard access denied. Please click Download instead.');
      }}
    }});

    function showToast(msg) {{
      const toast = document.getElementById('toastMessage');
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2500);
    }}

    // Initial render
    render();
  </script>
</body>
</html>
'''

generator_path = r'C:\Users\Thoufeek\.gemini\antigravity\scratch\meme_page_project\generator.html'
with open(generator_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Also update index.html to be this studio app so opening the project opens the studio directly!
index_path = r'C:\Users\Thoufeek\.gemini\antigravity\scratch\meme_page_project\index.html'
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated generator.html and index.html successfully!')
