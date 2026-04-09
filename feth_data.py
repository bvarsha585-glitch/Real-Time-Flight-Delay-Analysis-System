
url = "https://opensky-network.org/api/states/all"

headers = {
    "User-Agent": "Mozilla/5.0"
}
all_data = []
for i in range(60):
    print("Collecting batch", i + 1)

    try:
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200 and response.text.strip():
            data = response.json()

            if "states" in data and data["states"] is not None:
                df = pd.DataFrame(
                    data["states"],
                    columns=[
                        "icao24","callsign","origin_country","time_position",
                        "last_contact","longitude","latitude","baro_altitude",
                        "on_ground","velocity","true_track","vertical_rate",
                        "sensors","geo_altitude","squawk","spi","position_source"
                    ]
                )

                df["collected_time"] = datetime.now(timezone.utc)
                all_data.append(df)

                print("Rows:", len(df))
            else:
                print("No data in this batch")

         else:
            print("API returned empty response")

    except Exception as e:
        print("Error:", e)

    time.sleep(60)

# Combine
final_df = pd.concat(all_data, ignore_index=True)
print("TOTAL ROWS:", final_df.shape)
final_df.to_csv("flight_data.csv", index=False)
