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
print("Hello World") ==> python2에서는 statement

```python
# Python 2.X 에서의 입력과 출력 부분에서 가장 뭄ㄴ제가 되는 부분은 "한글 인코딩"
# 한글을 지원하는 인코딩 : UTF8, EUC-KR
# Python 2.X의 기본 인코딩은 ascii
# Python 에서는 문자열을 표현할 수 있는 str, unicode 타입을 제공
# unicode는 문자표
# str은 그 문자표를 표현하기 위해 규정해 놓은 규칙?? 예) UTF-8 등
# 입력과 출력에서의 가장 큰 문제 - 인코딩
# Unicode is a character set
# UTF-8 is an encoding
```

```python
# 인코딩 정확하게 명시하기

print(type('한글')) # str
print(type(u'한글')) # unicod
```

```
$ python encoding.py

SyntaxError: Non-ASCII character '\xed' in file test.py on line 1,
but no encoding declared;
see http://python.org/dev/peps/pep-02
```

```python
# -*- coding: utf8 -*-

print(type('한글')) # str
print(type(u'한글')) # unicode
# 이렇게 파이썬 파일 제일 상단부에 # -*- coding: utf8 -*- 를 정확하게 명시
# 이 파이썬 파일이 UTF8 로 작성되었다는 것을 명시하는 것
```

```
$ python encoding.py

<type 'str'>
<type 'unicode'>
```

```python
# -*- coding: utf-8 -*-
print str(unicode("한글"))

# 한글 str을 uncode 로 변경했다가, 다시 str로 변경하면 문제가 생김
```

```
$ python encoding.py

UnicodeDecodeError: 'ascii' codec can't decode
byte 0xed in position 0: ordinal not in range(128)
```

```python
# -*- coding: utf-8 -*-
# 한글 인코딩 변환하기
print "한글".decode("utf8")
print "한글".decode("utf8").encode("utf8")

# 위와 같이 decode, encode를 통해서 변환가능
# 인코딩 방식을 명시해야 함
```

```python
# 다른 사람이 쓴 파일을 쓸 경우
# python 기본 인코딩을 ascii에서 utf-8로 변경하는 법

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
```

```
* Python 2.X 에서만 해당하는 내용

1. 파일 상단에 # -*-coding: utf-8 -*- 를 명시한다.
2. 파이썬 스크립트 내에서는 반드시 unicode 로 변경해서 사용한다.
3. 외부 파일을 읽거나 쓸 때는 str로 변경해서 읽거나 쓴다.
4. 외부 라이브러리를 사용할 때는 setdefaultencoding을 사용해서 기보적으로 utf8을 사용하도록하자.

# Python 3.X 는 모든 문자열이 unicode 이기 때문에 인코딩 신경안써도 된다.
```

```python
# ./ 현재폴더
# ../ 상위폴더
# ./test.txt 현재폴더의
# ../test.txt 상위폴더의
# ../../test.txt 상위폴더의 상위폴더의
```

```python
f = open("../animals.txt", "r") # mode => "w", "r", "a"
f.close()
# "w" (write) mode 로 파일을 여는 경우 기존 데이터는 모두 삭제
# "a" (append) mode 로 파일을 열어 내용 추가 가능(기존 데이터 그대로 있음)
```

```python
f.read() # 파일 안의 내용 전체를 문자열로 리턴
f.readline() # 파일 안의 내용을 한 줄씩 리턴.
f.readlines() # 파일 안의 모든 라인을 읽어 각각의 줄을 요소로 갖는 리스트로 리턴.
```
```python
f = open("./animals.txt", "w")
f.write("hello world")
f.close()

with open("./animals.txt","w") as f:
	f.write("hello world")

# with을 이용해서 파일 입/출력이 종료된 시점에서 자동으로  f.close 자동으로 실행시킬수 있음
# 가능하면 with을 사용하자
```

```python
# 작업 자동화
# 우리가 반복적으로 사용할 어떤 특정 기능들에 대해서 => "재사용 가능한 코드 덩어리"

# 함수정의
def greeting():
	username = input()
    print("{username}님, 가입을 축하드립니다.".format(username=username))
    
# 함수실행
greeting()
```
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
	print("{name}님, {course} 등록을 축하드립니다.".format(name = name, course = course))

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

```python
# tuple => 3개
# 이름, 수강신청이유, 코스명

def info(name, reason, course):
	print("{name}님이 {reason}의 이유로 {course}를 등록 하셨습니다".format(name=name, reason = reason, course = course ))

values = ("김태우", "심심하다", "마케팅")

info(*values)
```

```
김태우님이 심심하다의 이유로 마케팅를 등록 하셨습니다.
```

