def palindrome(s):
    fact = s
    real_s = list(fact)
    print(real_s)
    n = 1
    x = 0
    y = 0
    s_list = []
    for q in range(len(real_s)):
        if real_s.pop(n - 1) == real_s.pop(-n):
            s_list.append(real_s.pop(-n))
            n += 1
        else:
            n += 1
    for j, k in zip(real_s, s_list):
        if j == k:
            x += 1
        else:
            y += 1
        
    if len(real_s) == x:
        return "True"

    else: 
        return "False"
s = input()
print(palindrome(s))