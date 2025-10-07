import subprocess
import re
import datetime
import sys
import os

# 🔹 Terminal colorizer
def colorize(text, color):
    colors = {
        "GREEN": "\033[32m",
        "MAGENTA_BOLD": "\033[1;35m",
        "YELLOW": "\033[33m",
        "BLUE": "\033[34m",
        "CYAN_BOLD": "\033[1;36m",
        "YELLOW_BOLD": "\033[1;33m",
        "GREEN_BOLD": "\033[1;32m",
        "RED": "\033[31m",
        "RED_BOLD": "\033[1;31m",
        "RESET": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['RESET']}"

# 🔹 FFmpeg path dynamic for EXE
if getattr(sys, 'frozen', False):
    ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg.exe")
else:
    ffmpeg_path = r"C:\Users\Mic\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"

# 🔹 Display warning box before start
def print_warning_box():
    warning = """
⚠️ WARNING - READ CAREFULLY ⚠️

This program records your screen + audio using FFmpeg.

➤ It will:
  • Capture your desktop (video)
  • Mix your microphone and system sound
  • Save output as a high-quality MP4 file

💡 Tips:
  • Make sure your microphone and speakers are active.
  • Stop the process manually (Ctrl + C or (pres (q) for safe recording)) to end recording.
  • Saved files appear in the same directory as this script.

🚫 Do not use for unauthorized screen/audio recording.
Use responsibly and ethically.
"""
    lines = warning.strip().splitlines()
    width = max(len(line) for line in lines) + 6
    print(colorize("=" * width, "RED_BOLD"))
    for line in lines:
        print(colorize("| " + line.ljust(width - 4) + " |", "RED_BOLD"))
    print(colorize("=" * width, "RED_BOLD"))
    choice = input(colorize("Press ENTER to continue or type 'exit' to quit: ", "YELLOW_BOLD")).strip().lower()
    if choice == "exit":
        print(colorize("Program exited by user.", "GREEN_BOLD"))
        sys.exit(0)

print_warning_box()

# 🔹 Banner
def main_banner():
    print(colorize("\n···············································································", "GREEN"))
    print(colorize(":.###....###...######.............######....#######..#########...########..########............................:", "RED"))
    print(colorize(":.####..####..##....##...........##....##..##.....##..##.....##..##........##.....##.........................:", "RED"))
    print(colorize(":.##..##..##..##.................##........##.....##..##.....##..##........##.....##...........................:", "RED"))
    print(colorize(":.##..#...##...######............##........##.....##..##.....##..#####.....##.####.............................:", "RED"))
    print(colorize(":.##......##........##...........##........##.....##..##.....##..##........##....##...............................:", "RED"))
    print(colorize(":.##......##..##....##...........##....##..##.....##..##.....##..##........##.....##..............................:", "RED"))
    print(colorize(":.##......##...######.............######....#######..#########...########..##.....##..........................:", "RED"))
    print(colorize("·················································································", "GREEN"))

main_banner()

# 🔹 List audio devices
print(colorize("\n🔍 Scanning available audio devices...\n", "CYAN_BOLD"))
try:
    result = subprocess.run(
        [ffmpeg_path, "-list_devices", "true", "-f", "dshow", "-i", "dummy"],
        stderr=subprocess.PIPE,
        text=True
    )
except FileNotFoundError:
    print(colorize("❌ FFmpeg not found! Please check your ffmpeg.exe path.", "RED_BOLD"))
    sys.exit(1)

audio_devices = re.findall(r'"([^"]+)" \(audio\)', result.stderr)

if not audio_devices:
    print(colorize("❌ No audio devices found! Make sure your mic is connected.", "RED_BOLD"))
    sys.exit(1)

# 🔹 Show devices
print(colorize("🎧 Available audio devices:", "GREEN_BOLD"))
for i, dev in enumerate(audio_devices):
    print(colorize(f"   {i+1}. {dev}", "YELLOW"))

# 🔹 User selects mic
mic_choice = input(colorize(f"\nSelect microphone (1-{len(audio_devices)}) or press Enter to use first: ", "CYAN_BOLD"))
try:
    mic_index = int(mic_choice) - 1
    if 0 <= mic_index < len(audio_devices):
        mic_device = audio_devices[mic_index]
    else:
        mic_device = audio_devices[0]
except:
    mic_device = audio_devices[0]

print(colorize(f"\n🎙 Selected mic: {mic_device}", "MAGENTA_BOLD"))

# 🔹 Output filename
filename = datetime.datetime.now().strftime("record_%Y%m%d_%H%M%S.mp4")

# 🔹 FFmpeg recording command
command = [
    ffmpeg_path,
    "-f", "gdigrab", "-framerate", "60", "-i", "desktop",
    "-f", "dshow", "-i", "audio=virtual-audio-capturer",
    "-f", "dshow", "-i", f"audio={mic_device}",
    "-vcodec", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow", "-crf", "18",
    "-filter_complex",
    """
    [1:a]volume=6.0[a1];
    [2:a]highpass=f=100,lowpass=f=8000,afftdn=nf=-60,volume=6.0[a2];
    [a1][a2]amix=inputs=2:duration=longest[aout]
    """,
    "-map", "0:v", "-map", "[aout]",
    "-b:v", "15M", "-maxrate", "20M", "-bufsize", "25M",
    filename
]

# 🔹 Menu
print(colorize("\n===============================", "GREEN_BOLD"))
print(colorize("  1. Start Recording", "YELLOW_BOLD"))
print(colorize("  2. Exit", "YELLOW_BOLD"))
print(colorize("===============================\n", "GREEN_BOLD"))

choice = input(colorize("Enter your choice: ", "CYAN_BOLD")).strip()

if choice == "1":
    print(colorize("\n🎥 Starting screen recording...", "CYAN_BOLD"))
    print(colorize("Press Ctrl + C to stop recording or (q) for safe.\n", "YELLOW_BOLD"))
    subprocess.run(command)
    print(colorize(f"✅ Recording saved as {filename}", "GREEN_BOLD"))

elif choice == "2":
    print(colorize("\n👋 Thanks for using the Screen Recorder!", "YELLOW_BOLD"))
    sys.exit(0)
else:
    print(colorize("\n❌ Invalid choice! Please run again.", "RED_BOLD"))
