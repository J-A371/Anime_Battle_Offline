import subprocess
import sys
from pathlib import Path

# Détection mode script ou exe
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent

flash_player_path = BASE_DIR / "flashplayer_32_sa_debug.exe"
swf_path = BASE_DIR / "game.swf"
joytokey_path = BASE_DIR / "JoyToKey" / "JoyToKey.exe"

print("BASE_DIR:", BASE_DIR)
print("JoyToKey existe ?", joytokey_path.exists())

subprocess.Popen([str(joytokey_path)])
subprocess.Popen([str(flash_player_path), str(swf_path)])
