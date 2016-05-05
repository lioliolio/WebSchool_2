# WebSchool_2

1일차  
  
컴퓨터의 역사, 컴퓨터의 구성, 컴퓨터의 구조, 데이터의 표현방식  
  
2일차  
  
컴퓨터의 연산, 운영체제, 컴퓨터 동작체험  
  
3일차  
  
자료구조, 알고리즘, 데이터베이스  
  
4일차  
  
네트워크,  암호화  
  
5일차  
  
소프트웨어 공학, Week Review  
  
6일차  
  
프로그래밍 언어, 프로그래밍 용어, 현업에 대해서  
  
7일차  
  
개발환경 세팅, Git  
  
8일차  
  
**파이썬 1일차** 
  
- 파이썬은 왜 사용하는가?  
  
	처음 배우는 입장에서 쉽게 배울 수 있고 쉽지만 큰 그림을 그릴 수 있는 언어  
  
	웹프로그래밍, 데이터사이언스 둘다 사용 가능  
  
- REPL(Read Eval Print Loop)  
  
    코드를 실행하고 한 줄씩 실행할 수 있는 환경  
  
- 프로그래밍 언어를 배울 떄 처음 배워야 하는 것은?  
  
	언어가 만들어진 목적, 어떻게 발전해왔는지 등등~~~  
  
  
1. 자료형(Data Type)  
  
- 자료형(Data Type)과 자료구조(Data Structure)의 차이점은?  
  
	자료형은 프로그래밍 자체에 구현되어 있고  
	자료구조는 사용자가 직접 구현해야 한다.  
	따라서 구현하는 사람의 능력에 따라 성능 차이가 크다.  
  
- 자료형(Data Type)의 종류는?
  
	숫자, 문자, 리스트, 튜플, 딕셔너리, 셋, Boolean 등?  
  
- 자료구조(Data Structure)의 종류는?  
  
	배열, 집합, 키-값 등등  
  
	자료구조에서 배열이 파이썬에서 구현된 것이 리스트, 집합은 셋, 키-값은 딕셔너리이다.  
  
1) 숫자(Number)  
  
정수, 실수, 복소수, 8진수, 16진수 등등  
  
- 연산  
  
a = a + 1 == a += 1  
  
a * a == a ** 2  
  
14 % 3 ==> 나머지를 구하는 연산  
  
2) 문자열  
  
name[1:] ==> 1번부터 끝까지 문자열을 뽑아낸다.  
  
"%s님 안녕하세요." % "김태우" ==> 김태우님 안녕하세요.  
명시적이지 못하고 코드가 길다.  
  
"{0}님 안녕하세요.".format(0 = "김태우") ==> 김태우님 안녕하세요.  
"0"이 명시적이지 않다.  
  
"{name}님 안녕하세요.".format(name = "김태우") ==> 김태우님 안녕하세요.  
파이썬에서는 이것을 사용해야 함.  
  
3) List  
  
변수명 = ["", ""]  
  
List는 순서가 있고 변경이 가능하다.  
  
변수명.append("") ==> 추가  
  
len(변수명) ==> 요소 갯수  
  
변수명.pop("") ==> 특정 요소 제거  
  
변수명[0][0] ==> 변수 안에 있는 한 요소의 첫번째 문자?  
  
4) Tuple  
  
List와 동일하지만 Element 값이 변경되지 않는다.  
  
ex) width_and_height(120, 240)  
width, height = width_and_height  
#width, height = (120, 240)  
  
5) Set(집합)  
  
집합은 순서가 없고, 각각 Element 값이 유니크해야 한다.(중복되지 않아야 함)  
  
중복 제거할 때 사용할 수 있다.  
  
ex) name_set = set(["1", "1", "3", "5"]) ==> {'1', '3', '5'}  
  
중복값 제거방법  
  
ex) name_list = ["3", "3", "1", "5", "5"]  
name_list = list(set(name_list))  
  
6) Dict  
  
명시적이어서 활용도가 높다.
  
detail_dict = {"name": "김태우", "age": 31, "phone_number": "010-2359-9787"}  
  
7) Boolean  
  
& ==> and  
  
| ==> or  

2. 제어문  
  
1) if 문  


```python
a = 4
b = 3

if a > b:
	print("a > b")
elif a < b:
	print("a < b")
else:
	print("a = b")
```

2) while 문

```
a = 10

while a < 20:
	print(a)
    a += 1
```

3) for 문
  