```python
# unnamed argument => *args (tuple)
# named argument(keyword) => **kwargs (dict)

#예제

def greeting(name, course):
	print("{name}님, {course} 등록을 축하드립니다.".format(name = name, course = course))

values = {
	"name": "김태우",
    "course": "마케팅"
}

greeting(name="김태우", course="마케팅")
greeting(*values)
greeting(**values) #for문에서 dict에서의 key값을 이용하는 것과 같음.
```

```
김태우님, 마케팅 등록을 축하드립니다.
course님, name 등록을 축하드립니다.
김태우님, 마케팅 등록을 축하드립니다.
```

```python
# **kwargs 로 함수 만들기

def print_all_informations(**kwargs):
	for key, value in kwargs.items():
    	print("{key} => {value}",format(key=key, value=value))

informations = {
	"name": "김태우"
    "email": "kpc00100@gmail.com"
    "age": 31
}

print_all_informations(**infomations)
print_all_informations(name="김태우", course="경제학")
```

```
name => 김태우
age => 31
email => kpc00100@gmail.com
course => 경제학
name => 김태우
```

```python
# def 누가만들어둔함수(이건필수값1, 이건필수값2, *arg, **kwargs):
# 라이브러리의 경우 뒤에는 세부 옵션 같은 것
```

```python
# Lambda
# 이름이 없는 함수 (익명 함수)
# 재사용이 안되는 함수

def increment(x):
	return x + 1

increment_lambda = lambda x: x+1

increment(30)
increment_lambda(30)
```

```
31
31
```

```python
(lambda x: x+1)(34)
(lambda x, y: x**y)(2, 2)
```

```
35
4
```

```python
# List를 입력받아서 그 List 값을 제곱한 리스트를 리턴해주는 함수
# 내가 만든 함수

def get_square_list(numbers):
	square_list = []

	for number in numbers:
    	square_list.append(number**2)
    return square_list

get_square_list([3, 4, 5, 6])
```

```
[9, 16, 25, 36]
```

```python
# map은 List의 각각의 element에 대해서 특정 함수를 적용한다.
# map은 List와 함께 움직임???

def square(x):
	return x ** 2
list(map(lambda x: x**2, [1, 2, 3]))
list(map(square, [1, 2, 3]))
```

```
[1, 4, 9]
[1, 4, 9]
```

**파이썬 3일차**

1. 퀴즈

```python
# 1. 1 ~ 100까지의 숫자 중에서 3과 5로 나누어 떨어지는 수를 저장하는 List를 만들어 주세요.

# Lambda 함수 이용할 때

list(filter(
	lambda x: x % 3 == 0 or x % 5 == 0,
    range(1, 100+1)
))

# list comprehension 이용할 때

[i for i in range(1, 100+1) if i%3==0 or i%5==0]
# 연산자는 명시적으로 쓰자 => and, or 등등
```

```python
# 2. 3의 배수가 입력되면 fast, 5의 배수가 입력되면 campus, 15의 배수가 입력되면  fastcampus 입력

num = 100

result = ""

if num % 3 == 0:
	result += "fast"

if num % 5 == 0:
	result += "campus"

result
```

```python
# 1~100 리스트 작성
# ["", "", "fast", "", "campus", "", ..., "fastcampus", ...]
# for 문 사용

word_list = []

for i in range(1, 100+1):
	word = ""
    if i % 3 == 0:
    	word += "fast"
    if i % 5 == 0:
    	word += "campus"

	word_list.append(word)
word_list

# list comprehension
# ["", "", "fast", "", ...]
# ["", "", "", "", "campus", ...]
# 참일 때의 값 if 조건문 else  거짓일 때의 값
# 뒤에 쓰는 if는 lambda에서 filter와 같은 역할

fast_list = [
	"fast" if x % 3 == 0 else ""
    for x
    in range(1, 100+1)
]

campus_list = [
	"campus" if x % 5 == 0 else ""
    for x
    in range(1, 100+1)
]

# 가장 파이썬 다운 방법

[
	fast_list[i] + campus_list[i]
    for i
    in range(1, 100+1)
]
```

```python
# something(100, 3, "fast", 5, "campus")
# ["", "", "fast", "", "campus", ..., "fastcampus", ...]

def somethin(count, first_number, first_word, second_number, second_word):
	first_list = [
    	first_word if i % first_number == 0 else ""
        for i
        in range(1, count+1)
    ]

	second_list = [
    	second_word if i % second_number == 0 else ""
        for i
        in range(1, count+1)
    ]

	return [
    	first_list[i] + second_list[i]
        for i
        in range(count)
    ]
```

