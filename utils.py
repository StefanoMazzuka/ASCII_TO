import os
import itertools
import threading
import time
import sys


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def loading_animation(loading_event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if not loading_event.is_set():
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!  \n')


def exe_loading_animation():
    loading_event = threading.Event()
    loading_event.set()
    t = threading.Thread(target=loading_animation, args=(loading_event,))
    t.start()

    # Simulate a long-running process
    time.sleep(5)
    loading_event.clear()
    t.join()
