

-- CREATE TABLE manifest(
--     id SERIAL PRIMARY KEY,
--     device_id TEXT,
--     cargo_type TEXT,
--     load_point TEXT,
--     destination TEXT,
--     country TEXT,
--     transporter TEXT,
--     horse TEXT,
--     trailer_1 TEXT,
--     trailer_2 TEXT,
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
--     device_id TEXT,
--     horse TEXT,
--     sim_card TEXT,
--     iccid TEXT
-- );

-- CREATE TABLE route_tracking(
--     id SERIAL PRIMARY KEY,
--     horse TEXT,
--     device_id TEXT,
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
--     horse TEXT,
--     alarm_type VARCHAR(100),
--     alarm_time TIMESTAMP,
--     longitude TEXT,
--     latitude TEXT,
--     locate_time TIMESTAMP,
--     speed FLOAT,
--     device_location TEXT
-- );


-- CREATE TABLE alarms(
--     id SERIAL PRIMARY KEY,
--     rec_date  DATE NOT NULL DEFAULT CURRENT_DATE,
--     home TEXT,
--     away TEXT,
--     home_goals INT,
--     away_goals INT,
--     first_half_goals INT,
--     sec_half_goals INT,
--     total_goals INT,
--     match_result TEXT,
--     bet_value TEXT,
--     over_under TEXT,
--     bet_win_lose TEXT,
-- );
