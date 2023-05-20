#리스트와 곤련된 함수 &메서드
!추가, 빼기!

Arr = [10, 20, 30, 40, 50]
Arr.append(100)
'==>' [10, 20, 30, 40, 50, 100]

#백을 추가
Arr.pop()
'==>' [10, 20, 30, 40, 50]
#맨뒤에 있는것을 지움 또 반환을 하면서 뺀다
Arr.pop(2)
'==>' [10, 20, 40, 50]
#이럴떈 2번째 요소를 뺸다
Arr.insert(2, 500)
'==>' [10, 20, 500, 40, 50]
#Arr.insert(n, m ) 이라고하면 n은 n번째에 m의값 즉 m을넣는다

!정렬!
List = [5, 4, 3, 2, 1]
List.sort()
'==>' [1, 2, 3, 4, 5]
.#오름차순 정리
List0 = [5, 4, 3, 2, 1]
List0.sort(reverse=True)
.#내림차수 정리
."또는 "
List1 = [5, 4, 3, 2, 1]
List1.sort()
List1.reverse()
.'이렇게 사용해도 내림차순 정리가 된다'
.'어떤 리스트가 주어질때 그 리스트에서 n번쨰로 가자 큰값을 자져올떄 사용한다'

!sum, max, min, index, len!
List2 = [10, 30, 20, 4, 50]
print(sum(List2))
.'==>''114 즉 모두 더한값'
print(max(List2))
.'==>''50 즉 리스트의 요소중에 가장 큰값'
print(min(List2))
.'==>''4 즉 리스트의 요소중에 가장 작은값'
print(List2.index(n)))
.'==>''리스트에서 n 이 어느 번째 있는지 가져온다'
print(len(List2))
.'==>''5 즉 리스트의 길이 '

Arr1 = [10, 30, 20, 4, 50]
Arr2 = Arr1
Arr2[0] = 0
print(Arr)
.'==>0, 30, 20, 4, 50'
.'값만 복사하고 싶다면'
Arr1 = [10, 30, 20, 4, 50]
Arr2 = Arr1.copy() '-->이렇게 서야한다'
Arr2[0] = 0
print(Arr)

  