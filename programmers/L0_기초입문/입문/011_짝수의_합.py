# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 김형욱
# 작성일: 2026. 02. 04. 12:23:37

def solution(n):
    a = n // 2
    total = 0
    for i in range(1, a+1):
        b = i * 2
        total += b
    return total