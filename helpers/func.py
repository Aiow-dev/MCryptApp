class FuncSingleCall:
    def __init__(self):
        self.__calls = 0

    def is_call(self):
        self.__calls += 1
        return self.__calls < 2

    def reset(self):
        self.__calls = 0
