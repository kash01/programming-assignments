def valley(l1):
	l=len(l1)
	flag=True
	if(l%2==0 or l==1):
		flag=False
	else:
		for i in range(0,l//2):
			if(int(l1[i])==int(l1[i+1])+1):
				continue
			else:
				flag=False
				break
		for i in range(l//2,l-1):
			if(int(l1[i])==int(l1[i+1])-1):
				continue
			else:
				flag=False
				break
	return(flag)

import math
l2=input("Enter the sequence\n")
l1=l2.split(" ")
print(valley(l1))

