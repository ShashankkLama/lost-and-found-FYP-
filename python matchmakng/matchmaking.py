# Importing required libraries
import numpy as np 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import random 
from sklearn.neighbors import NearestNeighbors

# Loading the dataset
df = pd.read_csv("fypdata.csv")

# Displaying information about the dataset
df.info()

# Displaying the first few rows of the dataset
df.head()

# Reading modified data for lost and found items
lostitems= pd.read_csv("fypdata_modified.csv") 
founditems= pd.read_csv("fypdata_modified.csv")

# Generating random lost locations for each lost item
lost_locations = ["kumari hall", "nepal block", "london block", "alumni building", "brit house"]
for i in range(len(lostitems)):
    random_location = random.choice(lost_locations)
    lostitems.loc[i, 'lost locations'] = random_location
    
# Saving the modified lost items data with random locations
lostitems.to_csv("fypdata_modified_with_lost_locations.csv", index=False)
print(lostitems.head())

# Generating random found locations for each found item
found_locations = ["kumari hall", "nepal block", "london block", "alumni building", "brit house"]
for i in range(len(founditems)):
    random_location = random.choice(found_locations)
    founditems.loc[i, 'found locations'] = random_location
    
    # Displaying the first few rows of found items data
    print(founditems.head())
    
# Dropping duplicate found items
found_items=founditems.drop_duplicates()
found_items

# Dropping duplicate lost items
lost_items= lostitems.drop_duplicates()
lost_items

# Resetting index for lost items
lost_items.reset_index(drop=True, inplace=True)
lost_items

# Resetting index for found items
found_items.reset_index(drop=True, inplace=True)
found_items

# Function to match lost items with found items
def matchmaker(row):
    # Extracting values from each row
    brand_1 = row['brand']
    manufacturer_1 = row['manufacturer']
    category_1 = row['categories']
    lost_location = row['lost locations']
    
    # Checking if there is a corresponding row in found_items that matches the criteria
    matching_row = found_items[
        (found_items['brand'] == brand_1) &
        (found_items['manufacturer'] == manufacturer_1) &
        (found_items['categories'] == category_1) &
        (found_items['found locations'] == lost_location)
    ]
    
    # If a match is found, return 'matched', otherwise return 'unmatched'
    if not matching_row.empty:
        return 'matched'
    else:
        return 'unmatched'

# Applying the matching function to each row in lost_items and creating a new column 'Matched'
lost_items['Matched'] = lost_items.apply(matchmaker, axis=1)

# Saving the updated lost_items dataset with the new 'Matched' column
lost_items.to_csv('matched_lost_items.csv', index=False)

# Reading the final dataset with matched lost items
final_dataset = pd.read_csv('matched_lost_items.csv')
final_dataset

# Filtering unmatched rows from the final dataset
unmatched_rows = final_dataset[final_dataset['Matched'] == 'unmatched']

# Filtering matched rows from the final dataset
matched_rows = final_dataset[final_dataset['Matched'] == 'matched']
