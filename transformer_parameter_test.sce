exec('transformer_parameter_calculator.sce')
//双绕组变压器参数计算测试(归算到高压侧)
//课本例题
//chdir('./')
RT_test = transformer_R_calculate(123,110,31.5);
disp(RT_test)
XT_test = transformer_X_calculate(10.5,110,31.5);
disp(XT_test)
GT_test = transformer_G_calculate(32.5,110);
disp(GT_test)
BT_test = transformer_B_calculate(0.8,110,31.5);
disp(BT_test)
