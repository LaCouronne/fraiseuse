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

def work(work):
    global progress
    global completed

    value_in = 1
    value_out = 1

    #Mvt translation x x2 , translation z x2 , rotation x

    #Est ce que la fraiseuse s eloigne  du point initial sur x
    boolean_translation_x_positive = True

    #coordonnées z max et z min
    z_max = work.barrel.diameter + value_out
    z_min = work.barrel.diameter - value_in


    #Suppose que la fraiseuse est à la place initiale

    z_actuel = 0
    x_actuel = 0

    #Init first pixel
    previous_pixel = 0

    #Pattern
    for lines in work.matrix:

        #forward or backward ?
        if boolean_translation_x_positive:
            for pixels in lines:
                previous_pixel = move_to_next(previous_pixel,pixels)
        else:
            for pixels in reversed(lines):
                previous_pixel = move_to_next(previous_pixel,pixels)







    #End : retour init


def move_to_next(previous_pixel,pixel):
    #4 cases
    #down to down
    move_x(1,)

    #down to up
    #up to down
    #up to up

    #Line forwards, line backwards, next line (4Th case)
    #First step, last step

    return (pixel)