```python
# palindrome
# 기러기 => 기러기
# 소주만병만주소 => 소주만병만주소

# is_palindrome("기러기") => True
# is_palindrome("아버지") => False

# 답
# 정의 => 문자열을 받아서, 뒤집었을 때 같으면 True 틀리면 False
# len("기러기")

def reverse(word):
	reversed_word = ""
    for i in range(len(word)):
    	reversed_word += word[(len(word)-1-i)]
    return reversed_word

def in_palindrome(word):
	return word == reverse(word)

# 더 쉽게하는 법
# "기러기는기러기다"[::-1] => "다기러기는기러기"

def is_palindrome(word):
	return word == word[::-1]

# lambda 함수 사용

(lambde x: x == x[::-1])("김태우")
```

2. 문자열 처리

```python
# "패스트캠퍼스 스쿨 과정은 참 좋다"
# =>["패스트캠퍼스", "스쿨", "과정은", "참", "좋다"]

# 내가 작성한 코드

def word_split(sentence):

	result = ""
    word_split_list = []

	for i in range(len(sentence)):
    	if sentence[i] == " ":
        	word_split_list.append(result)
            result = ""
        else:
        	result += sentence[i]

	if result != " ":
    	word_split_list.append(result)

	return word_split_list

# 답
# 앞에서 부터 한글자 한글자 읽으면서 => " " 스페이스가 나올 때까지
# 기다렸다가, 이게 나오면 모아뒀던 단어들을 리스트에 추가한다.

def word_split(sentence):
	
    word_list = []
    word = ""
    
    # for i in range(len(sentence))
    for char in sentence:
    	if char == " ":
    		word_list.append(word)
        	word = ""
   		 else:
    		word += char
    # 이 시점에 word가 비어있지 않은 상태
    if word != "":
    	word_list.append(word)
        
    return word_list

def word_split(sentence, seperate=" "): # 함수에 기본값 넣는 방법

	word_list = []
    word = ""
    
    for char in sentence:
    	if char == seperate:
        	word_list.append(word)
            word = ""
        else:
        	word += char
    #이 시점에 word가 비어있지 않은 상태
    if word != "":
    	word_list.append(word)
        
    return word_list

# word_split => 문장을 받아 단어 리스트
# word_join => 단어 리스트를 받아 문장으로 만드는
# word_replace => 단어를 받아서 특정 단어만 다른 단어로 바꾸는 것

# word_join(["안녕하세요", "저는", "김태우입니다."], " ")
# => "안녕하세요 저는 김태우입니다."

# word_replace("패스트캠퍼스", "패스트", "Fast")
# => "Fast 캠퍼스"
# 숙제
```

```python
# word_join 답

def word_join(word_list, seperate=" "):
	result = ""
    for word in word_list:
    	result += word
        result += seperate
    return result
```

```python
# word_replace("패스트캠퍼스", "패스트", "Fast")
# => "Fast캠퍼스"
# 과제

def word_replace(full_word, first_word, last_word):
	pass
```

```python
# SPLIT
# JOIN
# REPLACE
```

```python
# SPLIT
# 문자열 => 리스트 형식으로
word_list ="패스트캠퍼스는 참 좋다".split(" ")

[word for word in word_list if not word == ""] # 뒤에 " " 안나오게 하기
```

```python
# JOIN
# word_join(문자 리스트, 구분자)

" ".join(["패스트캠퍼스", "참", "좋구나"]) # 구분자.join(문자리스트)
```

```python
# REPLACE
# word_replace

"패스트캠퍼스".replace("패스트", "Fast")
```

책 추천 - 컴퓨터 프로그램의 구조와 해석(SICP)

```python
# dict 형식 => {"김태우": "주소..."}

# List의 List => Dict의 List로 변경하기
# [{...}, {...}, {...}]

user_list = [
	["김태우", "주소1"]
    ["김하영", "주소2"]
]

# 1. for 문으로

user_dict_list = []

for user in user_list:
	name = user[0]
    address = user[1]
    user_dict = {
    	"name": name,
        "address": address
    }
    user_dict_list.append(user_dict)
    
user_dict_list

# 2. list comprehension으로

[
	{
    	"name": user[0],
        "address": user[1]
    }
	for user
    in user_list
]

# for 앞에 위치는 lambda x:... 함수부분 정의해주는 부분과 같음

def get_user_dict(user):
	return {
    	"name": user[0],
        "address": user[1]
    }

[
	get_user_dict(user)
    for user
    in user_list
]
# 빈 list 로 for 문 작업할 시 list comprehension으로 거의 표현 가능
# 처음부터 생각이 안날떄는 for문으로 먼저 해보고 그담에 list comprehension으로 만들자.
```

```python
# 파일 입출력 이용
# user.csv
# 위의 파일을 읽어서 dict 형식으로 만들자
# with open("../users.csv", "r") as f:
#	...

# 답 for문

with open("../users.csv", "r") as f:
	user_list = []
    
    for line in f.readlines():
    	user_list.append(
        	{
            	"name" : line.split(",")[0],
                "appress": line.split(",")[1].replace("\n", "")
            })
	user_list
    
# list comprehension

with open("../users.csv", "r") as f:
	user_list = [
    	{
        	"name": line.split(",")[0],
            "address": line.split(",")[1].replace("\n", "")
        }
        for line
        in f.readlines()
    ]
    user_list
```

