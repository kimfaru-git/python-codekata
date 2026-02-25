# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 김형욱
# 작성일: 2026. 02. 25. 14:25:48

def solution(s1, s2):
    answer = 0
    for i1 in s1:
            if i1 in s2:
                answer += 1
    return answer