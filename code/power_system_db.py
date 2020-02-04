class POWER_SYSTEM_DB():
    def __init__(self):
        self.__buses = []
        self.__lines = []
        self.__transformers2 = []
        self.__transformers3 = []
        self.__generators = []
        self.__loads = []
        self.__shunts = []
    def add_bus(self, bus):
        self.__buses.append(bus)