WITH GROUP_LIST AS (
    SELECT MCDP_CD AS "진료과코드"
        , COUNT(1) AS "5월예약건수"
    FROM APPOINTMENT
    WHERE 1=1
    -- AND APNT_CNCL_YN = 'N'
    AND TO_CHAR(APNT_YMD, 'YYYYMM') = '202205'
    GROUP BY MCDP_CD
)
SELECT *
FROM GROUP_LIST
ORDER BY "5월예약건수", "진료과코드"