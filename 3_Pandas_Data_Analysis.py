import pandas as pd
import numpy as np

def dataFrame101():
    df = pd.DataFrame([10, 20, 30, 40, 50],
        columns=["numbers"],
        index=["a", "b", "c", "d", "e"])
    df["name"]=(["Carlos", "Juan", "Veronica", "Ernesto", "Victor"])
    print(df)
    print("Indices: ", df.index)
    print("Columns: ", df.columns)
    print("Specific item: ", df["name"])
    print("Sum of numbers: ", df["numbers"].sum())
    print("Operations: ", df["numbers"] * 2)

    search = input("\nEnter index value: ")
    print(df.loc[search])
    search = input("\nEnter index  number: ")
    print(df.iloc[int(search)])
    df = df.append(pd.DataFrame({"numbers": 100, "name": "Claudia"},
        index=["f",]))
    print(df)


def dataFrame102():
    np.random.seed(100)
    array = np.random.standard_normal((7,4))
    print(array)
    print(type(array))
    df = pd.DataFrame(array)
    df.columns = ["Column1", "Column2", "Column3", "Column4"]
    print(df)

    print("\n")
    dates = pd.date_range("2022-1-1", periods=7, freq="w")
    print(dates)
    print(type(dates))
    df.index = dates
    print(df)
    print(df.values)


#dataFrame101()
dataFrame102()
