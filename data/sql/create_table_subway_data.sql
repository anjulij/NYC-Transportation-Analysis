CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE subway_data (
    transit_timestamp TIMESTAMP,
    transit_mode TEXT,
    station_complex_id TEXT,  
    station_complex TEXT,
    borough TEXT,
    payment_method TEXT,
    fare_class_category TEXT,
    ridership INTEGER,
    transfers INTEGER,
    latitude FLOAT,
    longitude FLOAT,
    georeference GEOMETRY(Point, 4326)
);