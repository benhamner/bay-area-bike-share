import pandas as pd

station = pd.read_csv("input/2015/201508_station_data.csv")
station.columns = ["id", "name", "lat", "long", "dock_count", "city", "installation_date"]
station.to_csv("output/station.csv", index=False)

status_2014_1 = pd.read_csv("input/201402_babs_open_data/201402_status_data.csv")
status_2014_2 = pd.read_csv("input/201408_babs_open_data/201408_status_data.csv")
status_2015   = pd.read_csv("input/2015/201508_status_data.csv")

status_columns = ["station_id", "bikes_available", "docks_available", "time"]
status_2014_1.columns = status_columns
status_2014_2.columns = status_columns
status_2015.columns   = status_columns

status = pd.concat([status_2014_1, status_2014_2, status_2015])
status.to_csv("output/status.csv", index=False)

trip_2014_1 = pd.read_csv("input/201402_babs_open_data/201402_trip_data.csv")
trip_2014_2 = pd.read_csv("input/201408_babs_open_data/201408_trip_data.csv")
trip_2015   = pd.read_csv("input/2015/201508_trip_data.csv")

trip_columns = ["id", "duration", "start_date", "start_station_name", "start_station_id", "end_date", "end_station_name", "end_station_id", "bike_id", "subscription_type", "zip_code"]
trip_2014_1.columns = trip_columns
trip_2014_2.columns = trip_columns
trip_2015.columns   = trip_columns

trip = pd.concat([trip_2014_1, trip_2014_2, trip_2015])
trip.to_csv("output/trip.csv", index=False)

weather_2014_1 = pd.read_csv("input/201402_babs_open_data/201402_weather_data.csv")
weather_2014_2 = pd.read_csv("input/201408_babs_open_data/201408_weather_data.csv")
weather_2015   = pd.read_csv("input/2015/201508_weather_data.csv")

weather_columns = ["date", "max_temperature_f", "mean_temperature_f", "min_temperature_f", "max_dew_point_f", "mean_dew_point_f", "min_dew_point_f", "max_humidity", "mean_humidity", "min_humidity", "max_sea_level_pressure_inches", "mean_sea_level_pressure_inches", "min_sea_level_pressure_inches", "max_visibility_miles", "mean_visibility_miles", "min_visibility_miles", "max_wind_Speed_mph", "mean_wind_speed_mph", "max_gust_speed_mph", "precipitation_inches", "cloud_cover", "events", "wind_dir_degrees", "zip_code"]
weather_2014_1.columns = weather_columns
weather_2014_2.columns = weather_columns
weather_2015.columns   = weather_columns

weather = pd.concat([weather_2014_1, weather_2014_2, weather_2015])
weather.to_csv("output/weather.csv", index=False)
