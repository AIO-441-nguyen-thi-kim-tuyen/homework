import os
import sys

import numpy as np

from homework.module_2_week_1.advertising_analysis import AdvertisingAnalysis

file_path = os.path.join(os.path.dirname(__file__), 'advertising.csv')
analysis = AdvertisingAnalysis(file_path)

epsilon = sys.float_info.epsilon


# Question 15
def test_highest_sales_strategy():
    max_index, max_value = analysis.find_highest_sales_strategy()
    assert max_index == 175
    assert abs(round(max_value, 1) - 27.0) < epsilon


# Question 16
def test_find_average_tv_advertise():
    result = analysis.find_average_tv_advertise()
    assert abs(round(result, 1) - 147.0) < epsilon


# Question 17
def test_count_record_sales_greater_equal_20():
    result = analysis.count_record_sales_greater_equal_20()
    assert result == 40


# Question 18
def test_average_radio_where_sales_greater_equal_15():
    result = analysis.average_radio_where_sales_greater_equal_15()
    assert abs(round(result, 1) - 26.2) < epsilon


# Question 19
def test_average_sales_where_newspaper_greater_average_newspaper_column():
    result = analysis.average_sales_where_newspaper_greater_average_newspaper_column()
    assert abs(round(result, 1) - 1405.1) < epsilon


# Question 20
def test_label_good_average_bad():
    result = analysis.label_good_average_bad()
    assert (result[7:10] == np.array(['Bad', 'Bad', 'Good'])).all()


# Question 21
def test_label_good_average_bad_2():
    result = analysis.label_good_average_bad_2()
    assert (result[7:10] == np.array(['Bad', 'Bad', 'Good'])).all()


