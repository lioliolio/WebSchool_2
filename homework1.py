# 문제2 방법1

for i in range(5):
	star = " " * (4 - i)
	for j in range(i + 1):
		star += "*"
	print(star)

# 문제2 방법2

for i in range(5):
	star = " " * (4 - i)
	star1 = "*" * (i + 1)
	star = star + star1
	print(star)

# 문제2 방법3

for i in range(5):
	print(" " * (4 - i) + "*" * (i + 1))

# 문제3 방법1

for i in range(5):
	star = "*" * (5 - i)
	print(star)

#문제3 방법2

for i in range(5):
	print("*" * (5 - i))

#문제4 방법1

for i in range(5):
	star = " " * i
	for j in range(5 - i):
		star += "*"
	print(star)

#문제4 방법2

for i in range(5):
	star = " " * i
	star1 = "*" * (5 - i)
	star = star + star1
	print(star)

#문제4 방법3

for i in range(5):
	print((" " * i) + ("*" * (5 - i)))

#--------------------------------------------------

#소수 구하기 Lambda 함수로 바꾸기
#우선 내 생각으로는 for 문 한번은 필요하다고 생각함.

MAX = 1000

for i in range(2, int(MAX**0.5) + 1):
	not_prime_list += list(map(lambda x: x, range(i*2, MAX + 1, i)))
	        
prime_list = list(filter(lambda x: x not in not_prime_list, range(2, MAX + 1)))

print(prime_list)

# 함수 선언하고 해본 코드
MAX = 1000

def non_prime(numbers):
	for i in range(2, int(numbers**0.5) + 1):
		for j in range(i*2, numbers+1, i):
			return j
					            
not_prime_list += list(map(lambda x: non_prime(x), range(2, MAX + 1)))
					    
prime_list = list(filter(lambda x: x not in not_prime_list, range(2, MAX + 1)))

print(prime_list)

# 이게 답인듯?(답아님)
MAX = 10

not_prime_list += list(map(lambda x: map(lambda x: x, range(2,int(MAX**0.5) +1)), range(i*2, MAX + 1, i)))
    
prime_list = list(filter(lambda x: x not in not_prime_list, range(2, MAX + 1)))
print(prime_list)
