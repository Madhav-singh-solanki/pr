import msvcrt
import time
import os
from datetime import datetime

def get_key():
    """Gets a single key press (Windows only)"""
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            try:
                return key.decode('utf-8')
            except UnicodeDecodeError:
                return str(key)

def log_key(key, log_file):
    """Logs the key with timestamp"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {key}\n")

def ethical_warning():
    """Displays ethical warning message"""
    print("\n" + "="*60)
    print(" IMPORTANT ETHICAL CONSIDERATIONS ".center(60, '#'))
    print("="*60)
    print("\nThis is a DEMONSTRATION KEYLOGGER.")
    print("- Only use for AUTHORIZED, LEGAL purposes")
    print("- Get EXPLICIT CONSENT before monitoring")
    print("- Misuse violates privacy laws")
    print("\nThis program will:")
    print("- Log keystrokes to 'keystrokes.log'")
    print("- Run for 1 minute max")
    print("- Automatically exit")
    print("\n" + "="*60)
    print("\nPress any key to continue (ESC to exit immediately)...")
    
    if get_key() == '\x1b':  # ESC key
        print("\nExiting...")
        exit()

def main():
    ethical_warning()
    
    lf = "keystrokes.log"
    st = time.time()
    max_duration = 60  # 1 minute max runtime
    
    print("\nLogging started (automatically stops after 1 minute)...")
    print("Press ESC to exit early\n")
    
    try:
        while time.time() - st < max_duration:
            key = get_key()
            if key == '\x1b':  # ESC key
                print("\nEarly exit requested...")
                break
            log_key(key, lf)
    finally:
        print("\nLogging stopped. Data saved to:", lf)

if __name__ == "__main__":
    main()
