# 피자 나눠 먹기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 알고리즘: 기초
# 작성자: 김형욱
# 작성일: 2026. 02. 05. 15:54:04

def solution(n):
    answer = n // 7
    if n % 7 != 0:
        answer += 1
    return answer