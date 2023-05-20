N = int(input())
for i in range(N):
    word = input("단어를 입력하세요: ")
    # 스택과 큐를 구현하기 위해 리스트를 사용합니다.
    stack = []
    queue = []
# 단어를 스택과 큐에 추가합니다.
    for char in word:
        stack.append(char)
        queue.append(char)

    # 스택과 큐에서 문자를 하나씩 꺼내서 비교합니다.
    while len(stack) > 0:
        if stack.pop() != queue.pop(0):
            print("회문이 아닙니다.")
            break
    else:
        print("회문입니다!")