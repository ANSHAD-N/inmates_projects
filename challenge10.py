class Power:
    def __init__(self, n):
        self.n = n

    def __mul__(self, other):
        n = self.n + other.n
        return n


x = Power(5)
y = Power(3)
print(x*y)
