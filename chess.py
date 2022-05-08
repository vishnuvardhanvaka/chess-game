
import random

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
def move(l,turn):
	wkills=[]
	bkills=[]
	if turn=='w':
		
	
	

