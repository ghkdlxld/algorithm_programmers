SELECT ao.ANIMAL_ID, ao.NAME 
FROM ANIMAL_OUTS ao JOIN ANIMAL_INS ai
ON ao.ANIMAL_ID = ai.ANIMAL_ID
WHERE ao.DATETIME < ai.DATETIME
ORDER BY ai.DATETIME;

