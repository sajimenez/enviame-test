UPDATE employees e 
JOIN countries c ON e.country_id = c.id 
JOIN continents c2 ON c.continent_id = c2.id 
SET e.salary = e.salary + c2.anual_adjustment 
WHERE e.salary <= 5000;
