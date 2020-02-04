import math

class BUS():
    def __init__(self):
        self.__bus_number = 0
        self.__bus_name = ""
        self.__bus_type = 0
        self.__base_voltage_kV = 0.0
        self.__voltage_pu = 1.0
        self.__angle_rad = 0.0
    def set_bus_number(self, number):
        self.__bus_number = number
    def set_bus_name(self, name):
        self.__bus_name = name
    def set_bus_type(self, type):
        self.__bus_type = type
    def set_base_voltage(self, voltage):
        self.__base_voltage_kV = voltage
    def set_voltage_pu(self, voltage):
        self.__voltage_pu = voltage
    def set_angle_rad(self, angle):
        self.__angle_rad = angle
    def set_angle_deg(self, angle):
        self.set_angle_rad(angle/180.0*math.pi)
    def get_bus_number(self):
        return self.__bus_number
    def get_bus_name(self):
        return self.__bus_name
    def get_bus_type(self):
        return self.__bus_type
    def get_base_voltage(self):
        return self.__base_voltage_kV
    def get_voltage_pu(self):
        return self.__voltage_pu
    def get_angle_rad(self):
        return self.__angle_rad
    def get_angle_deg(self):
        return self.get_angle_rad()*180.0/math.pi
        
class LINE():
    def __init__(self):
        self.__ibus = 0
        self.__jbus = 0
        self.__ickt = ""
        self.__status = False
        self.__Z1 = 0.0+0.0i
        self.__Z0 = 0.0+0.0i
        self.__Y1 = 0.0+0.0i
        self.__Y0 = 0.0+0.0i
    def set_ibus(self, bus):
        self.__ibus = bus
    def set_jbus(self, bus):
        self.__jbus = bus
    def set_ickt(self, ickt):
        self.__ickt = ickt
    def set_status(self, status=True):
        self.__status = status
    def set_Z1(self, z):
        self.__Z1 = z
    def set_Y1(self, y):
        self.__Y1 = y
    def set_Z0(self, z):
        self.__Z0 = z
    def set_Y0(self, y):
        self.__Y0 = y
    def get_ibus(self):
        return self.__ibus
    def get_jbus(self):
        return self.__jbus
    def get_ickt(self):
        return self.__ickt
    def get_status(self):
        return self.__status
    def get_Z1(self):
        return self.__Z1
    def get_Y1(self):
        return self.__Y1
    def get_Z0(self):
        return self.__Z0
    def get_Y0(self):
        return self.__Y0
        
class TRANSFORMER2():
    def __init__(self):
        self.__ibus = 0
        self.__jbus = 0
        self.__ickt = ""
        self.__status = False
        self.__ik = 1.0
        self.__jk = 1.0
        self.__Z1 = 0.0+0.0i
        self.__Z0 = 0.0+0.0i
        self.__Y1 = 0.0+0.0i
        self.__Y0 = 0.0+0.0i
    def set_ibus(self, bus):
        self.__ibus = bus
    def set_jbus(self, bus):
        self.__jbus = bus
    def set_ickt(self, ickt):
        self.__ickt = ickt
    def set_status(self, status=True):
        self.__status = status
    def set_ik(self, k=1.0):
        if self.get_jk()==1.0:
            self.__ik = k
    def set_jk(self, k=1.0):
        if self.get_ik()==1.0:
            self.__jk = k
    def set_Z1(self, z):
        self.__Z1 = z
    def set_Y1(self, y):
        self.__Y1 = y
    def set_Z0(self, z):
        self.__Z0 = z
    def set_Y0(self, y):
        self.__Y0 = y
    def get_ibus(self):
        return self.__ibus
    def get_jbus(self):
        return self.__jbus
    def get_ickt(self):
        return self.__ickt
    def get_status(self):
        return self.__status
    def get_ik(self):
        return self.__ik
    def get_jk(self):
        return self.__jk
    def get_Z1(self):
        return self.__Z1
    def get_Y1(self):
        return self.__Y1
    def get_Z0(self):
        return self.__Z0
    def get_Y0(self):
        return self.__Y0
        
