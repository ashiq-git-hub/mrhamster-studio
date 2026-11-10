# -*- coding: utf-8 -*-
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
