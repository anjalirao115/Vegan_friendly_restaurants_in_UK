# Vegan friendly restaurants in UK Cities

The rise of Veganism in the UK has prompted restaurants to include vegan friendly options on
their menus. While some restaurants have adapted with great speed, others have lagged
behind. This task is about finding the UK cities that are most suitable for vegans to eat out in.

## Approach
To answer this question, I find the number of vegan friendly restaurants per capita in each of the top 20 UK cities listed on TripAdvisor. This scraped data is supplemented by the data on population in these top 20 cities.


## Milestone 1 : Data extraction : Scrape links from Trip Advisor website
### (code: scrape_links.py)

This code uses selenium firefox webdriver (geckodriver) in python to visit the TripAdvisor website. It first handles the cookie and then reads out the links to individual pages for Restaurants in UK's top 20 cities. The scraped data on cities and their links is saved in data/city_link.json .

## Milestone 2 : Data extraction : Scrape the number of vegan friendly restaurant for each city 
### (code: scrape_restaurant_number.py)

The code first reads in the file generated in the previos step. The links to the individual cities are read in loop and their geo-ids are extracted. These geo_ids are specific to cities and are further used in generating links where establishment type is set as restaurant and 'Vegan Options' is tick-marked in diet options. These new generated links are visited by the selenium webdriver and the number of vegan friendly restaurants is extracted and the data is saved in data/city_vegan_restaurant_data.csv .



## Milestone 3 : Data preparation: Merging the population data in cities with the above data 
### (code: gen_data_for_viz.py)

Now the data about vegan friendly restaurants is saved in one file (data/city_vegan_restaurant_data.csv) and the data about population in these cities is stored in another file (data/city_population_data.csv). The two files are merged together and another column is generated to find vegan friendly restaurants per capita. This final data file is saved in data/output.csv and is also used in Tableau to generate Visualization Dashboard.



## Milestone 4 : Data Visualization with Tableau 
### (Tableau workbook: tableau_viz_vegan_restaurants.twbx)

The data file output.csv is loaded in Tableau Desktop and four different worksheets are generated. All four diagrams explaining the outcomes are also shown in pdf file (tableau_viz_vegan_restaurants.pdf) for quick view. A full report in pdf format is also provided.

## Conclusion:

It is found that the maximum number of vegan friendly restaurants are present in London, however it is the city with the highest population as well. When the population in the cities is also considered, Brighton tops the list to offer the maximum vegan friendly restaurants per capita. The other cities closely following Brighton are York, Edinburgh and Newcastle. Bradford in the city which offers minimum number of vegan friendly restaurants per capita.

