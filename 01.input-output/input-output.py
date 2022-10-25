print ("Hello World! \nYEWON's python basic studying for algorithm!")

#print 함수로 숫자 소수점 두 자리 까지만 출력
digit = 3.141592
print ("%.2f" % digit)

#사용자로부터 두 개의 숫자를 입력 받고 더한 값 출력
print("정수 입력 x2")
input01 = input()
input02 = input()
print (int(input01) + int(input02))

#문자열과 반복횟수를 입력받아 출력
print("문자열 & 반복횟수 입력")
inString = input()
inRepeat = input()
for i in range(int(inRepeat)):
    print(inString)

#문자열 '720'을 정수형으로 변환하기, 정수 100을 문자열 '100'으로 변환하기
str1 = "720"
dig1 = 100

print(int(str1))
print(str(dig1))

#두 개의 숫자 입력받아 사칙연산하기
print("두 개의 값을 입력받아 사칙연산 + 거듭제곱")
calcDig1 = input()
calcDig2 = input()
print ("덧셈 " + str(int(calcDig1) + int(calcDig2)))
print ("뺄셈 " + str(int(calcDig1) - int(calcDig2)))
print ("곱셈 " + str(int(calcDig1) * int(calcDig2)))
print ("나눗셈 " + str(int(calcDig1) / int(calcDig2)))
print ("거듭제곱 ", int(calcDig1) ** int(calcDig2))     # 이런 방식도 가능

#format() 함수를 이용한 프로그램 출력
print('{0} % {1} = {2}'.format(int(calcDig1), int(calcDig2), int(calcDig1) % int(calcDig2)))

