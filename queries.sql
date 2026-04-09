SELECT * FROM flight_db.flight_data;

ALTER TABLE flight_data
ADD COLUMN delay_flag INT;

SELECT MIN(velocity), MAX(velocity), AVG(velocity)
FROM flight_data;

#update
SET SQL_SAFE_UPDATES = 0;


UPDATE flight_data
SET delay_flag = CASE 
    WHEN on_ground = FALSE AND velocity < 50 THEN 1
    ELSE 0
END;
# Flights with Delay Greater than Average
SELECT *
FROM flight_data
WHERE delay_flag > (
    SELECT AVG(delay_flag) FROM flight_db.flight_data
);

## Country-wise Average Delay
SELECT origin_country, AVG(delay_flag) AS avg_delay
FROM flight_db.flight_data
GROUP BY origin_country
ORDER BY avg_delay DESC;

SELECT COUNT(*) AS delayed_on_ground
FROM flight_data
WHERE on_ground = TRUE AND delay_flag = 1;

## High-Speed Flights
SELECT *FROM flight_data
WHERE velocity > (
    SELECT AVG(velocity) FROM flight_data
);
## Real-Time Country-wise Delays (Last 1 Hour)
SELECT origin_country,
COUNT(*) AS total_flights,
SUM(CASE WHEN velocity < 50 AND on_ground = FALSE THEN 1 ELSE 0 END) AS delayed_flights
FROM flight_data WHERE collected_time >= NOW() - INTERVAL 1 HOUR
GROUP BY origin_country ORDER BY delayed_flights DESC;

## On-Ground Delayed Flights
SELECT on_ground, COUNT(*) AS total
FROM flight_data
GROUP BY on_ground;