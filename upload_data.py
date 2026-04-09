df.to_sql(
    name='flight_data',
    con=engine,
    if_exists='append',
    index=False
)