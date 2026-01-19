# 조건에 맞는 도서 리스트 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144853
# 작성자: 김형욱
# 작성일: 2026. 01. 19. 10:28:15

-- 코드를 입력하세요
SELECT
    BOOK_ID,
    date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book
where category = '인문'
    and PUBLISHED_DATE like '%2021%'
order by PUBLISHED_DATE asc;