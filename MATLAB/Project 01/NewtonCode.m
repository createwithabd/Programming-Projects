%{
----- Newton Raphson Method -----   
Author: Abdullah A.
%} 
x0=0;
error=0.002;
f= @(v) 100*sin(v)*exp(-v)-20;
d= @(v) 100*(exp(-v)*cos(v)-exp(-v)*sin(v));
disp('Iterations    Root Value  Percent Relative Error     ');
disp(' --------------------------------------------------- ');
if d(x0)~=0    
    for i=1:100
        x1=x0-f(x0)/d(x0);
        err=abs((x1-x0)/x1);
        fprintf('%7d %15f %15f \n', [i; x1; err]);
        if err< error
            break
        end
        x0 = x1;
    end
end
fprintf('Root of function is %f ', x1);