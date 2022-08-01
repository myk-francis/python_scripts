

-- CREATE TABLE manifest(
--     id SERIAL PRIMARY KEY,
--     device_id INT,
--     cargo_type TEXT,
--     load_point TEXT,
--     destination TEXT,
--     country TEXT,
--     transporter TEXT,
--     horse VARCHAR(10),
--     trailer_1 VARCHAR(10),
--     trailer_2 VARCHAR(10),
--     tag_request_date TIMESTAMP DEFAULT NULL,
--     tag_installation_date TIMESTAMP DEFAULT NULL,
--     trip_end_time TIMESTAMP DEFAULT NULL
-- );


-- CREATE TABLE history_tracking(
--     id SERIAL PRIMARY KEY,
--     horse VARCHAR(10),
--     speed FLOAT,
--     locate_type VARCHAR(10),
--     battery INT,
--     longitude FLOAT,
--     latitude FLOAT,
--     truck_location TEXT
-- );

-- CREATE TABLE device_list(
--     id SERIAL PRIMARY KEY,
--     device_id INT,
--     horse VARCHAR(10),
--     sim_card VARCHAR(25),
--     iccid VARCHAR(25)
-- );

-- CREATE TABLE route_tracking(
--     id SERIAL PRIMARY KEY,
--     horse VARCHAR(10),
--     device_id INT,
--     battery INT,
--     device_status VARCHAR(100),
--     device_location TEXT,
--     location_time TIMESTAMP,
--     speed FLOAT,
--     geo_fence TEXT,
--     date_from TIMESTAMP,
--     date_to TIMESTAMP,
--     distance FLOAT
-- );


-- CREATE TABLE alarms(
--     id SERIAL PRIMARY KEY,
--     horse VARCHAR(10),
--     alarm_type VARCHAR(100),
--     alarm_time TIMESTAMP,
--     longitude FLOAT,
--     latitude FLOAT,
--     locate_time TIMESTAMP,
--     speed FLOAT,
--     device_location TEXT
-- );