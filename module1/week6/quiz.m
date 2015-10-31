clear
clc

disp '-------- Option 1 ------------'
w0 = [-0.5 -1 1];
w1 = [1.5 -1 1];
w2 = [-0.5 1 1];

disp '[0 0]'
x = [1 0 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 0]'
x = [1 1 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[0 1]'
x = [1 0 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 1]'
x = [1 1 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '-------- Option 2 ------------'
w0 = [-1.5 1 1];
w1 = [0.5 -1 -1];
w2 = [-1.5 1 1];

disp '[0 0]'
x = [1 0 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 0]'
x = [1 1 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[0 1]'
x = [1 0 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 1]'
x = [1 1 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '-------- Option 3 ------------'
w0 = [-1.5 1 1];
w1 = [1.5 -1 -1];
w2 = [-0.5 1 1];

disp '[0 0]'
x = [1 0 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 0]'
x = [1 1 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[0 1]'
x = [1 0 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 1]'
x = [1 1 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '-------- Option 4 ------------'
w0 = [-1.5 1 1]
w1 = [0.5 -1 -1]
w2 = [-0.5 1 1]

disp '[0 0]'
x = [1 0 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 0]'
x = [1 1 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[0 1]'
x = [1 0 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 1]'
x = [1 1 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '-------- Option 5 ------------'
w0 = [-1.5 1 1];
w1 = [1.5 -1 -1];
w2 = [-1.5 1 1];

disp '[0 0]'
x = [1 0 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 0]'
x = [1 1 0];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[0 1]'
x = [1 0 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'

disp '[1 1]'
x = [1 1 1];
if (w0*x') > 0
    p1=1;
else
    p1=0;
end
if (w1*x') > 0
    p2=1;
else
    p2=0;
end
z = [1 p1 p2];
y = w2*z'
