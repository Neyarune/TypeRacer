from essential_generators import DocumentGenerator
from pynput.keyboard import Key, Listener
import time

goal = DocumentGenerator().sentence()
start = None
end = None
position = 0

def on_press(key):
    global goal, position, start, end

    try:
        key = key.char
    except AttributeError:
        key = key.value.char
    finally:
        if goal[position] == key:
            print(key, end='')
            position += 1
    
    if position == 1 and start is None:
        start = time.time()
    
    if position >= len(goal):
            end = time.time()
            epsil = end - start
            print(f"\n{epsil:.2f}")
            return False

with Listener(on_press=on_press) as listener:
    print(goal)
    listener.join()
