## PyFF Recorder 🎥
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)](https://github.com/yourusername/pytray-reminder)

A lightweight, Windows-focused screen recorder built in Python using FFmpeg. Capture your desktop, system audio (via Virtual Audio Cable), and microphone with built-in audio enhancements like volume boosting, noise reduction, and mixing. Outputs high-quality, timestamped MP4 files—perfect for tutorials, demos, gameplay, or quick shares!
Failed to load imageView link (Replace with a screenshot of the colorful banner)
### 🆕 Version 1.2 (October 2025)
- Added Pause & Resume recording feature 🎬
- Improved console output colors
- Minor bug fixes and optimizations

## ✨ Features

- Desktop Capture: Records full screen at 60 FPS using GDI Grab.
- Audio Support: Captures system audio (requires Virtual Audio Cable) and selectable microphone input.
- Audio Processing:

- Boosts volume (6x for both sources).
Applies filters: High-pass (100Hz), low-pass (8kHz), noise reduction (AFFTDN).
Mixes system and mic audio seamlessly.


- Device Selection: Lists and lets you choose from available audio devices.
- High-Quality Output: Uses libx264 with CRF 18, 15M bitrate for crisp video.
- CLI-Friendly: Colorful terminal interface with ASCII banner and simple menu.
- EXE-Ready: Handles FFmpeg path for PyInstaller bundles (no extra setup needed).
- Timestamped Files: Auto-saves as record_YYYYMMDD_HHMMSS.mp4.

## 📋 Requirements

- Python 3.8+ (uses standard libraries: subprocess, re, datetime, sys, os).
- FFmpeg: Installed via WinGet or similar (script auto-detects path).
- Virtual Audio Cable: For system audio capture (free from VB-Audio).
- No additional Python packages required—pure stdlib!
## Install dependencies quickly:

```bash
#FFmpeg (PowerShell)
winget install ffmpeg
```


1. ### Clone the repo:

```bash
git clone https://github.com/yourusername/pyff-recorder.git
cd pyff-recorder
```
2. ### Ensure FFmpeg is installed:

- Run in PowerShell: winget install ffmpeg
- Or download from ffmpeg.org.


3. ### Install Virtual Audio Cable for system sound:
- Download free from VB-Audio.


4. ### Run the script:
```bash
 python recorder.py  # Or whatever you name the main file
```

# 📖 Usage

1. ### Launch the App:
- Run python recorder.py.
- It displays an ASCII banner and lists available audio devices.


2. ### Select Microphone:

- Enter a number (1-N) or press Enter for the first device.
- Example output:
```text
Available audio devices:
1. Microphone (Realtek Audio)
2. Headset Mic (USB Device)
🎙 Selected mic: Microphone (Realtek Audio)
```

3. ### Start Recording:

- Choose 1. Start Recording from the menu.
- The script runs FFmpeg in the background—your screen starts capturing immediately!
- Stop by closing the terminal or Ctrl+C (FFmpeg will finalize the file) or press q for safe .


4. ### Output:

- File saved in the current directory, e.g., record_20251007_143022.mp4.
- Success message: ✅ Saved as record_20251007_143022.mp4.



#### Pro Tip: For longer recordings, ensure your disk has space—high bitrate means ~1GB per 5-10 minutes.

# 🛠 Customization
### Edit recorder.py for tweaks:

- FFmpeg Path: Update ffmpeg_path for your setup (e.g., custom install dir).
- Video Settings: Change -framerate, -crf, -preset, or -b:v in the command list.
- Audio Filters: Modify the filter_complex string (e.g., adjust volume=6.0 or add more effects).
- Output Format: Swap .mp4 for .mkv or add -t 300 for time-limited recordings.
- Banner/Colors: Tweak main_banner() or colorize() for your style.

### To bundle as EXE (portable app):
```bash
pip install pyinstaller
pyinstaller --onefile --add-data "ffmpeg.exe;." recorder.py
```
#### (Include FFmpeg.exe in the bundle for no-install runs.)
# 🤝 Contributing
### Love the project? Contribute!

1. Fork the repo.
2. Create a feature branch (git checkout -b feature/cool-enhancement).
3. Commit changes (git commit -m 'Add: Pause/Resume button').
4. Push to branch (git push origin feature/cool-enhancement).
5. Open a Pull Request!

#### Ideas: Cross-platform support (macOS/Linux via x11grab/screencapture), GUI with Tkinter, or hotkey recording.
# 📄 License
#### This project is licensed under the MIT License - see the LICENSE file for details.
# ❤️ Acknowledgments

- Built with ❤️ by MS Coder.
- Powered by FFmpeg and inspired by simple capture tools.
- Shoutout to VB-Audio for Virtual Cable—essential for system sound!

### Star ⭐ if this saves your screen-recording workflow! Questions? Open an issue.

