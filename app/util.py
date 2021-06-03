import pickle
import json
import numpy as np 
from sklearn.linear_model import RidgeCV

__locations = None
__data_columns = None
__model = None


def get_estimated_price(city, total_sqft, lot_size, bedrooms, bathrooms, yr_built):
    '''
    this function takes user inputs and returns a price prediction -- it will soon be deprecated in favor of util1.py
    Parameters
    ---------
    city - city where house is located
    total_sqft - finished square footage
    lot_size - lot size is in acres, if in town and unknown assume 0.2
    bedrooms - number of bedrooms
    bathrooms - number of bathrooms
    yr_built - year the house was built, for remodels enter current year
    
    Returns
    --------
    response - returns a price prediction from the ridge model
    '''
    
    
    try:
        loc_index = __data_columns.index(location)
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = lot_size
    x[2] = bedrooms
    x[3] = bathrooms
    x[4] = yr_built
    if loc_index>=0:
        x[loc_index] = 1

    prediction = np.exp(__model.predict([x])[0])
    val = np.ndarray.item(prediction)
    value = '${:,.0f}'.format(val)
    return value


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("/home/robert/cchp/app/data/columns1.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('/home/robert/cchp/app/data/ccmohp_model1.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price(3000, 5, 4, 3, 2020, 'town_Peculiar'))
    print(get_estimated_price(3000, 5, 4, 3, 2020, 'town_Raymore'))
    print(get_estimated_price(3000, 5, 4, 3, 2020, 'town_Lees Summit'))
    print(get_estimated_price(3000, 5, 4, 3, 2020, 'town_Belton'))
    print(get_estimated_price(2000, 5, 4, 3, 2020, 'town_Peculiar'))
    print(get_estimated_price(3000, 1, 4, 3, 2020, 'town_Peculiar'))
    print(get_estimated_price(3000, 5, 4, 3, 2020, 'town_Archie'))




