import numpy as np
import pandas as pd


def main(**kwargs):
    # question 1
    print(np.__version__)

    df = pd.read_csv("data/chapter-02-car-price.csv")

    # question 2
    print(df.shape[0])

    # question 3
    print(df.Make.value_counts().head(3).index.tolist())

    # question 4
    print(df.Model[df.Make == "Audi"].nunique())

    # question 5
    print(np.count_nonzero(df.isnull().sum().to_numpy()))

    # question 6
    a = df["Engine Cylinders"].median()
    b = df["Engine Cylinders"].fillna(df["Engine Cylinders"].mode()).median()
    print("Changed" if (a != b) else "Has not changed")

    # question 7
    x = (
        df[df.Make == "Lotus"][["Engine HP", "Engine Cylinders"]]
        .drop_duplicates()
        .to_numpy()
    )
    y = np.linalg.inv(np.matmul(x.T, x))
    z = [1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800]
    w = np.matmul(np.matmul(y, x.T), z)
    print(w[0])
    ## import pdb; pdb.set_trace()  # fmt: skip
