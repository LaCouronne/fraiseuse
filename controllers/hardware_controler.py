
import math
# import RPi.GPIO as GPIO
import time

XDir = 6
XStepPin = 13
XEnable = 5

YDir = 27
YStepPin = 22
YEnable = 17

ZDir = 19
ZStepPin = 4
ZEnable = 26

motor_pulse_cycle = 6400
motor_delay = 0.001


class Motor:

    def __init__(self, dir_pin, step_pin, en_pin):
        self.dir = dir_pin
        self.step = step_pin
        self.en = en_pin
        #
        # GPIO.setup(dir_pin, GPIO.OUT)
        # GPIO.setup(step_pin, GPIO.OUT)
        # GPIO.setup(en_pin, GPIO.OUT)
        # GPIO.output(en_pin, GPIO.HIGH)


class HardwareController:

    drill_depth = 6

    def __init__(self, work):
        self.work = work

        # Setup motors
        self.motor_x = Motor(XDir, XStepPin, XEnable)
        self.motor_y = Motor(YDir, YStepPin, YEnable)
        self.motor_z = Motor(ZDir, ZStepPin, ZEnable)

    def drill_on(self):
        pass

    def drill_off(self):
        pass

    def move_x(self, vector):
        pass

    def move_y(self, vector):
        pass

    def move_z(self, vector):

        assert isinstance(vector, int)
        if vector == 0:
            return

        pixel_size = self.work.drill.diameter
        diameter = self.work.barrel.diameter
        radius = diameter / 2

        # Requested motor angular move
        alpha = pixel_size * 180 / math.pi * radius

        # Coupled motor require conversion to actual required angle
        coupling = 25 / 15
        coupled_alpha = alpha * coupling

        # nb pulses required for on pixel displacement
        pixel_pulse = coupled_alpha * (360 / motor_pulse_cycle)

        vector_sign = 1 if vector > 0 else 0

        # # Set motor direction
        # GPIO.output(self.motor_z.dir, vector_sign)
        #
        # # Send pulses for requested move
        # for _ in range(abs(vector) * pixel_pulse):
        #     GPIO.output(self.motor_z.step, 1)
        #     time.sleep(motor_delay)
        #     GPIO.output(self.motor_z.step, 0)
