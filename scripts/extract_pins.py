from PIL import Image
import numpy as np

# Load screenshots
img1 = Image.open('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/.user_uploaded/media_1794307621470_23e2f760.jpg')
img2 = Image.open('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/.user_uploaded/media_1794307621524_c78f3fc2.jpg')
img3 = Image.open('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/.user_uploaded/media_1794307621546_fc5b2035.jpg')

# Let's inspect the cards:
# In img1:
# 1. 'Hamster smirk' (col 2, row 1):
# let's find the card around x=248..416, y=190..425
c_smirk = img1.crop((248, 192, 416, 424))
# Create clean 1:1 PFP
def make_square_pfp(crop, out_name):
    # crop has white/light background
    # find bounding box of non-background content or center it on white square
    w, h = crop.size
    dim = max(w, h) + 20
    sq = Image.new('RGB', (dim, dim), (255, 255, 255))
    sq.paste(crop, ((dim - w) // 2, (dim - h) // 2))
    # resize to 1024x1024 with NEAREST NEIGHBOR to preserve exact pixelated aesthetic!
    sq_large = sq.resize((1024, 1024), resample=Image.NEAREST)
    out_path = f'C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/{out_name}.png'
    sq_large.save(out_path)
    print(f'Saved {out_name}:', sq_large.size)

make_square_pfp(c_smirk, 'pfp_hamster_smirk')

# In img3:
# 'Look what we have here....' on top right
# let's inspect the card at x=804..976, y=190..400
c_look = img3.crop((804, 190, 976, 408))
make_square_pfp(c_look, 'pfp_look_what_we_have')

# In img2:
# 'Evil hamster' (col 4, row 1):
c_evil = img2.crop((618, 250, 788, 480))
make_square_pfp(c_evil, 'pfp_evil_hamster')

# In img1:
# The fedora hamster ('tips fedora' / neckbeard meme hamster):
c_fedora = img1.crop((618, 545, 788, 640)) # let's check
make_square_pfp(c_fedora, 'pfp_fedora_hamster')
