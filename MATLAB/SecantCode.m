
%{
----- Secant Method -----   
Author: Abdullah A.
%} 

f= @(v) 100*sin(v)*exp(-v)-20;

x1=0.6;
x2=0.4;
error=0.0002;
disp('Iterations  Root Value    x(i-1)    f(x(i-1))    x(i-2)    f(x(i-2)    Error     ');
disp(' ------------------------------------------------------------------------------------ ');

for i=1:100 
    x3 = x2-(f(x2)*((x2-x1)/(f(x2)-f(x1))));
    cal_error = abs((x3-x2)/x3);
    %percentage_error = abs((x3-x2)/x3)*100;
    fprintf('%7d %14f %10f %10f %10f %10f %11f \n', [i; x3; x2; f(x2); x1; f(x1); cal_error]); 
    if cal_error < error     
        break
    end
    x1 = x2;
    x2 = x3;
    
end
fprintf('the lowest root of functions is %f', x3);
