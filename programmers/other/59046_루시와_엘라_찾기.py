# 루시와 엘라 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59046
# 작성자: 김형욱
# 작성일: 2026. 01. 19. 10:21:48

-- 코드를 입력하세요
SELECT
    animal_id,
    name,
    sex_upon_intake
from animal_ins
where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by animal_id asc;