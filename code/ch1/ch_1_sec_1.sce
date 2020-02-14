// Power system analysis, Shandong University
// Ch.1, Sec. 1,load data module
function data = get_all_load_data(data_name)  
    load_data = read_csv(data_name);
    data = struct()
    data.date = load_data(2:$,1)
    data.load = strtod(load_data(2:$,2:$))
endfunction
function load = get_load_of_day(data, year, month, day)
    index = get_index_of_day(data, year, month, day)
    if isempty(index) | index==%inf then
        load = []
    else
        load = data.load(index,:)
        n = length(load); hours = [0:1:n-1]*0.25
        load = [hours; load]
    end
endfunction
function load = get_load_of_month(data, year, month)
    start_date_index = get_index_of_day(data, year, month, 1)
    end_date_index = get_index_of_day(data, year, month+1, 1)
    load = get_load_between_index(start_date_index, end_date_index)
endfunction
function load = get_load_of_year(data, year)
    start_date_index = get_index_of_day(data, year, 1, 1)
    end_date_index = get_index_of_day(data, year+1, 1, 1)
    load = get_load_between_index(start_date_index, end_date_index)
endfunction
function index = get_index_of_day(data, year, month, day)
    date = string(year)+'/'+string(month)+'/'+string(day)
    index = find(data.date==date)
    if isempty(index) & year>2019 then
        index = %inf
    end
endfunction
function load = get_load_between_index(start_date_index, end_date_index)
    if end_date_index==%inf | isempty(end_date_index) then
        load = data.load(start_date_index:$, :)
    else
        load = data.load(start_date_index:end_date_index, :)
    end
    load = matrix(load',1,-1); hours = [0:1:length(load)-1]*0.25;
    load = [hours; load]
endfunction
function pv_loads = get_daily_peak_and_valley_loads_of_year(data, year)
    pv_loads = []; ndays = 0;
    for month = 1:12
        for day = 1:31
            load = get_load_of_day(data, year, month, day)
            if ~isempty(load)
                ndays = ndays+1
                pv_loads=[pv_loads,[ndays;max(load(2,:));min(load(2,:))]]
            end
        end
    end
endfunction
function distribution = get_load_distribution_of_year(data, year)
    load = get_load_of_year(data, year)
    max_load = max(load(2,:)); min_load = min(load(2,:))
    n = 1000; step = (max_load-min_load)/(n-1)
    distribution = zeros(n,2)
    for i = 1:n
        load_value = min_load+step*(i-1)
        distribution(i,1) = load_value
        distribution(i,2) = sum(load(2,:)>load_value)*0.25 // convert to hour
    end
endfunction
function load = interpolate_load_of_day(data, year, month, day)
    load = get_load_of_day(data, year, month, day)
    n = 4; newstep = 0.25/(n+1);
    load = smooth(load, newstep)
endfunction

load_data = get_all_load_data('load_data.csv');
year = 2018; month = 12; day = 4;
// draw load curve of specific day
data = get_load_of_day(load_data, year, month, day)
figure(1); plot(data(1,:), data(2,:))
xtitle(string(year)+'/'+string(month)+'/'+string(day)+' Load Curve', 'Time/hour', 'Load/MW')
// draw load curve of specific month
data = get_load_of_month(load_data, year, month)
figure(2); plot(data(1,:), data(2,:))
xtitle(string(year)+'/'+string(month)+' Load Curve', 'Time/hour', 'Load/MW')
// draw load curve of specific year
data = get_load_of_year(load_data, year)
figure(3); plot(data(1,:), data(2,:))
xtitle('Year '+string(year)+' Load Curve', 'Time/hour', 'Load/MW')
// draw daily peak & valley load of year
data = get_daily_peak_and_valley_loads_of_year(load_data, year)
figure(4); plot(data(1,:), data(2:3,:))
xtitle( 'Year '+string(year)+' Daily Peak & Valley Load Curve', 'Time/day', 'Load/MW')
// draw distribution of load of year
distribution = get_load_distribution_of_year(load_data, year)
figure(5); plot(distribution(:,2), distribution(:,1))
xtitle('Year '+string(year)+' Accumulated Load Curve', 'Time/hour', 'Load/MW')
// draw interpolated load of day
data = interpolate_load_of_day(load_data, year, month, day)
figure(6); plot(data(1,:), data(2,:))
xtitle(string(year)+'/'+string(month)+'/'+string(day)+' Interpolated Load Curve', 'Time/hour', 'Load/MW')
