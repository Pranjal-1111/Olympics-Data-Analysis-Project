
-- Create table
CREATE TABLE olympics_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INT,
    city TEXT,
    sport TEXT,
    discipline TEXT,
    event TEXT,
    athlete TEXT,
    gender CHAR(1),
    country TEXT,
    medal TEXT
);

-- Sample data
INSERT INTO olympics_data (year, city, sport, discipline, event, athlete, gender, country, medal) VALUES
(2008, 'Beijing', 'Aquatics', 'Swimming', '100m Freestyle', 'Michael Phelps', 'M', 'United States', 'Gold'),
(2004, 'Athens', 'Athletics', 'Athletics', 'Marathon', 'Stefano Baldini', 'M', 'Italy', 'Gold');

-- Top 5 countries
SELECT country, COUNT(*) AS total_medals
FROM olympics_data
WHERE medal IS NOT NULL
GROUP BY country
ORDER BY total_medals DESC
LIMIT 5;

-- Gender distribution
SELECT gender, COUNT(*) FROM olympics_data GROUP BY gender;

-- Medals by year
SELECT year, COUNT(*) FROM olympics_data
WHERE medal IS NOT NULL
GROUP BY year
ORDER BY year;
