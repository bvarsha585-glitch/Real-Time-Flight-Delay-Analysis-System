df = df.drop(['sensors','squawk','baro_altitude','geo_altitude','vertical_rate'], axis=1, errors='ignore')

df['callsign'] = df['callsign'].fillna("Unknown")
df['time_position'] = df['time_position'].fillna(df['last_contact'])
df['longitude'] = df['longitude'].fillna(0)
df['latitude'] = df['latitude'].fillna(0)
df['velocity'] = df['velocity'].fillna(df['velocity'].mean())

df['time_position'] = pd.to_datetime(df['time_position'], unit='s', errors='coerce')
df['last_contact'] = pd.to_datetime(df['last_contact'], unit='s', errors='coerce')

df['Departure_Delay_Minutes'] = (df['last_contact'] - df['time_position']).dt.total_seconds() / 60
df['Departure_Delay_Minutes'] = df['Departure_Delay_Minutes'].apply(lambda x: x if pd.notnull(x) and x > 0 else 0)


# Save the cleaned dataframe to a new CSV
df.to_csv("cleaned_flight_data.csv", index=False)
