xx = str(x);
ll = int(len(xx)/2);
for i in range(ll):
if(xx[i] != xx[-i-1]):
return False;
return True;