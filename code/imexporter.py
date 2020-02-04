import math

global power_system_db

class DATA_IMPORTER():
    def __init__(self):
        pass
    def load_powerflow_data(self, file):
        self.__load_powerflow_bus_data(file)
        self.__load_powerflow_line_data(file)
        self.__load_powerflow_transformer2_data(file)
        self.__load_powerflow_transformer3_data(file)
        self.__load_powerflow_generator_data(file)
        self.__load_powerflow_load_data(file)
        self.__load_powerflow_shunt_data(file)
    def __load_powerflow_bus_data(self, file):
        pass
    def __load_powerflow_line_data(self, file):
        pass
    def __load_powerflow_transformer2_data(self, file):
        pass
    def __load_powerflow_transformer3_data(self, file):
        pass
    def __load_powerflow_generator_data(self, file):
        pass
    def __load_powerflow_load_data(self, file):
        pass
    def __load_powerflow_shunt_data(self, file):
        pass
        
    def load_sequence_data(self, file):
        self.__load_sequence_line_data(file)
        self.__load_sequence_transformer2_data(file)
        self.__load_sequence_transformer3_data(file)
        self.__load_sequence_generator_data(file)
        self.__load_sequence_load_data(file)
        self.__load_sequence_shunt_data(file)
    def __load_sequence_line_data(self, file):
        pass
    def __load_sequence_transformer2_data(self, file):
        pass
    def __load_sequence_transformer3_data(self, file):
        pass
    def __load_sequence_generator_data(self, file):
        pass
    def __load_sequence_load_data(self, file):
        pass
    def __load_sequence_shunt_data(self, file):
        pass
        
    def load_dynamic_data(self, file):
        self.__load_dynamic_generator_data(file)
        self.__load_dynamic_load_data(file)
    def __load_dynamic_generator_data(self, file):
        pass
    def __load_dynamic_load_data(self, file):
        pass
        
class DATA_EXPORTER():
    def __init__(self):
        pass
    def export_powerflow_data(self, file):
        self.__export_powerflow_bus_data(file)
        self.__export_powerflow_line_data(file)
        self.__export_powerflow_transformer2_data(file)
        self.__export_powerflow_transformer3_data(file)
        self.__export_powerflow_generator_data(file)
        self.__export_powerflow_load_data(file)
        self.__export_powerflow_shunt_data(file)
    def __export_powerflow_bus_data(self, file):
        pass
    def __export_powerflow_line_data(self, file):
        pass
    def __export_powerflow_transformer2_data(self, file):
        pass
    def __export_powerflow_transformer3_data(self, file):
        pass
    def __export_powerflow_generator_data(self, file):
        pass
    def __export_powerflow_load_data(self, file):
        pass
    def __export_powerflow_shunt_data(self, file):
        pass
        
    def export_sequence_data(self, file):
        self.__export_sequence_line_data(file)
        self.__export_sequence_transformer2_data(file)
        self.__export_sequence_transformer3_data(file)
        self.__export_sequence_generator_data(file)
        self.__export_sequence_load_data(file)
        self.__export_sequence_shunt_data(file)
    def __export_sequence_line_data(self, file):
        pass
    def __export_sequence_transformer2_data(self, file):
        pass
    def __export_sequence_transformer3_data(self, file):
        pass
    def __export_sequence_generator_data(self, file):
        pass
    def __export_sequence_load_data(self, file):
        pass
    def __export_sequence_shunt_data(self, file):
        pass
        
    def export_dynamic_data(self, file):
        self.__export_dynamic_generator_data(file)
        self.__export_dynamic_load_data(file)
    def __export_dynamic_generator_data(self, file):
        pass
    def __export_dynamic_load_data(self, file):
        pass