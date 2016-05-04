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

ex)  
a = 3  
b = 8  

```python
def test():
	pass
```
if a > b
