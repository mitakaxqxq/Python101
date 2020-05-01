SELECT s.`NAME`, c.`COUNTRY`, c.`NUMGUNS`, s.`LAUNCHED` 
FROM `SHIPS` s 
INNER JOIN `CLASSES` c ON c.`CLASS` = s.`CLASS`

SELECT s.`NAME`, c.`COUNTRY`, c.`NUMGUNS`, s.`LAUNCHED`, c.`CLASS`  
FROM `SHIPS` s  
LEFT OUTER JOIN `CLASSES` c ON c.`CLASS` = s.`CLASS` 
WHERE c.`CLASS` != s.`NAME`;

SELECT o.`SHIP`
FROM `OUTCOMES` o 
INNER JOIN `BATTLES` b ON b.`NAME` = o.`BATTLE`
WHERE b.`DATE` LIKE '1942%'

SELECT c.`COUNTRY`, s.`NAME` 
FROM `SHIPS` s 
INNER JOIN `CLASSES` c ON s.`CLASS` = c.`CLASS`
WHERE `NAME` IN 
(
    SELECT `SHIP` 
    FROM `OUTCOMES`
) 
ORDER BY c.`COUNTRY` 