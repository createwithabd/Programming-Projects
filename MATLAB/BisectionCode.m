%{
----- Bisection Method -----   
Author: Abdullah A.
%} 
clc
clear all
f = @(v) 100*sin(v)*exp(-v)-20;

xl=0;   % Lower Guess
xu=0.6; % Upper Guess
tolerance=0.0002; % Approximate Percent Relative Error

if f(xl)*f(xu) < 0 
    disp('Iterations    Root Value  Percent Relative Error     xl Value       xu Value');
    disp(' ---------------------------------------------------------------------------- ');
    for i=1:100
        xr = (xl+xu)/2;
        er = abs((xr-xl)/xr);
        m1 = f(xl)*f(xr);
        fprintf('%7d %15f %15f %20f %15f \n', [i; xr; er; xl; xu])
        if abs((xr-xl)/xr)<tolerance % Termination 
            break
        end 
        if m1 < 0 % Step # 03 
            xu = xr; 
        elseif m1 > 0 % step # 04 
            xl = xr;
        end      
    end
end
        