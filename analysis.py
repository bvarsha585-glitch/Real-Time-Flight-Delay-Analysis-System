df["delay_flag"] = ((df["on_ground"] == False) & (df["velocity"] < 50)).astype(int)
ground_delay = df[df["on_ground"] == True]["delay_flag"]
air_delay = df[df["on_ground"] == False]["delay_flag"]

print("Mean On-Ground Delay:", ground_delay.mean())
print("Mean In-Air Delay:", air_delay.mean())

df.groupby('on_ground')['velocity'].mean()

if ground_delay.mean() > air_delay.mean():
    print("On-ground delays are higher than in-air delays")
else:
    print("In-air delays are higher")


import matplotlib.pyplot as plt
plt.hist(
    df['Departure_Delay_Minutes'],
    bins=5,
    color='skyblue',
    edgecolor='black'
)
plt.title("Departure Delay Distribution")
plt.xlabel("Delay Minutes")
plt.ylabel("Number of Flights")
plt.show()



# 2-Top Countries by Flight Count (Bar Chart)
df['origin_country'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title("Top 10 Countries by Number of Flights")
plt.xlabel("Country")plt.ylabel("Flights Count")plt.xticks(rotation=45)plt.show()



# Separate data
air = df[df['on_ground'] == False]
ground = df[df['on_ground'] == True]
# Scatter plot with different colors
plt.scatter(air['longitude'], air['latitude'], label='In Air', alpha=0.6)
plt.scatter(ground['longitude'], ground['latitude'], label='On Ground', alpha=0.8)
plt.title("Flight Positions Across Globe")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.show()