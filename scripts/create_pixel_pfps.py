from PIL import Image, ImageOps
import numpy as np

# Let's inspect the cards:
# 1. 'Look what we have here...'
# In img3 (1024x640):
img3 = Image.open('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/.user_uploaded/media_1794307621546_fc5b2035.jpg')
# card is at x ~ 804 to 974, y ~ 190 to 406
c_look = img3.crop((804, 192, 974, 406))
# Remove the card rounded border and make the background clean pure white
arr = np.array(c_look)
# Replace off-white/light grey card background with pure white (255, 255, 255)
# If pixel is near white (> 235 on all channels), make it 255
mask = (arr[:, :, 0] > 230) & (arr[:, :, 1] > 230) & (arr[:, :, 2] > 230)
arr[mask] = [255, 255, 255]
# Let's save as clean 1:1 PFP
c_look_clean = Image.fromarray(arr)
w, h = c_look_clean.size
size = max(w, h) + 40
pfp1 = Image.new('RGB', (size, size), (255, 255, 255))
pfp1.paste(c_look_clean, ((size - w) // 2, (size - h) // 2))
# Resize 3x with NEAREST NEIGHBOR to preserve exact pixel staircasing
pfp1 = pfp1.resize((pfp1.width * 3, pfp1.height * 3), resample=Image.NEAREST)
pfp1.save('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/pfp_pixel_look_what_we_have.png')

# 2. 'Hamster smirk'
img1 = Image.open('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/.user_uploaded/media_1794307621470_23e2f760.jpg')
c_smirk = img1.crop((248, 192, 416, 424))
arr_s = np.array(c_smirk)
mask_s = (arr_s[:, :, 0] > 230) & (arr_s[:, :, 1] > 230) & (arr_s[:, :, 2] > 230)
arr_s[mask_s] = [255, 255, 255]
c_smirk_clean = Image.fromarray(arr_s)
w, h = c_smirk_clean.size
size = max(w, h) + 40
pfp2 = Image.new('RGB', (size, size), (255, 255, 255))
pfp2.paste(c_smirk_clean, ((size - w) // 2, (size - h) // 2))
pfp2 = pfp2.resize((pfp2.width * 3, pfp2.height * 3), resample=Image.NEAREST)
pfp2.save('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/pfp_pixel_hamster_smirk.png')

# 3. 'Evil / Devious Flirty Hamster'
img2 = Image.open('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/.user_uploaded/media_1794307621524_c78f3fc2.jpg')
c_evil = img2.crop((618, 250, 788, 480))
arr_e = np.array(c_evil)
mask_e = (arr_e[:, :, 0] > 230) & (arr_e[:, :, 1] > 230) & (arr_e[:, :, 2] > 230)
arr_e[mask_e] = [255, 255, 255]
c_evil_clean = Image.fromarray(arr_e)
w, h = c_evil_clean.size
size = max(w, h) + 40
pfp3 = Image.new('RGB', (size, size), (255, 255, 255))
pfp3.paste(c_evil_clean, ((size - w) // 2, (size - h) // 2))
pfp3 = pfp3.resize((pfp3.width * 3, pfp3.height * 3), resample=Image.NEAREST)
pfp3.save('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/pfp_pixel_evil_flirty.png')

print('All 3 pixelated PFPs created successfully!')
