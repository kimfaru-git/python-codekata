# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 김형욱
# 작성일: 2026. 02. 09. 15:06:17

def solution(numbers):
    answer = sorted(numbers)[-1:-3:-1]
    answer = answer[0] * answer[1]
    return answer