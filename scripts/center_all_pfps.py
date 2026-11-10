from PIL import Image, ImageOps
import numpy as np
import os
import base64

assets_dir = r"c:\Users\Thoufeek\Desktop\mr hasmter\assets\pfps"

pfp_configs = {
    "pfp_mog_hamster.png": {"padding": 0.12},
    "pfp_look_what_we_have.png": {"padding": 0.08},
    "pfp_evil_flirty.png": {"padding": 0.08},
    "pfp_hamster_smirk.png": {"padding": 0.08}
}

for fname, cfg in pfp_configs.items():
    p = os.path.join(assets_dir, fname)
    im = Image.open(p).convert("RGBA")
    arr = np.array(im)

    # find non-white pixels
    # white is arr[:, :, 0] > 240 & arr[:, :, 1] > 240 & arr[:, :, 2] > 240
    is_content = ~((arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240))
    y, x = np.where(is_content)
    
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()
    w = x_max - x_min
    h = y_max - y_min
    
    cx = (x_min + x_max) / 2
    cy = (y_min + y_max) / 2
    
    # Calculate target square size with padding
    target_dim = int(max(w, h) * (1 + cfg["padding"] * 2))
    
    # Create new square transparent canvas
    centered = Image.new("RGBA", (target_dim, target_dim), (255, 255, 255, 0))
    
    # Paste original so that (cx, cy) ends up at (target_dim/2, target_dim/2)
    paste_x = int(target_dim / 2 - cx)
    paste_y = int(target_dim / 2 - cy)
    
    # Make white background transparent
    # convert white pixels in im to transparent
    im_arr = np.array(im)
    white_mask = (im_arr[:, :, 0] > 240) & (im_arr[:, :, 1] > 240) & (im_arr[:, :, 2] > 240)
    im_arr[white_mask, 3] = 0
    im_trans = Image.fromarray(im_arr)
    
    centered.paste(im_trans, (paste_x, paste_y), im_trans)
    
    # Resize to standard crisp 512x512
    centered_512 = centered.resize((512, 512), Image.Resampling.LANCZOS)
    
    # Save transparent centered version
    out_trans_path = os.path.join(assets_dir, f"centered_trans_{fname}")
    centered_512.save(out_trans_path, "PNG")
    
    # Also save white-bg centered version
    white_bg = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
    white_bg.paste(centered_512, (0, 0), centered_512)
    out_white_path = os.path.join(assets_dir, f"centered_white_{fname}")
    white_bg.save(out_white_path, "PNG")
    
    # Overwrite the original in assets/pfps/ so it is inherently centered everywhere!
    white_bg.save(os.path.join(assets_dir, fname), "PNG")
    # and in assets/
    white_bg.save(os.path.join(r"c:\Users\Thoufeek\Desktop\mr hasmter\assets", fname), "PNG")

    print(f"Centered {fname}: original bbox=({x_min},{y_min},{x_max},{y_max}), target_dim={target_dim}")

print("All 4 PFPs re-centered successfully!")
