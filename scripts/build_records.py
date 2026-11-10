# -*- coding: utf-8 -*-
import os
import json
import shutil

BASE_DIR = r"c:\Users\Thoufeek\Desktop\mr hasmter"
os.makedirs(os.path.join(BASE_DIR, "records"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "recordings"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "scripts"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "assets", "pfps"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "assets", "sample_posts"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "assets", "references"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "assets", "data"), exist_ok=True)

# 1. Build records/brand_records.json
brand_records = {
    "brand_name": "Mr. Hamster",
    "primary_handle": "@mrr.hamster",
    "platform": "Instagram",
    "secondary_handles": ["@mr.alibi", "@mrspill", "@themrspill", "@mr.habit", "@mrfaust"],
    "character_persona": {
        "title": "The Charismatic Degenerate & Anonymous Cynic",
        "archetype": "Anti-hero / Flirty cynic / 2 AM overthinker",
        "voice_attributes": [
            "Flirty without being desperate",
            "Dark humor delivered with complete calm",
            "Relatable self-sabotage & procrastination",
            "Blunt, unapologetic observations about modern dating and society",
            "Zero filter, mysterious and unhinged"
        ]
    },
    "visual_identity": {
        "primary_avatar": "pfp_mog_hamster.png",
        "avatar_style": "1-bit crunchy pixel lineart on white background with pink nose",
        "recommended_pfp_backdrop": "#ffd6e0",
        "backdrop_options": [
            {"name": "Soft Aesthetic Pink", "color": "#ffd6e0", "description": "Matches hamster pink nose; pops brilliantly on black feeds"},
            {"name": "Charcoal Rim", "color": "#1a1c23", "description": "Stealthy, sleek dark aesthetic"},
            {"name": "Hot Pink Neon", "color": "#ff477e", "description": "High contrast brand highlight"},
            {"name": "Pure White Ring", "color": "#ffffff", "description": "Clean minimalist outline"},
            {"name": "Mint Emerald", "color": "#10b981", "description": "Vibrant retro pop"},
            {"name": "Cyber Cyan", "color": "#38bdf8", "description": "Futuristic digital edge"}
        ],
        "canvas_format": {
            "aspect_ratio": "4:5 (Portrait) and 1:1 (Square)",
            "feed_resolution": "1080 x 1350 px (Maximum screen real estate)",
            "square_resolution": "1080 x 1080 px",
            "canvas_background": "#000000 (Pure OLED Pitch Black)",
            "typography": "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
            "text_color": "#f7f9f9 (Twitter/Threads Crisp Off-White)",
            "handle_color": "#71767b (Subtle Muted Charcoal)"
        }
    },
    "ready_to_use_bios": [
        {
            "title": "Option 1: The Mixed Signals Charmer (Recommended)",
            "bio": "Mr. Hamster ✨\nI don't give mixed signals, you just have selective hearing.\n🍸 Bad decisions posted daily\n📩 DMs open for regrettable choices\nthreads/tweets only"
        },
        {
            "title": "Option 2: The 2:43 AM Cynic",
            "bio": "Mr. Hamster 💀\nProfessionally unhinged.\nThoughts you have at 2:43 AM but shouldn't say out loud.\n⚠️ Not responsible for emotional damage.\n@mrr.hamster"
        },
        {
            "title": "Option 3: Minimalist Mog",
            "bio": "Mr. Hamster 🐹\nlooking respectfully\n• text only • dark humor • zero context\nswipe at your own risk"
        }
    ]
}

with open(os.path.join(BASE_DIR, "records", "brand_records.json"), "w", encoding="utf-8") as f:
    json.dump(brand_records, f, indent=2, ensure_ascii=False)
print("Wrote brand_records.json")

