n = int(input("Enter number of applicants"))
l2=[]
for i in range(n):
	l1 = []
	str1 = input("Enter name\n")
	str2 = input("Enter gender\n")
	str3 = input("Enter language spoken\n")
	l1.append(str1)
	l1.append(str2)
	l1.append(str3)
	l2.append(l1)

class Gender_Exception(Exception):
	pass
		
class Language_Exception(Exception):
	pass

k = len(l2)
for j in range(k):
	try:
		if l2[j][1].upper() != "FEMALE":
			raise Gender_Exception
	except(Gender_Exception):
		print("Gender Exception was raised for "+l2[j][0])
	try:
		if l2[j][2].upper() != "ENGLISH":
			raise Language_Exception
	except(Language_Exception):
		print("Language Exception was raised for "+l2[j][0])
	else:
		print(l2[j])