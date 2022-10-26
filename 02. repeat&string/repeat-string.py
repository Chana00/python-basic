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