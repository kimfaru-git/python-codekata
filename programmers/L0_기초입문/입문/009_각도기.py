# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 김형욱
# 작성일: 2026. 01. 21. 11:29:32

def solution(angle):
    if angle < 90 and angle > 0:
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    elif angle == 180:
        return 4
    else:
        print("0도 초과 180이하의 값을 입력하세요")
