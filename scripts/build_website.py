# -*- coding: utf-8 -*-
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
      letter-spacing: -0.01em;
    }}

    /* Understated Minimalist Scrollbars */
    ::-webkit-scrollbar {{
      width: 7px;
      height: 7px;
    }}
    ::-webkit-scrollbar-track {{
      background: var(--bg-sidebar);
    }}
    ::-webkit-scrollbar-thumb {{
      background: #beb6a5;
      border: 1px solid var(--border-hairline);
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #9c9381;
    }}

    /* Top Atelier Header (Bold Contrast & Defined Shadows) */
    header {{
      background: #e8e2d6;
      border-bottom: 1.5px solid #c8c0b0;
      padding: 13px 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 14px rgba(32, 28, 22, 0.08);
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    /* Brand Logo Box - Bold Contrast & High Visibility */
    .brand-box {{
      width: 42px;
      height: 42px;
      background: #1c1b18;
      border: 1.5px solid #1c1b18;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
      box-shadow: 2px 2px 0px rgba(0, 0, 0, 0.25), 0 3px 8px rgba(0, 0, 0, 0.15);
      flex-shrink: 0;
    }}

    .title-group {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .app-title {{
      font-family: var(--font-serif);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .handle-badge {{
      background: #1c1b18;
      color: #dfba6c;
      border: 1px solid #1c1b18;
      padding: 2px 9px;
      font-size: 0.74rem;
      font-weight: 700;
      font-family: var(--font-mono);
      letter-spacing: 0.05em;
      box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.15);
    }}

    .subtitle {{
      font-size: 9.5px;
      color: var(--text-dim);
      font-family: var(--font-mono);
      letter-spacing: 0.14em;
      text-transform: uppercase;
      font-weight: 600;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .status-tag {{
      font-size: 10px;
      font-family: var(--font-mono);
      color: #52401c;
      background: #f5eedc;
      border: 1.5px solid #cfbe95;
      padding: 7px 13px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.06);
    }}

    /* Elegant Box Buttons with Crisp Tactile Shadows */
    .btn {{
      padding: 9px 18px;
      font-size: 0.76rem;
      font-weight: 700;
      font-family: var(--font-mono);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      border: 1.5px solid transparent;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.14s ease-in-out;
      text-decoration: none;
      user-select: none;
    }}

    .btn-primary {{
      background: #1c1b18;
      color: #f7f6f2;
      border-color: #1c1b18;
      box-shadow: 0 4px 14px rgba(28, 27, 24, 0.25), 3px 3px 0px rgba(0, 0, 0, 0.2);
    }}
    .btn-primary:hover {{
      background: var(--gold);
      color: #ffffff;
      border-color: var(--gold);
      box-shadow: 0 6px 18px rgba(158, 122, 47, 0.35), 3px 3px 0px rgba(110, 85, 30, 0.4);
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
      padding: 6px 13px;
      font-size: 0.72rem;
    }}

    /* Main Atelier Layout */
    .app-layout {{
      display: grid;
      grid-template-columns: 460px 1fr;
      flex: 1;
      overflow: hidden;
      min-height: calc(100vh - 67px);
    }}

    /* Mobile Mode Switcher Bar (Hidden on Desktop, Visible <= 960px) */
    .mobile-mode-bar {{
      display: none;
      background: #dfd8cb;
      border-bottom: 1.5px solid var(--border-hairline);
      padding: 8px 12px;
      gap: 8px;
      position: sticky;
      top: 56px;
      z-index: 95;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    .mobile-mode-btn {{
      flex: 1;
      padding: 10px 14px;
      font-size: 0.74rem;
      font-family: var(--font-mono);
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      background: #ffffff;
      color: var(--text-dim);
      border: 1.5px solid var(--border-hairline);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      transition: all 0.12s;
      min-height: 42px;
    }}
    .mobile-mode-btn.active {{
      background: #1c1b18;
      color: #ffffff;
      border-color: #1c1b18;
      box-shadow: 0 3px 8px rgba(0,0,0,0.18);
    }}
    .mobile-preview-badge {{
      background: var(--gold);
      color: #ffffff;
      font-size: 0.65rem;
      padding: 2px 6px;
      font-weight: 800;
    }}

    /* Mobile Floating Action Bar */
    .mobile-floating-bar {{
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(232, 226, 214, 0.97);
      backdrop-filter: blur(12px);
      border-top: 1.5px solid var(--border-hairline);
      padding: 10px 14px;
      gap: 10px;
      z-index: 90;
      box-shadow: 0 -4px 18px rgba(0,0,0,0.12);
    }}
    .mobile-floating-bar .btn {{
      flex: 1;
      padding: 12px 14px;
      font-size: 0.8rem;
      min-height: 46px;
    }}

    @media (max-width: 960px) {{
      body {{
        overflow-x: hidden;
        overflow-y: auto;
        -webkit-overflow-scrolling: touch;
      }}

      .mobile-mode-bar {{
        display: flex;
      }}
      .mobile-floating-bar {{
        display: flex;
      }}

      .app-layout {{
        display: block !important;
        min-height: auto;
        overflow: visible !important;
      }}

      .controls-panel {{
        max-height: none !important;
        overflow-y: visible !important;
        padding: 14px 12px 85px 12px !important;
        border-right: none !important;
      }}

      .preview-workspace {{
        padding: 18px 12px 85px 12px !important;
        min-height: calc(100vh - 125px) !important;
      }}

      /* Smooth Tab Display Switch */
      .app-layout.view-controls .controls-panel {{
        display: flex !important;
      }}
      .app-layout.view-controls .preview-workspace {{
        display: none !important;
      }}

      .app-layout.view-preview .controls-panel {{
        display: none !important;
      }}
      .app-layout.view-preview .preview-workspace {{
        display: flex !important;
      }}

      .canvas-pedestal {{
        max-width: 100% !important;
        max-height: 70vh !important;
        box-shadow: 0 14px 40px rgba(0, 0, 0, 0.4), 0 0 0 1.5px rgba(0, 0, 0, 0.25) !important;
      }}

      #postCanvas {{
        max-width: 100% !important;
        max-height: 68vh !important;
        width: auto !important;
        height: auto !important;
      }}

      /* Prevent iOS auto-zoom on input focus */
      .input-field, .textarea-field, select {{
        font-size: 16px !important;
        padding: 12px 10px !important;
      }}

      /* Touch-optimized slider */
      input[type=range] {{
        height: 7px !important;
      }}
      input[type=range]::-webkit-slider-thumb {{
        width: 26px !important;
        height: 32px !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
      }}

      /* Touch targets for buttons */
      .btn {{
        min-height: 44px;
      }}
      .btn-ratio {{
        min-height: 52px;
        padding: 10px 8px !important;
      }}
      .btn-ratio span.label {{
        font-size: 0.72rem !important;
      }}
      .btn-ratio span.dim {{
        font-size: 0.62rem !important;
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
        font-size: 0.92rem !important;
        gap: 6px !important;
      }}
      .subtitle, .status-tag {{
        display: none !important;
      }}
      .header-actions .btn {{
        padding: 6px 9px !important;
        font-size: 0.68rem !important;
        min-height: 34px !important;
      }}
    }}

    /* Left Control Panel (Rich Warm Stone with Depth) */
    .controls-panel {{
      background: var(--bg-sidebar);
      border-right: 1.5px solid var(--border-hairline);
      padding: 22px;
      overflow-y: auto;
      max-height: calc(100vh - 67px);
      display: flex;
      flex-direction: column;
      gap: 16px;
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
      min-height: 120px;
      resize: vertical;
      line-height: 1.55;
      font-family: var(--font-sans);
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
      border: 1.5px solid #a89f8d;
      border-left: 4px solid var(--gold);
      color: var(--text-main);
      box-shadow: 0 4px 12px rgba(158, 122, 47, 0.12), 2px 2px 0px rgba(158, 122, 47, 0.25);
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
      border: none;
      background: #ffffff;
      cursor: pointer;
      text-align: center;
      transition: all 0.12s;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }}

    .btn-toggle:hover {{
      color: var(--text-main);
      background: #f5f0e4;
    }}

    .btn-toggle.active {{
      background: #ede5d5;
      color: var(--text-main);
      box-shadow: inset 0 -2px 0 var(--gold);
    }}

    /* Profile Avatar Slot (High Contrast & Clear Boundary) */
    .pfp-slot-container {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 4px 0;
    }}

    .pfp-preview-box {{
      width: 82px;
      height: 82px;
      background: #ded7c9;
      border: 2px solid #a39985;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      position: relative;
      box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.15), 0 2px 6px rgba(0, 0, 0, 0.08);
    }}

    .pfp-preview-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    .pfp-upload-actions {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      flex: 1;
    }}

    .pfp-upload-btn-wrap {{
      display: flex;
      gap: 6px;
    }}

    /* Tactile Retro Sliders */
    .slider-row {{
      margin-top: 12px;
    }}
    .slider-label-row {{
      display: flex;
      justify-content: space-between;
      font-size: 0.71rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      margin-bottom: 6px;
      letter-spacing: 0.05em;
      font-weight: 600;
    }}

    input[type=range] {{
      -webkit-appearance: none;
      appearance: none;
      width: 100%;
      height: 3px;
      background: #bfb7a6;
      outline: none;
      border: none;
    }}
    input[type=range]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      appearance: none;
      width: 12px;
      height: 18px;
      background: #1c1b18;
      border: 1.5px solid var(--gold);
      cursor: pointer;
      transition: background 0.1s;
      box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }}
    input[type=range]::-webkit-slider-thumb:hover {{
      background: var(--gold);
    }}

    /* Dropzone (Decent & Vintage Minimalist) */
    .dropzone {{
      border: 2px dashed #b5ab99;
      padding: 20px;
      text-align: center;
      cursor: pointer;
      background: #faf8f4;
      transition: all 0.15s;
      box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.04);
    }}
    .dropzone:hover, .dropzone.dragover {{
      border-color: var(--gold);
      background: #f4efe4;
      box-shadow: inset 0 2px 8px rgba(158, 122, 47, 0.1);
    }}

    .attach-preview-bar {{
      margin-top: 8px;
      display: none;
      align-items: center;
      justify-content: space-between;
      background: #ffffff;
      padding: 8px 12px;
      border: 1.5px solid var(--border-hairline);
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
    }}

    /* Right Preview Pedestal (Rich Warm Gallery Wall - Post Canvas Remains 100% Black) */
    .preview-workspace {{
      background: #d4cdc0;
      background-image: radial-gradient(rgba(0, 0, 0, 0.1) 1px, transparent 1px);
      background-size: 22px 22px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 28px;
      position: relative;
      overflow: auto;
    }}

    .canvas-pedestal {{
      box-shadow: 0 28px 75px rgba(0, 0, 0, 0.4), 0 8px 24px rgba(0, 0, 0, 0.2), 0 0 0 2px rgba(0, 0, 0, 0.25);
      overflow: hidden;
      background: #000000; /* POST REMAINS STRICT OLED BLACK */
      max-width: 100%;
      max-height: 86vh;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }}

    #postCanvas {{
      display: block;
      max-width: 100%;
      max-height: 84vh;
      width: auto;
      height: auto;
      object-fit: contain;
      background: #000000; /* POST REMAINS PURE BLACK */
    }}

    /* Retro Minimalist Checkboxes */
    .checkbox-container {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--text-dim);
      cursor: pointer;
      user-select: none;
      font-weight: 600;
    }}
    .checkbox-container input[type="checkbox"] {{
      -webkit-appearance: none;
      appearance: none;
      width: 16px;
      height: 16px;
      background: #ffffff;
      border: 1.5px solid var(--border-hairline);
      display: grid;
      place-content: center;
      cursor: pointer;
      box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.05);
    }}
    .checkbox-container input[type="checkbox"]:checked {{
      background: #1c1b18;
      border-color: #1c1b18;
    }}
    .checkbox-container input[type="checkbox"]:checked::before {{
      content: "✔";
      font-size: 10px;
      color: #ffffff;
      font-weight: 900;
    }}

    /* Toast Notification */
    #toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #1c1b18;
      color: #f7f6f2;
      border: 1.5px solid #333333;
      border-left: 4px solid var(--gold);
      padding: 11px 20px;
      font-size: 0.8rem;
      font-family: var(--font-mono);
      letter-spacing: 0.05em;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.35);
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transform: translateY(6px);
      transition: all 0.16s ease;
    }}
    #toast.show {{
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }}

    /* Credentials Gate Lockscreen */
    #authOverlay {{
      position: fixed;
      inset: 0;
      background: rgba(22, 20, 17, 0.88);
      backdrop-filter: blur(8px);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      transition: opacity 0.25s ease, visibility 0.25s ease;
    }}
    #authOverlay.hidden {{
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }}
    .auth-card {{
      background: #fbfaf7;
      border: 2px solid #1c1b18;
      box-shadow: 0 16px 50px rgba(0, 0, 0, 0.4), 6px 6px 0px #1c1b18;
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

  <!-- Top Atelier Header -->
  <header>
    <div class="header-left">
      <div class="brand-box" title="Mr. Hamster Mascot">🐹</div>
      <div class="title-group">
        <div class="app-title">
          <span>Mr. Hamster</span>
          <span class="handle-badge">@mrr.hamster</span>
        </div>
        <div class="subtitle">Post & Meme Atelier · Minimalist Edition</div>
      </div>
    </div>

    <div class="header-actions">
      <span class="status-tag">1080P Native</span>
      <button class="btn btn-secondary btn-sm" id="btnLockStudio" title="Lock the studio with credentials">
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

  <!-- Mobile Mode Switcher (Visible only on mobile/tablet <= 960px) -->
  <div class="mobile-mode-bar" id="mobileModeBar">
    <button class="mobile-mode-btn active" id="tabBtnControls">
      <span>✍️ EDIT CONTROLS</span>
    </button>
    <button class="mobile-mode-btn" id="tabBtnPreview">
      <span>👁️ LIVE PREVIEW</span>
      <span class="mobile-preview-badge" id="mobilePreviewRatioBadge">4:5</span>
    </button>
  </div>

  <!-- Main Atelier Layout -->
  <div class="app-layout view-controls">
    
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
                <span>Upload Photo</span>
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
            <button class="btn-toggle active" id="btnPfpCircle">● Circle</button>
            <button class="btn-toggle" id="btnPfpSquare">■ Square Box</button>
          </div>
        </div>

        <!-- Avatar Frame Rim Color (Matches Black Post & White PFP) -->
        <div style="margin-top: 12px;">
          <div class="slider-label-row">
            <span>Avatar Frame Rim Color</span>
            <span id="labelFrameColor" style="font-family: var(--font-mono); font-size: 0.68rem; color: var(--gold); font-weight: 700;">SLATE TITANIUM</span>
          </div>
          <select id="selectPfpFrameColor">
            <option value="#4a4f5c" selected>Slate Titanium (#4a4f5c) · Matches Post</option>
            <option value="#2b2d35">Deep Charcoal (#2b2d35) · Subtle Dark Rim</option>
            <option value="#9e7d3b">Vintage Brass (#9e7d3b) · Atelier Gold</option>
            <option value="#ded8cc">Warm Ivory (#ded8cc) · High Contrast</option>
            <option value="#737987">Classic Platinum (#737987) · Clean Metal Rim</option>
            <option value="none">None (Borderless)</option>
          </select>
        </div>

        <!-- Avatar Scale Slider -->
        <div class="slider-row">
          <div class="slider-label-row">
            <span>Avatar Scale</span>
            <span id="labelPfpSize">96 px</span>
          </div>
          <input type="range" id="rangePfpSize" min="60" max="150" value="96">
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
          <span id="charCount" style="color: var(--text-muted); font-family: var(--font-mono);">0 chars</span>
        </div>
        <textarea class="textarea-field" id="inputText" placeholder="Write whatever thought, quote, or observation you want..."></textarea>
      </div>

      <!-- Typography & Layout Settings -->
      <div class="control-card">
        <div class="group-label">
          <span class="section-title">Typography & Layout</span>
        </div>
        
        <div class="slider-row" style="margin-top: 0; margin-bottom: 14px;">
          <div class="slider-label-row">
            <span>Font Size</span>
            <span id="labelFontSize">46 px</span>
          </div>
          <input type="range" id="rangeFontSize" min="26" max="74" value="46">
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
      <div class="canvas-pedestal">
        <canvas id="postCanvas" width="1080" height="1350"></canvas>
      </div>
    </div>

  </div>

  <!-- Mobile Floating Quick Bar -->
  <div class="mobile-floating-bar" id="mobileFloatingBar">
    <button class="btn btn-secondary btn-sm" id="btnMobileQuickToggle">
      <span>👁️ View Live Post</span>
    </button>
    <button class="btn btn-primary btn-sm" id="btnMobileDownload" onclick="document.getElementById('btnDownload').click()">
      <span>📥 Download 1080p</span>
    </button>
  </div>

  <!-- Minimalist Toast Notification -->
  <div id="toast">Action Completed</div>

  <!-- Studio Script Logic -->
  <script>
    const DEFAULT_HAMSTER_B64 = "{mog_b64}";

    const canvas = document.getElementById('postCanvas');
    const ctx = canvas.getContext('2d');

    // Default configuration values
    const DEFAULTS = {{
      aspect: '4:5',
      width: 1080,
      height: 1350,
      name: 'Mr. Hamster',
      handle: '@mrr.hamster',
      text: 'flirting is easy until you have to flirt\\nwith someone you actually want.',
      pfpSrc: DEFAULT_HAMSTER_B64,
      pfpShape: 'circle', // 'circle' or 'square'
      pfpFrameColor: '#4a4f5c',
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

      document.getElementById('rangeFontSize').value = state.fontSize;
      document.getElementById('labelFontSize').textContent = `${{state.fontSize}} px`;
      document.getElementById('rangePfpSize').value = state.pfpSize;
      document.getElementById('labelPfpSize').textContent = `${{state.pfpSize}} px`;
      document.getElementById('selectVAlign').value = state.vAlign;
      document.getElementById('selectTextAlign').value = state.textAlign;
      document.getElementById('selectHeaderAlign').value = state.headerAlign;
      document.getElementById('selectFontStyle').value = state.fontStyle;
      selectPfpFrameColor.value = state.pfpFrameColor;
      labelFrameColor.textContent = 'SLATE TITANIUM';

      btnPfpCircle.classList.add('active');
      btnPfpSquare.classList.remove('active');

      render();
      showToast('Default Settings Restored');
    }});

    // Aspect Ratio Toggles
    document.querySelectorAll('.btn-ratio').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.btn-ratio').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        state.aspect = btn.dataset.ratio;
        state.width = parseInt(btn.dataset.w, 10);
        state.height = parseInt(btn.dataset.h, 10);
        canvas.width = state.width;
        canvas.height = state.height;

        document.getElementById('currentRatioBadge').textContent = `${{state.width}} × ${{state.height}}`;
        if (mobilePreviewRatioBadge) mobilePreviewRatioBadge.textContent = state.aspect;
        render();
        showToast(`Aspect Ratio: ${{state.aspect}} (${{state.width}}×${{state.height}})`);
      }});
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

      // Scalloped 12-point starburst in official blue #1d9bf0
      ctx.fillStyle = '#1d9bf0';
      ctx.beginPath();
      
      const points = 12;
      const innerRadius = radius * 0.88;
      for (let i = 0; i < points * 2; i++) {{
        const r = (i % 2 === 0) ? radius : innerRadius;
        const angle = (i * Math.PI) / points - (Math.PI / 2);
        const x = centerX + Math.cos(angle) * r;
        const y = centerY + Math.sin(angle) * r;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }}
      ctx.closePath();
      ctx.fill();

      // White checkmark accurately centered
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = Math.max(2.4, size * 0.125);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';

      ctx.beginPath();
      ctx.moveTo(centerX - size * 0.22, centerY + size * 0.02);
      ctx.lineTo(centerX - size * 0.05, centerY + size * 0.19);
      ctx.lineTo(centerX + size * 0.24, centerY - size * 0.16);
      ctx.stroke();

      ctx.restore();
    }}

    function render() {{
      const W = state.width;
      const H = state.height;

      // Pure Lossless Pitch Black for the Post Canvas (#000000)
      ctx.fillStyle = '#000000';
      ctx.fillRect(0, 0, W, H);

      const marginX = (W === 1920 && H === 1080) ? 220 : 86;
      const contentWidth = W - (marginX * 2);

      let fontFamily = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif';
      if (state.fontStyle === 'serif') fontFamily = '"Georgia", "Baskerville", "Times New Roman", serif';
      else if (state.fontStyle === 'mono') fontFamily = 'ui-monospace, "SF Mono", "Cascadia Code", Menlo, monospace';

      const fontText = `400 ${{state.fontSize}}px ${{fontFamily}}`;
      ctx.font = fontText;
      const lineHeight = Math.round(state.fontSize * 1.44);
      const textLines = getLines(ctx, state.text, contentWidth);
      const textBlockHeight = textLines.length * lineHeight;

      const pfpSize = state.pfpSize;
      const isCenteredHeader = (state.headerAlign === 'center');
      const headerHeight = isCenteredHeader ? (pfpSize + 76) : pfpSize;

      let attachHeight = 0;
      let attachWidth = contentWidth;

      if (state.attachedImg) {{
        const aspect = state.attachedImg.width / state.attachedImg.height;
        const maxAttachH = (H === 1920) ? 960 : ((H === 1350) ? 680 : 440);
        attachHeight = Math.min(Math.round(attachWidth / aspect), maxAttachH);
        attachWidth = Math.round(attachHeight * aspect);
      }} else if (state.attachedVideo && state.attachedVideo.videoWidth) {{
        const aspect = state.attachedVideo.videoWidth / state.attachedVideo.videoHeight;
        const maxAttachH = (H === 1920) ? 960 : ((H === 1350) ? 680 : 440);
        attachHeight = Math.min(Math.round(attachWidth / aspect), maxAttachH);
        attachWidth = Math.round(attachHeight * aspect);
      }}

      const spacingHeaderToText = 36;
      const spacingTextToAttach = (state.attachedImg || state.attachedVideo) ? 34 : 0;
      const totalBlockHeight = headerHeight + spacingHeaderToText + textBlockHeight + spacingTextToAttach + attachHeight;

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

      // Defined Avatar Frame Rim (Matches Black Post & White PFP)
      if (state.pfpFrameColor && state.pfpFrameColor !== 'none') {{
        ctx.save();
        ctx.beginPath();
        if (state.pfpShape === 'square') {{
          // Sharp rectangular box frame
          ctx.rect(pfpX, pfpY, pfpSize, pfpSize);
        }} else {{
          // Smooth circular ring frame
          ctx.arc(pfpX + radius, pfpY + radius, radius, 0, Math.PI * 2);
        }}
        ctx.strokeStyle = state.pfpFrameColor;
        ctx.lineWidth = Math.max(3, Math.round(pfpSize * 0.035));
        ctx.stroke();
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
        ctx.fillText(displayName, W / 2, nameY);

        if (state.verified) {{
          const nameWidth = ctx.measureText(displayName).width;
          const badgeSize = 24;
          const badgeCenterX = Math.round(W / 2 + nameWidth / 2 + 16);
          const badgeCenterY = Math.round(nameY - 11);
          drawAccurateVerifiedBadge(ctx, badgeCenterX, badgeCenterY, badgeSize);
        }}

        ctx.font = fontHandle;
        ctx.fillStyle = '#71767b';
        ctx.textAlign = 'center';
        ctx.fillText(state.handle, W / 2, handleY);

      }} else {{
        const textStartX = pfpX + pfpSize + 22;
        const nameY = pfpY + Math.round(pfpSize * 0.42);
        const handleY = pfpY + Math.round(pfpSize * 0.82);

        ctx.font = fontName;
        ctx.fillStyle = '#f7f9f9';
        ctx.textAlign = 'left';
        ctx.fillText(displayName, textStartX, nameY);

        if (state.verified) {{
          const nameWidth = ctx.measureText(displayName).width;
          const badgeSize = 24;
          const badgeCenterX = Math.round(textStartX + nameWidth + 16);
          const badgeCenterY = Math.round(nameY - 11);
          drawAccurateVerifiedBadge(ctx, badgeCenterX, badgeCenterY, badgeSize);
        }}

        ctx.font = fontHandle;
        ctx.fillStyle = '#71767b';
        ctx.textAlign = 'left';
        ctx.fillText(state.handle, textStartX, handleY);
      }}

      // 3. Render Post Content Text
      ctx.font = fontText;
      ctx.fillStyle = '#f7f9f9';
      let textCurrentY = startY + headerHeight + spacingHeaderToText + Math.round(state.fontSize * 0.85);

      for (let i = 0; i < textLines.length; i++) {{
        const line = textLines[i];
        if (state.textAlign === 'center') {{
          ctx.textAlign = 'center';
          ctx.fillText(line, W / 2, textCurrentY);
        }} else {{
          ctx.textAlign = 'left';
          ctx.fillText(line, marginX, textCurrentY);
        }}
        textCurrentY += lineHeight;
      }}

      // 4. Render Attached Meme (Sharp Box Framing with zero curves)
      const attachY = textCurrentY - lineHeight + spacingTextToAttach;
      const attachX = Math.round(marginX + (contentWidth - attachWidth) / 2);

      if (state.attachedImg) {{
        ctx.save();
        ctx.beginPath();
        ctx.rect(attachX, attachY, attachWidth, attachHeight);
        ctx.clip();
        ctx.drawImage(state.attachedImg, attachX, attachY, attachWidth, attachHeight);
        ctx.restore();

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.16)';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(attachX, attachY, attachWidth, attachHeight);
      }} else if (state.attachedVideo && state.attachedVideo.readyState >= 2) {{
        ctx.save();
        ctx.beginPath();
        ctx.rect(attachX, attachY, attachWidth, attachHeight);
        ctx.clip();
        ctx.drawImage(state.attachedVideo, attachX, attachY, attachWidth, attachHeight);
        ctx.restore();

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.18)';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(attachX, attachY, attachWidth, attachHeight);
      }}
    }}

    function startVideoLoop() {{
      if (videoAnimId) cancelAnimationFrame(videoAnimId);
      function loop() {{
        if (state.attachedVideo && !state.attachedVideo.paused && !state.attachedVideo.ended) {{
          render();
        }}
        videoAnimId = requestAnimationFrame(loop);
      }}
      loop();
    }}

    // Form Event Listeners
    document.getElementById('inputText').addEventListener('input', (e) => {{
      state.text = e.target.value;
      document.getElementById('charCount').textContent = `${{state.text.length}} chars`;
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

    document.getElementById('rangeFontSize').addEventListener('input', (e) => {{
      state.fontSize = parseInt(e.target.value, 10);
      document.getElementById('labelFontSize').textContent = `${{state.fontSize}} px`;
      render();
    }});

    document.getElementById('rangePfpSize').addEventListener('input', (e) => {{
      state.pfpSize = parseInt(e.target.value, 10);
      document.getElementById('labelPfpSize').textContent = `${{state.pfpSize}} px`;
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

    // Meme Attachment (Photo & Video)
    const dropzone = document.getElementById('dropzone');
    const inputAttach = document.getElementById('inputAttach');
    const attachPreviewBar = document.getElementById('attachPreviewBar');
    const attachFileName = document.getElementById('attachFileName');
    const attachTypeIcon = document.getElementById('attachTypeIcon');
    const btnRemoveAttach = document.getElementById('btnRemoveAttach');
    const videoControlsRow = document.getElementById('videoControlsRow');
    const btnToggleVideoPlay = document.getElementById('btnToggleVideoPlay');
    const btnToggleVideoMute = document.getElementById('btnToggleVideoMute');
    const btnExportVideo = document.getElementById('btnExportVideo');
    const btnDownloadText = document.getElementById('btnDownloadText');

    dropzone.addEventListener('click', () => inputAttach.click());
    dropzone.addEventListener('dragover', (e) => {{ e.preventDefault(); dropzone.classList.add('dragover'); }});
    dropzone.addEventListener('dragleave', () => dropzone.classList.remove('dragover'));
    dropzone.addEventListener('drop', (e) => {{
      e.preventDefault();
      dropzone.classList.remove('dragover');
      if (e.dataTransfer.files && e.dataTransfer.files[0]) {{
        handleAttachedMedia(e.dataTransfer.files[0]);
      }}
    }});

    inputAttach.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files[0]) {{
        handleAttachedMedia(e.target.files[0]);
      }}
    }});

    function handleAttachedMedia(file) {{
      const isVideo = file.type.startsWith('video/');
      const isImage = file.type.startsWith('image/');
      if (!isImage && !isVideo) return;

      const fileUrl = URL.createObjectURL(file);
      attachFileName.textContent = file.name;

      if (isVideo) {{
        if (state.attachedVideo) {{
          state.attachedVideo.pause();
          state.attachedVideo.remove();
        }}
        const vid = document.createElement('video');
        vid.src = fileUrl;
        vid.crossOrigin = 'anonymous';
        vid.loop = true;
        vid.muted = true;
        vid.playsInline = true;
        vid.autoplay = true;

        vid.onloadedmetadata = () => {{
          state.attachedVideo = vid;
          state.attachedImg = null;
          attachTypeIcon.textContent = '[VIDEO]';
          attachPreviewBar.style.display = 'flex';
          videoControlsRow.style.display = 'block';
          btnExportVideo.style.display = 'inline-flex';
          btnDownloadText.textContent = 'Capture Frame (PNG)';
          vid.play();
          startVideoLoop();
          showToast('Video Attached to Canvas');
        }};
      }} else {{
        if (state.attachedVideo) {{
          state.attachedVideo.pause();
          state.attachedVideo = null;
        }}
        if (videoAnimId) cancelAnimationFrame(videoAnimId);
        videoControlsRow.style.display = 'none';
        btnExportVideo.style.display = 'none';
        btnDownloadText.textContent = 'Download Post (1080p Lossless PNG)';

        const img = new Image();
        img.onload = () => {{
          state.attachedImg = img;
          attachTypeIcon.textContent = '[PHOTO]';
          attachPreviewBar.style.display = 'flex';
          render();
          showToast('Photograph Attached');
        }};
        img.src = fileUrl;
      }}
    }}

    btnRemoveAttach.addEventListener('click', () => {{
      if (state.attachedVideo) {{
        state.attachedVideo.pause();
        state.attachedVideo = null;
      }}
      if (videoAnimId) cancelAnimationFrame(videoAnimId);
      state.attachedImg = null;
      inputAttach.value = '';
      attachPreviewBar.style.display = 'none';
      videoControlsRow.style.display = 'none';
      btnExportVideo.style.display = 'none';
      btnDownloadText.textContent = 'Download Post (1080p Lossless PNG)';
      render();
    }});

    btnToggleVideoPlay.addEventListener('click', () => {{
      if (!state.attachedVideo) return;
      if (state.attachedVideo.paused) {{
        state.attachedVideo.play();
        btnToggleVideoPlay.textContent = '⏸️ Pause';
      }} else {{
        state.attachedVideo.pause();
        btnToggleVideoPlay.textContent = '▶️ Play';
      }}
    }});

    btnToggleVideoMute.addEventListener('click', () => {{
      if (!state.attachedVideo) return;
      state.attachedVideo.muted = !state.attachedVideo.muted;
      btnToggleVideoMute.textContent = state.attachedVideo.muted ? '🔇 Muted' : '🔊 Sound';
    }});

    // Export Video Meme Recording
    btnExportVideo.addEventListener('click', async () => {{
      const vid = state.attachedVideo;
      if (!vid) return;

      try {{
        showToast('Rendering Video Recording...');
        const stream = canvas.captureStream(30);

        if (vid.captureStream) {{
          try {{
            const vStream = vid.captureStream();
            const aTracks = vStream.getAudioTracks();
            if (aTracks.length > 0) stream.addTrack(aTracks[0]);
          }} catch(e) {{}}
        }}

        const mime = MediaRecorder.isTypeSupported('video/mp4;codecs=avc1') ? 'video/mp4' : 'video/webm';
        const recorder = new MediaRecorder(stream, {{ mimeType: mime }});
        const chunks = [];

        recorder.ondataavailable = e => {{ if (e.data.size > 0) chunks.push(e.data); }};
        recorder.onstop = () => {{
          const blob = new Blob(chunks, {{ type: mime }});
          const url = URL.createObjectURL(blob);
          const link = document.createElement('a');
          const ext = mime.includes('mp4') ? 'mp4' : 'webm';
          link.download = `mrr_hamster_meme_${{Date.now()}}.${{ext}}`;
          link.href = url;
          link.click();
          showToast('Video Exported Successfully');
        }};

        vid.currentTime = 0;
        await vid.play();
        recorder.start();

        const duration = Math.min(vid.duration || 6, 15);
        setTimeout(() => {{
          if (recorder.state === 'recording') recorder.stop();
        }}, duration * 1000 + 300);

      }} catch (err) {{
        alert('Video recording: ' + err.message);
      }}
    }});

    // Lossless PNG Download (24-bit, uncompressed)
    document.getElementById('btnDownload').addEventListener('click', () => {{
      const link = document.createElement('a');
      const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
      link.download = `mrr_hamster_post_${{state.aspect.replace(':', 'x')}}_${{timestamp}}.png`;
      link.href = canvas.toDataURL('image/png', 1.0);
      link.click();
      showToast('1080p Lossless PNG Downloaded');
    }});

    // Copy to Clipboard
    document.getElementById('btnCopy').addEventListener('click', async () => {{
      try {{
        canvas.toBlob(async (blob) => {{
          const item = new ClipboardItem({{ 'image/png': blob }});
          await navigator.clipboard.write([item]);
          showToast('Copied to Clipboard');
        }}, 'image/png', 1.0);
      }} catch (err) {{
        showToast('Clipboard access unavailable');
      }}
    }});

    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2200);
    }}

    // Credentials Gate Authentication System
    const AUTH_CREDS = {{
      username: 'hamster_boss',
      password: 'MogMaster#2026'
    }};

    function checkAuth() {{
      const isAuth = sessionStorage.getItem('mr_hamster_auth') === 'granted';
      const overlay = document.getElementById('authOverlay');
      if (isAuth) {{
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

    // Mobile Mode Switcher (Controls vs Live Preview)
    const appLayout = document.querySelector('.app-layout');
    const tabBtnControls = document.getElementById('tabBtnControls');
    const tabBtnPreview = document.getElementById('tabBtnPreview');
    const btnMobileQuickToggle = document.getElementById('btnMobileQuickToggle');
    const mobilePreviewRatioBadge = document.getElementById('mobilePreviewRatioBadge');

    function setMobileMode(mode) {{
      if (mode === 'preview') {{
        appLayout.classList.remove('view-controls');
        appLayout.classList.add('view-preview');
        tabBtnPreview.classList.add('active');
        tabBtnControls.classList.remove('active');
        if (btnMobileQuickToggle) btnMobileQuickToggle.innerHTML = '<span>✍️ Edit Controls</span>';
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
        render();
      }} else {{
        appLayout.classList.remove('view-preview');
        appLayout.classList.add('view-controls');
        tabBtnControls.classList.add('active');
        tabBtnPreview.classList.remove('active');
        if (btnMobileQuickToggle) btnMobileQuickToggle.innerHTML = '<span>👁️ View Live Post</span>';
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}
    }}

    if (tabBtnControls) tabBtnControls.addEventListener('click', () => setMobileMode('controls'));
    if (tabBtnPreview) tabBtnPreview.addEventListener('click', () => setMobileMode('preview'));
    if (btnMobileQuickToggle) {{
      btnMobileQuickToggle.addEventListener('click', () => {{
        const isCurrentlyPreview = appLayout.classList.contains('view-preview');
        setMobileMode(isCurrentlyPreview ? 'controls' : 'preview');
      }});
    }}

    checkAuth();

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
