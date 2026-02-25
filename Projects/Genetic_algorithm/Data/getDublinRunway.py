import pandas as pd

input_file = "runways.csv"  
df = pd.read_csv(input_file)

dub_airport_df = df[df['airport_ident'] == 'EIDW']

output_file = "dublin_runways.csv"
dub_airport_df.to_csv(output_file, index=False)

print(f"Filtered {len(dub_airport_df)} rows for Dublin Airport. Saved to {output_file}.")