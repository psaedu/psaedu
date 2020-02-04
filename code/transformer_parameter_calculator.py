class TRANSFORMER2_PARAMETER_CALCULATOR():
    def __init__(self):
        self.__ibase_voltage = 0.0
        self.__jbase_voltage = 0.0
        self.__capacity = 0.0
        self.__P0_open_circuit = 0.0
        self.__I0_open_circuit = 0.0
        self.__P0_short_circuit = 0.0
        self.__V0_short_circuit = 0.0
    def set_primary_winding_base_voltage(self, v):
        self.__ibase_voltage = v
    def set_secondary_winding_base_voltage(self, v):
        self.__jbase_voltage = v
    def set_capacity(self, s):
        self.__capacity = s
    def set_open_circuit_P0_kW(self, p):
        self.__P0_open_circuit = p
    def set_open_circuit_I0_pu(self, i):
        self.__I0_open_circuit = i
    def set_short_circuit_P0_kW(self, p):
        self.__P0_short_circuit = p
    def set_short_circuit_V0_pu(self, v):
        self.__V0_short_circuit = v
    def get_primary_winding_base_voltage(self):
        return self.__ibase_voltage
    def get_secondary_winding_base_voltage(self):
        return self.__jbase_voltage
    def get_capacity(self):
        return self.__capacity
    def get_open_circuit_P0_kW(self):
        return self.__P0_open_circuit
    def get_open_circuit_I0_pu(self):
        return self.__I0_open_circuit
    def get_short_circuit_P0_kW(self):
        return self.__P0_short_circuit
    def get_short_circuit_V0_pu(self):
        return self.__V0_short_circuit
    def set_transformer_type(self, type):
        # get and set transformer data from given file: transformer2_data.csv
        pass
    def calculate_on_primary_side(self):
        # main function
        # return z, y
        pass
    def calculate_on_secondary_side(self):
        # main function
        # return z, y
        pass

class TRANSFORMER3_PARAMETER_CALCULATOR():
    def __init__(self):
        self.__ibase_voltage = 0.0
        self.__jbase_voltage = 0.0
        self.__kbase_voltage = 0.0
        self.__icapacity = 0.0
        self.__jcapacity = 0.0
        self.__kcapacity = 0.0
        self.__P0_open_circuit = 0.0
        self.__I0_open_circuit = 0.0
        self.__P0_short_circuit_ij = 0.0
        self.__V0_short_circuit_ij = 0.0
        self.__P0_short_circuit_jk = 0.0
        self.__V0_short_circuit_jk = 0.0
        self.__P0_short_circuit_ki = 0.0
        self.__V0_short_circuit_ki = 0.0
    def set_primary_winding_base_voltage(self, v):
        self.__ibase_voltage = v
    def set_secondary_winding_base_voltage(self, v):
        self.__jbase_voltage = v
    def set_tertiary_winding_base_voltage(self, v):
        self.__kbase_voltage = v
    def set_primary_winding_capacity(self, s):
        self.__icapacity = s
    def set_secondary_winding_capacity(self, s):
        self.__jcapacity = s
    def set_tertiary_winding_capacity(self, s):
        self.__kcapacity = s
    def set_open_circuit_P0_kW(self, p):
        self.__P0_open_circuit = p
    def set_open_circuit_I0_pu(self, i):
        self.__I0_open_circuit = i
    def set_primary_secondary_winding_short_circuit_P0_kW(self, p):
        self.__P0_short_circuit_ij = p
    def set_primary_secondary_winding_short_circuit_V0_pu(self, v):
        self.__V0_short_circuit_ij = v
    def set_secondary_tertiary_winding_short_circuit_P0_kW(self, p):
        self.__P0_short_circuit_jk = p
    def set_secondary_tertiary_winding_short_circuit_V0_pu(self, v):
        self.__V0_short_circuit_jk = v
    def set_tertiary_primary_winding_short_circuit_P0_kW(self, p):
        self.__P0_short_circuit_ki = p
    def set_tertiary_primary_winding_short_circuit_V0_pu(self, v):
        self.__V0_short_circuit_ki = v
    def get_primary_winding_base_voltage(self):
        return self.__ibase_voltage
    def get_secondary_winding_base_voltage(self):
        return self.__jbase_voltage
    def get_tertiary_winding_base_voltage(self):
        return self.__kbase_voltage
    def get_primary_winding_capacity(self):
        return self.__icapacity
    def get_secondary_winding_capacity(self):
        return self.__jcapacity
    def get_tertiary_winding_capacity(self):
        return self.__kcapacity
    def get_open_circuit_P0_kW(self):
        return self.__P0_open_circuit
    def get_open_circuit_I0_pu(self):
        return self.__I0_open_circuit
    def get_primary_secondary_winding_short_circuit_P0_kW(self):
        return self.__P0_short_circuit_ij
    def get_primary_secondary_winding_short_circuit_V0_pu(self):
        return self.__V0_short_circuit_ij
    def get_secondary_tertiary_winding_short_circuit_P0_kW(self):
        return self.__P0_short_circuit_jk
    def get_secondary_tertiary_winding_short_circuit_V0_pu(self):
        return self.__V0_short_circuit_jk
    def get_tertiary_primary_winding_short_circuit_P0_kW(self):
        return self.__P0_short_circuit_ki
    def get_tertiary_primary_winding_short_circuit_V0_pu(self):
        return self.__V0_short_circuit_ki
    def set_transformer_type(self, type):
        # get and set transformer data from given file: transformer3_data.csv
        pass
    def calculate_on_primary_side(self):
        # main function
        # return zi, zj, zk, y
        pass
    def calculate_on_secondary_side(self):
        # main function
        # return zi, zj, zk, y
        pass
    def calculate_on_tertiary_side(self):
        # main function
        # return zi, zj, zk, y
        pass
