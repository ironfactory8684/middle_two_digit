def look_and_say(n):
    # 첫 항은 '1'
    result = "1"
    for _ in range(1, n):
        new_result = ""
        i = 0
        while i < len(result):
            # 현재 숫자와 연속되는 숫자의 개수를 센다
            count = 1
            while i + 1 < len(result) and result[i] == result[i + 1]:
                i += 1
                count += 1
            new_result += str(count) + result[i]
            i += 1
        result = new_result
    return result

def middle_two_digits(n):
    # n번째 Look and Say 수열의 항을 찾는다
    term = look_and_say(n)
    # 가운데 두 자릿수를 찾는다
    mid_index = len(term) // 2
    # 수열의 길이가 짝수인 경우
    if len(term) % 2 == 0:
        return term[mid_index - 1:mid_index + 1]
    # 홀수인 경우 주변 두 숫자를 선택
    else:
        return term[mid_index - 1:mid_index + 2]

# 사용자 입력
def run():
    while True:
        input_str = input("Enter a number (or 'exit' to quit): ")
        if input_str.lower() == 'exit':
            print("Exiting...")
            break
        try:
            number = int(input_str)
            print("Result:", middle_two_digits(number))
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    run()