```python
# 데이터 전처리

# phonenumber.txt 파일 안에 있는 자료를 
# phonenumber_preprocess.txt 에 수정해서 저장하기
# 형식 01025430432
# 010-2454-0011 => 01024540011
# 공일공2552-공공일일 => 01025520011
# 공일공 => 010

def preprocess(phonenumber):
	hangul_to_number_dict = {
    	"공": 0,
        "영": 0,
        "일": 1,
        "이": 2,
        "삼": 3,
        "사": 4,
        "오": 5,
        "육": 6,
        "칠": 7,
        "팔": 8,
        "구": 9,
        "-": "",
        " ": ""
    }
    
    for key, value in hangul_to_number_dict.items():
    	phonenumber = phonenumber.replace(key, str(value))
    
    return phonenumber

with open("../phonenumber.txt", "r") as input_file:
	with open("./phonenumber_preprocessed.txt", "w") as output_file:
    	phonenumber_list = [
        	preprocess(line.replace("\n", ""))
            for line
            in input_file.readlines()
        ]
        
        for phonenumber in phonenumber_list:
        	output_file.write(phonenumber + "\n")

# 위의 코드 개선

with open("../phonenumber.txt", "r") as input_file:
	with open("./phonenumber_preprocessed.txt", "w") as output_file:
    	[
        	output_file.write(
            	preprocess(line.replace("\n", "")) + "\n")
            for line
            in input_file.readlines()
        ]
```

*객체 지향 프로그래밍*

```python
# 객체 지향 프로그래밍 (Object Oriented Programming)

# 절차 지향 프로그래밍
# 데이터, 데이터 처리하는 함수

# 객체 지향 프로그래밍
# 절차 <<<<<< 개개체
# 둥둥 떠다니는 객체
# 객체(데이터, 각각의 데이터를 처리하는 방법) <=> 객체 : 메세지를 전달
# 실험 => 완벽하게 적합한 알고리즘

# 함수형 프로그래밍 => Lambda, Lambda Operator, List Comprehension
# 모든 객체 자체를 함수로 생각
```

```python
# 김태우 학생
# 학생이 무엇인가?

class Student():
	__campus = "패스트캠퍼스"
	# private => 객체 내부에서만 호출할 수 있는 변수
    # 변경되면 안되는 변수에 사용...하지만 이것도 변경 가능...
    def __init__(self, name, age):
    # init => initialize (초기화하다)
    # Student() => __init__ 함수가 실행되는 것
    #이름을 입력 안 했을 때 => 객체가 만들어지지 않도록 해야합니다.	
        self.name = name
        self.age = age
        print("학생 {name}({age})) 가 태어났습니다.".format(
        	name=self.name,
            age=self.age
        ))
        
	# 자기 소개를 할 수 있다.
    def introduce(self):
    	print("안녕하세요. 저는 [campus]에 다니는 {age}살 {name}입니다.").format(
        	campus=self.__campus
            age=self.age,
            name=self.name
		))

lioliolio = Student("김태우", 31) #Student Class => 학생 객체
dir(lioliolio) # dir 이 어떤 명령어 인지 찾아보기
```

```python
# 직사각형 클래스 만들기

class Rectangle():

	def __init__(self, width, height):
    	self.width = width
        self.height = height
        
	def area(self):		# 면적
    	return self.width * self*height
        
    def girth(self): 	# 둘레
    	return 2 * (self.width + self.height)
        
    def is_bigger(self, another):
    	if self.area() - another.area() >= 0:
        	print("내가 큼")
        else:
        	print("내가 작음")

# Class (Rectangle) => 명세, 붕어빵틀, 이데아, ...
# 객체 (rec, rec1) => 실제 있는 애, 붕어빵, ...

rec = Rectangle(2, 3)
rec1 = Rectangle(4, 5)

rec1.is_bigger(rec)
```

```python
# 클래스를 만들고
# users.csv 파일의 내용을
# 객체형으로 리스트에 저장

# 답

class Student():
	
    def __init__(self, name, address):
    	self.name = name
        self.address = address
        
    def introduce(self):
    	print("저는 {address}에 살고 있는, {name}입니다.".format(
        address = self.address
        name = self.name
        ))
        
with open("../users.csv", "r") as f:
	student_list = [
    	Student(
        	line.split(",")[0],
            line.split(",")[1].replace("\n", "")
        )

        for line
        in f.readlines()
    ]
for student in student_list:
	student.introduce()
```

**파이썬 12일차**

```
디버깅 (Debugging) - "버그를 잡는다"" (de + bugg + ing)
오류 (errors)
예외 (Execptions), 처리 (Handling)
```
