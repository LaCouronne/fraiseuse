
class Demo:

    toto = "abc"

    def __init__(self, tata):
        self.tata = tata

    @staticmethod
    def static(a, b):
        print(a)

    @classmethod
    def class_method(cls, a):
        print(cls.toto, a)

    def method(self, a):
        print(self.tata, Demo.toto, a)


Demo.static(0, 1)

Demo.toto = "cde"
Demo.class_method("xyz")

demo1 = Demo(tata="def")
demo1.method("012")

demo2 = Demo(tata="patate")
demo2.method("012")


