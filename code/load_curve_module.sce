//Power system analysis course supporting software package
//Load data searching module

function data = get_all_load_data(data_name)  
    //Load standard load data  
	//data_name = "load_2017_2019.csv"
    load_data = read_csv(data_name);    //Warning:Work path can only contain one "code"
    data = struct()
    data.date = load_data(2:$,1)
    data.load = strtod(load_data(2:$,2:$))
endfunction

function load = get_load_of_day(data, year, month, day)
    //Get data of a day
    index = get_index_of_day(data, year, month, day)
    if index==-1 | index==%inf then
        load = []
    else
        load = data.load(index,:)
		n = length(load)
		hours = [0:1:n-1]*0.25
		load = [hours; load]  
    end
endfunction

function load = get_load_of_month(data, year, month)
    //Get the load data of a month
    start_date_index = get_index_of_day(data, year, month, 1)
    end_date_index = get_index_of_day(data, year, month+1, 1)-1
    if end_date_index~=%inf then
        load = data.load(start_date_index:end_date_index, :)
    else
        load = data.load(start_date_index:$, :)
    end
    load = matrix(load',1,-1)  
	n = length(load)
	hours = [0:1:n-1]*0.25
	load = [hours; load] 
endfunction

function load = get_load_of_year(data, year)
    //Get the load data of a year
    start_date_index = get_index_of_day(data, year, 1, 1)
    end_date_index = get_index_of_day(data, year+1, 1, 1)-1
    if end_date_index~=%inf then
        load = data.load(start_date_index:end_date_index, :)
    else
        load = data.load(start_date_index:$, :)
    end
    load = matrix(load',1,-1)    
	n = length(load)
	hours = [0:1:n-1]*0.25
	load = [hours; load] 
endfunction

function index = get_index_of_day(data, year, month, day)
    //Get specific coordinates of a day
    if year<2017 then
        index = -1
        return
    end
    if month>12 then
        year = year+1
        month = month-12
    end
    if year>2019 then
        index = %inf
        return
    end
    date = string(year)+'/'+string(month)+'/'+string(day)
    index = find(data.date==date)
endfunction

function peak_load = get_peak_load_of_day(data, year, month, day)
    //Get peak load of the day
    load = get_load_of_day(data, year, month, day)
    peak_load = max(load(2,:))
endfunction

function peak_load = get_peak_load_of_month(data, year, month)
    //Get the peak load of a month
    load = get_load_of_month(data, year, month)
    peak_load = max(load(2,:))
endfunction

function peak_load = get_peak_load_of_year(data, year)
    //Get the peak load of a year
    load = get_load_of_year(data, year)
    peak_load = max(load(2,:))
endfunction

function valley_load = get_valley_load_of_day(data, year, month, day)
    load = get_load_of_day(data, year, month, day)
    valley_load = min(load(2,:))
endfunction

function valley_load = get_valley_load_of_month(data, year, month)
    load = get_load_of_month(data, year, month)
    valley_load = min(load(2,:))
endfunction

function valley_load = get_valley_load_of_year(data, year)
    load = get_load_of_year(data, year)
    valley_load = min(load(2,:))
endfunction

function peak_loads = get_peak_loads_of_all_days_in_month(data, year, month)
    //Get the maximum daily load of a month
    peak_loads = []
    for day = 1:31
        day_peak_load = get_peak_load_of_day(data, year, month, day)
        if isempty(day_peak_load)
            return
        else
            peak_loads($+1) = day_peak_load
        end
    end
endfunction

function valley_loads = get_valley_loads_of_all_days_in_month(data, year, month)
    //Get the minimum daily load of a month
    valley_loads = []
    for day = 1:31
        day_valley_load = get_valley_load_of_day(data, year, month, day)
        if isempty(day_peak_load)
            return
        else
            valley_loads($+1) = day_valley_load
        end
    end
endfunction

function peak_loads = get_peak_loads_of_all_days_in_year(data, year)
    //Get the maximum daily load of the year
    peak_loads = []
    for month = 1:12
       peak_loads = [peak_loads;get_peak_loads_of_all_days_in_month(data, year, month)] 
    end
endfunction

function valley_loads = get_valley_loads_of_all_days_in_year(data, year)
    //Get the maximum daily load of the year
    valley_loads = []
    for month = 1:12
       valley_loads = [valley_loads;get_valley_loads_of_all_days_in_month(data, year, month)] 
    end
endfunction

function distribution = get_load_distribution_of_day(data, year, month, day)
	load = get_load_of_day(data, year, month, day)
	n = 50
	distribution = get_distribution_of_load(load, n)
endfunction

function distribution = get_load_distribution_of_month(data, year, month)
	load = get_load_of_month(data, year, month)
	n = 100
	distribution = get_distribution_of_load(load, n)
endfunction

function distribution = get_load_distribution_of_year(data, year)
	load = get_load_of_year(data, year)
	n = 1000
	distribution = get_distribution_of_load(load, n)
endfunction

function distribution = get_distribution_of_load(load, n)
	max_load = max(load(2,:))
	min_load = min(load(2,:))
	step = (max_load-min_load)/(n-1)
	distribution = zeros(n,2)
    disp(min_load)
	for i = 1:1:n
		load_value = min_load+step*(i-1)
		distribution(i,1) = load_value
        //disp(load_value)
        //disp(sum(load(:,2)>load_value))
		distribution(i,2) = sum(load(2,:)>load_value)*0.25 // convert to hour
	end
endfunction

function load = interpolate_load_of_day(data, year, month, day, method)
	load = get_load_of_day(data, year, month, day)
	n = 4
	load = get_interpolated_load(load, n, method)
endfunction

function load = interpolate_load_of_month(data, year, month, method)
	load = get_load_of_month(data, year, month)
	n = 4
	load = get_interpolated_load(load, n, method)
endfunction

function load = interpolate_load_of_year(data, year, method)
	load = get_load_of_year(data, year)
	n = 4
	load = get_interpolated_load(load, n, method)
endfunction

function load = get_interpolated_load(load, n, method)
	newstep = 0.25/(n+1)
	if method == 'interpln'
		newx = [load(1,1):newstep:load($,1)]
		load = interpln(load, newx)
	elseif method == 'smooth'
		load = smooth(load, newstep)
	end
endfunction
 

