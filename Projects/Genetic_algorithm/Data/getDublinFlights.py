import pandas as pd
from geopy.distance import geodesic
import os

dub_airport_coords = (53.4213, -6.2701)  
DISTANCE_THRESHOLD_KM = 50

input_file = "states_2018-05-28-22.csv"  
df = pd.read_csv(input_file)

df = df.dropna(subset=['lat', 'lon'])

approaching_planes = []

for icao24, plane_data in df.groupby('icao24'):
    plane_data_sorted = plane_data.sort_values('time')
    last_row = plane_data_sorted.iloc[-1]

    plane_pos = (last_row['lat'], last_row['lon'])
    
    if pd.isna(plane_pos[0]) or pd.isna(plane_pos[1]):
        continue

    distance_to_dub = geodesic(plane_pos, dub_airport_coords).km

    if distance_to_dub <= DISTANCE_THRESHOLD_KM:
        approaching_planes.append(icao24)

dub_flights_df = df[df['icao24'].isin(approaching_planes)]

output_file = "flights_to_dublin.csv"

if os.path.exists(output_file):
    dub_flights_df.to_csv(output_file, mode='a', index=False, header=False)
else:
    dub_flights_df.to_csv(output_file, index=False)

print(f"Inserted {len(approaching_planes)} flights into {output_file}.")