import pandas as pd
import numpy as np

def get_all_load_data(data_name):
    load_data = pd.read_csv(data_name,header = 0)
    data_date = load_data['时间'].values
    data_load = load_data.iloc[:,1:].values
    return data_date,data_load
    
def get_index_of_day(load_date, year, month, day):
    date = str(year)+'/'+str(month)+'/'+str(day)
    date_index = np.where(load_date==date)
    if len(date_index[0]) == 0:
        date_index = float('inf')
    else:
        date_index = date_index[0][0]
    return date_index  
    
def get_load_of_day(date, data, year, month, day):
    index = get_index_of_day(date, year, month, day)
    if index==float('inf'):
        load = []
    else:
        load = data[index,:]
        n = len(load)
        hours = np.arange(0,n,1)*0.25
        load = np.vstack((hours,load))
    return load

def get_load_between_index(data, start_date_index, end_date_index):
    if end_date_index==float('inf'):
        load = data[start_date_index:, :]
    else:
        load = data[start_date_index:end_date_index, :]
    n = len(load[0,:])
    hours = np.arange(0,n,1)*0.25
    load = np.vstack((hours,load))
    return load
    
def get_load_of_month(date, data, year, month):
    start_date_index = get_index_of_day(date, year, month, 1)
    end_date_index = get_index_of_day(date, year, month+1, 1)
    load = get_load_between_index(data, start_date_index, end_date_index)
    return load 
   
def get_load_of_year(date, data, year):
    start_date_index = get_index_of_day(date, year, 1, 1)
    end_date_index = get_index_of_day(date, year+1, 1, 1)
    load = get_load_between_index(data, start_date_index, end_date_index)
    return load

def get_day_minmax_load(date, data, year):
    pv_loads = [[],[],[]]
    ndays = 0
    month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    day_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    for month in month_list:
        for day in day_list:
            load = get_load_of_day(date, data, year, month, day)
            if len(load) !=0:
                ndays = ndays+1
                pv_loads[0].append(ndays)
                pv_loads[1].append(np.max(load[1,:]))
                pv_loads[2].append(np.min(load[1,:]))                
    return pv_loads

def get_load_distribution(date, data, year):
    load = get_load_of_year(date, data, year)
    max_load = np.max(np.max(load[1:,:]))
    min_load = np.min(np.min(load[1:,:]))
    n = 1000    
    step = (max_load-min_load)/(n-1)
    distribution = np.zeros((n,2))
    for i in range(n):
        load_value = min_load+step*i
        distribution[i,1] = load_value
        distribution[i,0] = np.sum(load[1:,:]>load_value)*0.25 
    return distribution

def interpolate_load_of_day(date, data, year, month, day):
    load = get_load_of_day(date, data, year, month, day)
    x = np.linspace(0,23.75,476)
    load = np.interp(x, load[0,:],load[1,:],1000,4000)
    load = np.vstack((x,load))
    return load 
      










