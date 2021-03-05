# 평점 계산 함수
def grade_average_calculator():
    # 과목 갯수 입력
    number = int(input("과목 갯수를 입력하세요 : "))

    # while문 루프 돌리기위한 변수 i 할당
    # 등급을 매기기위한 빈리스트 생성
    i = 1
    grades_list = []
    score_dict = {
        'A+': 4.5,
        'A': 4.0,
        'B+': 3.5,
        'B': 3.0,
        'C': 2.5,
        'F': 0
    }

    # while문 돌면서 과목 점수를 받아서 등급으로 변환 후 grades_list에 추가
    while i <= number:
        score = input("점수를 입력하시오 : ")
        if score == 'q':
            break
        score = int(score)
        if score > 94:
            grades_list.append('A+')
        elif score > 89:
            grades_list.append('A')
        elif score > 84:
            grades_list.append('B+')
        elif score > 79:
            grades_list.append('B')
        elif score > 69:
            grades_list.append('C')
        else:
            grades_list.append('F')
        i += 1

    # 점수별 학점 계산
    result = 0
    for i in grades_list:
        result += score_dict[i]

    # 평균 학점 계산
    result = round((result / number), 1)

    return f"등급 : {grades_list}\n평점 : {result}"

# Test
print(grade_average_calculator())