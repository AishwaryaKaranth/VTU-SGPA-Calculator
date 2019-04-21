import numpy as np
y={1:79,2:80,3:70,4:64,5:70,6:63,7:96,8:98}
c=([4,3,4,4,4,4,2,2])
d=y.values()
g=([])

gp=0
for i in d:
	if i in range(0,40):
		gp=0
		g.append(gp)
	elif i in range(40,45):
		gp=4
		g.append(gp)
	elif i in range(45,50):
		gp=5
		g.append(gp)
	elif i in range(50,60):
		gp=6
		g.append(gp)
	elif i in range(60,70):
		gp=7
		g.append(gp)
	elif i in range(70,80):
		gp=8
		g.append(gp)
	elif i in range(80,90):
		gp=9
		g.append(gp)
	else:
    gp=10
		g.append(gp)

c=([4,3,4,4,4,4,2,2])
a=np.array(g)
b=np.array(c)
z=np.dot(a,b)

op=True
if op ==True:
	total=(z/28)+(10/28)
else:
	total=z/28
print(total)

