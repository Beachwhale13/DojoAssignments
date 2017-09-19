SELECT countries.name, government_form FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE government_form = "Constitutional Monarchy"
AND life_expectancy > 75
AND countries.capital > 200
