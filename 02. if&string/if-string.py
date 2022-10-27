#각 데이터 타입 출력하기
digit1_1 = 10
digit1_2 = 2.2
str1_1 = "fun-coding"

print(type(digit1_1))
print(type(digit1_2))
print(type(str1_1))

#조건문 - 두개의 숫자를 입력받은 후 더 큰 숫자 화면에 출력
print("정수 입력 x 2")
dig2_1 = input()
dig2_2 = input()

if dig2_1 > dig2_2:
    print(dig2_1)
elif dig2_1 < dig2_2:
    print(dig2_2)

#입력받은 숫자가 짝수인지 홀수인지 출력
print("정수 입력")
dig3 = int(input())
if dig3 % 2 == 0:
    print("짝수")
else:
    print("홀수")

#주민번호를 입력받아 출생연도 출력, 뒷자리 맨 앞 숫자 출력
print("주민등록번호 입력")
persID = input()
print(persID[0:2])
print(persID[7])
if persID[7] == ("1" or "3"):
    print("남성")
elif persID[7] == ("2" or "4"):
    print("여성")

#문자열 파트
#strip : 양옆 문자열 제거 ( lstrip과 rstrip도 존재)
mystr = " a man goes into the room..."
print(mystr)
print(mystr.strip("."))

mystr2 = "      a man goes \n    into the room...      \n"
print(mystr2)
print(mystr2.strip(" \n"))

#count : 빈도수
python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes cod readability, notably using significant whitespace."
print(python_desc.count("Python"))

#문자열 인덱싱
#find
letters = input()

if letters.find("n") >= 0:
    print("n이 들어있습니다.")
else:
    print("n이 안들어있습니다.")

#주민번호 출생지역 코드 분리
# 00 ~ 08 서울
# 09 ~ 12 부산
num = "991012-1012232"
code = int(num[8:10])
print(code)

if(code >= 0 and code <= 8):
    print("서울")
elif (code >= 9 and code <= 12):
    print("부산")

#split
letters= "Dave, David, Andy, 222, 33331, Hello"
letter_list = letters.split(",")

print(letter_list)
for letter in letter_list :
    print(letter)

#split 예시2
filename = 'exercise01.docx'
print(filename.split(".")[0])