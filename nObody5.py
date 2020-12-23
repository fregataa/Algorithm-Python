# C5
def count(input_string: str):
    # 숫자의 갯수, 알파벳의 갯수, 공백의 갯수, 기타 문자의 갯수를 선언합니다.
    digit, alpha, blank, etc = 0, 0, 0, 0

    # 입력받은 문자열을 반복문으로 하나하나 숫자인지 알파벳인지 공백인지 등등을 비교합니다.
    # 그리고 해당하는 갯수의 카운트를 증가시켜줍니다.
    for munja in input_string:
        if munja.isdigit():
            digit += 1
        elif munja.isalpha():
            alpha += 1
        elif munja == ' ':
            blank += 1
        else:
            etc += 1
        
    # 결과를 튜플로 묶어서 반환합니다.
    return (digit, alpha, blank, etc)

# count 함수를 실행해봅니다.
print(count("Hello, today... I am happy. 2020-12-14"))



