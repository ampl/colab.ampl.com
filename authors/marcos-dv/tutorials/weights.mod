param n;
set I := 1..n;
var x{I} integer >= 0 <= 2;
param w{i in I} := 10 + floor(Uniform(0,500)) mod 200;

maximize profit:
    sum{i in I} w[i] * x[i];

s.t. capacity:
    sum{i in I} x[i] <= 133;
