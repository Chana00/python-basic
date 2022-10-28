#반복문
#1에서 10까지 더하기
sum = 0
for num in range(1, 11):
    sum += num
print(sum)

#숫자를 입력받고 구구단 출력
dig = int(input())
for num in range (1, 10):
    print(dig, "x", num, "=", dig*num)

#반복문 + 문자열다루기
strings = "[Dave],[David],[Andy],[Arthor]"
print(strings)

for str in strings.split(","):
    print(str.strip("[]"))


#while
total, num = 0, 1
while num < 101:
    total += num
    num+= 1

print(total)

#비밀번호
password="4312"
data = str()

while data != password:
    data = input()
    if data == password:
        print("정답")
        break
    else:
        print("비밀번호가 틀렸습니다")


#다음 리스트에서 음수 삭제, 양수만 가진 리스트 만들기
num_list = [0, -1, 34, 7, -99, 83, -22, 5]
new_list = []

for num in num_list:
    if num >= 0:
        new_list.append(num)

print(new_list)

list_data = ["fun-coding", "Dave", "Linux", "python"]
for data in list_data:
    print(data + " is", len(data))


##역순 출력
data = [1,2,3,4,5,6,7,8,9,10]
data.reverse()
print(data)

#확장자 제거하고 이름만 출력
filelist = ['exec.docx','hello.py','code001.c','exec2.docx', 'myname.txt']

for f in filelist:
    print(f.split(".")[0])

#.txt인 파일 출력
for f in filelist:
    if f.split(".")[1] == "txt":
        print(f)

#원으로 바꿔서 계산
# 1달러 --> 1112원 , 1위안 ---> 171원으로 계산
prices = "100 위안"
price = prices.split()
if price[1] == "위안":
    print(int(price[0]) * 171, "원")
elif price[1] == "달러":
    print(int(price[0]) * 1112, "원")

#구구단 2 ~ 9단 출력
#단, 계산 값이 짝수인 경우만 출력
for i in range(2, 10) :
    for j in range (1, 9) :
        if i * j % 2 == 0 :
            print(i,"x", j, "=", i*j)
