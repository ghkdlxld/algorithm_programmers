SELECT info.INGREDIENT_TYPE, SUM(fh.TOTAL_ORDER)
FROM FIRST_HALF fh JOIN ICECREAM_INFO info
ON fh.FLAVOR = info.FLAVOR
GROUP BY info.INGREDIENT_TYPE;