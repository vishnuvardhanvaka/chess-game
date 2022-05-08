
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
				k.append(' ')
		l.append(k)
def show(l):
	for i in l:
		print(f'| {i} |')
		print('\n')
show(l)
def pawn(i,j):
	if i+1!=8 and ( l[i+1][j]==' ' or l[i+1][j][0]!=m[0]):
				temp=l[i][j]
				l[i][j]=' '
				l[i+1][j]=temp
	show(l)
	time.sleep(2)
	return l
m=input('enter which piece should move : ')
if m[1]!='p':
	st=int(input('enter number of steps : '))
else:
	st=1
for i in range(8):
	for j in range(8):
		if l[i][j]==m:
			print(i,j)
			if m[1]=='p':
				l=pawn(i,j)
show(l)
			