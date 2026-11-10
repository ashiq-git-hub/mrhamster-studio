import os, shutil

project_dir = r'C:\Users\Thoufeek\.gemini\antigravity\scratch\meme_page_project'
assets_dir = os.path.join(project_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

brain_dir = r'C:\Users\Thoufeek\.gemini\antigravity\brain\ab5d6534-892b-4bbc-b5f5-13c218bbb0bb'

files_to_copy = {
    'pfp_pixel_mog_hamster.png': 'pfp_mog_hamster.png',
    'pfp_pixel_look_what_we_have.png': 'pfp_look_what_we_have.png',
    'pfp_pixel_evil_flirty.png': 'pfp_evil_flirty.png',
    'pfp_pixel_hamster_smirk.png': 'pfp_hamster_smirk.png',
    'badboy_hamster_pfp_1794307109930.jpg': 'pfp_badboy_3d.jpg',
    'sunglasses_hamster_pfp_1794307101960.jpg': 'pfp_sunglasses_3d.jpg',
    'flirty_hamster_pfp_1794306949758.jpg': 'pfp_gentleman_3d.jpg',
    'chaplin_hamster_pfp_1794307454126.jpg': 'pfp_chaplin_vintage.jpg',
    'retro_disney_2d_hamster_1794307212715.jpg': 'pfp_sketch_vintage.jpg'
}

for src_name, dst_name in files_to_copy.items():
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(assets_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f'Copied: {src_name} -> {dst_name}')
    else:
        print(f'Not found: {src_name}')
