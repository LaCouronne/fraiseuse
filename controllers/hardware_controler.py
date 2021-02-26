
import math
#import RPi.GPIO as GPIO
import time
pin_fraise = 10

XDir = 13
XStepPin = 15
XEnable = 11

YDir = 31
YStepPin = 33
YEnable = 29

ZDir = 23
ZStepPin = 24
ZEnable = 12

motor_pulse_cycle = 6400
motor_delay = 0.001

#GPIO.setmode(GPIO.BOARD)


class Motor:

    def __init__(self, dir_pin, step_pin, en_pin):
        self.dir = dir_pin
        self.step = step_pin
        self.en = en_pin

        # GPIO.setup(dir_pin, GPIO.OUT)
        # GPIO.setup(step_pin, GPIO.OUT)
        # GPIO.setup(en_pin, GPIO.OUT)

        #moteurs en flottement pour pouvoir le positionner
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
        GPIO.output(pin_fraise, GPIO.HIGH)
        pass

    def drill_off(self):
        GPIO.output(pin_fraise, GPIO.LOW)

        pass

    def move_x(self, vector):
        # 1 turn - 2mm
        # 1 turn : 6400 pulses
        pixel_size = self.work.drill.diameter
        diameter = self.work.barrel.diameter
        radius = diameter / 2

        # # Send pulses for requested move
        # for _ in range(abs(vector) * pixel_pulse):
        #     GPIO.output(self.motor_z.step, 1)
        #     time.sleep(motor_delay)
        #     GPIO.output(self.motor_z.step, 0)


        pass

    def move_y(self, vector):
        #1 turn - 2mm
        #1 turn : 6400 pulses
        assert isinstance(vector, int)
        if vector == 0:
            return
        #move 6 mm up or down depending on the vector sign
        pixels_pulses = motor_pulse_cycle * 6

        #Vector sign + => cw    - => ccw
        vector_sign = 1 if vector > 0 else 0
        for _ in range(abs(vector) * pixel_pulse):
            pass

        #     GPIO.output(self.motor_y.step, 1)
        #     time.sleep(motor_delay)
        #     GPIO.output(self.motor_y.step, 0)

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
