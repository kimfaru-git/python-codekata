# 인기있는 아이스크림
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133024
# 작성자: 김형욱
# 작성일: 2026. 01. 19. 10:19:35

-- 코드를 입력하세요
SELECT
    flavor
from first_half
order by total_order desc, shipment_id asc;