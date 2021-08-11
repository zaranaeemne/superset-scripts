import healper

sql_statement_station_data = """ CREATE OR REPLACE VIEW view_station_data AS
select sm.* from stations as s 
left outer join station_metadata as sm on s.id=sm."kioskId"
order by sm."kioskId"
"""
a = healper.CreateView(sql_statement_station_data)
a.view_creator()

sql_statement_data_view = """
CREATE OR REPLACE VIEW view_reporting_log_data AS
SELECT    
    vsd_start."addressStreet" as "start_address",
    vsd_start."addressCity" as "start_city",
    vsd_start."addressState" as "start_state",
    vsd_start."addressZipCode" as "start_code",
    vsd_start."bikesAvailable" as "bikes_at_start_station",
    vsd_start."docksAvailable" as "docks_at_start_station",
    vsd_start."kioskId" as "start_station_id",
    vsd_start."name" as "start_station_name",
    vsd_start."totalDocks" as "start_capacity",
    vsd_start."trikesAvailable" as "start_trikes",
    vsd_start."kioskType" as "start_station_type",
    vsd_start."latitude" as "start_station_lat",
    vsd_start."longitude"  as "start_station_long",
    vsd_start."hasGeofence" as "start_station_geo",
    vsd_start."classicBikesAvailable" as "start_classical_start_bikes",
    vsd_start."smartBikesAvailable" as "start_smart_bikes",
    vsd_start."electricBikesAvailable"  as "start_electric_bikes",
    vsd_end."addressStreet" as "end_address",
    vsd_end."addressCity" as "end_city",
    vsd_end."addressState" as "end_state",
    vsd_end."addressZipCode" as "end_code",
    vsd_end."bikesAvailable" as "bikes_at_end_station",
    vsd_end."docksAvailable" as "docks_at_end_station",
    vsd_end."kioskId" as "end_station_id",
    vsd_end."name" as "end_station_name",
    vsd_end."totalDocks" as "end_capacity",
    vsd_end."trikesAvailable" as "end_trikes",
    vsd_end."kioskType" as "end_station_type",
    vsd_end."latitude" as "end_station_lat",
    vsd_end."longitude"  as "end_station_long",
    vsd_end."hasGeofence" as "end_station_geo",
    vsd_end."classicBikesAvailable" as "end_classical_end_bikes",
    vsd_end."smartBikesAvailable" as "end_smart_bikes",
    vsd_end."electricBikesAvailable"  as "end_electric_bikes",
     bdl.*
FROM biking_data_logs AS bdl
INNER JOIN view_station_data AS vsd_start ON vsd_start."kioskId"=bdl.start_station
INNER JOIN view_station_data AS vsd_end ON vsd_end."kioskId"=bdl.end_station
ORDER BY trip_id DESC
"""

b = healper.CreateView(sql_statement_data_view)
b.view_creator()
