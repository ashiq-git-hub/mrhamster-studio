# -*- coding: utf-8 -*-
"""
Mr. Hamster Studio - Swiss Minimalist Luxury Atelier Architecture
- Color Palette: Luminous Gallery Alabaster (#FAF8F5), Studio White (#FFFFFF), Hairline (#E5E0D8), Champagne Gold (#946E26)
- Typography: Editorial Modern Serif ('Cinzel', 'Playfair Display', Georgia) + Precision Grotesque
- Semantic HTML5: <header>, <main>, <aside>, <section>, <figure>, <figcaption>, <nav>, <footer>
- Desktop: Left 440px Atelier Sidebar, Right Museum Pedestal (100% OLED Black Canvas)
- Mobile: Pinned Live Preview at Top, Segmented Tool Dock below, No iOS Zoom-Jacking (16px inputs), Butter-Smooth UX
- Media Attachment: Upload Photo, GIF, or Video Clip, Centered by Default, Blunt Corner Trim (0-48px), Live Video Playback
- Frame Rim System: Circle & Square Frame with Crisp Titanium White, Champagne Ivory, Antique Gold rims
- Zero Horizontal Overflow, Mathematical Precision
- Master Credentials Gate: ashiq / ashiq14726
"""

import os
import json
import base64

BASE_DIR = r"c:\Users\Thoufeek\Desktop\mr hasmter"

with open(os.path.join(BASE_DIR, "assets", "data", "pfps_base64.json"), "r", encoding="utf-8") as f:
    pfps_base64 = json.load(f)

mog_b64 = pfps_base64.get("pfp_mog_hamster.png", "")

