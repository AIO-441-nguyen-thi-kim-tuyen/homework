import numpy as np
import pandas as pd


class AdvertisingAnalysis:
    def __init__(self, file_path):
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv(file_path)
        # data = np.genfromtxt(file_path, delimiter=',', dtype=None, names=True, encoding=None)
        self.data = df.to_numpy()

    # Question 15
    def find_highest_sales_strategy(self):
        sales = self.data[:, 3]
        max_sales_index = np.argmax(sales)
        max_sales_strategy = self.data[max_sales_index, 3]
        return max_sales_index, max_sales_strategy

    # def print_highest_sales_strategy(self):
    #     max_sales_strategy = self.find_highest_sales_strategy()[1]
    #     print("Chiến lược quảng cáo có doanh số cao nhất:")
    #     for name in self.data.dtype.names:
    #         print(f"{name}: {max_sales_strategy[name]}")

    # Question 16
    def find_average_tv_advertise(self):
        tv = self.data[:, 0]
        average_tv = np.mean(tv)
        return average_tv

    # Question 17
    def count_record_sales_greater_equal_20(self):
        sales = self.data[:, 3]
        return np.count_nonzero(sales >= 20)

    # Question 18

    def average_radio_where_sales_greater_equal_15(self):
        average_radio = np.mean(self.data[self.data[:, 3] >= 15, 1])
        return average_radio

    # Question 19
    def average_sales_where_newspaper_greater_average_newspaper_column(self):
        average_newspaper = np.mean(self.data[:, 2])
        sales_sum = np.sum(self.data[self.data[:, 2] > average_newspaper, 3])
        return sales_sum

    # Question 20
    def label_good_average_bad(self):
        average_sales = np.mean(self.data[:, 3])
        scores = np.where(self.data[:, 3] > average_sales, 'Good',
                          np.where(self.data[:, 3] < average_sales, 'Bad', 'Average'))
        return scores

    # Question 21
    def label_good_average_bad_2(self):
        sales = self.data[:, 3]
        average_sales = np.mean(sales)
        closest_average_sales = sales[np.abs(sales - average_sales).argmin()]
        scores = np.where(sales > closest_average_sales, 'Good',
                          np.where(sales < closest_average_sales, 'Bad', 'Average'))
        return scores
