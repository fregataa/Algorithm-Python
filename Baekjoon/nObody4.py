# C4

# 정답 문자열을 선언합니다.
answer = ""

# 문자열을 입력받습니다.
print("문자열을 입력하시오: ")
input_string = input()

# 입력받은 문자열을 공백을 기준으로 나누어 리스트 형태로 만듭니다.
words = input_string.split()

# 공백으로 나누어진 문자열은 단어 리스트가 됩니다.
# 각 단어의 첫 글자를 대문자로 만들어서 붙여주고 점(.)을 붙입니다.
for word in words:
    answer = answer + word[0].upper() + '.'

# 정답 문자열을 출력합니다.
print(answer)
