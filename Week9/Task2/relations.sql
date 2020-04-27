SELECT m.name
FROM MOVIESTAR m
INNER JOIN STARSIN s ON m.name = s.starname
WHERE m.GENDER = 'M' AND s.movietitle = 'Terms of Endearment';

SELECT s.starname
FROM MOVIE m
INNER JOIN STARSIN s ON s.movietitle = m.title AND s.MOVIEYEAR = m.YEAR
WHERE m.studioname = 'MGM' AND m.year = 1995;

ALTER TABLE STUDIO
ADD COLUMN president VARCHAR(255);

UPDATE STUDIO
SET president = 'Barack Obama'
WHERE name = 'MGM';

UPDATE STUDIO
SET president = 'Donald Trump'
WHERE name = 'USA Entertainm.';

SELECT president
FROM STUDIO
WHERE name = 'MGM';

