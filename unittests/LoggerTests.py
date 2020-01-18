#!/usr/bin/env python
"""
model tests
"""

import os
import sys
import unittest
import pathlib as pl
# lib_path = os.path.abspath(os.path.join('../'))
# sys.path.append(lib_path)

## import model specific functions and variables
from model import *


class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """

    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        # lib_path = os.path.abspath(os.path.join('../'))
        # sys.path.append(lib_path)
        model_train('cs-train')
        self.assertTrue(os.path.exists('models'))

    def test_02_load(self):
        """
        test the train functionality
        """
                        
        ## load the model
        all_data, all_models = model_load()
        self.assertTrue(all_data)
        self.assertTrue(all_models)

    def test_03_predict(self):
        """
        test the predict functionality
        """
        
        ## example predict
        country= ['all', 'united_kingdom']
        year= ['2018', '2018']
        month=['01', '02']
        day=['05', '06']
        result1 = model_predict(country[0],year[0],month[0],day[0])
        result2 = model_predict(country[1],year[1],month[1],day[1])
        result_list = [result1, result2]
        print(result_list)
        for result in result_list:
            self.assertTrue(result)


### Run the tests
if __name__ == '__main__':
    unittest.main()