```
for _ in range(10):
	print("Hello World.")
#for문에서 변수를 사용하지 않을 경우 _ 사용한다.
```
  
while문은 명시적이지 않고 while문 안에서 계속 제어를 해야하기 때문에 파이썬에서는 for문을 더 선호한다.

for문으로 별 찍기

```
#방법 1
for i in range(5):
	star = ""
    for j in range(i + 1):
    	star += "*"
    print(star)

#방법 2
star = ""
for i in range(5):
	star += "*"
    print(star)
    
#방법 3
for i in range(5):
	print("*" * (i + 1))

```

3. 입력과 출력

username = input() ==> python3
username = raw_input() ==> python2

input은 str로 받는다.

print("Hello World") ==> python3에서는 함수
print "Hello World") ==> python2에서는 statement

9일차

++**파이썬 2일차**++

```python
# 별만들기 코드 (1)

# 1. 입력받은 숫자에 따라 몇번 돌아야하는지, 어디서 분할 해야하는지 파악
# 2. 처음 시작할때 " "과 "*"의 갯수 파악하고 규칙 찾기
# 3. 코드 쓰기

def star():
	print("숫자를 입력하세요.")
    count = int(input())

	for i in range(count * 2 - 1):
    	if i < count:
        	print(
            " " * i + 
            "*" * ((count * 2 - 1) - (i *2))
            )
        else:
        	print(
            " " * (2 * count - i - 2) + 
            "*" * (2 * i - 2 * count + 3)
            )
            
# 별만드기 코드 (2)
# last_count를 어떻게 사용할 지 고민 중

def star():
    print("숫자를 입력하세요.")
    count = int(input())
    last_count = count * 2 - 1
    
    for i in range(last_count):
        if i < count:
            print(
            " " * i + 
            "*" * (last_count - (i * 2))
            )
        else:
            print(
            " " * (count - 2 + count + i) + 
            "*" * (3 + 2 * i - 2 * count)
            )

# 조교님 답안 코드

def start9():

    cnt = int(input('숫자 입력해보셈: '))
    for i in range(1, cnt):
        print(" "*(i-1), end="")
        print("*"*(-2*i+(2*cnt+1)), end="")
        print()
    for i in range(1, cnt+1):
        print(" "*(-1*i+cnt), end="")
        print("*"*(i*2-1), end="")
        print()

start9()
```

**1. List와 Dict의 for loop**

List와 Tuple은 순서가 의미 있음.
Set과 Dict은 순서가 의미가 없음.
Dict은 Key 값이 존재 하기 때문에...
list(range(i, j))로 range를 리스트 형식으로 확인할 수 있음

```python
# List, Dict

animal = ["tiger", "cat", "dog", "bear"]
my_info = {
	"name": "김태우
    "age": 31
    "location": "김포"
}
```
```python
# List for loop

for animal in animals:
	print(animal)
```
```
tiger
cat
dog
bear
```
```python
# dict for loop (1)

for my_info in my_infos:
	print(my_info)
    print(my_infos[my_info])
```
```
name
김태우
location
김포
age
31
```
```python
# dict for loop (2)

for my_info in my_infos.items():
	print(my_info)
    
#tuple 형태로 나옴
```
```
('name', '김태우')
('location', '김포')
('age', 31)
```
```python
# dict for loop (3)

for my_info in my_infos.items():
	key, value = my_info
    print(key)
    print(value)
```
```
name
김태우
location
김포
age
31
```
```python
# dict for loop (4)
# 가장 많이 쓰이는 방식

for key, value in my_infos.items():
	print(key)
    print(value)
```
```
name
김태우
location
김포
age
31
```
```python
print(my_infos.keys())
```
```
dict_keys(['name', 'location', age'])
```
```python
print(my_infos.values())
```
```
dict_values(['김태우', '김포', 31])
```
```python
# 연습문제 (1)
# 하나씩 출력을 하는데
# Index가 2번인 애를 "파이썬"으로 변경하자.

#나의 처음 코드

for i in range(len(animals)):
	if i == 2:
    	animals[2] = "파이썬"
        print(animals[2])
    else:
    	print(animals[i])
```

```python
# 연습문제 (1) 답 (1)

for i in range(len(animals)):
	if i == 2:
    	animals[i] = "파이썬"
        print(animals[i])
    else:
    	print(animals[i])
        
#위의 코드 중 중복되는 부분을 제거한 코드

for i in range(len(animals)):
	if i == 2:
    	animals[i] == "파이썬"
    print(animals[i])
```

