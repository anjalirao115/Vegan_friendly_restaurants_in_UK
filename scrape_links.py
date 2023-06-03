#%%
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def collect_all_links(selenium_element_for_restaurant_list):
    ''' This function collects all links to individual restaurant '''

    print('Now collecting links for')

    list_of_dict = []           # empty list to collect dictionaries for all restaurants

    for restaurant in selenium_element_for_restaurant_list:
        dict = {}               # creating empty dict for each restaurant in loop
        
        link = restaurant.get_attribute('href')  # link collected

        # Extracing city names from links
        city_name = link[50:]

        if "England" in link :
            city = city_name[:-13]  #this is done becuase different counties have different num of characters

        if "Scotland" in link:
            city = city_name[:-14]

        if "South_Wales" in link:
            city = city_name[:-23]

        if "Ireland" in link:
            city = city_name[:-22]

        print(city)
        dict['city'] = city         # adding city data to dictionary
        dict['link'] = link         # adding link data to dictionary

        list_of_dict.append(dict)

    driver.quit()
    return list_of_dict


# Executing the code below to perform scrapping task            
if __name__ == '__main__':

    url = 'https://www.tripadvisor.co.uk/Restaurants-g186216-United_Kingdom.html'

    driver = webdriver.Firefox()
    driver.get(url)

    # Waiting for the Cookie frame to appear
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()

    # Locating links to all restaurants
    restaurant_list = driver.find_elements(by=By.XPATH, value='//body/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[2]/a')

    # collecting links to all restaurants
    list_of_dict = collect_all_links(restaurant_list)
    
    # writing the list of dictionary to a json file
    target_file = "data/city_link.json"
    with open(target_file, 'w') as fp:
        json.dump(list_of_dict, fp)