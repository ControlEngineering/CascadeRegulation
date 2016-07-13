
class FirstOrderObject:
    """
              K
    G(s) = --------
            sT + 1

                             T
            U * K + y(t-1)* ---
                            dt
    y(t) = ----------------------
                 T
                ---  +  1
                 dt
    """
    __T = 1
    __K = 1
    __Yprev = 0

    def __init__(self, T, K):
        self.__T = T
        self.__K = K

    def __call__(self, U, dt):
        Y = 1.0 * U + self.__Yprev * self.__T / dt
        Y = Y / (self.__T / dt + 1)
        self.__Yprev = Y
        
        return Y