```python
# 위의 코드를 직관적으로 바꾸기
# List에는 index라는 함수가 존재

animals.index("파이썬")
```
```
2
```
```python
# animal은 for문 지정할 때 초기화 됨

for animal in animals:
	index = animals.index(animal)
    
    if index == 2:
    	animals[index] = "파이썬"
    print(animals[index])
```
```
tiger
cat
파이썬
bear
```
```python
# List를 dict의 .item() 처럼 튜플형식으로 만듬

for something in enumerate(animals):
	print(something)
```
```
(0, 'tiger')
(1, 'cat')
(2, '파이썬')
(3, 'bear')
```
```python
for index, value in enumerate(animals):
	print(index, value)
```
```
0 tiger
1 cat
2 파이썬
3 bear
```
```python
# for index, value in enumerate(animals):
# value 값을 사용하지 않을 거라 _ 를 사용
for index, _ in enumerate(animals):
	if index == 2:
    	animals[index] = "파이썬"
    print(animals[index])
```
```
tiger
cat
파이썬
bear
```
```python
# 소수 구하기 (Prime Number)
# [2, 3, 5, ..., 997]
# 내가 처음 작성한 코드...결과값 안나옴
# 나중에 공부 더 해서 수정 예정

def get_prime_num(number):
    prime_number = []
    for i in range(number):
        for j in range(i + 1):
            if i + 2 == 2:
                prime_number.append(2)
            elif (i + 2) % (j + 2) != 0:
                prime_number.append(i + 2)
    print(prime_number)
```

```python
# 답
# number 만큼 for 문을 돌면서
# 각각의 숫자가 소수인지/아닌지 체크를
# 빈 리스트 하나 만들어서,
# 소수면 => 빈 리스트에 추가하고
# for 끝나는 시점에 빈 리스트를 출력

# 소수인지 아닌지 체크하는 함수
# 2부터 number-1까지의 숫자로 각각 나눠서 체크해본다
def is_prime(number):
	for i in range(2, number):
    	if (number % i == 0):
        	return False
        return True

def get_prime_numbers(number):
	prime_number = []
    for i in range(2, number):
    	if is_prime(i):
        	prime_numbers.append(i)
     return prime_numbers
```

```python
# is_prime 함수 개선하기

# 10 => 2, 3, 4, 5, 6, 7, 8, 9 (1번 돌기떄문에 꽤 빠르다)
# 101 => 2, 3, 4, 5, ..., 100
# 101 => 2, 3, 5, 7, ..., 100 (짝수만 뺀다)

# 1번째
# 2로 나누어떨어지는 숫자까지
# 101 => 51, ...,(51 * 2 = 102 > 101)
# 2번째
# 101의 루트2 (제곱근) 까지만 체크를
# 100 => 10
# 101 => 101**0.5 => 10.x => 11

def is_prime(number):
	for i in range(2, int(number**0.5) + 1):
    	if (number % i == 0):
        	return False
     return True
```

```python
# 시간 재는 코드

import time

start_time = time.time()
get_prime_numbers()
end_time = time.time()
end_time - start_time
```

**2. 함수**

```python
def sum(a, b):
	return a + b

result = sum(1, 3)
print(result)

# sum => Function
# a, b => Parameter
# 1, 3 => Argument
```

```python
4
```

```python
def sum(a, b):
	print("sum: {result}".format(result=a+b))
```

```python
# 입력받은 모든 숫자를 더해주는 'sum 이라는 함수를 만들어라.

# 내가 만든 함수

def sum(number_list):
	number_list = []
    total = 0
    for i in range(len(number_list)):
    	a = a + lnt(number_list[i])
    return total

# 답

def sum(number_list):
	total = 0
    for number in number_list:
    	total += number
    return total
```

```python
# 여러개의 변수를 입력받는 법
# * => 튜플형태로 한번에 받겠다라는 의미

def sum(*args):
	total = 0
    for arg in args:
    	total += arg
    return total

print(sum(1, 3, 5))
```

```
9
```

```python
def greeting(name, course):
	print("{name}님, {course} 등록을 축하드립니다.".format(name = name, course, course))

values = ("김태우", "마케팅")

greeting("김태우", "마케팅")

# unpack / unpacking
greetin(*values) # => greeting("김태우", "마케팅")

# *values 만 따로 사용하는 것은 안됨.
```

```
김태우님, 마케팅 등록을 축하드립니다.
김태우님, 마케팅 등록을 축하드립니다.
```