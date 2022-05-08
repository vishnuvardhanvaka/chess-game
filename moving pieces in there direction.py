

import time
l=[]
w0=['r','h','b','q','k','b','h','r']
b0=['r','h','b','k','q','b','h','r']
for p in range(8):
		k=[]
		if p==0:
			for i in w0:
				k.append('w'+i)
		elif p==7:
			for i in w0:
				k.append('b'+i)
		elif p==1:
			for i in range(8):
				k.append('wp')
		elif p==6:
			for  i in range(8):
				k.append('bp')
		else:
			for i in range(8):
				k.append('  ')
		l.append(k)
l[2][2]='wb'
def show(l):
	for i in l:
		print(f'| {i} |',end='\r')
		print('\n')
	print('++++++++++++++++++++++++++++++++++++++')
show(l)
def pawn(i,j,m):
	if i+1!=8 and ( l[i+1][j]=='  ' or l[i+1][j][0]!=m[0]) and (i==1 or i==6):
		steps=input('enter number of steps you want to move (1 or 2 ) : ')
		if steps==2 and l[i+1][j]=='  ':
			temp=l[i+2][j]
			l[i][j]='  '
			l[i+2][j]=temp
		elif steps==2 and l[i+1][j]!='  ':
			print('invalid move !')
	elif i+1!=8 and ( l[i+1][j]=='  ' or l[i+1][j][0]!=m[0]):
			temp=l[i][j]
			l[i][j]='  '
			l[i+1][j]=temp
	else:
		print('invalid move !')
	time.sleep(2)
	return l
def bishop(i,j,m):
	pass
m=input('enter which piece should move : ')
r,c=map(int,input('enter row and column to move : ').split(','))
if m[1]!='p':
	st=int(input('enter number of steps : '))
else:
	st=1
l=pawn(r-1,c-1,m)
show(l)
			
