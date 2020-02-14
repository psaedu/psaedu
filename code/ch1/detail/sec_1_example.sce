//Power system analysis course supporting software package
//Load curve drawing module

module_path = 'sec_1.sce';
exec(module_path); // load module
data_path = '../load_data.csv';
load_data = get_all_load_data(data_path); // load data

year = 2017; month = 3; day = 4;

// draw load curve of specific day
//data = get_load_of_day(load_data, year, month, day)
//plot(data(1,:), data(2,:))
//fig_title = string(year)+"年"+string(month)+"月"+string(day)+"日负荷曲线"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw load curve of specific month
//data = get_load_of_month(load_data, year, month)
//plot(data(1,:), data(2,:))
//fig_title = string(year)+"年"+string(month)+"月负荷曲线"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw load curve of specific year
//data = get_load_of_year(load_data, year)
//plot(data(1,:), data(2,:))
//fig_title = string(year)+"年负荷曲线"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw peak & valley load of month
//data = get_peak_loads_of_all_days_in_month(load_data, year, month)
//plot(data)
//data = get_valley_loads_of_all_days_in_month(load_data, year, month)
//plot(data)
//fig_title = string(year)+"年"+string(month)+"月逐日峰谷负荷曲线"
//fig_xlable = '时间/天'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw peak & valley load of year
//data = get_peak_loads_of_all_days_in_year(load_data, year)
//plot(data)
//data = get_valley_loads_of_all_days_in_year(load_data, year)
//plot(data)
//fig_title = string(year)+"年逐日峰谷负荷曲线"
//fig_xlable = '时间/天'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw distribution of load of day
//distribution = get_load_distribution_of_day(load_data, year, month, day)
//plot(distribution(:,2), distribution(:,1))
//fig_title = string(year)+"年"+string(month)+"月"+string(day)+"日持续负荷曲线"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw distribution of load of month
//distribution = get_load_distribution_of_month(load_data, year, month)
//plot(distribution(:,2), distribution(:,1))
//fig_title = string(year)+"年"+string(month)+"月持续负荷曲线"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw distribution of load of year
//distribution = get_load_distribution_of_year(load_data, year)
//plot(distribution(:,2), distribution(:,1))
//fig_title = string(year)+"年持续负荷曲线"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw interpolated load of day
//data = interpolate_load_of_day(load_data, year, month, day, 'smooth')
//plot(data(1,:), data(2,:))
//fig_title = string(year)+"年"+string(month)+"月"+string(day)+"日负荷曲线（插值）"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw interpolated load of month
//data = interpolate_load_of_month(load_data, year, month, 'smooth')
//plot(data(1,:), data(2,:))
//fig_title = string(year)+"年"+string(month)+"月负荷曲线（插值）"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)

// draw interpolated load of year
//data = interpolate_load_of_year(load_data, year, 'smooth')
//plot(data(1,:), data(2,:))
//fig_title = string(year)+"年负荷曲线（插值）"
//fig_xlable = '时间/小时'; fig_ylable = '负荷/MW';
//xtitle(fig_title, fig_xlable, fig_ylable)
