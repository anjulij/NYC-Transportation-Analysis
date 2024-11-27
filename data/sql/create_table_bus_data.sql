CREATE TABLE bus_data (
    RecordedAtTime TIMESTAMP,
    DirectionRef INTEGER,
    PublishedLineName TEXT,
    OriginName TEXT,
    OriginLat FLOAT,
    OriginLong FLOAT,
    DestinationName TEXT,
    DestinationLat FLOAT,
    DestinationLong FLOAT,
    VehicleRef TEXT,
    VehicleLocation_Latitude FLOAT,
    VehicleLocation_Longitude FLOAT,
    NextStopPointName TEXT,
    ArrivalProximityText TEXT,
    DistanceFromStop INTEGER,
    ExpectedArrivalTime TIMESTAMP,
    ScheduledArrivalTime TIME
);