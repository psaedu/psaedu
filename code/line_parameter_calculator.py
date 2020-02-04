class LINE_PARAMETER_CALCULATOR():
    def __init__(self):
        self.__line_r = 0.0
        self.__phase_r = 0.0
        self.__AB_distance = 0.0
        self.__BC_distance = 0.0
        self.__CA_distance = 0.0
    def set_line_radius(self, r):
        self.__line_r = r
    def set_phase_radius(self, r):
        self.__phase_r = r
    def set_AB_phase_distance(self, d):
        self.__AB_distance = d
    def set_BC_phase_distance(self, d):
        self.__BC_distance = d
    def set_CA_phase_distance(self, d):
        self.__CA_distance = d
    def get_line_radius(self, r):
        return self.__line_r
    def get_phase_radius(self, r):
        return self.__phase_r
    def get_AB_phase_distance(self):
        return self.__AB_distance
    def get_BC_phase_distance(self):
        return self.__BC_distance
    def get_CA_phase_distance(self):
        return self.__CA_distance
    def set_line_type(self, type):
        # get and set line data from given file: line_data.csv
        pass
    def calculate(self):
        # main function
        # return r, x, g, b
        pass
