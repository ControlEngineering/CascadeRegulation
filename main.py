
from objects import FirstOrderObject
from regulators import RegulatorPI

obj = FirstOrderObject(2, 1)
reg = RegulatorPI(10, 3)

SP = 25
PV = 0
for _ in range(10):
    y = reg(SP, PV, 0.1)
    if y > 150 : y = 150
    if y < 0 : y = 0
    PV = obj(y, 0.1)
    print "{} {}".format(y, PV)
