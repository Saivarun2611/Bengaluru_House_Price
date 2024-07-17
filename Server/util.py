import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def location_names():
    return __locations
def load_saved_artifacts():
    print("Loading Saved Artifacts....Start")
    global __data_columns
    global __locations
    with open("./Artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]
    global __model    
    with open("./Artifacts/Bengaluru_house_Price.pickle",'rb') as f:
        __model=pickle.load(f)
if __name__=='__main__': 
    load_saved_artifacts()
    print(location_names())   
    get_estimated_price('Chikka Tirupathi',2800,4,4)