with open(os.path.join(BASE_DIR, "assets", "icons", "verified_badge.svg"), "rb") as f:
    verified_badge_b64 = "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode("ascii")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="description" content="Mr. Hamster — Minimalist 1080p social post generator.">
  <title>Mr. Hamster</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-core: #FAF8F5;              /* Luminous Gallery Alabaster */
      --bg-surface: #FFFFFF;           /* Crisp Atelier White */
      --bg-card: #FFFFFF;              /* Pure Card Surface */
      --bg-card-hover: #FDFCF9;        /* Subtle Ivory Hover */
      --bg-recessed: #F3EFE8;          /* Recessed Track & Inputs */
      --border-hairline: #E5E0D8;      /* Warm Architectural Hairline */
      --border-hover: #C9C2B5;         /* Hairline Hover */
      --border-focus: #181715;         /* Obsidian Ink Focus */
      --gold: #946E26;                 /* Antique Champagne Brass */
      --gold-light: #F9F5EC;           /* Soft Champagne Tint */
      --gold-border: rgba(148, 110, 38, 0.28);
      --text-main: #181715;            /* Deep Obsidian Ink */
      --text-dim: #555048;             /* Warm Editorial Graphite */
      --text-muted: #8A8478;           /* Quiet Stone Ash */
      --shadow-sm: 0 1px 3px rgba(24, 23, 21, 0.04);
      --shadow-card: 0 3px 14px rgba(24, 23, 21, 0.04), 0 1px 3px rgba(24, 23, 21, 0.02);
      --shadow-hover: 0 6px 20px rgba(24, 23, 21, 0.07), 0 2px 6px rgba(24, 23, 21, 0.03);
      --font-serif: "Cinzel", "Playfair Display", "Baskerville", serif;
      --font-body: "Space Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: "JetBrains Mono", "SF Mono", Consolas, monospace;
      --radius-sm: 4px;
      --radius-md: 6px;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    html, body {{
      width: 100%;
      max-width: 100vw;
      overflow-x: hidden;
      background-color: var(--bg-core);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
    }}

    body {{
      display: flex;
      flex-direction: column;
    }}

    /* Top Atelier Header (Symmetric, Refined, Zero Overflow) */
    .atelier-header {{
      background: #FFFFFF;
      border-bottom: 1px solid var(--border-hairline);
      padding: 12px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 1px 6px rgba(24, 23, 21, 0.03);
      width: 100%;
      max-width: 100vw;
      box-sizing: border-box;
    }}

    .brand-section {{
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      color: inherit;
    }}

    .brand-mark {{
      width: 40px;
      height: 40px;
      background: #181715;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
      border-radius: var(--radius-sm);
      box-shadow: 0 2px 6px rgba(24, 23, 21, 0.18);
      flex-shrink: 0;
      transition: transform 0.15s ease;
    }}
    .brand-mark:hover {{
      transform: scale(1.03);
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .brand-title-wrap {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    h1.app-title {{
      font-family: var(--font-serif);
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-main);
      margin: 0;
      line-height: 1.1;
    }}

    .app-handle-badge {{
      font-family: var(--font-mono);
      font-size: 0.70rem;
      color: var(--gold);
      background: var(--gold-light);
      padding: 2px 7px;
      font-weight: 600;
      border: 1px solid var(--gold-border);
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
    }}

    .atelier-subtitle {{
      font-size: 0.67rem;
      font-family: var(--font-mono);
      color: var(--text-muted);
      letter-spacing: 0.09em;
      text-transform: uppercase;
      margin: 0;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .badge-resolution {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 11px;
      background: var(--bg-core);
      border: 1px solid var(--border-hairline);
      font-size: 0.68rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      text-transform: uppercase;
      font-weight: 600;
      border-radius: var(--radius-sm);
      letter-spacing: 0.06em;
    }}
    .badge-resolution::before {{
      content: "";
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #2E7D32;
      display: inline-block;
    }}

    /* Buttons */
    .btn {{
      padding: 9px 18px;
      font-size: 0.75rem;
      font-family: var(--font-mono);
      font-weight: 600;
      letter-spacing: 0.07em;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.15s ease;
      border: 1px solid transparent;
      border-radius: var(--radius-sm);
      user-select: none;
      -webkit-tap-highlight-color: transparent;
      white-space: nowrap;
      text-decoration: none;
    }}
    .btn:active {{
      transform: translateY(1px);
    }}

    .btn-primary {{
      background: #181715;
      color: #FFFFFF;
      border-color: #181715;
      box-shadow: 0 2px 6px rgba(24, 23, 21, 0.15);
    }}
    .btn-primary:hover {{
      background: #2A2825;
      box-shadow: 0 4px 12px rgba(24, 23, 21, 0.22);
    }}

    .btn-secondary {{
      background: #FFFFFF;
      color: var(--text-main);
      border-color: var(--border-hairline);
      box-shadow: var(--shadow-sm);
    }}
    .btn-secondary:hover {{
      background: var(--bg-core);
      border-color: var(--border-hover);
    }}

    .btn-sm {{
      padding: 6px 12px;
      font-size: 0.70rem;
    }}

    .btn-action-text {{
      padding: 4px 9px;
      background: var(--bg-recessed);
      border: 1px solid var(--border-hairline);
      font-size: 0.67rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-weight: 600;
      transition: all 0.12s;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .btn-action-text:hover, .btn-action-text:active {{
      background: #181715;
      color: #FFFFFF;
      border-color: #181715;
    }}

    /* Desktop Layout */
    .app-layout {{
      display: grid;
      grid-template-columns: 440px 1fr;
      flex: 1;
      overflow: hidden;
      min-height: calc(100vh - 65px);
      width: 100%;
      max-width: 100vw;
    }}

    /* Controls Panel */
    .controls-panel {{
      background: #FFFFFF;
      border-right: 1px solid var(--border-hairline);
      padding: 22px 20px;
      overflow-y: auto;
      max-height: calc(100vh - 65px);
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-sizing: border-box;
    }}

    /* Semantic Control Card */
    .control-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-hairline);
      border-radius: var(--radius-md);
      padding: 18px;
      position: relative;
      box-shadow: var(--shadow-card);
      box-sizing: border-box;
      width: 100%;
      transition: box-shadow 0.2s, border-color 0.2s;
    }}
    .control-card:hover {{
      border-color: var(--border-hover);
      box-shadow: var(--shadow-hover);
    }}

    /* Clean Card Header */
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-hairline);
      padding-bottom: 9px;
      margin-bottom: 14px;
      width: 100%;
    }}
    .card-title {{
      font-size: 0.73rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--text-dim);
      font-family: var(--font-mono);
      display: flex;
      align-items: center;
      margin: 0;
    }}
    .card-title span.section-index {{
      color: var(--gold);
      font-weight: 700;
      margin-right: 7px;
    }}

    /* Form Fields */
    .input-field, .textarea-field, select {{
      width: 100%;
      background: #FFFFFF;
      border: 1px solid var(--border-hairline);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      color: var(--text-main);
      font-size: 0.90rem;
      font-family: var(--font-body);
      outline: none;
      transition: border-color 0.15s, box-shadow 0.15s;
      box-shadow: inset 0 1px 2px rgba(24, 23, 21, 0.02);
      box-sizing: border-box;
    }}
    .input-field:focus, .textarea-field:focus, select:focus {{
      border-color: var(--border-focus);
      box-shadow: inset 0 1px 2px rgba(24, 23, 21, 0.04), 0 0 0 2px rgba(24, 23, 21, 0.08);
    }}
    .textarea-field {{
      min-height: 110px;
      resize: vertical;
      line-height: 1.55;
      font-size: 0.95rem;
    }}

    /* Ratio Grid */
    .ratio-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      width: 100%;
    }}
    .btn-ratio {{
      padding: 12px 14px;
      background: #FFFFFF;
      border: 1px solid var(--border-hairline);
      border-radius: var(--radius-sm);
      color: var(--text-dim);
      cursor: pointer;
      text-align: left;
      transition: all 0.15s;
      display: flex;
      flex-direction: column;
      gap: 3px;
      box-shadow: var(--shadow-sm);
      -webkit-tap-highlight-color: transparent;
      box-sizing: border-box;
    }}
    .btn-ratio span.label {{
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 0.76rem;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--text-main);
    }}
    .btn-ratio span.dim {{
      font-size: 0.67rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-weight: 500;
    }}
    .btn-ratio:hover {{
      border-color: var(--border-hover);
      background: var(--bg-core);
    }}
    .btn-ratio.active {{
      background: var(--gold-light);
      border: 1px solid var(--gold);
      border-left: 4px solid var(--gold);
      color: var(--text-main);
      box-shadow: 0 2px 8px rgba(148, 110, 38, 0.12);
    }}
    .btn-ratio.active span.dim {{
      color: var(--gold);
      font-weight: 700;
    }}

    /* Toggle Group */
    .btn-toggle-group {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
      gap: 2px;
      background: var(--border-hairline);
      border: 1px solid var(--border-hairline);
      border-radius: var(--radius-sm);
      overflow: hidden;
      width: 100%;
    }}
    .btn-toggle {{
      padding: 10px;
      font-size: 0.72rem;
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--text-dim);
      background: #FFFFFF;
      border: none;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      transition: all 0.15s;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      -webkit-tap-highlight-color: transparent;
    }}
    .btn-toggle.active {{
      background: #181715;
      color: #FFFFFF;
    }}

    /* Avatar Box */
    .pfp-slot-container {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 14px;
      width: 100%;
    }}
    .pfp-preview-box {{
      width: 74px;
      height: 74px;
      border: 1px solid var(--border-hairline);
      border-radius: var(--radius-sm);
      background: var(--bg-recessed);
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      flex-shrink: 0;
      box-shadow: var(--shadow-sm);
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
      width: 100%;
    }}

    /* Steppers & Sliders */
    .slider-row {{
      margin-top: 14px;
      width: 100%;
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
      background: #FFFFFF;
      border: 1px solid var(--border-hairline);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      font-family: var(--font-mono);
      font-size: 1.15rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: var(--shadow-sm);
      transition: all 0.1s;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
      flex-shrink: 0;
    }}
    .btn-stepper:active {{
      background: #181715;
      color: #FFFFFF;
      border-color: #181715;
      transform: translateY(1px);
    }}
    input[type=range] {{
      -webkit-appearance: none;
      width: 100%;
      height: 6px;
      background: #E5E0D8;
      border-radius: 3px;
      outline: none;
      border: none;
      box-shadow: inset 0 1px 2px rgba(24,23,21,0.06);
      touch-action: pan-x;
    }}
    input[type=range]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      appearance: none;
      width: 18px;
      height: 22px;
      background: #181715;
      border: 1px solid #FFFFFF;
      border-radius: 3px;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(24, 23, 21, 0.25);
      transition: background 0.12s;
    }}
    input[type=range]::-webkit-slider-thumb:hover {{
      background: var(--gold);
    }}

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
      accent-color: #181715;
      cursor: pointer;
    }}

    /* Preview Pedestal (Right Side Desktop) */
    .preview-workspace {{
      background: radial-gradient(circle at 50% 32%, #F6F3EB 0%, #E8E3DA 100%);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      padding: 32px;
      overflow: auto;
      box-sizing: border-box;
      width: 100%;
    }}

    .canvas-pedestal {{
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.35), 0 6px 18px rgba(0, 0, 0, 0.15), 0 0 0 1px rgba(0, 0, 0, 0.12);
      border-radius: var(--radius-sm);
      overflow: hidden;
      background: #000000; /* STRICT OLED BLACK POST */
      max-width: 100%;
      max-height: 84vh;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      position: relative;
      line-height: 0;
      margin: 0 auto;
    }}

    #postCanvas {{
      display: block;
      width: 100%;
      height: 100%;
      max-width: 100%;
      max-height: 82vh;
      object-fit: contain;
    }}

    .btn-pedestal-expand {{
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(24, 23, 21, 0.85);
      backdrop-filter: blur(6px);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: var(--radius-sm);
      padding: 6px 12px;
      font-size: 0.69rem;
      font-family: var(--font-mono);
      font-weight: 700;
      cursor: pointer;
      z-index: 10;
      transition: all 0.15s;
    }}
    .btn-pedestal-expand:hover, .btn-pedestal-expand:active {{
      background: #181715;
      border-color: #FFFFFF;
      transform: scale(1.02);
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #181715;
      color: #FFFFFF;
      padding: 10px 18px;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      border-radius: var(--radius-sm);
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.25);
      opacity: 0;
      transform: translateY(12px);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
      z-index: 999;
    }}
    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* Fullscreen Modal */
    .fullscreen-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(14, 13, 12, 0.94);
      backdrop-filter: blur(8px);
      z-index: 2000;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 18px;
      box-sizing: border-box;
      opacity: 1;
      transition: opacity 0.2s ease;
    }}
    .fullscreen-overlay.hidden {{
      display: none;
      opacity: 0;
    }}
    .fullscreen-top-bar {{
      width: 100%;
      max-width: 900px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .fullscreen-ratio-badge {{
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: #FFFFFF;
      background: rgba(255, 255, 255, 0.12);
      padding: 5px 12px;
      border-radius: var(--radius-sm);
    }}
    .fullscreen-canvas-wrap {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 900px;
      padding: 14px 0;
      box-sizing: border-box;
    }}
    .fullscreen-canvas-wrap img {{
      max-width: 100%;
      max-height: 78vh;
      object-fit: contain;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6);
      border-radius: var(--radius-sm);
    }}
    .fullscreen-bottom-bar {{
      width: 100%;
      max-width: 900px;
      display: flex;
      justify-content: center;
      padding-top: 10px;
    }}

    /* Auth Gate Modal */
    #authOverlay {{
      position: fixed;
      inset: 0;
      background: rgba(24, 23, 21, 0.88);
      backdrop-filter: blur(8px);
      z-index: 3000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      box-sizing: border-box;
    }}
    #authOverlay.hidden {{
      display: none;
    }}
    .auth-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-hairline);
      border-radius: var(--radius-md);
      padding: 34px 28px;
      width: 100%;
      max-width: 380px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
      text-align: center;
      animation: modalFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .auth-badge {{
      width: 48px;
      height: 48px;
      background: #181715;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      margin: 0 auto 14px auto;
    }}
    .auth-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-main);
      margin-bottom: 4px;
    }}
    .auth-subtitle {{
      font-family: var(--font-mono);
      font-size: 0.68rem;
      color: var(--text-muted);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 22px;
    }}
    .auth-error {{
      background: #FFF5F5;
      border: 1px solid #FFCDD2;
      color: #C62828;
      font-size: 0.72rem;
      font-family: var(--font-mono);
      padding: 8px;
      border-radius: var(--radius-sm);
      margin-bottom: 14px;
      display: none;
    }}

    /* Hidden Utility */
    .sr-only {{
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border-width: 0;
    }}

    /* Hide desktop controls on mobile by default */
    .mobile-tool-tabs {{
      display: none;
    }}
    .mobile-floating-bar {{
      display: none;
    }}

    /* ======================================================== */
    /* RESPONSIVE MOBILE ARCHITECTURE (Screens <= 960px)        */
    /* Pinned Live Preview at Top + Tabbed Tool Dock Beneath    */
    /* ZERO SCROLL TRAPPING, PERFECT SYMMETRY, ZERO OVERFLOW    */
    /* ======================================================== */
    @media (max-width: 960px) {{
      html, body {{
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
        overflow-y: auto !important;
        -webkit-overflow-scrolling: touch;
      }}

      /* Prevent iOS Safari auto-zoom on input focus */
      .input-field, .textarea-field, select {{
        font-size: 16px !important;
      }}

      /* Mobile Header: Clean, balanced, fits in 100vw */
      .atelier-header {{
        padding: 10px 14px !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
      }}
      .brand-mark {{
        width: 34px !important;
        height: 34px !important;
        font-size: 1.15rem !important;
      }}
      h1.app-title {{
        font-size: 0.94rem !important;
      }}
      .atelier-subtitle, .badge-resolution, #btnLockStudio, #btnQuickExport {{
        display: none !important;
      }}
      .header-actions {{
        gap: 6px !important;
      }}
      .header-actions .btn {{
        padding: 6px 10px !important;
        font-size: 0.70rem !important;
        min-height: 34px !important;
      }}

      /* App Layout: Vertical flow */
      .app-layout {{
        display: flex !important;
        flex-direction: column !important;
        min-height: auto !important;
        overflow: visible !important;
        width: 100% !important;
        max-width: 100vw !important;
      }}

      /* Live Preview at Top: Compact, proportioned */
      .preview-workspace {{
        order: 1 !important;
        padding: 12px 14px !important;
        min-height: auto !important;
        background: radial-gradient(circle at 50% 35%, #F4F0E8 0%, #E6E1D7 100%) !important;
        border-bottom: 1px solid var(--border-hairline) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
      }}

      .canvas-pedestal {{
        max-width: min(92vw, 300px) !important;
        max-height: 29vh !important;
        margin: 0 auto !important;
        box-shadow: 0 10px 26px rgba(24, 23, 21, 0.28), 0 0 0 1px rgba(0, 0, 0, 0.12) !important;
      }}

      #postCanvas {{
        max-height: 28vh !important;
        width: 100% !important;
        height: auto !important;
      }}

      /* Segmented Tool Tabs (Pinned under Live Preview) */
      .mobile-tool-tabs {{
        display: flex !important;
        order: 2 !important;
        background: #FFFFFF !important;
        border-bottom: 1px solid var(--border-hairline) !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
        position: sticky !important;
        top: 55px !important;
        z-index: 80 !important;
        overflow-x: auto !important;
        scrollbar-width: none;
      }}
      .mobile-tool-tabs::-webkit-scrollbar {{
        display: none;
      }}
      .mobile-tool-tab {{
        flex: 1 0 auto;
        min-width: 68px;
        padding: 11px 4px;
        background: #FFFFFF;
        border: none;
        border-bottom: 3px solid transparent;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 4px;
        cursor: pointer;
        font-family: var(--font-mono);
        font-size: 0.70rem;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--text-dim);
        transition: all 0.12s;
        -webkit-tap-highlight-color: transparent;
      }}
      .mobile-tool-tab.active {{
        color: var(--text-main);
        border-bottom-color: var(--gold);
        background: var(--gold-light);
      }}

      /* Controls Panel on Mobile */
      .controls-panel {{
        order: 3 !important;
        display: flex !important;
        flex-direction: column !important;
        max-height: none !important;
        overflow-y: visible !important;
        padding: 14px 14px 95px 14px !important;
        border-right: none !important;
        gap: 12px !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
      }}

      /* Mobile Tab Switching: Only show active card */
      .controls-panel.mobile-tab-view .control-card {{
        display: none;
      }}
      .controls-panel.mobile-tab-view .control-card.active-tab-card {{
        display: block !important;
        animation: fadeIn 0.15s ease;
      }}

      @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(4px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}

      /* Hide redundant desktop download buttons on mobile */
      .desktop-export-actions {{
        display: none !important;
      }}

      /* Mobile Floating Action Bar */
      .mobile-floating-bar {{
        display: flex !important;
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-top: 1px solid var(--border-hairline) !important;
        padding: 10px 14px calc(10px + env(safe-area-inset-bottom, 0px)) 14px !important;
        gap: 8px !important;
        z-index: 90 !important;
        box-shadow: 0 -4px 18px rgba(24, 23, 21, 0.08) !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
      }}

      .toast {{
        bottom: calc(76px + env(safe-area-inset-bottom, 0px)) !important;
        right: 14px !important;
        left: 14px !important;
        text-align: center !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Credentials Gate Lockscreen (Accessible Semantic Dialog) -->
  <div id="authOverlay" role="dialog" aria-modal="true" aria-labelledby="authTitle">
    <div class="auth-card">
      <div class="auth-badge">🐹</div>
      <div class="auth-title" id="authTitle">Mr. Hamster</div>
      <div class="auth-subtitle">Restricted Access · Enter Credentials</div>

      <div class="auth-error" id="authError" role="alert">
        ✕ Invalid username or password. Access denied.
      </div>

      <form id="authForm" onsubmit="event.preventDefault(); handleLogin();" style="display: flex; flex-direction: column; gap: 12px;">
        <div>
          <label for="authUsername" style="display: block; font-size: 0.72rem; font-family: var(--font-mono); color: var(--text-dim); font-weight: 700; margin-bottom: 4px; text-transform: uppercase;">Username</label>
          <input type="text" id="authUsername" class="input-field" placeholder="Username" autocomplete="username" required>
        </div>
        <div>
          <label for="authPassword" style="display: block; font-size: 0.72rem; font-family: var(--font-mono); color: var(--text-dim); font-weight: 700; margin-bottom: 4px; text-transform: uppercase;">Password</label>
          <input type="password" id="authPassword" class="input-field" placeholder="Password" autocomplete="current-password" required>
        </div>

        <button type="submit" class="btn btn-primary" style="padding: 13px; font-size: 0.84rem; margin-top: 6px;">
          <span>🔓 Unlock Studio</span>
        </button>
      </form>
    </div>
  </div>

  <!-- Fullscreen Post Preview Modal -->
  <div id="fullscreenOverlay" class="fullscreen-overlay hidden" role="dialog" aria-modal="true" aria-label="High-Resolution Post Preview">
    <div class="fullscreen-top-bar">
      <span class="fullscreen-ratio-badge" id="fullscreenRatioBadge">4:5 · 1080 × 1350</span>
      <button class="btn btn-secondary btn-sm" id="btnCloseFullscreen">✕ Close</button>
    </div>
    <div class="fullscreen-canvas-wrap">
      <img id="fullscreenImg" alt="High Resolution Mr. Hamster Statement Preview">
    </div>
    <div class="fullscreen-bottom-bar">
      <button class="btn btn-primary" id="btnFullscreenDownload" style="width: 100%; max-width: 380px; gap: 8px;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        <span>Download 1080p Lossless PNG</span>
      </button>
    </div>
  </div>

  <!-- Semantic Atelier Header -->
  <header class="atelier-header" role="banner">
    <div class="brand-section">
      <div class="brand-mark" aria-hidden="true">🐹</div>
      <div class="brand-text">
        <div class="brand-title-wrap">
          <h1 class="app-title">Mr. Hamster</h1>
          <span class="app-handle-badge">@mrr.hamster</span>
        </div>
      </div>
    </div>

    <nav class="header-actions" aria-label="Studio Controls">
      <span class="badge-resolution">1080p Lossless</span>
      <button class="btn btn-secondary btn-sm" id="btnLockStudio" title="Lock Studio Access">
        <span>Lock</span>
      </button>
      <button class="btn btn-secondary btn-sm" id="btnResetAllDefaults" title="Restore default sizing and layout">
        <span>Defaults</span>
      </button>
      <button class="btn btn-primary btn-sm" id="btnQuickExport" title="Quick Download 1080p">
        <span>Export</span>
      </button>
    </nav>
  </header>

  <!-- Semantic Main Studio Layout -->
  <main class="app-layout" id="studioMain">
    
    <!-- Left Controls Panel -->
    <aside class="controls-panel mobile-tab-view" id="controlsPanel" aria-label="Studio Controls">
      
      <!-- Card 1: Aspect Ratio Format -->
      <section class="control-card" id="cardRatio" aria-labelledby="headingRatio">
        <div class="card-header">
          <h2 class="card-title" id="headingRatio">
            <span class="section-index">01</span> Aspect Ratio
          </h2>
          <span id="currentRatioBadge" style="color: var(--gold); font-weight: 700; font-family: var(--font-mono); font-size: 0.72rem;">1080 × 1350</span>
        </div>
        <div class="ratio-grid" role="radiogroup" aria-label="Social Media Aspect Ratio">
          <button type="button" class="btn-ratio active" data-ratio="4:5" data-w="1080" data-h="1350" role="radio" aria-checked="true">
            <span class="label">4:5 Portrait</span>
            <span class="dim">Feed (1080×1350)</span>
          </button>
          <button type="button" class="btn-ratio" data-ratio="1:1" data-w="1080" data-h="1080" role="radio" aria-checked="false">
            <span class="label">1:1 Square</span>
            <span class="dim">Feed (1080×1080)</span>
          </button>
          <button type="button" class="btn-ratio" data-ratio="9:16" data-w="1080" data-h="1920" role="radio" aria-checked="false">
            <span class="label">9:16 Story / Reel</span>
            <span class="dim">Vertical (1080×1920)</span>
          </button>
          <button type="button" class="btn-ratio" data-ratio="16:9" data-w="1920" data-h="1080" role="radio" aria-checked="false">
            <span class="label">16:9 Landscape</span>
            <span class="dim">Banner (1920×1080)</span>
          </button>
        </div>
      </section>

      <!-- Card 2: Statement Text (Default Active Tab on Mobile) -->
      <section class="control-card active-tab-card" id="cardText" aria-labelledby="headingText">
        <div class="card-header">
          <h2 class="card-title" id="headingText">
            <span class="section-index">02</span> Statement Text
          </h2>
          <div style="display: flex; gap: 6px; align-items: center;">
            <button type="button" class="btn-action-text" id="btnSampleText" title="Insert sample viral quote">↺ Sample</button>
            <button type="button" class="btn-action-text" id="btnClearText" title="Clear text box">✕ Clear</button>
            <span id="charCount" style="color: var(--text-muted); font-size: 0.68rem; font-family: var(--font-mono); margin-left: 4px;">72 Chars</span>
          </div>
        </div>
        <textarea id="inputText" class="textarea-field" rows="4" placeholder="Write your raw statement here..." aria-label="Statement Text"></textarea>
      </section>

      <!-- Card 3: Attached Media (Photo / GIF / Video Clip) -->
      <section class="control-card" id="cardMedia" aria-labelledby="headingMedia">
        <div class="card-header">
          <h2 class="card-title" id="headingMedia">
            <span class="section-index">03</span> Attached Media
          </h2>
          <span id="mediaStatusBadge" style="color: var(--text-muted); font-family: var(--font-mono); font-size: 0.72rem; font-weight: 600;">None</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 12px;">
          <!-- Upload Button & File Input -->
          <div style="display: flex; gap: 8px;">
            <button type="button" class="btn btn-secondary btn-sm" id="btnUploadMedia" style="flex: 1; gap: 6px;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
              <span>Upload Photo / GIF / Video</span>
            </button>
            <button type="button" class="btn btn-secondary btn-sm" id="btnRemoveMedia" title="Remove attached media" style="display: none;">
              <span>Remove</span>
            </button>
          </div>
          <input type="file" id="inputMediaFile" accept="image/*,video/*,.gif" style="display: none;">

          <!-- Media Preview Banner (Hidden when none) -->
          <div id="mediaPreviewBanner" style="display: none; align-items: center; gap: 10px; background: var(--bg-recessed); border: 1px solid var(--border-hairline); border-radius: var(--radius-sm); padding: 8px 10px;">
            <div id="mediaThumbBox" style="width: 48px; height: 48px; border-radius: 4px; overflow: hidden; background: #000; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"></div>
            <div style="flex: 1; overflow: hidden;">
              <div id="mediaFileName" style="font-size: 0.76rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: var(--text-main);"></div>
              <div id="mediaFileInfo" style="font-size: 0.68rem; color: var(--text-muted); font-family: var(--font-mono);"></div>
            </div>
          </div>

          <!-- Alignment: Default Center (Requested by User) -->
          <div>
            <div class="slider-label-row">
              <span>Media Alignment</span>
              <span id="labelMediaAlign" style="color: var(--gold); font-size: 0.68rem; font-family: var(--font-mono); font-weight: 700;">CENTER (DEFAULT)</span>
            </div>
            <div class="btn-toggle-group" role="radiogroup" aria-label="Media Alignment">
              <button type="button" class="btn-toggle active" id="btnMediaAlignCenter" role="radio" aria-checked="true">Center (Default)</button>
              <button type="button" class="btn-toggle" id="btnMediaAlignLeft" role="radio" aria-checked="false">Left</button>
              <button type="button" class="btn-toggle" id="btnMediaAlignFull" role="radio" aria-checked="false">Full Width</button>
            </div>
          </div>

          <!-- Corner Bluntness / Corner Trim (Requested by User) -->
          <div class="slider-row" style="margin-top: 4px;">
            <div class="slider-label-row">
              <span>Corner Trim (Blunt Edges)</span>
              <span id="labelMediaRadius">18 px</span>
            </div>
            <div class="slider-stepper-wrap">
              <button type="button" class="btn-stepper" id="btnMediaRadiusMinus" title="Decrease Bluntness">-</button>
              <input type="range" id="rangeMediaRadius" min="0" max="48" value="18" aria-label="Corner Bluntness Radius">
              <button type="button" class="btn-stepper" id="btnMediaRadiusPlus" title="Increase Bluntness">+</button>
            </div>
          </div>

          <!-- Media Max Height / Scale -->
          <div class="slider-row" style="margin-top: 4px;">
            <div class="slider-label-row">
              <span>Media Max Height</span>
              <span id="labelMediaMaxHeight">520 px</span>
            </div>
            <div class="slider-stepper-wrap">
              <button type="button" class="btn-stepper" id="btnMediaHeightMinus" title="Decrease Max Height">-</button>
              <input type="range" id="rangeMediaHeight" min="200" max="850" value="520" aria-label="Media Max Height">
              <button type="button" class="btn-stepper" id="btnMediaHeightPlus" title="Increase Max Height">+</button>
            </div>
          </div>

          <!-- Frame Rim Border for Media -->
          <div style="margin-top: 4px;">
            <div class="slider-label-row">
              <span>Media Border Rim</span>
            </div>
            <select id="selectMediaBorder" aria-label="Media Border Rim">
              <option value="rgba(255, 255, 255, 0.14)" selected>Subtle Steel Rim (rgba 14%) · Aesthetic</option>
              <option value="#ffffff">Crisp White Rim (#ffffff)</option>
              <option value="#c5a059">Champagne Gold (#c5a059)</option>
              <option value="none">None (Borderless)</option>
            </select>
          </div>
        </div>
      </section>

      <!-- Card 4: Profile Avatar -->
      <section class="control-card" id="cardAvatar" aria-labelledby="headingAvatar">
        <div class="card-header">
          <h2 class="card-title" id="headingAvatar">
            <span class="section-index">04</span> Profile Avatar
          </h2>
          <span id="pfpStatusBadge" style="color: var(--gold); font-weight: 700; font-family: var(--font-mono); font-size: 0.72rem;">Mog Hamster</span>
        </div>
        
        <div class="pfp-slot-container">
          <div class="pfp-preview-box" id="pfpPreviewBox">
            <img id="activePfpImg" src="{mog_b64}" onerror="this.src='assets/pfps/pfp_mog_hamster.png'" alt="Active Avatar">
          </div>

          <div class="pfp-upload-actions">
            <div class="pfp-upload-btn-wrap">
              <button type="button" class="btn btn-secondary btn-sm" id="btnUploadPfp" style="flex: 1;">
                <span>Upload Image</span>
              </button>
              <button type="button" class="btn btn-secondary btn-sm" id="btnResetPfp" title="Reset to default Mog Hamster">
                <span>Reset Mog</span>
              </button>
            </div>
            <input type="file" id="inputPfpFile" accept="image/*" style="display: none;">
          </div>
        </div>

        <!-- Avatar Shape Toggle -->
        <div style="margin-top: 14px;">
          <div class="slider-label-row">
            <span>Avatar Shape in Post</span>
          </div>
          <div class="btn-toggle-group" role="radiogroup" aria-label="Avatar Shape">
            <button type="button" class="btn-toggle active" id="btnPfpCircle" role="radio" aria-checked="true">● Circle Frame</button>
            <button type="button" class="btn-toggle" id="btnPfpSquare" role="radio" aria-checked="false">■ Square Frame</button>
          </div>
        </div>

        <!-- Avatar Frame Rim Color -->
        <div style="margin-top: 14px;">
          <div class="slider-label-row">
            <span>Avatar Frame Rim Color</span>
            <span id="labelFrameColor" style="font-family: var(--font-mono); font-size: 0.68rem; color: var(--gold); font-weight: 700;">CRISP WHITE</span>
          </div>
          <select id="selectPfpFrameColor" aria-label="Avatar Frame Rim Color">
            <option value="#ffffff" selected>Crisp Titanium White (#ffffff) · High Definition</option>
            <option value="#f4ede2">Warm Editorial Ivory (#f4ede2) · Classic Atelier</option>
            <option value="#c5a059">Champagne Gold (#c5a059) · Antique Luxury</option>
            <option value="#8e95a5">Slate Titanium (#8e95a5) · Neutral Steel Rim</option>
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
            <input type="range" id="rangePfpSize" min="60" max="150" value="96" aria-label="Avatar Scale Slider">
            <button type="button" class="btn-stepper" id="btnPfpSizePlus" title="Increase Size">+</button>
          </div>
        </div>
      </section>

      <!-- Card 5: Identity & Typography -->
      <section class="control-card" id="cardStyle" aria-labelledby="headingStyle">
        <div class="card-header">
          <h2 class="card-title" id="headingStyle">
            <span class="section-index">05</span> Identity &amp; Typography
          </h2>
        </div>
        <div style="display: flex; gap: 8px; margin-bottom: 12px;">
          <input type="text" class="input-field" id="inputName" value="Mr. Hamster" placeholder="Display Name" aria-label="Display Name">
          <input type="text" class="input-field" id="inputHandle" value="@mrr.hamster" placeholder="Handle" aria-label="Handle">
        </div>
        <div style="display: flex; gap: 18px; margin-bottom: 14px;">
          <label class="checkbox-container">
            <input type="checkbox" id="checkVerified" checked>
            <span>Verified Badge</span>
          </label>
        </div>

        <!-- Font Size Slider with Stepper [-] [+] -->
        <div class="slider-row" style="margin-top: 0; margin-bottom: 14px;">
          <div class="slider-label-row">
            <span>Font Size</span>
            <span id="labelFontSize">46 px</span>
          </div>
          <div class="slider-stepper-wrap">
            <button type="button" class="btn-stepper" id="btnFontSizeMinus" title="Decrease Font">-</button>
            <input type="range" id="rangeFontSize" min="26" max="74" value="46" aria-label="Font Size Slider">
            <button type="button" class="btn-stepper" id="btnFontSizePlus" title="Increase Font">+</button>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
          <div>
            <label for="selectTextAlign" style="display: block; font-size: 0.69rem; color: var(--text-dim); font-family: var(--font-mono); margin-bottom: 4px; text-transform: uppercase; font-weight: 600;">Text Align</label>
            <select id="selectTextAlign">
              <option value="left" selected>Left</option>
              <option value="center">Center</option>
            </select>
          </div>
          <div>
            <label for="selectHeaderAlign" style="display: block; font-size: 0.69rem; color: var(--text-dim); font-family: var(--font-mono); margin-bottom: 4px; text-transform: uppercase; font-weight: 600;">Header Layout</label>
            <select id="selectHeaderAlign">
              <option value="left" selected>Left (Classic)</option>
              <option value="center">Center (Editorial)</option>
            </select>
          </div>
        </div>
      </section>

      <!-- Export Actions (Desktop Only) -->
      <div class="desktop-export-actions" style="display: flex; flex-direction: column; gap: 10px; margin-top: 4px;">
        <button type="button" class="btn btn-primary" id="btnDownload" style="padding: 14px 20px; font-size: 0.88rem; gap: 8px;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          <span id="btnDownloadText">Download 1080p Post (Lossless PNG)</span>
        </button>
        <button type="button" class="btn btn-secondary" id="btnCopy" style="width: 100%; gap: 7px;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          <span>Copy to Clipboard</span>
        </button>
      </div>

    </aside>

    <!-- Right Live Canvas Workspace Pedestal -->
    <section class="preview-workspace" aria-label="Live Post Preview Pedestal">
      <figure class="canvas-pedestal" id="canvasPedestal">
        <button type="button" class="btn-pedestal-expand" id="btnOpenFullscreen" title="Expand Fullscreen Preview">⛶ Fullscreen</button>
        <canvas id="postCanvas" width="1080" height="1350" role="img" aria-label="Mr. Hamster generated post canvas"></canvas>
        <figcaption class="sr-only">High definition 1080p rendered statement post</figcaption>
      </figure>
    </section>

    <!-- Mobile Segmented Tool Tabs (Pinned under Live Preview) -->
    <nav class="mobile-tool-tabs" id="mobileToolTabs" aria-label="Mobile Tool Navigation">
      <button type="button" class="mobile-tool-tab active" data-target="cardText">
        <span>Statement</span>
      </button>
      <button type="button" class="mobile-tool-tab" data-target="cardMedia">
        <span>Media</span>
      </button>
      <button type="button" class="mobile-tool-tab" data-target="cardRatio">
        <span>Format</span>
      </button>
      <button type="button" class="mobile-tool-tab" data-target="cardAvatar">
        <span>Avatar</span>
      </button>
      <button type="button" class="mobile-tool-tab" data-target="cardStyle">
        <span>Identity</span>
      </button>
    </nav>

  </main>

  <!-- Mobile Floating Quick Bar -->
  <footer class="mobile-floating-bar" id="mobileFloatingBar" role="contentinfo" aria-label="Mobile Quick Export Bar">
    <button type="button" class="btn btn-secondary" id="btnMobileCopy" style="flex: 0 0 68px; min-height: 48px; padding: 0 8px; gap: 5px; font-size: 0.72rem;" title="Copy to Clipboard">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
      <span>Copy</span>
    </button>
    <button type="button" class="btn btn-primary" id="btnMobileDownload" style="flex: 1; min-height: 48px; font-size: 0.82rem; gap: 7px;">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
      <span>Download 1080p Post</span>
    </button>
  </footer>

  <!-- Toast Notification -->
  <div id="toast" class="toast" role="status" aria-live="polite"></div>

  <script>
    // System Master Credentials
    const AUTH_CREDS = {{
      username: 'ashiq',
      password: 'ashiq14726'
    }};

    const DEFAULT_HAMSTER_B64 = "{mog_b64}";
    const VERIFIED_BADGE_B64 = "{verified_badge_b64}";
    const verifiedBadgeImg = new Image();
    verifiedBadgeImg.onload = () => {{
      render();
    }};
    verifiedBadgeImg.src = VERIFIED_BADGE_B64;

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
      verified: true,
      fontSize: 46,
      vAlign: 'center',
      textAlign: 'left',
      // Attached Media defaults:
      mediaElement: null,
      mediaType: null, // 'image', 'gif', or 'video'
      mediaAlign: 'center', // DEFAULT CENTER ALIGNMENT
      mediaCornerRadius: 18, // DEFAULT BLUNT CORNERS (18px)
      mediaMaxHeight: 520,
      mediaBorder: 'rgba(255, 255, 255, 0.14)',
      mediaFileName: ''
    }};

    const state = Object.assign({{}}, DEFAULTS);
    document.getElementById('inputText').value = state.text.replace(/\\\\n/g, '\\n');

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
      btnPfpCircle.setAttribute('aria-checked', 'true');
      btnPfpSquare.setAttribute('aria-checked', 'false');
      state.pfpShape = 'circle';
      render();
    }});

    btnPfpSquare.addEventListener('click', () => {{
      btnPfpSquare.classList.add('active');
      btnPfpCircle.classList.remove('active');
      btnPfpSquare.setAttribute('aria-checked', 'true');
      btnPfpCircle.setAttribute('aria-checked', 'false');
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

    // ========================================================
    // ATTACHED MEDIA (PHOTO / GIF / VIDEO) CONTROLLER
    // ========================================================
    const inputMediaFile = document.getElementById('inputMediaFile');
    const btnUploadMedia = document.getElementById('btnUploadMedia');
    const btnRemoveMedia = document.getElementById('btnRemoveMedia');
    const mediaPreviewBanner = document.getElementById('mediaPreviewBanner');
    const mediaThumbBox = document.getElementById('mediaThumbBox');
    const mediaFileName = document.getElementById('mediaFileName');
    const mediaFileInfo = document.getElementById('mediaFileInfo');
    const mediaStatusBadge = document.getElementById('mediaStatusBadge');

    const btnMediaAlignCenter = document.getElementById('btnMediaAlignCenter');
    const btnMediaAlignLeft = document.getElementById('btnMediaAlignLeft');
    const btnMediaAlignFull = document.getElementById('btnMediaAlignFull');
    const labelMediaAlign = document.getElementById('labelMediaAlign');

    const rangeMediaRadius = document.getElementById('rangeMediaRadius');
    const labelMediaRadius = document.getElementById('labelMediaRadius');
    const rangeMediaHeight = document.getElementById('rangeMediaHeight');
    const labelMediaMaxHeight = document.getElementById('labelMediaMaxHeight');
    const selectMediaBorder = document.getElementById('selectMediaBorder');

    let videoLoopId = null;

    btnUploadMedia.addEventListener('click', () => inputMediaFile.click());

    inputMediaFile.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files[0]) {{
        const file = e.target.files[0];
        handleMediaFile(file);
      }}
    }});

    function handleMediaFile(file) {{
      const isVideo = file.type.startsWith('video/');
      const isGif = file.type === 'image/gif' || file.name.toLowerCase().endsWith('.gif');
      state.mediaFileName = file.name;

      if (isVideo) {{
        state.mediaType = 'video';
        const url = URL.createObjectURL(file);
        const vid = document.createElement('video');
        vid.src = url;
        vid.crossOrigin = 'anonymous';
        vid.loop = true;
        vid.muted = true;
        vid.playsInline = true;
        vid.autoplay = true;
        vid.onloadedmetadata = () => {{
          state.mediaElement = vid;
          vid.play().catch(() => {{}});
          updateMediaUI(file, 'Video Clip', `${{vid.videoWidth}}×${{vid.videoHeight}} · Loop`);
          startVideoLoop();
          render();
          showToast('Video Clip Attached (Playing Live)');
        }};
      }} else {{
        state.mediaType = isGif ? 'gif' : 'image';
        const reader = new FileReader();
        reader.onload = (evt) => {{
          const img = new Image();
          img.crossOrigin = 'anonymous';
          img.onload = () => {{
            state.mediaElement = img;
            if (videoLoopId) cancelAnimationFrame(videoLoopId);
            updateMediaUI(file, isGif ? 'GIF Animation' : 'Photo', `${{img.naturalWidth}}×${{img.naturalHeight}} px`);
            render();
            showToast(isGif ? 'GIF Attached' : 'Photo Attached');
          }};
          img.src = evt.target.result;
        }};
        reader.readAsDataURL(file);
      }}
    }}

    function updateMediaUI(file, typeDesc, dimsDesc) {{
      mediaStatusBadge.textContent = typeDesc;
      mediaStatusBadge.style.color = 'var(--gold)';
      mediaFileName.textContent = file.name;
      mediaFileInfo.textContent = `${{typeDesc}} · ${{dimsDesc}}`;
      mediaPreviewBanner.style.display = 'flex';
      btnRemoveMedia.style.display = 'inline-flex';

      // Thumbnail
      mediaThumbBox.innerHTML = '';
      if (state.mediaType === 'video') {{
        const thumbVid = document.createElement('video');
        thumbVid.src = state.mediaElement.src;
        thumbVid.muted = true;
        thumbVid.style.width = '100%';
        thumbVid.style.height = '100%';
        thumbVid.style.objectFit = 'cover';
        mediaThumbBox.appendChild(thumbVid);
      }} else {{
        const thumbImg = document.createElement('img');
        thumbImg.src = state.mediaElement.src;
        thumbImg.style.width = '100%';
        thumbImg.style.height = '100%';
        thumbImg.style.objectFit = 'cover';
        mediaThumbBox.appendChild(thumbImg);
      }}
    }}

    btnRemoveMedia.addEventListener('click', () => {{
      if (videoLoopId) cancelAnimationFrame(videoLoopId);
      if (state.mediaElement && state.mediaType === 'video') {{
        try {{ state.mediaElement.pause(); }} catch (e) {{}}
      }}
      state.mediaElement = null;
      state.mediaType = null;
      state.mediaFileName = '';
      inputMediaFile.value = '';
      mediaStatusBadge.textContent = 'None';
      mediaStatusBadge.style.color = 'var(--text-muted)';
      mediaPreviewBanner.style.display = 'none';
      btnRemoveMedia.style.display = 'none';
      render();
      showToast('Media Removed');
    }});

    function startVideoLoop() {{
      if (videoLoopId) cancelAnimationFrame(videoLoopId);
      function step() {{
        if (state.mediaType === 'video' && state.mediaElement && !state.mediaElement.paused && !state.mediaElement.ended) {{
          render();
          videoLoopId = requestAnimationFrame(step);
        }}
      }}
      videoLoopId = requestAnimationFrame(step);
    }}

    // Media Alignment (Center is default)
    btnMediaAlignCenter.addEventListener('click', () => {{
      btnMediaAlignCenter.classList.add('active');
      btnMediaAlignLeft.classList.remove('active');
      btnMediaAlignFull.classList.remove('active');
      state.mediaAlign = 'center';
      labelMediaAlign.textContent = 'CENTER (DEFAULT)';
      render();
    }});
    btnMediaAlignLeft.addEventListener('click', () => {{
      btnMediaAlignLeft.classList.add('active');
      btnMediaAlignCenter.classList.remove('active');
      btnMediaAlignFull.classList.remove('active');
      state.mediaAlign = 'left';
      labelMediaAlign.textContent = 'LEFT';
      render();
    }});
    btnMediaAlignFull.addEventListener('click', () => {{
      btnMediaAlignFull.classList.add('active');
      btnMediaAlignCenter.classList.remove('active');
      btnMediaAlignLeft.classList.remove('active');
      state.mediaAlign = 'full';
      labelMediaAlign.textContent = 'FULL WIDTH';
      render();
    }});

    // Corner Bluntness Slider & Steppers
    document.getElementById('btnMediaRadiusMinus').addEventListener('click', () => {{
      let v = parseInt(rangeMediaRadius.value, 10) - 2;
      if (v < 0) v = 0;
      rangeMediaRadius.value = v;
      state.mediaCornerRadius = v;
      labelMediaRadius.textContent = `${{v}} px`;
      render();
    }});
    document.getElementById('btnMediaRadiusPlus').addEventListener('click', () => {{
      let v = parseInt(rangeMediaRadius.value, 10) + 2;
      if (v > 48) v = 48;
      rangeMediaRadius.value = v;
      state.mediaCornerRadius = v;
      labelMediaRadius.textContent = `${{v}} px`;
      render();
    }});
    rangeMediaRadius.addEventListener('input', (e) => {{
      state.mediaCornerRadius = parseInt(e.target.value, 10);
      labelMediaRadius.textContent = `${{state.mediaCornerRadius}} px`;
      render();
    }});

    // Media Max Height Slider & Steppers
    document.getElementById('btnMediaHeightMinus').addEventListener('click', () => {{
      let v = parseInt(rangeMediaHeight.value, 10) - 20;
      if (v < 200) v = 200;
      rangeMediaHeight.value = v;
      state.mediaMaxHeight = v;
      labelMediaMaxHeight.textContent = `${{v}} px`;
      render();
    }});
    document.getElementById('btnMediaHeightPlus').addEventListener('click', () => {{
      let v = parseInt(rangeMediaHeight.value, 10) + 20;
      if (v > 850) v = 850;
      rangeMediaHeight.value = v;
      state.mediaMaxHeight = v;
      labelMediaMaxHeight.textContent = `${{v}} px`;
      render();
    }});
    rangeMediaHeight.addEventListener('input', (e) => {{
      state.mediaMaxHeight = parseInt(e.target.value, 10);
      labelMediaMaxHeight.textContent = `${{state.mediaMaxHeight}} px`;
      render();
    }});

    // Media Border Selector
    selectMediaBorder.addEventListener('change', (e) => {{
      state.mediaBorder = e.target.value;
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
      state.mediaAlign = DEFAULTS.mediaAlign;
      state.mediaCornerRadius = DEFAULTS.mediaCornerRadius;
      state.mediaMaxHeight = DEFAULTS.mediaMaxHeight;
      state.mediaBorder = DEFAULTS.mediaBorder;

      rangeFontSize.value = state.fontSize;
      labelFontSize.textContent = `${{state.fontSize}} px`;
      rangePfpSize.value = state.pfpSize;
      labelPfpSize.textContent = `${{state.pfpSize}} px`;
      rangeMediaRadius.value = state.mediaCornerRadius;
      labelMediaRadius.textContent = `${{state.mediaCornerRadius}} px`;
      rangeMediaHeight.value = state.mediaMaxHeight;
      labelMediaMaxHeight.textContent = `${{state.mediaMaxHeight}} px`;
      document.getElementById('selectTextAlign').value = state.textAlign;
      document.getElementById('selectHeaderAlign').value = state.headerAlign;
      selectPfpFrameColor.value = state.pfpFrameColor;
      labelFrameColor.textContent = 'CRISP WHITE';
      selectMediaBorder.value = state.mediaBorder;

      btnPfpCircle.classList.add('active');
      btnPfpSquare.classList.remove('active');
      btnPfpCircle.setAttribute('aria-checked', 'true');
      btnPfpSquare.setAttribute('aria-checked', 'false');

      btnMediaAlignCenter.classList.add('active');
      btnMediaAlignLeft.classList.remove('active');
      btnMediaAlignFull.classList.remove('active');
      labelMediaAlign.textContent = 'CENTER (DEFAULT)';

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
        document.querySelectorAll('.btn-ratio').forEach(b => {{
          b.classList.remove('active');
          b.setAttribute('aria-checked', 'false');
        }});
        btn.classList.add('active');
        btn.setAttribute('aria-checked', 'true');

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

    // Mobile Segmented Tool Dock Controller
    const mobileToolTabs = document.querySelectorAll('.mobile-tool-tab');
    const controlCards = document.querySelectorAll('.controls-panel .control-card');

    mobileToolTabs.forEach(tab => {{
      tab.addEventListener('click', () => {{
        mobileToolTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const targetId = tab.dataset.target;
        controlCards.forEach(c => {{
          if (c.id === targetId) {{
            c.classList.add('active-tab-card');
          }} else {{
            c.classList.remove('active-tab-card');
          }}
        }});
      }});
    }});

    // Quick text helpers
    const inputText = document.getElementById('inputText');
    document.getElementById('btnSampleText').addEventListener('click', () => {{
      inputText.value = 'flirting is easy until you have to flirt\\nwith someone you actually want.';
      state.text = inputText.value;
      document.getElementById('charCount').textContent = `${{state.text.length}} Chars`;
      render();
      showToast('Sample Quote Loaded');
    }});

    document.getElementById('btnClearText').addEventListener('click', () => {{
      inputText.value = '';
      state.text = '';
      document.getElementById('charCount').textContent = '0 Chars';
      render();
      showToast('Text Cleared');
    }});

    inputText.addEventListener('input', (e) => {{
      state.text = e.target.value;
      document.getElementById('charCount').textContent = `${{state.text.length}} Chars`;
      render();
    }});

    // Identity Listeners
    document.getElementById('inputName').addEventListener('input', (e) => {{
      state.name = e.target.value;
      render();
    }});
    document.getElementById('inputHandle').addEventListener('input', (e) => {{
      state.handle = e.target.value;
      render();
    }});
    document.getElementById('checkVerified').addEventListener('change', (e) => {{
      state.verified = e.target.checked;
      render();
    }});

    // Layout Selectors
    document.getElementById('selectTextAlign').addEventListener('change', (e) => {{
      state.textAlign = e.target.value;
      render();
    }});
    document.getElementById('selectHeaderAlign').addEventListener('change', (e) => {{
      state.headerAlign = e.target.value;
      render();
    }});

    // Line Breaking Utility
    function getLines(ctx, text, maxWidth) {{
      const lines = [];
      const paragraphs = text.split('\\n');
      for (const para of paragraphs) {{
        if (para === '') {{
          lines.push('');
          continue;
        }}
        const words = para.split(' ');
        let currentLine = words[0];
        for (let i = 1; i < words.length; i++) {{
          const word = words[i];
          const testLine = currentLine + ' ' + word;
          if (ctx.measureText(testLine).width < maxWidth) {{
            currentLine = testLine;
          }} else {{
            lines.push(currentLine);
            currentLine = word;
          }}
        }}
        lines.push(currentLine);
      }}
      return lines;
    }}

    // Helper: Rounded Rectangle / Blunt Corner Trim Path
    function drawRoundedRect(ctx, x, y, width, height, radius) {{
      if (radius <= 0) {{
        ctx.beginPath();
        ctx.rect(x, y, width, height);
        return;
      }}
      const maxR = Math.min(width / 2, height / 2);
      const r = Math.min(radius, maxR);
      ctx.beginPath();
      ctx.moveTo(x + r, y);
      ctx.lineTo(x + width - r, y);
      ctx.arcTo(x + width, y, x + width, y + r, r);
      ctx.lineTo(x + width, y + height - r);
      ctx.arcTo(x + width, y + height, x + width - r, y + height, r);
      ctx.lineTo(x + r, y + height);
      ctx.arcTo(x, y + height, x, y + height - r, r);
      ctx.lineTo(x, y + r);
      ctx.arcTo(x, y, x + r, y, r);
      ctx.closePath();
    }}

    // Master High-Resolution Canvas Renderer (100% OLED Black)
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
      const fontFamily = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';

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

      const headerToTextGap = 34;

      // Determine Media Height if attached
      let mediaDrawW = 0;
      let mediaDrawH = 0;
      let mediaDrawX = 0;
      let hasMedia = false;
      const textToMediaGap = 26;

      if (state.mediaElement) {{
        const isReady = (state.mediaType === 'video') ? (state.mediaElement.readyState >= 2) : state.mediaElement.complete;
        if (isReady) {{
          hasMedia = true;
          const natW = state.mediaElement.videoWidth || state.mediaElement.naturalWidth || 800;
          const natH = state.mediaElement.videoHeight || state.mediaElement.naturalHeight || 600;
          const mediaAspect = natW / natH;

          let maxAllowedW = contentWidth;
          if (state.mediaAlign === 'full') {{
            maxAllowedW = contentWidth;
          }} else {{
            maxAllowedW = Math.min(contentWidth, 900);
          }}

          let maxAllowedH = state.mediaMaxHeight || 520;
          mediaDrawW = maxAllowedW;
          mediaDrawH = mediaDrawW / mediaAspect;

          if (mediaDrawH > maxAllowedH) {{
            mediaDrawH = maxAllowedH;
            mediaDrawW = mediaDrawH * mediaAspect;
          }}

          // Horizontal alignment (Default: Center)
          if (state.mediaAlign === 'left') {{
            mediaDrawX = marginX;
          }} else {{
            // Centered horizontally
            mediaDrawX = Math.round((W - mediaDrawW) / 2);
          }}
        }}
      }}

      const totalBlockHeight = headerHeight + headerToTextGap + textBlockHeight + (hasMedia ? (textToMediaGap + mediaDrawH) : 0);

      // Determine Start Y
      let startY = 120;
      if (state.vAlign === 'center') {{
        startY = Math.max(80, Math.round((H - totalBlockHeight) / 2));
      }} else if (state.aspect === '9:16') {{
        startY = 200;
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
      ctx.fillStyle = '#FFFFFF';
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
          // Circle frame
          ctx.arc(pfpX + radius, pfpY + radius, radius, 0, Math.PI * 2);
          ctx.stroke();
        }}
        ctx.restore();
      }}

      // 2. Render Name & Handle
      ctx.save();
      const nameSize = Math.max(26, Math.round(pfpSize * 0.36));
      const handleSize = Math.max(20, Math.round(nameSize * 0.74));

      if (isCenteredHeader) {{
        // Center-aligned editorial header
        const textCenterY = pfpY + pfpSize + 28;
        ctx.font = `700 ${{nameSize}}px ${{fontFamily}}`;
        ctx.fillStyle = '#FFFFFF';

        const nameWidth = ctx.measureText(state.name).width;
        const badgeSize = Math.max(20, Math.round(nameSize * 0.72));
        const badgeGap = 8;

        if (state.verified) {{
          const totalWidth = nameWidth + badgeGap + badgeSize;
          const startX = Math.round(W / 2 - totalWidth / 2);
          ctx.textAlign = 'left';
          ctx.textBaseline = 'middle';
          const nameMidY = Math.round(textCenterY + nameSize * 0.5);
          ctx.fillText(state.name, startX, nameMidY);

          const badgeX = startX + nameWidth + badgeGap;
          const badgeY = Math.round(nameMidY - badgeSize / 2);
          if (verifiedBadgeImg.complete && verifiedBadgeImg.naturalWidth !== 0) {{
            ctx.drawImage(verifiedBadgeImg, badgeX, badgeY, badgeSize, badgeSize);
          }}
        }} else {{
          ctx.textAlign = 'center';
          ctx.textBaseline = 'top';
          ctx.fillText(state.name, W / 2, textCenterY);
        }}

        ctx.font = `400 ${{handleSize}}px ${{fontFamily}}`;
        ctx.fillStyle = '#71767B';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'top';
        ctx.fillText(state.handle, W / 2, textCenterY + nameSize + 6);
      }} else {{
        // Left-aligned classic layout
        const textLeftX = pfpX + pfpSize + 18;
        const nameBaselineY = pfpY + Math.round(pfpSize * 0.42);

        ctx.font = `700 ${{nameSize}}px ${{fontFamily}}`;
        ctx.fillStyle = '#FFFFFF';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'middle';
        ctx.fillText(state.name, textLeftX, nameBaselineY);

        if (state.verified) {{
          const nameWidth = ctx.measureText(state.name).width;
          const badgeSize = Math.max(20, Math.round(nameSize * 0.72));
          const badgeGap = 8;
          const badgeX = Math.round(textLeftX + nameWidth + badgeGap);
          const badgeY = Math.round(nameBaselineY - badgeSize / 2);
          if (verifiedBadgeImg.complete && verifiedBadgeImg.naturalWidth !== 0) {{
            ctx.drawImage(verifiedBadgeImg, badgeX, badgeY, badgeSize, badgeSize);
          }}
        }}

        const handleBaselineY = pfpY + Math.round(pfpSize * 0.76);
        ctx.font = `400 ${{handleSize}}px ${{fontFamily}}`;
        ctx.fillStyle = '#71767B';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'middle';
        ctx.fillText(state.handle, textLeftX, handleBaselineY);
      }}
      ctx.restore();

      // 3. Render Statement Text Lines
      ctx.save();
      const textStartY = startY + headerHeight + headerToTextGap;
      ctx.font = `400 ${{state.fontSize}}px ${{fontFamily}}`;
      ctx.fillStyle = '#E7E9EA'; // Crisp White-Silver Tweet Text
      ctx.textBaseline = 'top';

      lines.forEach((line, index) => {{
        const lineY = textStartY + (index * lineHeight);
        if (state.textAlign === 'center') {{
          ctx.textAlign = 'center';
          ctx.fillText(line, W / 2, lineY);
        }} else {{
          ctx.textAlign = 'left';
          ctx.fillText(line, marginX, lineY);
        }}
      }});
      ctx.restore();

      // 4. Render Attached Media (Centered by default, Blunt Trimmed Corners)
      if (hasMedia) {{
        const mediaY = textStartY + textBlockHeight + textToMediaGap;
        const r = state.mediaCornerRadius; // Blunt corner radius

        ctx.save();
        drawRoundedRect(ctx, mediaDrawX, mediaY, mediaDrawW, mediaDrawH, r);
        ctx.clip();
        ctx.drawImage(state.mediaElement, mediaDrawX, mediaY, mediaDrawW, mediaDrawH);
        ctx.restore();

        // Optional Rim Outline
        if (state.mediaBorder && state.mediaBorder !== 'none') {{
          ctx.save();
          ctx.lineWidth = 2;
          ctx.strokeStyle = state.mediaBorder;
          drawRoundedRect(ctx, mediaDrawX, mediaY, mediaDrawW, mediaDrawH, r);
          ctx.stroke();
          ctx.restore();
        }}
      }}
    }}

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

    // Mobile Pinned Actions
    document.getElementById('btnMobileDownload').addEventListener('click', () => {{
      document.getElementById('btnDownload').click();
    }});
    document.getElementById('btnMobileCopy').addEventListener('click', () => {{
      document.getElementById('btnCopy').click();
    }});
    document.getElementById('btnQuickExport').addEventListener('click', () => {{
      document.getElementById('btnDownload').click();
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
      setTimeout(() => t.classList.remove('show'), 2400);
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
print(f"Wrote generator.html ({len(html_content)} bytes)")
