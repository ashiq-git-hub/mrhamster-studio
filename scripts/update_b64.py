import os
import json
import base64

assets_dir = r"c:\Users\Thoufeek\Desktop\mr hasmter\assets\pfps"
data_dir = r"c:\Users\Thoufeek\Desktop\mr hasmter\assets\data"

pfp_files = [
    "pfp_mog_hamster.png",
    "pfp_look_what_we_have.png",
    "pfp_evil_flirty.png",
    "pfp_hamster_smirk.png"
]

b64_data = {}
for fname in pfp_files:
    p = os.path.join(assets_dir, fname)
    with open(p, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
        # Store with standard data URI prefix
        b64_data[fname] = f"data:image/png;base64,{encoded}"
    print(f"Encoded {fname}: len={len(b64_data[fname])}")

with open(os.path.join(data_dir, "pfps_base64.json"), "w", encoding="utf-8") as f:
    json.dump(b64_data, f, indent=2)

# Also update mog_base64.txt
with open(os.path.join(data_dir, "mog_base64.txt"), "w", encoding="utf-8") as f:
    f.write(b64_data["pfp_mog_hamster.png"])

# Also in assets/
with open(os.path.join(r"c:\Users\Thoufeek\Desktop\mr hasmter\assets", "pfps_base64.json"), "w", encoding="utf-8") as f:
    json.dump(b64_data, f, indent=2)
with open(os.path.join(r"c:\Users\Thoufeek\Desktop\mr hasmter\assets", "mog_base64.txt"), "w", encoding="utf-8") as f:
    f.write(b64_data["pfp_mog_hamster.png"])

print("pfps_base64.json and mog_base64.txt updated successfully!")
