import pickle
import json
import pandas as pd
from scipy.special import inv_boxcox

# __city = None
__data_columns = None
__model = None



def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    #with open("/home/robert/cc2/app/data/columns20210601.json", "r") as f:
    with open("C:/Users/EKKRY/Documents/stuff/hpp2/data/data/columns.json", "r") as f:    
        __data_columns = json.load(f)["data_columns"]

    global __model
    if __model is None:
        # with open("/home/robert/cc2/app/data/stacked_pipe20210601.pickle", "rb") as f:
        with open("C:/Users/EKKRY/Documents/stuff/hpp2/data/data/gradient_pipe.pickle", "rb") as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def predict_price(city, total_sqft, lot_size, bedrooms, bathrooms, yr_built):
    """
    price prediction with sklearns pipeline instead of creating dummy columns
    lambda was found to be 0.20522 - todo don't hard code this
    """
    lam = 0.20522214306942227
    x = [city, total_sqft, lot_size, bedrooms, bathrooms, yr_built]
    cols = __data_columns
    data = pd.DataFrame(data=[x], columns=cols)
    prediction = inv_boxcox(__model.predict(data)[0], lam)
    return f"${round(prediction)}"


def get_location_names():
    return [
        "Garden City",
        "Pleasant Hill",
        "Strasburg",
        "Archie",
        "Belton",
        "Harrisonville",
        "Raymore",
        "Drexel",
        "Cleveland",
        "Peculiar",
        "East Lynne",
        "Freeman",
        "Creighton",
        "Lake Winnebago",
        "Lees Summit",
        "Greenwood",
        "Loch Lloyd",
    ]


def get_data_columns():
    return __data_columns


if __name__ == "__main__":
    load_saved_artifacts()
    print(predict_price("Belton", 3000, 5, 4, 3, 2021))
    print(predict_price("Raymore", 3000, 5, 4, 3, 2021))
