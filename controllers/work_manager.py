import time
import threading

import concurrent.futures

from objects.work import Work

progress = 0
abort = False
completed = False
current_work = None


def do_work(callback=None, update_callback=None, check_delay=0.1):

    assert isinstance(current_work, Work)

    global progress
    global abort
    global completed

    progress = 0
    abort = False
    completed = False

    def check_progress():
        while True:

            # Close thread if abort
            if abort:
                break

            # Waith before next check
            time.sleep(check_delay)

            # Call update function with current progress
            if update_callback:
                update_callback(progress)

            # Close loop on task completion, with callback if provided
            if completed:
                if callback:
                    callback()
                break

    threading.Thread(target=check_progress).start()
    threading.Thread(target=fake_work, args=(current_work,)).start()


def generate_matrix_thread(callback):

    assert isinstance(current_work, Work)

    def callback_thread():
        assert isinstance(current_work, Work)

        # Launch thread with future to allow return catch
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(current_work.generate_matrix)
            return_value = future.result()

            # Call callback function with generated matrix
            callback(return_value)

    threading.Thread(target=callback_thread).start()


def fake_work(work):
    global progress
    global completed

    iterations = len(work.matrix) * len(work.matrix[0])
    p = iterations // 100
    r = iterations % 100

    for i in range(100):
        time.sleep(0.1)
        progress += p

    progress += r
    completed = True