# 2. Build records/quote_records.json
quotes = [
    # Flirty & Situationship Banter
    {"id": "flirt-01", "category": "Flirty & Situationship", "tags": ["dating", "crush", "flirting"], "text": "flirting is easy until you have to flirt\nwith someone you actually want."},
    {"id": "flirt-02", "category": "Flirty & Situationship", "tags": ["mixed-signals", "sarcasm"], "text": "i don't give mixed signals.\nyou just have selective hearing and wishful thinking."},
    {"id": "flirt-03", "category": "Flirty & Situationship", "tags": ["texting", "habits"], "text": "if i like you, i will reply in 2 seconds or 2 business days.\nthere is no in-between."},
    {"id": "flirt-04", "category": "Flirty & Situationship", "tags": ["romance", "sleep"], "text": "you're my favorite reason\nto lose sleep and ignore everyone else."},
    {"id": "flirt-05", "category": "Flirty & Situationship", "tags": ["warning", "banter"], "text": "texting me is high risk, high reward.\nmostly high risk."},
    {"id": "flirt-06", "category": "Flirty & Situationship", "tags": ["naps", "funny"], "text": "i'm not hard to get.\nyou just have to catch me between naps and existential dread."},
    {"id": "flirt-07", "category": "Flirty & Situationship", "tags": ["red-flags", "dating"], "text": "my red flags are visible from outer space\nyet here you are setting up camp."},
    {"id": "flirt-08", "category": "Flirty & Situationship", "tags": ["panic", "texting"], "text": "accidentally opened your message immediately.\nnow i have to fake my own death."},
    {"id": "flirt-09", "category": "Flirty & Situationship", "tags": ["hamster", "cute", "flirty"], "text": "i look at you the way\na hamster looks at the last sunflower seed."},
    {"id": "flirt-10", "category": "Flirty & Situationship", "tags": ["exes", "pride"], "text": "i said i was over you\nnot that i have self-respect."},
    {"id": "flirt-11", "category": "Flirty & Situationship", "tags": ["toxic", "games"], "text": "we could be toxic together\nbut you're playing games with amateur rules."},
    {"id": "flirt-12", "category": "Flirty & Situationship", "tags": ["reels", "love-language"], "text": "my love language is sending 47 reels\nand expecting you to watch every single one."},
    {"id": "flirt-13", "category": "Flirty & Situationship", "tags": ["audacity", "feelings"], "text": "i didn't catch feelings.\ni slipped on your audacity and fell."},
    {"id": "flirt-14", "category": "Flirty & Situationship", "tags": ["arguments", "brain"], "text": "sorry for being late,\ni was having an imaginary argument in my head."},
    {"id": "flirt-15", "category": "Flirty & Situationship", "tags": ["respect", "smirk"], "text": "looking respectfully.\n(not respectfully at all)"},

    # 2 AM Unhinged Thoughts
    {"id": "2am-01", "category": "2 AM Unhinged", "tags": ["midnight", "chaos"], "text": "it's 2:43 AM.\ntime to either change my entire identity\nor eat cold leftovers in complete darkness."},
    {"id": "2am-02", "category": "2 AM Unhinged", "tags": ["overthinking", "brain"], "text": "my brain at 2 PM: *dial-up connection noise*\nmy brain at 2 AM: here is a 45-slide presentation on why you are doomed."},
    {"id": "2am-03", "category": "2 AM Unhinged", "tags": ["adulting", "scam"], "text": "do you ever just sit there and think\n'who gave me permission to be an adult?'"},
    {"id": "2am-04", "category": "2 AM Unhinged", "tags": ["cringe", "memories"], "text": "staring at the ceiling recalculating\nevery conversation i've had since 2018."},
    {"id": "2am-05", "category": "2 AM Unhinged", "tags": ["forest", "escape"], "text": "i am one mild inconvenience away\nfrom moving into the forest and befriending crows."},
    {"id": "2am-06", "category": "2 AM Unhinged", "tags": ["bed", "memory"], "text": "my bed is a magical place where i suddenly\nremember everything i forgot to do today."},
    {"id": "2am-07", "category": "2 AM Unhinged", "tags": ["silence", "intrusive"], "text": "the silence in my room is loud\nbut my intrusive thoughts are louder."},
    {"id": "2am-08", "category": "2 AM Unhinged", "tags": ["sleep", "peace"], "text": "sleep is so nice because you're not dead\nand you're not awake. it's the perfect middle ground."},
    {"id": "2am-09", "category": "2 AM Unhinged", "tags": ["tabs", "anxiety"], "text": "i have 43 tabs open in my browser\nand 792 open in my brain."},
    {"id": "2am-10", "category": "2 AM Unhinged", "tags": ["schedule", "insomnia"], "text": "my sleep schedule isn't even a schedule anymore.\nit's just a roulette wheel."},
    {"id": "2am-11", "category": "2 AM Unhinged", "tags": ["calories", "worry"], "text": "if overthinking burned calories\ni would have vanished into thin air by now."},
    {"id": "2am-12", "category": "2 AM Unhinged", "tags": ["squirrels", "unhinged"], "text": "i don't have ducks in a row.\ni have squirrels at a rave."},
    {"id": "2am-13", "category": "2 AM Unhinged", "tags": ["damage", "sleep"], "text": "why fall in love when you can fall asleep\nand avoid all emotional collateral damage."},
    {"id": "2am-14", "category": "2 AM Unhinged", "tags": ["pigeon", "tired"], "text": "i'm not a night owl or an early bird.\ni'm some sort of exhausted pigeon."},

    # Dark Humor & Blunt Realism
    {"id": "dark-01", "category": "Dark Humor", "tags": ["choices", "truth"], "text": "everything happens for a reason.\nsometimes that reason is you're stupid and make bad choices."},
    {"id": "dark-02", "category": "Dark Humor", "tags": ["optimism", "experience"], "text": "i'm not pessimistic.\ni'm just an optimist with life experience."},
    {"id": "dark-03", "category": "Dark Humor", "tags": ["therapist", "hugs"], "text": "my therapist told me to embrace my mistakes.\nso i hugged myself."},
    {"id": "dark-04", "category": "Dark Humor", "tags": ["difficulty", "game"], "text": "i entered adulthood with zero tutorial\nand the difficulty set on extreme nightmare."},
    {"id": "dark-05", "category": "Dark Humor", "tags": ["stairs", "chaos"], "text": "life is like a wheel.\nexcept someone greased it and threw it down a flight of stairs."},
    {"id": "dark-06", "category": "Dark Humor", "tags": ["arguments", "ego"], "text": "i'm not arguing.\ni'm just explaining why i'm right and you should listen."},
    {"id": "dark-07", "category": "Dark Humor", "tags": ["taco", "happiness"], "text": "you can't make everyone happy.\nyou're not a taco or a sleeping pill."},
    {"id": "dark-08", "category": "Dark Humor", "tags": ["grudges", "facts"], "text": "i don't hold grudges.\ni just remember facts with extreme emotional intensity."},
    {"id": "dark-09", "category": "Dark Humor", "tags": ["coffee", "money"], "text": "money can't buy happiness\nbut it can buy a black coffee and peace of mind."},
    {"id": "dark-10", "category": "Dark Humor", "tags": ["historians", "downfall"], "text": "i am currently experiencing what historians\nwill refer to as 'the downfall'."},
    {"id": "dark-11", "category": "Dark Humor", "tags": ["parties", "canceled"], "text": "i've reached the point in life where my favorite party\nis the one that gets canceled."},
    {"id": "dark-12", "category": "Dark Humor", "tags": ["growing-up", "scam"], "text": "remember when you were a kid and wanted to be older?\nwhat an absolute scam."},

    # Relatable Everyday Chaos
    {"id": "rel-01", "category": "Relatable Chaos", "tags": ["social", "introvert"], "text": "i'm not antisocial.\ni'm selectively social. there's a difference."},
    {"id": "rel-02", "category": "Relatable Chaos", "tags": ["hunger", "mood"], "text": "my mood depends heavily on\nwhether someone spoke to me before my first meal."},
    {"id": "rel-03", "category": "Relatable Chaos", "tags": ["battery", "eye-contact"], "text": "social battery at 2%.\nplease do not make eye contact or ask how i am."},
    {"id": "rel-04", "category": "Relatable Chaos", "tags": ["telepathy", "replies"], "text": "i replied in my head.\nin my heart, we have concluded the conversation."},
    {"id": "rel-05", "category": "Relatable Chaos", "tags": ["plans", "dopamine"], "text": "canceling plans gives me a dopamine hit\nthat modern science cannot explain."},
    {"id": "rel-06", "category": "Relatable Chaos", "tags": ["horizontal", "overwhelmed"], "text": "i have two speeds:\n1. completely overwhelmed\n2. horizontal in bed doing nothing."},
    {"id": "rel-07", "category": "Relatable Chaos", "tags": ["no-worries", "drowning"], "text": "saying 'no worries' while actively drowning in worry."},
    {"id": "rel-08", "category": "Relatable Chaos", "tags": ["outside", "graphics"], "text": "i went outside once.\nthe graphics were okay but the plot and NPCs were terrible."},
    {"id": "rel-09", "category": "Relatable Chaos", "tags": ["shopping", "cart"], "text": "my favorite hobby is putting things in online shopping carts\nand then closing the tab."},
    {"id": "rel-10", "category": "Relatable Chaos", "tags": ["cleaning", "chair"], "text": "cleaning my room by moving clothes\nfrom the chair to the bed and back to the chair."},

    # Red Flags & Modern Dating
    {"id": "rf-01", "category": "Red Flags & Dating", "tags": ["fix-him", "trauma"], "text": "he said he was emotionally unavailable.\ni said 'say less, let me fix you'."},
    {"id": "rf-02", "category": "Red Flags & Dating", "tags": ["modern-dating", "2026"], "text": "dating in 2026 is just two emotionally damaged people\nasking each other 'so what's your trauma?'."},
    {"id": "rf-03", "category": "Red Flags & Dating", "tags": ["rent", "alone"], "text": "i don't need a relationship.\ni need someone to pay half my rent and leave me alone."},
    {"id": "rf-04", "category": "Red Flags & Dating", "tags": ["stories", "stalking"], "text": "saw your story within 0.4 seconds.\ni'm not obsessed, i just have no life."},
    {"id": "rf-05", "category": "Red Flags & Dating", "tags": ["dates", "9pm"], "text": "my ideal date: you talk, i nod,\nwe eat good food, and we leave before 9 PM."},
    {"id": "rf-06", "category": "Red Flags & Dating", "tags": ["disappointment", "population"], "text": "never let someone waste your time twice.\nthere are 8 billion people, let someone new disappoint you."},
    {"id": "rf-07", "category": "Red Flags & Dating", "tags": ["blindfold", "red-flag"], "text": "i see your red flag and i raise you\nmy pathological desire to ignore it."}
]

