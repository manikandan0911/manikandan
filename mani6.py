e=int(input())
if (e%100==0):
	if(e%400==0):
		print('yes')
	else:
		print('no')
else:
	if (e%4==0):
		print('yes')
	else:
		print('no')
