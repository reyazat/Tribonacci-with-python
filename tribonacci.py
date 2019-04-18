import sys

def get_input(q):
	if(sys.version_info > (3, 0)) :
		arg = input(q)
	else :
		arg = raw_input(q)
	return arg;

def get_list(arg , type = int):
	if(sys.version_info > (3, 0)) :
		numbers = list(map(type, arg.split()))
	else :
		numbers = map(type, arg.split())
	return numbers;

def tribonacci(n, start):
	if n >2 :
		j =3
		while j < n+1 :
			
			sum = start[0] + start[1] + start[2]
			start = [start[1], start[2] , sum]
			j +=1
			
	else:
		return start[n]
	return start[2]
	
