# 세균 증식
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 알고리즘: 기초
# 작성자: 김형욱
# 작성일: 2026. 02. 06. 19:42:49

def solution(n, t):
    answer = n
    for i in range(1, t+1):
        answer = answer * 2
    return answer
