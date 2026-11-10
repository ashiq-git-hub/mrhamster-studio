# -*- coding: utf-8 -*-
"""
Mr. Hamster Studio Website Builder
Generates index.html and generator.html with:
- Warm vintage stone aesthetic & tactile retro drop shadows
- Pitch-black OLED post canvas (1080p lossless)
- Complete mobile responsive UX overhaul (natural stacked layout, live preview at top, zero scroll-trapping)
- Stepper buttons for micro-adjustments on mobile
- Defined avatar frames (Circle & Square) with Crisp Titanium White default
- Credentials lockscreen (hamster_boss / MogMaster#2026)
"""

import os
import json

BASE_DIR = r"c:\Users\Thoufeek\Desktop\mr hasmter"

with open(os.path.join(BASE_DIR, "assets", "data", "pfps_base64.json"), "r", encoding="utf-8") as f:
    pfps_base64 = json.load(f)

mog_b64 = pfps_base64.get("pfp_mog_hamster.png", "")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>Mr. Hamster — Post Atelier</title>
  <style>
    :root {{
      --bg-core: #eae4d8;              /* Warm vintage oat/stone background - NOT plain white */
      --bg-sidebar: #dfd8cb;           /* Rich tactile warm clay/parchment sidebar */
      --bg-card: #ffffff;              /* Crisp gallery white block */
      --bg-card-hover: #faf9f6;        /* Subtle ivory hover */
      --bg-recessed: #f3efe6;          /* Recessed field */
      --border-hairline: #cac2b2;      /* Defined warm border */
      --border-hover: #9c9381;         /* Border hover */
      --border-focus: #1c1b18;         /* High-contrast dark focus border */
      --gold: #9e7a2f;                 /* Antique vintage brass / warm gold */
      --gold-soft: rgba(158, 122, 47, 0.12);
      --gold-hover: #836423;
      --text-main: #181714;            /* Rich vintage ink */
      --text-dim: #544f47;             /* Muted graphite */
      --text-muted: #827c71;           /* Quiet ash */
      --font-serif: "Georgia", "Baskerville", "Playfair Display", "Times New Roman", serif;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
      --font-mono: "SF Mono", "Cascadia Code", "Consolas", monospace;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      border-radius: 0 !important; /* ZERO CURVES - STRICT RETRO BOX SYSTEM */
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      background-color: var(--bg-core);
      color: var(--text-main);
      font-family: var(--font-sans);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      background-image: 
        linear-gradient(to right, rgba(0, 0, 0, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(0, 0, 0, 0.02) 1px, transparent 1px);
      background-size: 28px 28px;
    }}

    /* Top Atelier Header (Minimalist Warm Retro) */
    header {{
      background: #fbfaf7;
      border-bottom: 2px solid #1c1b18;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 14px rgba(28, 24, 18, 0.08);
    }}

    .brand-section {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-box {{
      width: 42px;
      height: 42px;
      background: #1c1b18;
      color: #ffffff;
      border: 1.5px solid #1c1b18;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.45rem;
      box-shadow: 3px 3px 0px rgba(0, 0, 0, 0.22);
      flex-shrink: 0;
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .app-title {{
      font-family: var(--font-serif);
      font-size: 1.18rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .app-handle {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: #796024;
      background: #f4ecda;
      padding: 2px 7px;
      font-weight: 700;
      border: 1px solid #dcd1ba;
      letter-spacing: 0.04em;
    }}

    .subtitle {{
      font-size: 0.69rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .status-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 10px;
      background: #f3efe6;
      border: 1px solid var(--border-hairline);
      font-size: 0.68rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      text-transform: uppercase;
      font-weight: 600;
      letter-spacing: 0.06em;
    }}

    .status-tag::before {{
      content: "";
      width: 6px;
      height: 6px;
      background: #2e7d32;
      display: inline-block;
    }}

    /* Tactile Retro Buttons */
    .btn {{
      padding: 9px 18px;
      font-size: 0.76rem;
      font-family: var(--font-mono);
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.12s cubic-bezier(0.4, 0, 0.2, 1);
      border: 1.5px solid transparent;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }}

    .btn:active {{
      transform: translateY(1.5px);
    }}

    .btn-primary {{
      background: #1c1b18;
      color: #ffffff;
      border-color: #1c1b18;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.18), 2.5px 2.5px 0px rgba(0, 0, 0, 0.28);
    }}
    .btn-primary:hover {{
      background: #32302b;
      box-shadow: 0 5px 14px rgba(0, 0, 0, 0.25), 2.5px 2.5px 0px rgba(0, 0, 0, 0.35);
    }}

    .btn-secondary {{
      background: #ffffff;
      color: var(--text-main);
      border-color: var(--border-hairline);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06), 2px 2px 0px rgba(200, 192, 178, 0.4);
    }}
    .btn-secondary:hover {{
      background: #f4efe5;
      border-color: var(--border-hover);
      color: #000000;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08), 2px 2px 0px rgba(175, 166, 150, 0.6);
    }}

    .btn-sm {{
      padding: 6px 12px;
      font-size: 0.7rem;
    }}

    .btn-micro {{
      padding: 3px 8px;
      background: #f3efe6;
      border: 1px solid var(--border-hairline);
      font-size: 0.65rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      cursor: pointer;
      font-weight: 600;
      transition: all 0.1s;
    }}
    .btn-micro:hover, .btn-micro:active {{
      background: #1c1b18;
      color: #ffffff;
      border-color: #1c1b18;
    }}

    /* Main Atelier Layout */
    .app-layout {{
      display: grid;
      grid-template-columns: 460px 1fr;
      flex: 1;
      overflow: hidden;
      min-height: calc(100vh - 67px);
    }}

    /* Left Control Panel */
    .controls-panel {{
      background: var(--bg-sidebar);
      border-right: 1.5px solid var(--border-hairline);
      padding: 22px;
      overflow-y: auto;
      max-height: calc(100vh - 67px);
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: 2px 0 10px rgba(28, 24, 18, 0.04);
    }}

    /* Tactile Block with Distinct Drop Shadow */
    .control-card {{
      background: var(--bg-card);
      border: 1.5px solid var(--border-hairline);
      padding: 18px 20px;
      position: relative;
      transition: all 0.15s ease-in-out;
      box-shadow: 0 4px 18px rgba(28, 24, 18, 0.09), 0 1px 4px rgba(28, 24, 18, 0.05), 3px 3px 0px rgba(200, 192, 178, 0.5);
    }}
    .control-card:hover {{
      border-color: var(--border-hover);
      box-shadow: 0 8px 24px rgba(28, 24, 18, 0.13), 0 2px 6px rgba(28, 24, 18, 0.07), 3px 3px 0px rgba(180, 172, 158, 0.7);
    }}

    /* Clean Editorial Group Header */
    .group-label {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: var(--text-dim);
      font-family: var(--font-mono);
      margin-bottom: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid #e5ded2;
      padding-bottom: 7px;
    }}

    .group-label span.section-title {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .group-label span.section-title::before {{
      content: "—";
      color: var(--gold);
      font-weight: 800;
    }}

    .input-field, .textarea-field, select {{
      width: 100%;
      background: #ffffff;
      border: 1.5px solid var(--border-hairline);
      padding: 10px 12px;
      color: var(--text-main);
      font-size: 0.88rem;
      font-family: var(--font-sans);
      outline: none;
      transition: border-color 0.15s, box-shadow 0.15s;
      box-shadow: inset 0 1px 3px rgba(32, 28, 22, 0.05);
    }}

    .input-field:focus, .textarea-field:focus, select:focus {{
      border-color: var(--border-focus);
      box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08), 0 0 0 2px rgba(28, 27, 24, 0.1);
    }}

    .textarea-field {{
      min-height: 110px;
      resize: vertical;
      line-height: 1.55;
      font-size: 0.94rem;
    }}

    /* Aspect Ratio Grid */
    .ratio-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }}

    .btn-ratio {{
      padding: 12px 14px;
      background: #ffffff;
      border: 1.5px solid #d4cdbe;
      color: var(--text-dim);
      cursor: pointer;
      text-align: left;
      transition: all 0.12s;
      display: flex;
      flex-direction: column;
      gap: 4px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05), 2px 2px 0px rgba(215, 208, 195, 0.4);
      -webkit-tap-highlight-color: transparent;
    }}

    .btn-ratio span.label {{
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 0.76rem;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}

    .btn-ratio span.dim {{
      font-size: 0.67rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-weight: 500;
    }}

    .btn-ratio:hover {{
      border-color: var(--border-hover);
      color: var(--text-main);
      background: #faf8f3;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08), 2px 2px 0px rgba(190, 182, 168, 0.6);
    }}

    .btn-ratio.active {{
      background: #f6f1e5;
      border: 1.5px solid #1c1b18;
      border-left: 5px solid var(--gold);
      color: var(--text-main);
      box-shadow: 0 4px 12px rgba(158, 122, 47, 0.15), 2px 2px 0px rgba(158, 122, 47, 0.28);
    }}
    .btn-ratio.active span.dim {{
      color: var(--gold);
      font-weight: 700;
    }}

    /* Minimalist Retro Segmented Toggles */
    .btn-toggle-group {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1px;
      background: var(--border-hairline);
      border: 1.5px solid var(--border-hairline);
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
    }}

    .btn-toggle {{
      padding: 9px 10px;
      font-size: 0.72rem;
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--text-dim);
      background: #ffffff;
      border: none;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      transition: all 0.12s;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      -webkit-tap-highlight-color: transparent;
    }}

    .btn-toggle.active {{
      background: #1c1b18;
      color: #ffffff;
    }}

    /* Profile Avatar Section */
    .pfp-slot-container {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 12px;
    }}

    .pfp-preview-box {{
      width: 76px;
      height: 76px;
      border: 2px solid #1c1b18;
      background: #ded7c9;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      flex-shrink: 0;
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15), inset 0 2px 4px rgba(0,0,0,0.1);
    }}

    .pfp-preview-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}

    .pfp-upload-actions {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .pfp-upload-btn-wrap {{
      display: flex;
      gap: 6px;
    }}

    /* Slider Row with Stepper [-] [+] */
    .slider-row {{
      margin-top: 14px;
    }}

    .slider-label-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      font-size: 0.71rem;
      font-family: var(--font-mono);
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: var(--text-dim);
    }}

    .slider-stepper-wrap {{
      display: flex;
      align-items: center;
      gap: 8px;
      width: 100%;
    }}

    .btn-stepper {{
      width: 38px;
      height: 36px;
      background: #ffffff;
      border: 1.5px solid var(--border-hairline);
      color: var(--text-main);
      font-family: var(--font-mono);
      font-size: 1.15rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
      transition: all 0.1s;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
      flex-shrink: 0;
    }}
    .btn-stepper:active {{
      background: #1c1b18;
      color: #ffffff;
      border-color: #1c1b18;
      transform: translateY(1px);
    }}

    input[type=range] {{
      -webkit-appearance: none;
      width: 100%;
      height: 6px;
      background: #d4cdbe;
      outline: none;
      border: none;
      box-shadow: inset 0 1px 2px rgba(0,0,0,0.15);
      touch-action: pan-x;
    }}

    input[type=range]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      appearance: none;
      width: 22px;
      height: 26px;
      background: #1c1b18;
      border: 1.5px solid #ded7c9;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.35);
      transition: background 0.12s;
    }}

    input[type=range]::-webkit-slider-thumb:hover {{
      background: var(--gold);
    }}

    /* Checkbox & Dropzone */
    .checkbox-container {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.77rem;
      font-family: var(--font-mono);
      cursor: pointer;
      user-select: none;
      font-weight: 600;
      color: var(--text-main);
    }}

    .checkbox-container input[type=checkbox] {{
      width: 17px;
      height: 17px;
      accent-color: #1c1b18;
      cursor: pointer;
    }}

    .dropzone {{
      border: 1.5px dashed var(--border-hairline);
      background: var(--bg-recessed);
      padding: 16px;
      text-align: center;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .dropzone:hover {{
      border-color: var(--border-focus);
      background: #ede8dc;
    }}

    .attach-preview-bar {{
      display: none;
      margin-top: 8px;
      background: #ffffff;
      border: 1.5px solid var(--border-hairline);
      padding: 7px 10px;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }}

    /* Right Preview Pedestal (Exhibition Gallery Wall) */
    .preview-workspace {{
      background: #d4cdc0;
      background-image: radial-gradient(rgba(0, 0, 0, 0.1) 1px, transparent 1px);
      background-size: 22px 22px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      padding: 36px 24px;
      overflow: auto;
    }}

    .canvas-pedestal {{
      box-shadow: 0 28px 75px rgba(0, 0, 0, 0.45), 0 8px 24px rgba(0, 0, 0, 0.22), 0 0 0 2px #1c1b18;
      overflow: hidden;
      background: #000000; /* POST CANVAS STRICTLY OLED BLACK */
      max-width: 100%;
      max-height: 86vh;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      position: relative;
      line-height: 0;
    }}

    #postCanvas {{
      display: block;
      width: 100%;
      height: 100%;
      max-width: 100%;
      max-height: 84vh;
      object-fit: contain;
    }}

    .btn-pedestal-expand {{
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(28, 27, 24, 0.82);
      backdrop-filter: blur(4px);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 5px 10px;
      font-size: 0.68rem;
      font-family: var(--font-mono);
      font-weight: 700;
      cursor: pointer;
      z-index: 10;
      transition: all 0.15s;
      letter-spacing: 0.04em;
    }}
    .btn-pedestal-expand:hover, .btn-pedestal-expand:active {{
      background: var(--gold);
      border-color: var(--gold);
      color: #ffffff;
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #1c1b18;
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 12px 18px;
      font-size: 0.76rem;
      font-family: var(--font-mono);
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
      z-index: 999;
      transform: translateY(80px);
      opacity: 0;
      transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.2s;
      pointer-events: none;
    }}
    .toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}

    /* Credentials Gate Lockscreen */
    #authOverlay {{
      position: fixed;
      inset: 0;
      background: rgba(28, 24, 18, 0.88);
      backdrop-filter: blur(10px);
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      transition: opacity 0.25s ease;
    }}
    #authOverlay.hidden {{
      opacity: 0;
      pointer-events: none;
    }}
    .auth-card {{
      background: #fbfaf7;
      border: 2px solid #1c1b18;
      box-shadow: 0 16px 50px rgba(0, 0, 0, 0.5), 6px 6px 0px #1c1b18;
      width: 100%;
      max-width: 420px;
      padding: 32px 28px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .auth-header {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 8px;
    }}
    .auth-badge {{
      width: 48px;
      height: 48px;
      background: #1c1b18;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      box-shadow: 3px 3px 0px rgba(0, 0, 0, 0.2);
    }}
    .auth-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-main);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }}
    .auth-subtitle {{
      font-size: 0.72rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      font-weight: 600;
    }}
    .auth-error {{
      display: none;
      background: #fdf2f2;
      border: 1.5px solid #d9534f;
      color: #c92a2a;
      padding: 8px 12px;
      font-size: 0.76rem;
      font-family: var(--font-mono);
      font-weight: 600;
    }}

    /* Fullscreen Overlay Modal */
    .fullscreen-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.96);
      backdrop-filter: blur(8px);
      z-index: 10001;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 16px;
    }}
    .fullscreen-overlay.hidden {{
      display: none;
    }}
    .fullscreen-top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
    }}
    .fullscreen-ratio-badge {{
      color: var(--gold);
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.08em;
    }}
    .fullscreen-canvas-wrap {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px 0;
      overflow: hidden;
    }}
    #fullscreenImg {{
      max-width: 100%;
      max-height: 75vh;
      object-fit: contain;
      box-shadow: 0 16px 50px rgba(0,0,0,0.9), 0 0 0 1.5px rgba(255,255,255,0.2);
    }}
    .fullscreen-bottom-bar {{
      display: flex;
      justify-content: center;
      width: 100%;
    }}

    /* Mobile Floating Bar */
    .mobile-floating-bar {{
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(232, 226, 214, 0.98);
      backdrop-filter: blur(12px);
      border-top: 1.5px solid #1c1b18;
      padding: 10px 14px;
      gap: 10px;
      z-index: 90;
      box-shadow: 0 -4px 18px rgba(0,0,0,0.14);
    }}
    .mobile-floating-bar .btn {{
      flex: 1;
      padding: 12px 14px;
      font-size: 0.8rem;
      min-height: 48px;
    }}

    /* ======================================================== */
    /* RESPONSIVE UX ENGINE (Mobile & Tablet <= 960px)          */
    /* Smooth, natural vertical stack with LIVE PREVIEW AT TOP */
    /* ======================================================== */
    @media (max-width: 960px) {{
      body {{
        overflow-x: hidden;
        overflow-y: auto;
        -webkit-overflow-scrolling: touch;
      }}

      .mobile-floating-bar {{
        display: flex;
      }}

      .app-layout {{
        display: flex !important;
        flex-direction: column !important;
        min-height: auto !important;
        overflow: visible !important;
      }}

      /* Live Post Preview Hero anchored at the top */
      .preview-workspace {{
        order: 1 !important;
        padding: 16px 12px !important;
        min-height: auto !important;
        background: #ded7c9 !important;
        border-bottom: 2px solid var(--border-hairline) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
      }}

      .canvas-pedestal {{
        max-width: min(100%, 360px) !important;
        max-height: 48vh !important;
        margin: 0 auto !important;
        box-shadow: 0 16px 36px rgba(28, 24, 18, 0.32), 0 0 0 1.5px #1c1b18 !important;
      }}

      #postCanvas {{
        max-height: 46vh !important;
        width: 100% !important;
        height: auto !important;
      }}

      /* Smooth, natural scrolling controls directly beneath preview */
      .controls-panel {{
        order: 2 !important;
        display: flex !important;
        flex-direction: column !important;
        max-height: none !important;
        overflow-y: visible !important;
        padding: 16px 12px 95px 12px !important;
        border-right: none !important;
        gap: 14px !important;
      }}

      /* Prevent iOS auto-zoom on input focus */
      .input-field, .textarea-field, select {{
        font-size: 16px !important;
        padding: 12px 10px !important;
      }}

      /* Touch Ergonomics for Sliders & Steppers */
      .slider-stepper-wrap {{
        gap: 10px !important;
      }}
      .btn-stepper {{
        width: 44px !important;
        height: 42px !important;
        font-size: 1.3rem !important;
      }}

      input[type=range] {{
        height: 8px !important;
      }}
      input[type=range]::-webkit-slider-thumb {{
        width: 28px !important;
        height: 36px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.35) !important;
      }}

      /* Touch targets for buttons */
      .btn {{
        min-height: 46px;
      }}
      .btn-ratio {{
        min-height: 56px;
        padding: 12px 10px !important;
      }}
      .btn-ratio span.label {{
        font-size: 0.74rem !important;
      }}
      .btn-ratio span.dim {{
        font-size: 0.65rem !important;
      }}

      /* PFP preview & upload buttons on mobile */
      .pfp-slot-container {{
        flex-wrap: wrap;
      }}

      /* Header mobile layout */
      header {{
        padding: 10px 12px !important;
      }}
      .brand-box {{
        width: 36px !important;
        height: 36px !important;
        font-size: 1.15rem !important;
      }}
      .app-title {{
        font-size: 0.95rem !important;
        gap: 6px !important;
      }}
      .subtitle, .status-tag {{
        display: none !important;
      }}
      .header-actions .btn {{
        padding: 6px 10px !important;
        font-size: 0.7rem !important;
        min-height: 36px !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Credentials Gate Lockscreen -->
  <div id="authOverlay">
    <div class="auth-card">
      <div class="auth-header">
        <div class="auth-badge">🐹</div>
        <div class="auth-title">Mr. Hamster Atelier</div>
        <div class="auth-subtitle">Restricted Access · Enter Credentials</div>
      </div>

      <div class="auth-error" id="authError">
        ✕ Invalid username or password. Access denied.
      </div>

      <form id="authForm" onsubmit="event.preventDefault(); handleLogin();" style="display: flex; flex-direction: column; gap: 12px;">
        <div>
          <label style="display: block; font-size: 0.72rem; font-family: var(--font-mono); color: var(--text-dim); font-weight: 700; margin-bottom: 4px; text-transform: uppercase;">Username</label>
          <input type="text" id="authUsername" class="input-field" placeholder="Username" autocomplete="username" required>
        </div>
        <div>
          <label style="display: block; font-size: 0.72rem; font-family: var(--font-mono); color: var(--text-dim); font-weight: 700; margin-bottom: 4px; text-transform: uppercase;">Password</label>
          <input type="password" id="authPassword" class="input-field" placeholder="Password" autocomplete="current-password" required>
        </div>

        <button type="submit" class="btn btn-primary" style="padding: 13px; font-size: 0.84rem; margin-top: 6px;">
          <span>🔓 Unlock Studio</span>
        </button>
      </form>
    </div>
  </div>

  <!-- Fullscreen Post Preview Modal (Especially Great on Mobile) -->
  <div id="fullscreenOverlay" class="fullscreen-overlay hidden">
    <div class="fullscreen-top-bar">
      <span class="fullscreen-ratio-badge" id="fullscreenRatioBadge">4:5 · 1080 × 1350</span>
      <button class="btn btn-secondary btn-sm" id="btnCloseFullscreen">✕ Close</button>
    </div>
    <div class="fullscreen-canvas-wrap">
      <img id="fullscreenImg" alt="High Resolution Post Preview">
    </div>
    <div class="fullscreen-bottom-bar">
      <button class="btn btn-primary" id="btnFullscreenDownload" style="width: 100%; max-width: 380px;">
        <span>📥 Download 1080p Lossless PNG</span>
      </button>
    </div>
  </div>

  <!-- Header -->
  <header>
    <div class="brand-section">
      <div class="brand-box">🐹</div>
      <div class="brand-text">
        <div class="app-title">
          <span>Mr. Hamster</span>
          <span class="app-handle">@mrr.hamster</span>
        </div>
        <div class="subtitle">Post & Meme Atelier · Minimalist Edition</div>
      </div>
    </div>

    <div class="header-actions">
      <span class="status-tag">1080p Native</span>
      <button class="btn btn-secondary btn-sm" id="btnLockStudio" title="Lock Studio Access">
        <span>🔒 Lock</span>
      </button>
      <button class="btn btn-secondary btn-sm" id="btnResetAllDefaults" title="Restore default sizing and layout">
        <span>↺ Defaults</span>
      </button>
      <button class="btn btn-primary btn-sm" id="btnQuickExport" onclick="document.getElementById('btnDownload').click()">
        <span>Download Post</span>
      </button>
    </div>
  </header>

  <!-- Main Atelier Layout -->
  <div class="app-layout">
    
    <!-- Left Controls Panel -->
    <div class="controls-panel">
      
      <!-- Aspect Ratio Box Grid -->
      <div class="control-card">
        <div class="group-label">
          <span class="section-title">Aspect Ratio</span>
          <span id="currentRatioBadge" style="color: var(--gold); font-weight: 700;">1080 × 1350</span>
        </div>
        <div class="ratio-grid">
          <button class="btn-ratio active" data-ratio="4:5" data-w="1080" data-h="1350">
            <span class="label">4:5 Portrait</span>
            <span class="dim">Feed (1080×1350)</span>
          </button>
          <button class="btn-ratio" data-ratio="1:1" data-w="1080" data-h="1080">
            <span class="label">1:1 Square</span>
            <span class="dim">Feed (1080×1080)</span>
          </button>
          <button class="btn-ratio" data-ratio="9:16" data-w="1080" data-h="1920">
            <span class="label">9:16 Story / Reel</span>
            <span class="dim">Vertical (1080×1920)</span>
          </button>
          <button class="btn-ratio" data-ratio="16:9" data-w="1920" data-h="1080">
            <span class="label">16:9 Landscape</span>
            <span class="dim">Cover (1920×1080)</span>
          </button>
        </div>
      </div>

      <!-- Profile Avatar (Clean, Natural) -->
      <div class="control-card">
        <div class="group-label">
          <span class="section-title">Profile Avatar</span>
          <span id="pfpStatusBadge" style="color: var(--gold); font-weight: 700;">Mog Hamster</span>
        </div>
        
        <div class="pfp-slot-container">
          <div class="pfp-preview-box" id="pfpPreviewBox">
            <img id="activePfpImg" src="{mog_b64}" onerror="this.src='assets/pfps/pfp_mog_hamster.png'" alt="Active Avatar">
          </div>

          <div class="pfp-upload-actions">
            <div class="pfp-upload-btn-wrap">
              <button class="btn btn-secondary btn-sm" id="btnUploadPfp" style="flex: 1;">
                <span>📷 Upload Photo</span>
              </button>
              <button class="btn btn-secondary btn-sm" id="btnResetPfp" title="Reset to default Mog Hamster">
                <span>↺ Reset</span>
              </button>
            </div>
            <input type="file" id="inputPfpFile" accept="image/*" style="display: none;">
          </div>
        </div>

        <!-- Avatar Shape in Post Toggle -->
        <div style="margin-top: 14px;">
          <div class="slider-label-row">
            <span>Avatar Shape in Post</span>
          </div>
          <div class="btn-toggle-group">
            <button class="btn-toggle active" id="btnPfpCircle">● Circle Frame</button>
            <button class="btn-toggle" id="btnPfpSquare">■ Square Box Frame</button>
          </div>
        </div>

        <!-- Avatar Frame Rim Color (Matches Black Post & White PFP) -->
        <div style="margin-top: 12px;">
          <div class="slider-label-row">
            <span>Avatar Frame Rim Color</span>
            <span id="labelFrameColor" style="font-family: var(--font-mono); font-size: 0.68rem; color: var(--gold); font-weight: 700;">CRISP WHITE</span>
          </div>
          <select id="selectPfpFrameColor">
            <option value="#ffffff" selected>Crisp Titanium White (#ffffff) · High Definition</option>
            <option value="#ded8cc">Warm Editorial Ivory (#ded8cc) · Classic Atelier</option>
            <option value="#8e95a5">Slate Titanium (#8e95a5) · Neutral Steel Rim</option>
            <option value="#c5a059">Champagne Gold (#c5a059) · Antique Luxury</option>
            <option value="#2b2d35">Deep Charcoal (#2b2d35) · Stealth Dark Rim</option>
            <option value="none">None (Borderless)</option>
          </select>
        </div>

        <!-- Avatar Scale Slider with Stepper [-] [+] -->
        <div class="slider-row">
          <div class="slider-label-row">
            <span>Avatar Scale</span>
            <span id="labelPfpSize">96 px</span>
          </div>
          <div class="slider-stepper-wrap">
            <button type="button" class="btn-stepper" id="btnPfpSizeMinus" title="Decrease Size">-</button>
            <input type="range" id="rangePfpSize" min="60" max="150" value="96">
            <button type="button" class="btn-stepper" id="btnPfpSizePlus" title="Increase Size">+</button>
          </div>
        </div>
      </div>

      <!-- Account Identity -->
      <div class="control-card">
        <div class="group-label">
          <span class="section-title">Identity</span>
        </div>
        <div style="display: flex; gap: 8px; margin-bottom: 10px;">
          <input type="text" class="input-field" id="inputName" value="Mr. Hamster" placeholder="Display Name">
          <input type="text" class="input-field" id="inputHandle" value="@mrr.hamster" placeholder="Handle">
        </div>
        <div style="display: flex; gap: 18px;">
          <label class="checkbox-container">
            <input type="checkbox" id="checkSparkle" checked>
            <span>Sparkle ✨</span>
          </label>
          <label class="checkbox-container">
            <input type="checkbox" id="checkVerified" checked>
            <span>Verified Badge</span>
          </label>
        </div>
      </div>

      <!-- Post Content Free Writing Area -->
      <div class="control-card">
        <div class="group-label">
          <span class="section-title">Post Text</span>
          <div style="display: flex; align-items: center; gap: 8px;">
            <button type="button" class="btn-micro" id="btnSampleText" title="Insert Sample Quote">↻ Sample</button>
            <button type="button" class="btn-micro" id="btnClearText" title="Clear Text">✕ Clear</button>
            <span id="charCount" style="color: var(--text-muted); font-family: var(--font-mono); font-size: 0.68rem;">0 chars</span>
          </div>
        </div>
        <textarea class="textarea-field" id="inputText" placeholder="Write whatever thought, quote, or observation you want..."></textarea>
      </div>

      <!-- Typography & Layout Settings -->
      <div class="control-card">
        <div class="group-label">
          <span class="section-title">Typography & Layout</span>
        </div>
        
        <!-- Font Size Slider with Stepper [-] [+] -->
        <div class="slider-row" style="margin-top: 0; margin-bottom: 14px;">
          <div class="slider-label-row">
            <span>Font Size</span>
            <span id="labelFontSize">46 px</span>
          </div>
          <div class="slider-stepper-wrap">
            <button type="button" class="btn-stepper" id="btnFontSizeMinus" title="Decrease Font">-</button>
            <input type="range" id="rangeFontSize" min="26" max="74" value="46">
            <button type="button" class="btn-stepper" id="btnFontSizePlus" title="Increase Font">+</button>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 10px;">
          <div>
            <div style="font-size: 0.69rem; color: var(--text-dim); font-family: var(--font-mono); margin-bottom: 4px; text-transform: uppercase; font-weight: 600;">Vertical Placement</div>
            <select id="selectVAlign">
              <option value="center" selected>Centered</option>
              <option value="top">Top Header</option>
            </select>
          </div>
          <div>
            <div style="font-size: 0.69rem; color: var(--text-dim); font-family: var(--font-mono); margin-bottom: 4px; text-transform: uppercase; font-weight: 600;">Text Align</div>
            <select id="selectTextAlign">
              <option value="left" selected>Left</option>
              <option value="center">Center</option>
            </select>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
          <div>
            <div style="font-size: 0.69rem; color: var(--text-dim); font-family: var(--font-mono); margin-bottom: 4px; text-transform: uppercase; font-weight: 600;">Header Align</div>
            <select id="selectHeaderAlign">
              <option value="left" selected>Left (Classic)</option>
              <option value="center">Center (Post)</option>
            </select>
          </div>
          <div>
            <div style="font-size: 0.69rem; color: var(--text-dim); font-family: var(--font-mono); margin-bottom: 4px; text-transform: uppercase; font-weight: 600;">Font Style</div>
            <select id="selectFontStyle">
              <option value="sans" selected>Modern Sans-Serif</option>
              <option value="serif">Editorial Serif</option>
              <option value="mono">Classic Monospace</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Meme Media Attachment (Photo & Video) -->
      <div class="control-card">
        <div class="group-label">
          <span class="section-title">Meme Media Attachment</span>
          <span style="color: var(--gold); font-family: var(--font-mono); font-size: 0.68rem; font-weight: 700;">Photo / Video</span>
        </div>

        <div class="dropzone" id="dropzone">
          <div style="font-size: 1.2rem; margin-bottom: 4px; opacity: 0.85; font-family: var(--font-mono);">[ + ]</div>
          <div style="font-size: 0.78rem; font-weight: 700; font-family: var(--font-mono); letter-spacing: 0.04em;">Select or Drop Photo / Video</div>
          <div style="font-size: 0.69rem; color: var(--text-muted); font-family: var(--font-mono); margin-top: 4px;">JPG, PNG, GIF, MP4, WEBM — Crisp rectangular framing</div>
        </div>
        <input type="file" id="inputAttach" accept="image/*,video/*" style="display: none;">
        
        <div class="attach-preview-bar" id="attachPreviewBar">
          <div style="display: flex; align-items: center; gap: 8px; overflow: hidden;">
            <span id="attachTypeIcon" style="font-family: var(--font-mono); font-size: 0.76rem; color: var(--gold); font-weight: 700;">[MEDIA]</span>
            <span id="attachFileName" style="font-size: 0.76rem; font-family: var(--font-mono); color: var(--text-main); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 220px; font-weight: 600;">file</span>
          </div>
          <button class="btn btn-secondary btn-sm" id="btnRemoveAttach" style="color: #b03a3a;">✕ Remove</button>
        </div>

        <div id="videoControlsRow" style="display: none; margin-top: 8px; background: #ffffff; padding: 8px; border: 1.5px solid var(--border-hairline); box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
          <div style="display: flex; gap: 6px; justify-content: space-between;">
            <button class="btn btn-secondary btn-sm" id="btnToggleVideoPlay" style="flex: 1;">⏸️ Pause</button>
            <button class="btn btn-secondary btn-sm" id="btnToggleVideoMute" style="flex: 1;">🔇 Muted</button>
          </div>
        </div>
      </div>

      <!-- Export Actions -->
      <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 8px;">
        <button class="btn btn-primary" id="btnDownload" style="padding: 13px 20px; font-size: 0.86rem;">
          <span id="btnDownloadText">Download Post (1080p Lossless PNG)</span>
        </button>
        <div style="display: flex; gap: 6px;">
          <button class="btn btn-secondary" id="btnCopy" style="flex: 1;">
            <span>Copy to Clipboard</span>
          </button>
          <button class="btn btn-secondary" id="btnExportVideo" style="flex: 1; display: none;">
            <span>🎬 Export Video Meme</span>
          </button>
        </div>
      </div>

    </div>

    <!-- Right Live Canvas Workspace Pedestal (Warm Gallery Light Backdrop) -->
    <div class="preview-workspace">
      <div class="canvas-pedestal" id="canvasPedestal">
        <button type="button" class="btn-pedestal-expand" id="btnOpenFullscreen" title="Expand Fullscreen Preview">⛶ Fullscreen</button>
        <canvas id="postCanvas" width="1080" height="1350"></canvas>
      </div>
    </div>

  </div>

  <!-- Mobile Floating Quick Bar (Pinned on screens <= 960px) -->
  <div class="mobile-floating-bar" id="mobileFloatingBar">
    <button class="btn btn-secondary" id="btnMobileScrollTop">
      <span>👁️ View Post</span>
    </button>
    <button class="btn btn-primary" id="btnMobileDownload">
      <span>📥 Download 1080p</span>
    </button>
  </div>

  <!-- Hidden Media Containers -->
  <video id="activeVideo" playsinline loop muted style="display: none;"></video>
  <img id="activeImgAttach" style="display: none;">

  <!-- Toast Notification Box -->
  <div class="toast" id="toast">Settings Updated</div>

  <script>
    // System Master Credentials
    const AUTH_CREDS = {{
      username: 'hamster_boss',
      password: 'MogMaster#2026'
    }};

    const DEFAULT_HAMSTER_B64 = "{mog_b64}";

    const DEFAULTS = {{
      aspect: '4:5',
      width: 1080,
      height: 1350,
      name: 'Mr. Hamster',
      handle: '@mrr.hamster',
      text: 'flirting is easy until you have to flirt\\nwith someone you actually want.',
      pfpSrc: DEFAULT_HAMSTER_B64,
      pfpShape: 'circle', // 'circle' or 'square'
      pfpFrameColor: '#ffffff', // Crisp Titanium White default
      pfpSize: 96,
      headerAlign: 'left',
      fontStyle: 'sans',
      sparkle: true,
      verified: true,
      fontSize: 46,
      vAlign: 'center',
      textAlign: 'left'
    }};

    const state = Object.assign({{}}, DEFAULTS);
    document.getElementById('inputText').value = state.text.replace(/\\\\n/g, '\\n');

    let videoAnimId = null;

    const pfpImageObj = new Image();
    pfpImageObj.crossOrigin = 'anonymous';
    pfpImageObj.onload = () => render();
    pfpImageObj.src = state.pfpSrc;

    // Profile Avatar Upload Handling
    const inputPfpFile = document.getElementById('inputPfpFile');
    const btnUploadPfp = document.getElementById('btnUploadPfp');
    const btnResetPfp = document.getElementById('btnResetPfp');
    const activePfpImg = document.getElementById('activePfpImg');
    const pfpStatusBadge = document.getElementById('pfpStatusBadge');

    const btnPfpCircle = document.getElementById('btnPfpCircle');
    const btnPfpSquare = document.getElementById('btnPfpSquare');

    btnUploadPfp.addEventListener('click', () => inputPfpFile.click());

    inputPfpFile.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files[0]) {{
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onload = (evt) => {{
          state.pfpSrc = evt.target.result;
          pfpImageObj.src = state.pfpSrc;
          activePfpImg.src = state.pfpSrc;
          pfpStatusBadge.textContent = 'Custom Photo';
          showToast('Custom Avatar Loaded');
        }};
        reader.readAsDataURL(file);
      }}
    }});

    btnResetPfp.addEventListener('click', () => {{
      state.pfpSrc = DEFAULT_HAMSTER_B64;
      pfpImageObj.src = state.pfpSrc;
      activePfpImg.src = state.pfpSrc;
      pfpStatusBadge.textContent = 'Mog Hamster';
      inputPfpFile.value = '';
      showToast('Avatar Reset to Mog Hamster');
    }});

    // Avatar Shape Toggle
    btnPfpCircle.addEventListener('click', () => {{
      btnPfpCircle.classList.add('active');
      btnPfpSquare.classList.remove('active');
      state.pfpShape = 'circle';
      render();
    }});

    btnPfpSquare.addEventListener('click', () => {{
      btnPfpSquare.classList.add('active');
      btnPfpCircle.classList.remove('active');
      state.pfpShape = 'square';
      render();
    }});

    // Avatar Frame Color Listener
    const selectPfpFrameColor = document.getElementById('selectPfpFrameColor');
    const labelFrameColor = document.getElementById('labelFrameColor');
    selectPfpFrameColor.addEventListener('change', (e) => {{
      state.pfpFrameColor = e.target.value;
      const opt = e.target.options[e.target.selectedIndex].text.split('·')[0].trim();
      labelFrameColor.textContent = opt.toUpperCase();
      render();
    }});

    // Slider Stepper Buttons: Avatar Scale
    const rangePfpSize = document.getElementById('rangePfpSize');
    const labelPfpSize = document.getElementById('labelPfpSize');
    document.getElementById('btnPfpSizeMinus').addEventListener('click', () => {{
      let v = parseInt(rangePfpSize.value, 10) - 2;
      if (v < 60) v = 60;
      rangePfpSize.value = v;
      state.pfpSize = v;
      labelPfpSize.textContent = `${{v}} px`;
      render();
    }});
    document.getElementById('btnPfpSizePlus').addEventListener('click', () => {{
      let v = parseInt(rangePfpSize.value, 10) + 2;
      if (v > 150) v = 150;
      rangePfpSize.value = v;
      state.pfpSize = v;
      labelPfpSize.textContent = `${{v}} px`;
      render();
    }});
    rangePfpSize.addEventListener('input', (e) => {{
      state.pfpSize = parseInt(e.target.value, 10);
      labelPfpSize.textContent = `${{state.pfpSize}} px`;
      render();
    }});

    // Slider Stepper Buttons: Font Size
    const rangeFontSize = document.getElementById('rangeFontSize');
    const labelFontSize = document.getElementById('labelFontSize');
    document.getElementById('btnFontSizeMinus').addEventListener('click', () => {{
      let v = parseInt(rangeFontSize.value, 10) - 2;
      if (v < 26) v = 26;
      rangeFontSize.value = v;
      state.fontSize = v;
      labelFontSize.textContent = `${{v}} px`;
      render();
    }});
    document.getElementById('btnFontSizePlus').addEventListener('click', () => {{
      let v = parseInt(rangeFontSize.value, 10) + 2;
      if (v > 74) v = 74;
      rangeFontSize.value = v;
      state.fontSize = v;
      labelFontSize.textContent = `${{v}} px`;
      render();
    }});
    rangeFontSize.addEventListener('input', (e) => {{
      state.fontSize = parseInt(e.target.value, 10);
      labelFontSize.textContent = `${{state.fontSize}} px`;
      render();
    }});

    // Reset All Defaults Button
    document.getElementById('btnResetAllDefaults').addEventListener('click', () => {{
      state.fontSize = DEFAULTS.fontSize;
      state.pfpSize = DEFAULTS.pfpSize;
      state.vAlign = DEFAULTS.vAlign;
      state.textAlign = DEFAULTS.textAlign;
      state.headerAlign = DEFAULTS.headerAlign;
      state.fontStyle = DEFAULTS.fontStyle;
      state.pfpShape = DEFAULTS.pfpShape;
      state.pfpFrameColor = DEFAULTS.pfpFrameColor;

      rangeFontSize.value = state.fontSize;
      labelFontSize.textContent = `${{state.fontSize}} px`;
      rangePfpSize.value = state.pfpSize;
      labelPfpSize.textContent = `${{state.pfpSize}} px`;
      document.getElementById('selectVAlign').value = state.vAlign;
      document.getElementById('selectTextAlign').value = state.textAlign;
      document.getElementById('selectHeaderAlign').value = state.headerAlign;
      document.getElementById('selectFontStyle').value = state.fontStyle;
      selectPfpFrameColor.value = state.pfpFrameColor;
      labelFrameColor.textContent = 'CRISP WHITE';

      btnPfpCircle.classList.add('active');
      btnPfpSquare.classList.remove('active');

      render();
      showToast('Default Settings Restored');
    }});

    // Aspect Ratio Toggles & Dynamic Frame Synchronization
    const canvas = document.getElementById('postCanvas');
    const canvasPedestal = document.getElementById('canvasPedestal');

    function syncAspectRatio() {{
      const aspectStr = `${{state.width}} / ${{state.height}}`;
      canvas.style.aspectRatio = aspectStr;
      canvasPedestal.style.aspectRatio = aspectStr;
    }}

    document.querySelectorAll('.btn-ratio').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.btn-ratio').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        state.aspect = btn.dataset.ratio;
        state.width = parseInt(btn.dataset.w, 10);
        state.height = parseInt(btn.dataset.h, 10);
        canvas.width = state.width;
        canvas.height = state.height;

        syncAspectRatio();

        document.getElementById('currentRatioBadge').textContent = `${{state.width}} × ${{state.height}}`;
        render();
        showToast(`Aspect Ratio: ${{state.aspect}} (${{state.width}}×${{state.height}})`);
      }});
    }});

    // Quick text helpers
    const inputText = document.getElementById('inputText');
    document.getElementById('btnSampleText').addEventListener('click', () => {{
      inputText.value = 'flirting is easy until you have to flirt\\nwith someone you actually want.';
      state.text = inputText.value;
      render();
      showToast('Sample Quote Inserted');
    }});

    document.getElementById('btnClearText').addEventListener('click', () => {{
      inputText.value = '';
      state.text = '';
      render();
      showToast('Text Cleared');
    }});

    function getLines(ctx, text, maxWidth) {{
      const lines = [];
      const paragraphs = text.split('\\n');
      for (let p = 0; p < paragraphs.length; p++) {{
        const words = paragraphs[p].split(' ');
        let currentLine = words[0] || '';
        for (let i = 1; i < words.length; i++) {{
          const testLine = currentLine + ' ' + words[i];
          if (ctx.measureText(testLine).width <= maxWidth) {{
            currentLine = testLine;
          }} else {{
            lines.push(currentLine);
            currentLine = words[i];
          }}
        }}
        lines.push(currentLine);
      }}
      return lines;
    }}

    // Accurate Verified Badge (12-Point Scalloped Starburst)
    function drawAccurateVerifiedBadge(ctx, centerX, centerY, size) {{
      const radius = size / 2;
      ctx.save();

      ctx.fillStyle = '#1d9bf0';
      ctx.beginPath();
      
      const points = 12;
      const innerRadius = radius * 0.88;
      for (let i = 0; i < points * 2; i++) {{
        const r = (i % 2 === 0) ? radius : innerRadius;
        const angle = (i * Math.PI) / points - Math.PI / 2;
        const x = centerX + Math.cos(angle) * r;
        const y = centerY + Math.sin(angle) * r;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }}
      ctx.closePath();
      ctx.fill();

      // Sharp white checkmark
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = Math.max(2, size * 0.125);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.beginPath();
      ctx.moveTo(centerX - radius * 0.42, centerY - radius * 0.02);
      ctx.lineTo(centerX - radius * 0.1, centerY + radius * 0.32);
      ctx.lineTo(centerX + radius * 0.44, centerY - radius * 0.34);
      ctx.stroke();

      ctx.restore();
    }}

    // Master Canvas Render Engine
    function render() {{
      const ctx = canvas.getContext('2d');
      const W = canvas.width;
      const H = canvas.height;

      // 100% OLED PITCH BLACK BACKGROUND
      ctx.fillStyle = '#000000';
      ctx.fillRect(0, 0, W, H);

      const marginX = (W === 1920) ? 140 : 80;
      const contentWidth = W - (marginX * 2);

      // Typography Configuration
      let fontFamily = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      if (state.fontStyle === 'serif') fontFamily = 'Georgia, "Playfair Display", "Times New Roman", serif';
      if (state.fontStyle === 'mono') fontFamily = '"SF Mono", "Cascadia Code", Consolas, monospace';

      ctx.font = `400 ${{state.fontSize}}px ${{fontFamily}}`;
      const lineHeight = Math.round(state.fontSize * 1.48);
      const lines = getLines(ctx, state.text, contentWidth);
      const textBlockHeight = lines.length * lineHeight;

      const pfpSize = state.pfpSize;
      const isCenteredHeader = (state.headerAlign === 'center');

      let headerHeight = pfpSize;
      if (isCenteredHeader) {{
        headerHeight = pfpSize + 72; // Space for stacked name & handle below pfp
      }}

      // Check Media Attachment
      let mediaHeight = 0;
      let mediaWidth = contentWidth;
      const mediaGap = 36;
      let activeMediaObj = null;

      if (state.attachType === 'image' && imgAttachObj.complete && imgAttachObj.naturalWidth > 0) {{
        activeMediaObj = imgAttachObj;
      }} else if (state.attachType === 'video' && videoElement.readyState >= 2) {{
        activeMediaObj = videoElement;
      }}

      if (activeMediaObj) {{
        const naturalW = activeMediaObj.videoWidth || activeMediaObj.naturalWidth || 1;
        const naturalH = activeMediaObj.videoHeight || activeMediaObj.naturalHeight || 1;
        const maxMediaH = Math.round(H * 0.42);
        mediaHeight = Math.round((contentWidth / naturalW) * naturalH);
        if (mediaHeight > maxMediaH) {{
          mediaHeight = maxMediaH;
          mediaWidth = Math.round((maxMediaH / naturalH) * naturalW);
        }}
      }}

      const headerToTextGap = 34;
      let totalBlockHeight = headerHeight + headerToTextGap + textBlockHeight;
      if (activeMediaObj) {{
        totalBlockHeight += mediaGap + mediaHeight;
      }}

      // Determine Start Y
      let startY = 120;
      if (state.vAlign === 'center') {{
        startY = Math.max(90, Math.round((H - totalBlockHeight) / 2));
      }} else if (state.aspect === '9:16') {{
        startY = 240;
      }}

      // 1. Render Profile Avatar
      const radius = pfpSize / 2;
      let pfpX, pfpY;

      if (isCenteredHeader) {{
        pfpX = Math.round(W / 2 - radius);
        pfpY = startY;
      }} else {{
        pfpX = marginX;
        pfpY = startY;
      }}

      ctx.save();
      ctx.beginPath();
      if (state.pfpShape === 'square') {{
        ctx.rect(pfpX, pfpY, pfpSize, pfpSize);
      }} else {{
        ctx.arc(pfpX + radius, pfpY + radius, radius, 0, Math.PI * 2);
      }}
      ctx.fillStyle = '#ffffff';
      ctx.fill();
      ctx.clip();

      if (pfpImageObj.complete && pfpImageObj.naturalWidth > 0) {{
        ctx.drawImage(pfpImageObj, pfpX, pfpY, pfpSize, pfpSize);
      }}
      ctx.restore();

      // Defined Avatar Frame Rim (Crisp, High Visibility Border)
      if (state.pfpFrameColor && state.pfpFrameColor !== 'none') {{
        ctx.save();
        const strokeW = Math.max(5, Math.round(pfpSize * 0.052));
        ctx.lineWidth = strokeW;
        ctx.strokeStyle = state.pfpFrameColor;
        ctx.beginPath();
        if (state.pfpShape === 'square') {{
          // Sharp rectangular box frame
          ctx.strokeRect(pfpX, pfpY, pfpSize, pfpSize);
        }} else {{
          // Smooth circular ring frame
          ctx.arc(pfpX + radius, pfpY + radius, radius, 0, Math.PI * 2);
          ctx.stroke();
        }}
        ctx.restore();
      }}

      // 2. Render Name, Sparkle & Centered Verified Badge
      let displayName = state.name;
      if (state.sparkle && !displayName.includes('✨')) displayName += ' ✨';

      const fontName = '700 32px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      const fontHandle = '400 27px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';

      if (isCenteredHeader) {{
        const nameY = pfpY + pfpSize + 36;
        const handleY = pfpY + pfpSize + 70;

        ctx.font = fontName;
        ctx.fillStyle = '#f7f9f9';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        const nameMetrics = ctx.measureText(displayName);
        const badgeSize = 25;
        const badgeGap = 8;
        const totalW = nameMetrics.width + (state.verified ? (badgeSize + badgeGap) : 0);
        const startTextX = Math.round(W / 2 - totalW / 2 + nameMetrics.width / 2);

        ctx.fillText(displayName, startTextX, nameY);

        if (state.verified) {{
          const badgeCenterX = Math.round(startTextX + nameMetrics.width / 2 + badgeGap + badgeSize / 2);
          drawAccurateVerifiedBadge(ctx, badgeCenterX, nameY, badgeSize);
        }}

        ctx.font = fontHandle;
        ctx.fillStyle = '#71767b';
        ctx.fillText(state.handle, Math.round(W / 2), handleY);

      }} else {{
        const textStartX = pfpX + pfpSize + 18;
        const nameY = pfpY + Math.round(pfpSize * 0.34);
        const handleY = pfpY + Math.round(pfpSize * 0.76);

        ctx.font = fontName;
        ctx.fillStyle = '#f7f9f9';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'middle';
        ctx.fillText(displayName, textStartX, nameY);

        if (state.verified) {{
          const nameMetrics = ctx.measureText(displayName);
          const badgeSize = 25;
          const badgeGap = 8;
          const badgeCenterX = Math.round(textStartX + nameMetrics.width + badgeGap + badgeSize / 2);
          drawAccurateVerifiedBadge(ctx, badgeCenterX, nameY, badgeSize);
        }}

        ctx.font = fontHandle;
        ctx.fillStyle = '#71767b';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'middle';
        ctx.fillText(state.handle, textStartX, handleY);
      }}

      // 3. Render Post Thought / Quote Text
      const textStartY = startY + headerHeight + headerToTextGap;
      ctx.font = `400 ${{state.fontSize}}px ${{fontFamily}}`;
      ctx.fillStyle = '#f7f9f9';
      ctx.textBaseline = 'top';

      if (state.textAlign === 'center') {{
        ctx.textAlign = 'center';
        for (let i = 0; i < lines.length; i++) {{
          ctx.fillText(lines[i], Math.round(W / 2), textStartY + (i * lineHeight));
        }}
      }} else {{
        ctx.textAlign = 'left';
        for (let i = 0; i < lines.length; i++) {{
          ctx.fillText(lines[i], marginX, textStartY + (i * lineHeight));
        }}
      }}

      // 4. Render Meme Media Attachment (if present)
      if (activeMediaObj) {{
        const mediaY = textStartY + textBlockHeight + mediaGap;
        let mediaX = marginX;
        if (state.textAlign === 'center') {{
          mediaX = Math.round(W / 2 - mediaWidth / 2);
        }}

        ctx.save();
        ctx.strokeStyle = '#282828';
        ctx.lineWidth = 2;
        ctx.strokeRect(mediaX, mediaY, mediaWidth, mediaHeight);

        ctx.drawImage(activeMediaObj, mediaX, mediaY, mediaWidth, mediaHeight);
        ctx.restore();
      }}

      document.getElementById('charCount').textContent = `${{state.text.length}} chars`;
    }}

    // Real-Time Input Event Listeners
    inputText.addEventListener('input', (e) => {{
      state.text = e.target.value;
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

    document.getElementById('selectVAlign').addEventListener('change', (e) => {{
      state.vAlign = e.target.value;
      render();
    }});

    document.getElementById('selectTextAlign').addEventListener('change', (e) => {{
      state.textAlign = e.target.value;
      render();
    }});

    document.getElementById('selectHeaderAlign').addEventListener('change', (e) => {{
      state.headerAlign = e.target.value;
      render();
    }});

    document.getElementById('selectFontStyle').addEventListener('change', (e) => {{
      state.fontStyle = e.target.value;
      render();
    }});

    // Meme Media Dropzone & Attachment Handling
    const dropzone = document.getElementById('dropzone');
    const inputAttach = document.getElementById('inputAttach');
    const attachPreviewBar = document.getElementById('attachPreviewBar');
    const attachFileName = document.getElementById('attachFileName');
    const attachTypeIcon = document.getElementById('attachTypeIcon');
    const btnRemoveAttach = document.getElementById('btnRemoveAttach');
    const videoControlsRow = document.getElementById('videoControlsRow');
    const videoElement = document.getElementById('activeVideo');
    const imgAttachObj = document.getElementById('activeImgAttach');
    const btnToggleVideoPlay = document.getElementById('btnToggleVideoPlay');
    const btnToggleVideoMute = document.getElementById('btnToggleVideoMute');
    const btnExportVideo = document.getElementById('btnExportVideo');

    dropzone.addEventListener('click', () => inputAttach.click());

    dropzone.addEventListener('dragover', (e) => {{
      e.preventDefault();
      dropzone.style.borderColor = 'var(--gold)';
    }});
    dropzone.addEventListener('dragleave', () => {{
      dropzone.style.borderColor = 'var(--border-hairline)';
    }});
    dropzone.addEventListener('drop', (e) => {{
      e.preventDefault();
      dropzone.style.borderColor = 'var(--border-hairline)';
      if (e.dataTransfer.files && e.dataTransfer.files[0]) {{
        handleMediaFile(e.dataTransfer.files[0]);
      }}
    }});

    inputAttach.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files[0]) {{
        handleMediaFile(e.target.files[0]);
      }}
    }});

    function handleMediaFile(file) {{
      const isVid = file.type.startsWith('video/');
      const url = URL.createObjectURL(file);

      if (isVid) {{
        state.attachType = 'video';
        videoElement.src = url;
        videoElement.play();
        attachTypeIcon.textContent = '[VIDEO]';
        videoControlsRow.style.display = 'block';
        btnExportVideo.style.display = 'block';

        if (!videoAnimId) {{
          function step() {{
            if (state.attachType === 'video') {{
              render();
              videoAnimId = requestAnimationFrame(step);
            }}
          }}
          videoAnimId = requestAnimationFrame(step);
        }}
      }} else {{
        state.attachType = 'image';
        imgAttachObj.onload = () => render();
        imgAttachObj.src = url;
        attachTypeIcon.textContent = '[PHOTO]';
        videoControlsRow.style.display = 'none';
        btnExportVideo.style.display = 'none';
        if (videoAnimId) {{
          cancelAnimationFrame(videoAnimId);
          videoAnimId = null;
        }}
      }}

      attachFileName.textContent = file.name;
      attachPreviewBar.style.display = 'flex';
      showToast(`Attached: ${{file.name}}`);
    }}

    btnRemoveAttach.addEventListener('click', () => {{
      state.attachType = null;
      attachPreviewBar.style.display = 'none';
      videoControlsRow.style.display = 'none';
      btnExportVideo.style.display = 'none';
      inputAttach.value = '';
      if (videoAnimId) {{
        cancelAnimationFrame(videoAnimId);
        videoAnimId = null;
      }}
      videoElement.pause();
      render();
      showToast('Attachment Removed');
    }});

    btnToggleVideoPlay.addEventListener('click', () => {{
      if (videoElement.paused) {{
        videoElement.play();
        btnToggleVideoPlay.textContent = '⏸️ Pause';
      }} else {{
        videoElement.pause();
        btnToggleVideoPlay.textContent = '▶️ Play';
      }}
    }});

    btnToggleVideoMute.addEventListener('click', () => {{
      videoElement.muted = !videoElement.muted;
      btnToggleVideoMute.textContent = videoElement.muted ? '🔇 Muted' : '🔊 Sound';
    }});

    // Lossless PNG Download
    document.getElementById('btnDownload').addEventListener('click', () => {{
      render();
      const a = document.createElement('a');
      const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
      a.download = `mrhamster_${{state.aspect.replace(':', '-')}}_${{timestamp}}.png`;
      a.href = canvas.toDataURL('image/png', 1.0);
      a.click();
      showToast('Lossless 1080p Post Downloaded');
    }});

    // Mobile Pinned Bar Actions
    document.getElementById('btnMobileDownload').addEventListener('click', () => {{
      document.getElementById('btnDownload').click();
    }});

    document.getElementById('btnMobileScrollTop').addEventListener('click', () => {{
      document.querySelector('.preview-workspace').scrollIntoView({{ behavior: 'smooth' }});
    }});

    // Fullscreen Overlay Preview
    const fullscreenOverlay = document.getElementById('fullscreenOverlay');
    const fullscreenImg = document.getElementById('fullscreenImg');
    const fullscreenRatioBadge = document.getElementById('fullscreenRatioBadge');
    const btnOpenFullscreen = document.getElementById('btnOpenFullscreen');
    const btnCloseFullscreen = document.getElementById('btnCloseFullscreen');
    const btnFullscreenDownload = document.getElementById('btnFullscreenDownload');

    function openFullscreenModal() {{
      render();
      fullscreenImg.src = canvas.toDataURL('image/png', 1.0);
      fullscreenRatioBadge.textContent = `${{state.aspect}} · ${{state.width}} × ${{state.height}}`;
      fullscreenOverlay.classList.remove('hidden');
    }}

    btnOpenFullscreen.addEventListener('click', openFullscreenModal);
    canvas.addEventListener('click', () => {{
      if (window.innerWidth <= 960) openFullscreenModal();
    }});
    btnCloseFullscreen.addEventListener('click', () => fullscreenOverlay.classList.add('hidden'));
    btnFullscreenDownload.addEventListener('click', () => {{
      document.getElementById('btnDownload').click();
      fullscreenOverlay.classList.add('hidden');
    }});

    // Copy to Clipboard
    document.getElementById('btnCopy').addEventListener('click', async () => {{
      render();
      try {{
        canvas.toBlob(async (blob) => {{
          await navigator.clipboard.write([
            new ClipboardItem({{ 'image/png': blob }})
          ]);
          showToast('Copied to Clipboard!');
        }});
      }} catch (err) {{
        showToast('Clipboard access not permitted');
      }}
    }});

    // Toast Utility
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2600);
    }}

    // Credentials Gate Check & Handlers
    function checkAuth() {{
      const auth = sessionStorage.getItem('mr_hamster_auth');
      const overlay = document.getElementById('authOverlay');
      if (auth === 'granted') {{
        overlay.classList.add('hidden');
      }} else {{
        overlay.classList.remove('hidden');
        setTimeout(() => {{
          const uInput = document.getElementById('authUsername');
          if (uInput) uInput.focus();
        }}, 100);
      }}
    }}

    window.handleLogin = function() {{
      const user = document.getElementById('authUsername').value.trim();
      const pass = document.getElementById('authPassword').value;
      const errorBox = document.getElementById('authError');

      if (user === AUTH_CREDS.username && pass === AUTH_CREDS.password) {{
        sessionStorage.setItem('mr_hamster_auth', 'granted');
        document.getElementById('authOverlay').classList.add('hidden');
        errorBox.style.display = 'none';
        showToast('WELCOME TO MR. HAMSTER ATELIER');
      }} else {{
        errorBox.style.display = 'block';
        document.getElementById('authPassword').value = '';
        document.getElementById('authPassword').focus();
      }}
    }};

    document.getElementById('btnLockStudio').addEventListener('click', () => {{
      sessionStorage.removeItem('mr_hamster_auth');
      document.getElementById('authUsername').value = '';
      document.getElementById('authPassword').value = '';
      document.getElementById('authError').style.display = 'none';
      document.getElementById('authOverlay').classList.remove('hidden');
      showToast('STUDIO LOCKED');
    }});

    checkAuth();
    syncAspectRatio();

    // Initial Render
    render();
  </script>
</body>
</html>
"""

# Write index.html
with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Wrote index.html ({len(html_content)} bytes)")

# Write generator.html
with open(os.path.join(BASE_DIR, "generator.html"), "w", encoding="utf-8") as f:
    f.write(html_content)
print("Wrote generator.html")
