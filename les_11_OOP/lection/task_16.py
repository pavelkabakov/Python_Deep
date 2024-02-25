class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b

    def __str__(self):
        return f'MyClass(a={self.a}, b={self.b}, c={self.c})'

    def __repr__(self):
        return str(self.a) + str(self.b) + str(self.c) # тут ошибка

cl_1 = MyClass(2, 3)
print(cl_1)
print(repr(cl_1))
