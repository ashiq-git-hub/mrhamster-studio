from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1350
img = Image.new('RGB', (W, H), (0, 0, 0))
draw = ImageDraw.Draw(img)

# Load PFP
assets_dir = r'C:\Users\Thoufeek\.gemini\antigravity\scratch\meme_page_project\assets'
pfp_path = os.path.join(assets_dir, 'pfp_mog_hamster.png')
pfp = Image.open(pfp_path).convert('RGBA')

pfp_size = 94
pfp = pfp.resize((pfp_size, pfp_size), Image.Resampling.NEAREST)

# Create circular mask and soft pink circle background
mask = Image.new('L', (pfp_size, pfp_size), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0, 0, pfp_size, pfp_size), fill=255)

# PFP background circle in soft pink to match hamster nose
pfp_circle = Image.new('RGBA', (pfp_size, pfp_size), (255, 214, 224, 255))
pfp_circle.paste(pfp, (0, 0), pfp)

# Coordinates
marginX = 90
startY = 520  # Centered look for short punchy quote

# Paste circular PFP
img.paste(pfp_circle, (marginX, startY), mask)

# Draw PFP outline ring
draw.ellipse([marginX, startY, marginX + pfp_size, startY + pfp_size], outline=(255, 71, 126, 120), width=2)

# Load standard fonts or default
try:
    font_name = ImageFont.truetype('arialbd.ttf', 32)
    font_handle = ImageFont.truetype('arial.ttf', 24)
    font_text = ImageFont.truetype('arial.ttf', 44)
except Exception:
    font_name = ImageFont.load_default()
    font_handle = ImageFont.load_default()
    font_text = ImageFont.load_default()

# Header text
infoX = marginX + pfp_size + 20
draw.text((infoX, startY + 12), "Mr. Hamster", fill=(255, 255, 255), font=font_name)
draw.text((infoX, startY + 50), "@mrr.hamster", fill=(113, 118, 123), font=font_handle)

# Quote text
quote = "flirting is easy until you have to flirt\nwith someone you actually want."
textY = startY + pfp_size + 36
draw.text((marginX, textY), quote, fill=(247, 249, 249), font=font_text, spacing=14)

out_path = r'C:\Users\Thoufeek\.gemini\antigravity\scratch\meme_page_project\assets\sample_post_1080x1350.png'
img.save(out_path)

# Also save in artifacts brain dir so we can embed it directly in chat!
brain_sample = r'C:\Users\Thoufeek\.gemini\antigravity\brain\ab5d6534-892b-4bbc-b5f5-13c218bbb0bb\sample_post_1080x1350.png'
img.save(brain_sample)
print('Sample post generated successfully!')
