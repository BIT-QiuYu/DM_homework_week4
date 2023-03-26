import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

root = 'movies_dataset_1'
after = 'movies_dataset_'


def load_data(path):
    return pd.read_csv(path, keep_default_na=False, low_memory=False, encoding='ISO-8859-1')


def show_col():
    return load_data(root+'.csv').columns


def get_row_index(col, value):
    data = load_data(root+'.csv')
    lst = []
    entity = []
    for i in range(data.shape[0]):
        if data.loc[i, col] == value:
            lst.append(i)
            entity.append(data.loc[i].values)
    return lst, entity


def delete_row(index_lst,i):
    data = load_data(root+'.csv')
    data = data.drop(index=index_lst)
    data.to_csv(after+f'{i}'+'.csv')

class col_helper():
    def __init__(self,i):
        self.data2 = load_data(root+'.csv');
        self.data = load_data(after+f'{i}'+'.csv');
        self.column = ''

    def select_col(self,col):
        self.column = col

    def grab_col(self, col):
        self.data = []
        self.data.append(load_data(root)[col])
        self.data = np.array(self.data)

    def generate_new_col(self,col1,col2,f):
        self.data = []
        for i in file_lst:
            res = f(load_data(root, i)[col1],load_data(root, i)[col2])
            self.data.append(res)
        self.data = np.array(self.data)

    def five_number(self):
        col = np.array(self.data[self.column].values)
        print('Min:', col.min())
        print('Q1:', np.percentile(col, 25))
        print('Q2:', np.percentile(col, 50))
        print('Q3:', np.percentile(col, 75))
        print('Max:', col.max())

    def box(self,w,h,xlabel):
        col = np.array(self.data[self.column].values)
        print(col)
        col = np.asarray(col, dtype = np.float64)
        fig = plt.figure(figsize=(w, h))
        plt.boxplot(col, notch=False, vert=False)
        plt.xlabel(xlabel)
        plt.show()
        outlier = np.percentile(col, 75) + (np.percentile(col, 75) - np.percentile(col, 25)) * 1.5
        print(outlier)

    def box2(self,w,h,xlabel):
        col = np.array(self.data[self.column].values)
        print(col)
        col = np.asarray(col, dtype = np.float64)
        fig = plt.figure(figsize=(w, h))
        plt.boxplot(col, notch=False, vert=False)
        plt.xlabel(xlabel)
        plt.show()
        outlier = np.percentile(col, 75) + (np.percentile(col, 75) - np.percentile(col, 25)) * 1.5
        print(outlier)

    def normal_hist(self,w,h,xlabel,ylabel):
        col = np.array(self.data[self.column].values)
        fig1 = plt.figure(figsize=(w, h))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.hist(col, bins=40, facecolor="#cddc39", edgecolor="#afb42b", alpha=0.7)

    def hist_bar(self,w,h,number):
        fig = plt.figure(figsize=(w, h))
        plt.title('language')
        X = self.data2[self.column].value_counts().index[:number]
        Y = self.data2[self.column].value_counts().values[:number]
        plt.bar(X, Y, facecolor='#cddc39', edgecolor='#afb42b')
        for x, y in zip(X, Y):
            plt.text(x, y, '%d' % y, ha='center', va='bottom')

    def count_none(self,none_token=' '):
        col = np.array(self.data2[self.column].values);
        cnt = 0
        for i in col:
            if i == none_token:
                cnt += 1
        print(cnt)
        return cnt


    def count_none_after(self,none_token=' '):
        col = np.array(self.data[self.column].values);
        cnt = 0
        for i in col:
            if i == none_token:
                cnt += 1
        print(cnt)
        return cnt


