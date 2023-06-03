#%%
import pandas as pd

# reading in the data on vegan friendly restaurants in different cities
df_1 = pd.read_csv("data/city_vegan_restaurant_data.csv")

# reading in the data on population in different cities
df_2 = pd.read_csv("data/city_population_data.csv")

# reading into variables
city                = df_1['city']
vegan_restaurant    = df_1['vegan_restaurant']
population_2023     = df_2['population_2023']
lat                 = df_2['lat']
long                = df_2['long']
vegan_restaurant_per_capita = vegan_restaurant/population_2023

# defining a combined dataframe
df = pd.DataFrame({ 'city': city, 'vegan_restaurant': vegan_restaurant,  'population_2023': population_2023,
                   'vegan_restaurant_per_capita': vegan_restaurant_per_capita, 'lat': lat, 'long': long })

# writing the combined dataframe to csv file
df.to_csv('data/ooutput.csv', index=False)
# %%
