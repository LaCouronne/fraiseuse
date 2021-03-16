import time
import threading


import concurrent.futures

from controllers.hardware_controler import HardwareController
from objects.work import Work

progress = 0
completed = False
current_work = None
emergency_stop = False

# Work status
FORWARD = 1
BACKWARD = -1


def do_work(callback=None, update_callback=None, check_delay=0.1):

    assert isinstance(current_work, Work)

    global progress
    global completed
    global emergency_stop

    progress = 0
    completed = False

    def check_progress():
        while True:

            # Close thread if abort
            if emergency_stop:
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
    # threading.Thread(target=fake_work, args=(current_work,)).start()
    threading.Thread(target=execute_work, args=(current_work,)).start()


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
    global emergency_stop

    iterations = len(work.matrix) * len(work.matrix[0])
    p = iterations // 100
    r = iterations % 100

    for i in range(100):
        if emergency_stop:
            emergency_stop = False
            return
        time.sleep(0.1)
        progress += p

    progress += r
    completed = True


def execute_work(work):
    global progress
    global completed
    global emergency_stop

    iterations = len(work.matrix) * len(work.matrix[0])
    p = iterations // 100
    r = iterations % 100

    hw_controller = HardwareController(work)

    direction = FORWARD

    # Init first pixel
    previous_pixel = 0
    hw_controller.drill_on()

    # Set drill to starting position
    hw_controller.lock_motors()
    hw_controller.move_y(-0.5)
    print(len(work.matrix))
    # Pattern
    for lines in work.matrix:
        # forward or backward ?
        print("line "+str(lines))
        for pixel in (lines if direction == FORWARD else reversed(lines)):
            print("pixel"+str(pixel))
            pixel=(pixel[0]+pixel[1]+pixel[2])/3
            if emergency_stop:
                emergency_stop = False
                hw_controller.drill_off()
                hw_controller.unlock_motors()
                return

            # Same depth
            if previous_pixel == pixel:
                hw_controller.move_x(direction)
                print("move")

            # down to up
            if previous_pixel > pixel:
                hw_controller.move_y(1)
                hw_controller.move_x(direction)

            # up to down
            else:
                hw_controller.move_x(direction)
                hw_controller.move_y(-1)
            previous_pixel = pixel
        progress += p
        print(progress)
        direction = BACKWARD if direction == FORWARD else FORWARD
        hw_controller.move_z(1)
        print("move z")
    progress += r
    hw_controller.drill_off()
    hw_controller.unlock_motors()
    completed = True

