import time
import threading

progress = 0


def do_work(thread_function, update_callback, check_delay=1):
    def check_progress():
        global progress
        while True:
            time.sleep(check_delay)
            update_callback(progress)

    threading.Thread(target=check_progress).start()
    threading.Thread(target=thread_function).start()


def fake_work():
    global progress
    for i in range(100):
        time.sleep(0.1)
        progress += 1
