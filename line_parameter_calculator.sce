//实现线路参数r，x，b计算（每千米长度）
//计算电阻 参数：电阻率，横截面积，分裂方式
function r = r_calculate(resistivity,cross_sectional_area,split_mode)
	r = 1/split_mode*resistivity/cross_sectional_area;
endfunction
//几何均距（m）
function Dm = Dm_calculate(AB_phase_distance,BC_phase_distance,CA_phase_distance)
	Dm = (AB_phase_distance*BC_phase_distance*CA_phase_distance)^(1/3);
endfunction
//计算分裂导线等值半径,最多4分裂
function req = req_calculate(radius,split_mode,split_distance)
	if split_mode==1
		req = radius;
	elseif split_mode==2
		req = sqrt(radius*split_distance)
	elseif split_mode==3
		req = sqrt(radius*split_distance*split_distance)
	else
		req = sqrt(radius*split_distance*split_distance*split_distance*1.4142135)
	end
endfunction		
//计算电抗 参数：几何均距（m），等效半径（mm），分裂方式,u=1
function x = x_calculate(Dm,equivalence_radius,split_mode,u)
	x = 0.1445*log(Dm/(0.001*equivalence_radius))+0.0157*u/split_mode;
endfunction
//计算电纳 参数：几何均距（m），等效半径（mm）
function b = b_calculate(Dm,equivalence_radius)
	b = 7.58e-6*log(Dm/(0.001*equivalence_radius));
endfunction
//电导计算，一般为0
function g = g_calculate(P0,U)
	g=0
endfunction
