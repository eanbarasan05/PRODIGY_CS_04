#!/usr/bin/env python3
"""
Terminal Key Logger (Educational Version)

Features:
- Logs keystrokes ONLY inside this terminal session
- Saves logs to file
- Timestamps every key
- Session statistics
- Live dashboard
- Special key recognition

Author: Educational Cybersecurity Project
"""

import os
import sys
import time
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(
    LOG_DIR,
    f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
)

total_keys = 0
special_keys = 0
start_time = datetime.now()


# -----------------------------
# Platform-specific key reader
# -----------------------------
if os.name == "nt":
    import msvcrt

    def get_key():
        key = msvcrt.getch()

        if key in [b'\x00', b'\xe0']:
            special = msvcrt.getch()

            mapping = {
                b'H': '[UP]',
                b'P': '[DOWN]',
                b'K': '[LEFT]',
                b'M': '[RIGHT]'
            }

            return mapping.get(special, '[SPECIAL]')

        try:
            return key.decode('utf-8')
        except:
            return '[UNKNOWN]'

else:
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)

            if ch == '\x1b':
                seq = ch + sys.stdin.read(2)

                arrows = {
                    '\x1b[A': '[UP]',
                    '\x1b[B': '[DOWN]',
                    '\x1b[C': '[RIGHT]',
                    '\x1b[D': '[LEFT]'
                }

                return arrows.get(seq, '[ESC]')

            return ch

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


# -----------------------------
# Logging Function
# -----------------------------
def write_log(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {key}\n")


# -----------------------------
# Banner
# -----------------------------
def banner():
    print("=" * 60)
    print(" TERMINAL KEY LOGGER (EDUCATIONAL)")
    print("=" * 60)
    print(f"Log File : {log_file}")
    print("Press ESC to stop logging.")
    print("=" * 60)


# -----------------------------
# Dashboard
# -----------------------------
def dashboard():
    runtime = datetime.now() - start_time

    print("\n")
    print("=" * 60)
    print("SESSION SUMMARY")
    print("=" * 60)
    print(f"Runtime      : {runtime}")
    print(f"Total Keys   : {total_keys}")
    print(f"Special Keys : {special_keys}")
    print(f"Log File     : {log_file}")
    print("=" * 60)


# -----------------------------
# Main
# -----------------------------
def main():
    global total_keys
    global special_keys

    banner()

    while True:
        key = get_key()

        if key == '\r':
            key_name = '[ENTER]'

        elif key == '\n':
            key_name = '[ENTER]'

        elif key == '\t':
            key_name = '[TAB]'

        elif key == '\x7f':
            key_name = '[BACKSPACE]'

        elif key == '[ESC]':
            write_log('[ESC]')
            print("\n\nStopping logger...")
            break

        else:
            key_name = key

        total_keys += 1

        if key_name.startswith('['):
            special_keys += 1

        write_log(key_name)

        print(f"\rLast Key: {key_name:<20} Total: {total_keys}", end='')

    dashboard()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        dashboard()
