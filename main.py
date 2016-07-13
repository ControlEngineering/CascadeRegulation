
from objects import FirstOrderObject

obj = FirstOrderObject(2, 1)
for _ in range(1000):
    print obj(10, 0.1)
