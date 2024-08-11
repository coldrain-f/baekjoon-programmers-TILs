-- 5월 예약건수는 예약 취소도 포함한 건수?
WITH GROUP_LIST AS (
    SELECT MCDP_CD AS "진료과코드"
        , COUNT(1) AS "5월예약건수"
    FROM APPOINTMENT
    WHERE 1=1
    AND (YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5)
    GROUP BY MCDP_CD
)
SELECT *
FROM GROUP_LIST
ORDER BY 5월예약건수, 진료과코드