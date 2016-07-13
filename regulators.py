
class RegulatorPI:
    """
                  _         _
                 |       1   |
    G(s) = Kp *  | 1 +  ---  |
                 |_     Tis _|

    """
    __Kp = 1
    __Ti = 1
    __Err = [0, 0]
    __Y = [0 , 0]

    def __init__(self, Kp, Ti):
        self.__Kp = Kp
        self.__Ti = Ti

    def __call__(self, SP, PV, dt):
        self.__Err[0] = SP - PV

        self.__Y[0] = 1.0 * self.__Err[0] * (1 + dt/self.__Ti) - self.__Err[1];
        self.__Y[0] = (self.__Y[0] * self.__Kp) + self.__Y[1]

        self.__Err[1] = self.__Err[0]
        self.__Y[1] = self.__Y[0]

        return self.__Y[0]
