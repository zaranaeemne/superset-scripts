# To create and Seed data to the two tables in the dataset
# Important! Run this once only!!!!!
from typing import Text
import glob
from sqlalchemy.types import BigInteger, Text, DateTime, Boolean, Float, Integer
import healper

trips = glob.glob("data/biking_project/rides/*")
stations = glob.glob(
    "data/biking_project/station_metadata/metro-bike-share-stations-2021-07-01.csv")

station_schema = {
    "id": BigInteger,
    "name": Text,
    "go_live_on": DateTime,
    "region": Text,
    "status": Boolean,
}
log_data_schema = {
    "trip_id": BigInteger,
    "duration": Float,
    "start_time": DateTime,
    "end_time": DateTime,
    "start_station": Integer,
    "start_lat": Float,
    "start_lon": Float,
    "end_station": Integer,
    "end_lat": Float,
    "end_lon": Float,
    "bike_id": Text,
    "plan_duration": Float,
    "trip_route_category": Text,
    "passholder_type": Text,
}
station = healper.InjectorWithSchema()
station.data_injector(stations, "stations", station_schema, "replace")
logs = healper.InjectorWithSchema()
logs.data_injector(trips, "biking_data_logs", log_data_schema)