with open(os.path.join(BASE_DIR, "records", "quote_records.json"), "w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=2, ensure_ascii=False)
print(f"Wrote quote_records.json with {len(quotes)} items.")

# 3. Build records/content_calendar.md
calendar_content = """# 📅 Mr. Hamster — 30-Day Content Strategy & Posting Records

Brand: **@mrr.hamster**  
Theme: **Anonymous Meme Personality / Tweet & Threads Dark-Mode Formats**

---

## ⏰ Optimal Posting Windows (IST & UTC)
* **Morning Peak**: 11:30 AM – 1:00 PM (Lunch scrolling & quick dopamine)
* **Late Night Peak (Prime for Mr. Hamster)**: 8:45 PM – 11:30 PM (Peak unhinged & relatable engagement)

---

## 🗓️ Weekly Content Rhythm

| Day | Vibe / Topic | Quote Style | Recommended Post Format |
|---|---|---|---|
| **Monday** | Existential & Work Sarcasm | "graphics were okay, NPCs terrible" | Single 4:5 Tweet Card |
| **Tuesday** | Flirty Banter & Red Flags | "red flags visible from outer space" | 4:5 Tweet Card + Reaction Photo |
| **Wednesday** | 2 AM Brain & Overthinking | "brain at 2 PM vs 2 AM" | Single 4:5 Tweet Card |
| **Thursday** | Cynical Life Lessons & Dark Truths | "everything happens for a reason" | 4:5 Card with Hamster Smirk |
| **Friday** | Weekend Situationship Chaos | "flirting is easy until..." | 4:5 Tweet Card + Caption Hook |
| **Saturday** | Pure Unhinged Out-of-Pocket | "squirrels at a rave" | Tweet Card + Audio Voice Reel |
| **Sunday** | Low Battery & Procrastination | "horizontal in bed doing nothing" | Single 1:1 or 4:5 Post |

---

## ✍️ High-Converting Caption Formulas

### Formula 1: The Blunt Agreement
> "agree or lie to yourself in the comments."  
> 🐹 `@mrr.hamster`

### Formula 2: The Question Hook
> "at what point in your life did you realize this was 100% accurate?"  
> 🍸 Drop your red flags below.

### Formula 3: The 2 AM Callout
> "who's reading this at 2 AM instead of fixing their sleep schedule?"  
> ✨ save this for your next late-night spiral.

---

## 🏷️ Curated Hashtag Bank
`#mrrhamster #tweetmemes #textmemes #darkhumor #2amthoughts #relatablememes #unhinged #situationship #redflags #memepage #tweetsdaily`
"""

with open(os.path.join(BASE_DIR, "records", "content_calendar.md"), "w", encoding="utf-8") as f:
    f.write(calendar_content)
print("Wrote content_calendar.md")

# 4. Build recordings/README.md
recordings_readme = """# 🎙️ Mr. Hamster — Audio Recordings & Voice Studio Notes

This directory stores voice memos, voiceovers, and audio recordings generated with the **Voice Studio & Audio Recorder** in `index.html` or via `scripts/voice_recorder_cli.py`.

---

## 💡 How to Use Audio with Mr. Hamster Posts:
1. **Instagram Reels & Stories Background Audio**:
   - Record your funny observation or tweet reading in the built-in Voice Recorder.
   - Apply the **Hamster Speed / Chipmunk** pitch effect (+5 semitones) or **Deep Narrator** voice.
   - Download the `.wav` file directly from the browser.
   - Combine the audio with your rendered 1080x1350 meme image in Instagram Reels or CapCut.

2. **File Naming Convention**:
   - `mrr_hamster_voice_[YYYYMMDD]_[topic].wav`
   - e.g., `mrr_hamster_voice_20261110_mixed_signals.wav`
"""

with open(os.path.join(BASE_DIR, "recordings", "README.md"), "w", encoding="utf-8") as f:
    f.write(recordings_readme)
print("Wrote recordings/README.md")

# 5. Build scripts/voice_recorder_cli.py
cli_script = '''# -*- coding: utf-8 -*-
"""
Mr. Hamster — Standalone Audio Recorder CLI
Records voice notes directly from your microphone into the recordings/ folder.
"""
import os
import sys
import time
from datetime import datetime

RECORDINGS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "recordings")
os.makedirs(RECORDINGS_DIR, exist_ok=True)

def record_audio(duration=10, filename=None):
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"mrr_hamster_recording_{timestamp}.wav"
    output_path = os.path.join(RECORDINGS_DIR, filename)

    try:
        import sounddevice as sd
        import numpy as np
        import scipy.io.wavfile as wav
    except ImportError:
        print("[!] Note: python packages 'sounddevice', 'numpy', 'scipy' are needed for CLI recording.")
        print("[*] TIP: You can use the built-in Voice Studio in 'index.html' directly in your browser with zero install!")
        return

    sample_rate = 44100
    print(f"[*] Recording for {duration} seconds... Speak now!")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    wav.write(output_path, sample_rate, audio_data)
    print(f"[+] Saved recording to: {output_path}")

if __name__ == "__main__":
    dur = 10
    if len(sys.argv) > 1:
        try: dur = int(sys.argv[1])
        except ValueError: pass
    record_audio(dur)
'''

with open(os.path.join(BASE_DIR, "scripts", "voice_recorder_cli.py"), "w", encoding="utf-8") as f:
    f.write(cli_script)
print("Wrote voice_recorder_cli.py")

# 6. Build Open Studio.bat
bat_content = """@echo off
title Mr. Hamster Meme Studio & Voice Recorder
echo Opening Mr. Hamster Studio in your default browser...
start "" "%~dp0index.html"
exit
"""

with open(os.path.join(BASE_DIR, "Open Studio.bat"), "w", encoding="utf-8") as f:
    f.write(bat_content)
print("Wrote Open Studio.bat")

print("All record files and scripts created successfully!")
