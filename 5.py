cnt = int(input())

for i in range(cnt):
    status = False # 점검이 끝났는지 확인하는 변수
    stack = []

    data = input()
    for v in data:
        if v == '(':
            stack.append(v)
        else:
            if len(stack) == 0:
                status = True
                print("NO")
                break
            else:
                stack.pop()

    if not status: # if 조건절 => 조건이 뭐가됐든 무조건 True
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")

