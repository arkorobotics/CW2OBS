#!/usr/bin/env python3
"""
Stream ggmorse-gui stdout → OBS Text source in real time
-------------------------------------------------------
• ggmorse-gui must already be built (see README) and sit in ./ggmorse/build/…
• OBS must have obs-websocket enabled (Tools ▸ WebSocket Server Settings).

Run:  python3 ggmorse_to_obs.py
"""
import os, subprocess, sys, string, time
from obswebsocket import obsws, requests

# ────────── CONFIG ──────────
GG_BIN   = os.path.join(os.path.dirname(__file__),
                        "ggmorse", "build", "bin", "ggmorse-gui")
AUDIO_DEV  = "2"                        # ggmorse -d index
OBS_HOST   = "localhost"
OBS_PORT   = 4455
OBS_PASS   = "supersecret"
OBS_TEXT_SRC = "CWbanner"
MAX_CHARS  = 25
# ────────────────────────────

PRINTABLE = set(string.ascii_uppercase + string.digits + "/?= " + string.ascii_lowercase)

def main():
    # Launch ggmorse-gui unbuffered
    proc = subprocess.Popen(
        [GG_BIN, f"-c{AUDIO_DEV}", "-r", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=0,              # unbuffered! read(1) delivers instantly
        text=True
    )


    ws = obsws(OBS_HOST, OBS_PORT, OBS_PASS); ws.connect()

    rolling = ""
    skip_banner = False        # inside a “[+] …” banner line?

    while True:
        ch = proc.stdout.read(1)          # read exactly one char
        if not ch:                        # process exited
            break

        # Detect and skip banner lines that start with '['
        if ch == '[' and not skip_banner:
            skip_banner = True
            continue
        if skip_banner:
            if ch == '\n':                # banner ended
                skip_banner = False
            continue

        if ch in PRINTABLE:
            rolling = (rolling + ch)[-MAX_CHARS:]
            ws.call(requests.SetInputSettings(
                inputName=OBS_TEXT_SRC,
                inputSettings={"text": rolling},
                overlay=False))
        # ignore '\r' '\n' and other non-printables

    ws.disconnect()
    proc.wait()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
