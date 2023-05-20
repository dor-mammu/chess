# 링크드리스트 머라고?
# => 우와... 머라고요?
# => 머가? 리스트가 연결되어있는데 하나는 뭐들어간ㄷ 데이터, 나머지하나?
# => null or 그다음에 연결될 리스트의 메모리주소 주소도되고여 ㅇㅋ

class chess:
    def __init__(self, data, node=None) -> None:
        # 하나는 데이터
        self.data = data
        self.node = node

    def chess2(self):
        print(f"현재 데이터: {self.data}\n다음 노드: {self.node}")


a = chess('chess체스') # [jfkladf | None]
b = chess('chess2체스2') # [dfjaklfda | None]
a.chess2()
b.chess2()

# b -> a
a.node = b
a.chess2()

# 유닛테스트Unit test => 큰 프로젝트나 협업을할때 쓰는 건데
# => 그냥 print() -> 테스트 자료를 통일화할려고 => 적어도 이런 상황은 
# 무조건 됨
# assert

# assert 조건, 출력할 문장
# 1 , 2 => assert 1 == 2, "ㄹ어마ㅣ러ㅏㅣ"
assert 1 == 1, "abc" # => 틀린지 아닌지만 확인하는거

