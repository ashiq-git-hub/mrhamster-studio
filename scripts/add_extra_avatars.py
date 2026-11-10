import os
import json
import base64

assets_dir = r"c:\Users\Thoufeek\Desktop\mr hasmter\assets\pfps"
data_dir = r"c:\Users\Thoufeek\Desktop\mr hasmter\assets\data"

extra_files = [
    "pfp_badboy_3d.jpg",
    "pfp_sunglasses_3d.jpg",
    "pfp_gentleman_3d.jpg",
    "pfp_disney_vintage.jpg"
]

with open(os.path.join(data_dir, "pfps_base64.json"), "r") as f:
    b64_data = json.load(f)

for fname in extra_files:
    p = os.path.join(assets_dir, fname)
    if os.path.exists(p):
        with open(p, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            b64_data[fname] = f"data:image/jpeg;base64,{encoded}"
        print(f"Added extra avatar {fname}: {len(b64_data[fname])} chars")

with open(os.path.join(data_dir, "pfps_base64.json"), "w", encoding="utf-8") as f:
    json.dump(b64_data, f, indent=2)

print("Updated pfps_base64.json with 8 avatars!")
