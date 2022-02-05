from _ import api
t=str(input("Enter victim ph.no:"))
if len(t)==10:
	print("+91"+t)
	
elif len(t)!=10:
	print("Invalid number")
	exit()
	
else:
	print("Please enter correct number")

max=10**500
m=int(input("Enter msg count(enter 0 for unlimited sms):"))
if m==0:
	m=max
else:
	m=m
api(t,m)
		