class TRANSFORMER3():
    def __init__(self):
        self.__ibus = 0
        self.__jbus = 0
        self.__kbus = 0
        self.__sbus = 0
        self.__ickt = ""
        self.__status = False
        self.__ik = 1.0
        self.__jk = 1.0
        self.__kk = 1.0
        self.__Zi1 = 0.0+0.0i
        self.__Zj1 = 0.0+0.0i
        self.__Zk1 = 0.0+0.0i
        self.__Zi0 = 0.0+0.0i
        self.__Zj0 = 0.0+0.0i
        self.__Zk0 = 0.0+0.0i
        self.__Y1 = 0.0+0.0i
        self.__Y0 = 0.0+0.0i
    def set_ibus(self, bus):
        self.__ibus = bus
    def set_jbus(self, bus):
        self.__jbus = bus
    def set_kbus(self, bus):
        self.__kbus = bus
    def set_sbus(self, bus):
        self.__sbus = bus
    def set_ickt(self, ickt):
        self.__ickt = ickt
    def set_status(self, status=True):
        self.__status = status
    def set_ik(self, k=1.0):
        if self.get_jk()==1.0 or self.get_kk()==1.0:
            self.__ik = k
    def set_jk(self, k=1.0):
        if self.get_ik()==1.0 or self.get_kk()==1.0:
            self.__jk = k
    def set_kk(self, k=1.0):
        if self.get_ik()==1.0 or self.get_jk()==1.0:
            self.__kk = k
    def set_Zi1(self, z):
        self.__Zi1 = z
    def set_Zj1(self, z):
        self.__Zj1 = z
    def set_Zk1(self, z):
        self.__Zk1 = z
    def set_Y1(self, y):
        self.__Y1 = y
    def set_Zi0(self, z):
        self.__Zi0 = z
    def set_Zj0(self, z):
        self.__Zj0 = z
    def set_Zk0(self, z):
        self.__Zk0 = z
    def set_Y0(self, y):
        self.__Y0 = y
    def get_ibus(self):
        return self.__ibus
    def get_jbus(self):
        return self.__jbus
    def get_kbus(self):
        return self.__kbus
    def get_sbus(self):
        return self.__sbus
    def get_ickt(self):
        return self.__ickt
    def get_status(self):
        return self.__status
    def get_ik(self):
        return self.__ik
    def get_jk(self):
        return self.__jk
    def get_kk(self):
        return self.__kk
    def get_Zi1(self):
        return self.__Zi1
    def get_Zj1(self):
        return self.__Zj1
    def get_Zk1(self):
        return self.__Zk1
    def get_Y1(self):
        return self.__Y1
    def get_Zi0(self):
        return self.__Zi0
    def get_Zj0(self):
        return self.__Zj0
    def get_Zk0(self):
        return self.__Zk0
    def get_Y0(self):
        return self.__Y0
        
class GENERATOR():
    def __init__(self):
        self.__bus = 0
        self.__status = False
        self.__Mbase = 0.0
        self.__P = 0.0
        self.__Q = 0.0
        self.__Qmax =  999.0
        self.__Qmin = -999.0
        self.__Vschedule = 1.0
        self.__Z1 = 0.0+0.0i
        self.__Z2 = 0.0+0.0i
        self.__Z0 = 0.0+0.0i
    def set_bus(self, bus):
        self.__bus = bus
    def set_status(self, status=True):
        self.__status = status
    def set_Mbase(self, s):
        self.__Mbase = s
    def set_P(self, p):
        self.__P = p
    def set_Q(self, q):
        self.__Q = q
    def set_Qmax(self, q):
        self.__Qmax = q
    def set_Qmin(self, q):
        self.__Qmin = q
    def set_Z1(self, z):
        self.__Z1 = z
    def set_Z2(self, z):
        self.__Z2 = z
    def set_Z0(self, z):
        self.__Z0 = z
    def get_bus(self):
        return self.__bus
    def get_status(self):
        return self.__status
    def get_Mbase(self):
        return self.__Mbase
    def get_P(self):
        return self.__P
    def get_Q(self):
        return self.__Q
    def get_Qmax(self):
        return self.__Qmax
    def get_Qmin(self):
        return self.__Qmin
    def get_Z1(self):
        return self.__Z1
    def get_Z2(self):
        return self.__Z2
    def get_Z0(self):
        return self.__Z0
        
class LOAD():
    def __init__(self):
        self.__bus = 0
        self.__status = False
        self.__P = 0.0
        self.__Q = 0.0
        self.__Z1 = 0.0+0.0i
        self.__Z2 = 0.0+0.0i
        self.__Z0 = 0.0+0.0i
    def set_bus(self, bus):
        self.__bus = bus
    def set_status(self, status=True):
        self.__status = status
    def set_P(self, p):
        self.__P = p
    def set_Q(self, q):
        self.__Q = q
        self.__Qmin = q
    def set_Z1(self, z):
        self.__Z1 = z
    def set_Z2(self, z):
        self.__Z2 = z
    def set_Z0(self, z):
        self.__Z0 = z
    def get_bus(self):
        return self.__bus
    def get_status(self):
        return self.__status
    def get_P(self):
        return self.__P
    def get_Q(self):
        return self.__Q
    def get_Z1(self):
        return self.__Z1
    def get_Z2(self):
        return self.__Z2
    def get_Z0(self):
        return self.__Z0
        
class SHUNT():
    def __init__(self):
        self.__bus = 0
        self.__status = False
        self.__Q = 0.0
    def set_bus(self, bus):
        self.__bus = bus
    def set_status(self, status=True):
        self.__status = status
    def set_Q(self, q):
        self.__Q = q
    def get_bus(self):
        return self.__bus
    def get_status(self):
        return self.__status
    def get_Q(self):
        return self.__Q