#%% 
import csv
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Extracting list of dictionaries from json file
with open("data/city_link.json", "r") as file:
    list_of_dict = json.load(file)

updated_list_of_dict = []  #another key value pair for vegan restaurant will be added to these dictionaries

for idx, dict in enumerate(list_of_dict):
    city = dict['city']
    link = dict['link']
    geo_id = link[43:49]    #different geo_ids identify different cities

    # these links have Vegan options tick-marked and establishment type set as restaurant
    vegan_link = f"https://www.tripadvisor.co.uk/FindRestaurants?geo={geo_id}&diets=10697&establishmentTypes=10591&broadened=false"

    driver = webdriver.Firefox() 
    driver.get(vegan_link)

    # accepting the cookie
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()

    # finding the number of vegan friendly restaurants
    vegan_restaurant = driver.find_element(By.XPATH, '//span[@class="b"]').text
    print(f"{city} has {vegan_restaurant} vegan friendly restaurants")
 
    # adding another key value pair to dict for vegan friendly restaurant
    dict["vegan_restaurant"] = int(vegan_restaurant)
    
    updated_list_of_dict.append(dict)

    driver.quit()
    time.sleep(25)

# writing the dictionary data as csv file
csv_columns = ['city','vegan_restaurant','link']

csv_file = "data/city_vegan_restaurant_data.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in updated_list_of_dict:
        writer.writerow(data)



# %%
