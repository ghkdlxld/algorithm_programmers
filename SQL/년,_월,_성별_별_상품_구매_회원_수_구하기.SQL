# 한사람의 구매기록이 많을 수 있으므로 DISTINCT 해준다
SELECT YEAR(os.SALES_DATE) AS YEAR, MONTH(os.SALES_DATE) AS MONTH, ui.GENDER, COUNT(DISTINCT os.USER_ID)
FROM ONLINE_SALE os JOIN USER_INFO ui
ON os.USER_ID = ui.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER;