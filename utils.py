import os
import json
import pickle
import pandas as pd
import numpy as np
from  config import *


class MedicalInsurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def load_model(self):

        with open(MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(JSON_DATA_PATH, "r") as f:
            self.json_data = json.load(f)


    def predict_charges(self):
        try:
            self.load_model()
            test_array = np.zeros(9,dtype=int)

            test_array[0] = self.age
            test_array[1] = self.json_data['gender'][self.gender]
            test_array[2] = self.bmi
            test_array[3] = self.children
            test_array[4] = self.json_data['smoker'][self.smoker]
            test_array[self.json_data['columns'].index(self.region)] = 1

            print('test array>>>', test_array)

            predicted_charges = self.model.predict([test_array])[0]

            print('predicted price is:', predicted_charges)

            return "Insurance charges will be:" , round(predicted_charges,0)
        except:
            return 'Error!'

obj = MedicalInsurance(61,'male',28.4,1,'no','southwest')
obj.predict_charges()