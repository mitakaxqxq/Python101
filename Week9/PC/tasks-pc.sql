SELECT AVG(speed) 
FROM pc

SELECT AVG(l.screen) 
FROM laptop l 
INNER JOIN product p ON l.model = p.model 
GROUP BY p.maker

SELECT AVG(speed) 
FROM (SELECT speed 
    FROM laptop 
    WHERE price > 1000)

SELECT AVG(price) 
FROM pc 
GROUP BY hd

SELECT AVG(price) 
FROM pc 
WHERE speed > 500 
GROUP BY speed

SELECT AVG(price) 
FROM pc p 
INNER JOIN product pr ON p.model = pr.model 
WHERE pr.maker = 'A'

SELECT AVG(price) 
FROM 
(SELECT l.price 
    FROM laptop l 
    JOIN product pr ON pr.model = l.model 
    WHERE pr.maker = 'B' 
    UNION ALL 
    SELECT p.price 
    FROM pc p
        JOIN product pr ON p.model = pr.model WHERE pr.maker ='B')

SELECT maker 
FROM product pr 
WHERE type = 'PC' 
GROUP BY pr.maker 
HAVING COUNT(model) >= 3

SELECT DISTINCT maker 
FROM product pr JOIN pc p ON pr.model = p.model 
WHERE p.price = (SELECT MAX(price) FROM pc)

SELECT AVG(hd) 
FROM pc p 
INNER JOIN product pr ON pr.model = p.model
WHERE pr.maker IN 
    (SELECT maker 
        FROM product 
        WHERE type = 'Printer')
