'''Phương trình bậc 3'''
#ax3+bx2+cx+d=0

import math
import cmath

phuongtrinh = input("Phuong Trinh Bac 3: ")

#(heso3)y^3+(heso2)y^2+(heso1)y+(heso0)=0 (1)

heso3s = ''
heso2s = ''
heso1s = ''
heso0s = ''

intclass = ['0','1','2','3','4','5','6','7','8','9','+','-','.']

for i in range(len(phuongtrinh)):
	if phuongtrinh[i] == 'x':
		if phuongtrinh[i+2] == '3':
			for n in range(len(phuongtrinh)):
				if phuongtrinh[i-n-1] in intclass:
					heso3s = phuongtrinh[i-n-1] + heso3s
				if phuongtrinh[i-n-1] not in intclass: break
			heso3 = float(heso3s)
		elif phuongtrinh[i+2] == '2':
			for n in range(len(phuongtrinh)):
				if phuongtrinh[i-n-1] in intclass:
					heso2s = phuongtrinh[i-n-1] + heso2s
				if phuongtrinh[i-n-1] not in intclass: break
			heso2 = float(heso2s)
		else:
			for n in range(len(phuongtrinh)):
				if phuongtrinh[i-n-1] in intclass:
					heso1s = phuongtrinh[i-n-1] + heso1s
				if phuongtrinh[i-n-1] not in intclass: break
			heso1 = float(heso1s)
	elif phuongtrinh[i] == '=':
		for n in range(len(phuongtrinh)):
			if phuongtrinh[i-n-1] in intclass:
				heso0s = phuongtrinh[i-n-1] + heso0s
			if phuongtrinh[i-n-1] not in intclass: break
		heso0 = float(heso0s)

#print(heso3) print(heso2) print(heso1) print(heso0)

#(1) <=> y^3 + my^2 + ny + p = 0 (2)

m = heso2s / heso3
n = heso1s / heso3
p = heso0s / heso3

#to y=x-m/3
#(2) => x^3 + ax + b = 0 (3)

a = (n - m**2 /2)
b = (2 * m**3 /27 - m*n /3 + p)

#to x=u+v
#(3) => (u^3+v^3+b) + (u+v)(3uv+a) = 0 
#<=> u^3 + v^3 = -b and u^3.v^3 = -a^3 /27
#t^2 - b - a^3 /27 =0

D = (b /2)**2 + (a /3)**3
if D >= 0:
	sqrtD = math.sqrt(D)
else: sqrtD = cmath.sqrt(D)

u3 = -b /2 + sqrtD
v3 = -b /2 - sqrtD

u1 = u3**(1/3)
v1 = v3**(1/3)

x1 = u1 + v1
x2 = complex((-1/2)*(u1 + v1), (math.sqrt(3)/2)*(u1 - v1))
x3 = complex((-1/2)*(u1 + v1), -(math.sqrt(3)/2)*(u1 - v1))

if D != 0:
	print('phuong trinh co 3 nghiem phan biet la: ' + str(x1) + '; ' + str(x2) + '; ' + str(x3))
else:
	if x1 == x2 or x2 == x3:
		print('phuong trinh co 2 nghiem thuc la: ' + str(x1) + '; ' + str(x3))
	else: print('phuong trinh co 2 nghiem thuc la: ' + str(x1) + '; ' + str(x2))
