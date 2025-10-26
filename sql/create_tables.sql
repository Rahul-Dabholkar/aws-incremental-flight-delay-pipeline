-- Create schema for the project
CREATE SCHEMA PROJECT1_AIRLINES;

-- Create the airports dimension table
CREATE TABLE project1_airlines.airports_dim(
    airport_id BIGINT,
    city VARCHAR(100),
    state VARCHAR(100),
    name VARCHAR(100)
)

-- Create the flights fact table
CREATE TABLE project1_airlines.daily_flights_fact (
    carrier VARCHAR(10),
    dep_airport VARCHAR(200),
    arr_airport VARCHAR(200),
    dep_city VARCHAR(100),
    arr_city VARCHAR(100),
    dep_state VARCHAR(100),
    arr_state VARCHAR(100),
    dep_delay BIGINT,
    arr_delay BIGINT
);