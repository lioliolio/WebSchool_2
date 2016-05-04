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
