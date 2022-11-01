#튜플
tuple_data = ("a","b","c", "d", "e")
print(tuple_data[0], tuple_data[4])
print(tuple_data[1:])
#tuple_data[0] = "hi" // ERROR
#이유 : 튜플은 데이터 수정 및 삭제가 불가능하다, 중복 삽입이 가능하다


v1, v2, v3, v4 = 1, 2, 3, 4
v1, v2, v3, v4 = v4, v3, v2, v1
print(v1, v2, v3, v4)


#튜플 -> 리스트 -> 데이터추가 -> 튜플
list_data = list(tuple_data)
print(type(list_data))
list_data.append('hello!')
print(list_data)
tuple_data = tuple(list_data)
print(tuple_data)
print("----------")

#딕셔너리
dic = {'company' : '회사', 'apple' : '사과', 'face' : '얼굴', 'goverment' : '정부'}
dic_keys = [data for data in dic.keys()]
dic_values = [data for data in dic.values()]
print(dic_keys)
print(dic_values)
print("----------")

#키를 넣으면 값 출력
for data in dic.keys() :
    print ( data, ":", dic[data])   
print("----------")

#O 표시가 있는 값만 출력
dic = {'company' : ['회사', 'O'], 'apple' : ['사과', 'X'], 'face' : ['얼굴', 'O'], 'goverment' : ['정부','X']}

for data in dic.keys():
    if dic[data][1] == 'O':
        print(data, ":", dic[data][0])
print("----------")

#딕셔너리 합치기
dic_all = {'company' : '회사', 'apple' : '사과'}
dic2 = {'face' : '얼굴', 'goverment' : '정부'}
dic3 = {'dog' : '개'}

print(dic_all)
for data in dic2.keys():
    dic_all[data] = dic2[data]

for data in dic3.keys():
    dic_all[data] = dic3[data]

print(dic_all)
print("----------")


#집합
num_list = [5,1,2,2,3,3,4,5,5,6,6,6,7,8,9,9,10,11,11]
num_set = set(num_list)
print(num_set)