'''oan tu ti voi may tinh'''

#import ham randint tu thu vien random
from random import randint

#hien thi ten tro choi
print('\n| OAN TU TI GAME |')
print('---------------------')

#nhap lua chon cua nguoi choi
player = 0
while player not in ('keo','bua','bao'):
	player = input('select ? keo, bua or bao: ')

#random va gan doi tuong cho may tinh
computer = randint(0,2)
if computer == 0:
	computer = "keo"
elif computer == 1:
	computer = "bua"
else: computer = "bao"

#hien thi lua chon cua nguoi choi va may tinh len man hinh
print('---------------------')
print('You choose: ' + player)
print('Computer choose: ' + computer)
print('---------------------')

#so sanh gia tri va hien thi ket qua len man hinh
if player == computer:
	print('draw, because ' + player + ' = ' + computer)
elif player == 'keo':
	if computer == 'bua':
		print('you lose, because keo < bua')
	else: print('you win, because keo > bao')
elif player == 'bua':
	if computer == 'keo':
		print('you win, because bua > keo')
	else: print('you lose, because bua < bao')
else: 
	if computer == 'keo':
		print('you lose, because bao < keo')
	else: print('you win, because bao > bua')