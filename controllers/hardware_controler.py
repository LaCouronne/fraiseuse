
import math
import time
import sys
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
motor_delay = 0.0001

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:

    class MockGPIO:

        delta_time_limit = .5

        motorx = {}
        motory = {}
        motorz = {}

        BOARD = None
        OUT = None
        HIGH = None
        LOW = None

        @classmethod
        def setup(cls, *args, **kwargs):
            pass

        @classmethod
        def setmode(cls, *args, **kwargs):
            pass

        @classmethod
        def output(cls, addr, val):

            if cls.motorx.get("last_pulse_date") and time.time() > cls.motorx.get("last_pulse_date") + cls.delta_time_limit:
                cls.motorx["status"] = 0
            else:
                cls.motorx["status"] = 1
                
            if cls.motory.get("last_pulse_date") and time.time() > cls.motory.get("last_pulse_date") + cls.delta_time_limit:
                cls.motory["status"] = 0
            else:
                cls.motory["status"] = 1
                
            if cls.motorz.get("last_pulse_date") and time.time() > cls.motorz.get("last_pulse_date") + cls.delta_time_limit:
                cls.motorz["status"] = 0
            else:
                cls.motorz["status"] = 1

            if addr in [XDir, YDir, ZDir]:
                if addr == XDir:
                    cls.motorx["direction"] = val
                if addr == YDir:
                    cls.motory["direction"] = val
                if addr == ZDir:
                    cls.motorz["direction"] = val

            if addr in [XStepPin, YStepPin, ZStepPin]:
                if addr == XStepPin and val == 1:
                    cls.motorx["last_pulse_date"] = time.time()
                    cls.motorx["status"] = 1
                if addr == YStepPin and val == 1:
                    cls.motory["last_pulse_date"] = time.time()
                    cls.motory["status"] = 1
                if addr == ZStepPin and val == 1:
                    cls.motorz["last_pulse_date"] = time.time()
                    cls.motorz["status"] = 1

            print(
                "\r" +
                "[ Motor X: " + ("-" if not cls.motorx.get("status") else "→" if cls.motorx.get("direction") == 1 else "←") + " ] " +
                "[ Motor Y: " + ("-" if not cls.motory.get("status") else "→" if cls.motory.get("direction") == 1 else "←") + " ] " +
                "[ Motor Z: " + ("-" if not cls.motorz.get("status") else "→" if cls.motorz.get("direction") == 1 else "←") + " ] ",
                end="",
                flush=True
            )

    GPIO = MockGPIO


GPIO.setmode(GPIO.BOARD)


class Motor:

    def __init__(self, dir_pin, step_pin, en_pin):
        self.dir = dir_pin
        self.step = step_pin
        self.en = en_pin

        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(en_pin, GPIO.OUT)

        #moteurs en flottement pour pouvoir le positionner
        GPIO.output(en_pin, GPIO.HIGH)


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

        pixel_pulse = motor_pulse_cycle // 2
        # Send pulses for requested move
        for _ in range(abs(vector) * pixel_pulse):
             GPIO.output(self.motor_z.step, 1)
             time.sleep(motor_delay)
             GPIO.output(self.motor_z.step, 0)



    def move_y(self, vector):
        #1 turn - 2mm
        #1 turn : 6400 pulses
        #assert isinstance(vector, float)
        if vector == 0:
            return
        #move 6 mm up or down depending on the vector sign
        pixels_pulses = motor_pulse_cycle * 3

        #Vector sign + => cw    - => ccw
        vector_sign = 1 if vector > 0 else 0
        for _ in range(math.floor((vector) * pixels_pulses)):
             GPIO.output(self.motor_y.step, 1)
             time.sleep(motor_delay)
             GPIO.output(self.motor_y.step, 0)



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

        # Set motor direction
        GPIO.output(self.motor_z.dir, vector_sign)

        # Send pulses for requested move
        for _ in range(int(abs(vector) * pixel_pulse)):
            GPIO.output(self.motor_z.step, 1)
            time.sleep(motor_delay)
            GPIO.output(self.motor_z.step, 0)
