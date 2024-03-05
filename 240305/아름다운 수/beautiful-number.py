# 해당 숫자만큼 연달아 나오면 아름다운수

# 동일한 숫자에 대해 연달아 같은 숫자의 묶음이 나온것도 아름다운수
# 22 + 22 는 가능 22 + 2는 불가능

# 하나씩 보되 가망이 없는 애들은 쳐내기

N = int(input())

word = [] 

def check():
    idx = 0

    while idx < N:
        num = word[idx]
        isSame = True

        for j in range(idx, idx+num):
            if j >= N:
                return False
                break
            if word[j] != num:
                isSame = False
        
        if isSame:
            idx += num
        else:
            return False

    return True

answer = 0

def recursive():
    global answer

    if len(word) == N:
        # print(word, check())
        if check():
            # print(word)
            answer += 1
        return

    for i in range(1, 5):
        word.append(i)
        recursive()
        word.pop()

recursive()

print(answer)