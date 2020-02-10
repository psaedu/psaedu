//测试线路计算
exec('line_parameter_calculator.sce')
//测试不分裂导线
r1 =  r_calculate(31.5,600,1)
Dm = Dm_calculate(8,8,16)
req1 = req_calculate(16.6,1,0);
x1 = x_calculate(Dm,req1,1,1)
b1 = b_calculate(Dm,req1)
//测试分裂导线
r2 = r_calculate(31.5,300,2)
req2 = req_calculate(11.85,2,400);
x2 = x_calculate(Dm,req2,2,1)
b2 = b_calculate(Dm,req2)


