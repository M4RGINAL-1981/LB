import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":
    # Загрузка данных о Титанике
    titanic_df = sns.load_dataset('titanic')

    # Посмотрим на первые 5 строк таблицы
    print(titanic_df.head())