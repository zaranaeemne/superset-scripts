# This script is to get Station Details from Live API
import pandas as pd
import healper
from sqlalchemy.types import BigInteger, Text, Boolean, Float, Integer

station_properties_schema = {
    "addressStreet": Text,
    "addressCity": Text,
    "addressState": Text,
    "addressZipCode": Text,
    "bikesAvailable": Integer,
    "closeTime": Text,
    "docksAvailable": Integer,
    "eventEnd": Boolean,
    "eventStart": Boolean,
    "isEventBased": Boolean,
    "isVirtual": Boolean,
    "isVisible": Boolean,
    "kioskId": BigInteger,
    "kioskPublicStatus": Boolean,
    "kioskStatus": Text,
    "name": Text,
    "notes": Text,
    "openTime": Text,
    "publicText": Text,
    "timeZone": Text,
    "totalDocks": Integer,
    "trikesAvailable": Integer,
    "kioskConnectionStatus": Boolean,
    "kioskType": Integer,
    "latitude": Float,
    "longitude": Float,
    "hasGeofence": Boolean,
    "classicBikesAvailable": Integer,
    "smartBikesAvailable": Integer,
    "electricBikesAvailable": Integer,
    "isArchived": Boolean,
    "clientVersion": Text,
}

# data = glob.glob("data/biking_project/station_metadata/data-2021-08-07.json")
df = pd.read_json("data/biking_project/station_metadata/data-2021-08-07.json")[
    "features"
]
list = []
for data in df:
    list.append(data["properties"])

station_metadata = healper.InjectorWithSchema()

station_metadata.data_list_injector(
    list, 'station_metadata', station_properties_schema)
