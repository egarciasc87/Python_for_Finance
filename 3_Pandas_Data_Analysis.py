import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
#from pylab import plt, mpl

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


def basicAnalytics():
    list1 = ["Erick", "Carlos", "Juan"]
    df = pd.DataFrame(list1)
    df["Height"]=([178, 182, 169])
    df.columns = ["Name", "Height"]
    print(df)
    print("\n")
    df.info()
    df.describe()

    #print(np.mean(df["Height"]))
    print("\nAverage height: ", df["Height"].mean())
    print("Sum of heights: ", df["Height"].sum())
    print("Acumulative sum: ", df["Height"].cumsum())

    return df


def basicVisualization():
    plt.style.use("seaborn")
    mpl.rcParams["font.family"] = "serif"
    #%matplotlib inline
    df = basicAnalytics()
    df.cumsum().plot(lw=2.0, figsize=(10, 6))


def seriesClass():
    df = pd.DataFrame()
    df["Name"] = (["Erick", "Carlos", "Juan", "Julia"])
    df["Age"] = ([32, 46, 23, 38])
    df["Height"] = ([180, 178, 167, 173])
    print(df)
    s = pd.Series(np.linspace(0, 15, 4), name="series")
    df["ColumnX"] = s
    print(df)
    print(s)
    s = df["Age"]
    print(s)
    print("Mean od series: ", s.mean())
    print("Sum of series: ", s.sum())
    #s.plot(lw=2.0, figsize=(10, 6))
    plt.plot(s)
    plt.show()


def groupOperations():
    np.random.seed(100)
    arrayPrices = np.random.standard_normal((24,4))
    #print(arrayPrices)
    df = pd.DataFrame(arrayPrices)
    df.columns = ["Open", "Low", "High", "Close"]

    list1 = ["AAPL"] * 12
    list2 = ["MSFT"] * 12
    df["Ticker"] = list1 + list2

    dates = pd.date_range("2021-1-1", periods=12, freq="m")
    dates = np.hstack((dates, dates))
    df["Date"] = dates

    listMonth = df["Date"].dt.month.values.tolist()
    listMonth = ["Q" + str(math.floor(x / 4) + 1) for x in listMonth]
    df["Quarter"] = listMonth

    print(df)
    df = df.set_index(["Ticker", "Date"])
    #print("\nIndices: ", df.index)
    #print("Columns: ", df.columns)

    print("\nGrouping:")
    groups = df.groupby(["Ticker", "Quarter"])
    #print(groups.size())
    #print(groups.mean())
    #print(groups.max())
    print(groups.aggregate([min, max]).round(2))

    print("\nComplex selection:")
    data = np.random.standard_normal((12, 2))
    dFrame = pd.DataFrame(data)
    dFrame.columns = ["X", "Y"]
    print(dFrame)
    #print(dFrame.info())
    print(dFrame.head())
    print(dFrame.tail())
    print(dFrame["X"] > 0.5)
    print(dFrame > 0)
    print(dFrame[dFrame["X"] > 0])
    print(dFrame.query("X > 0"))


def concatenationJoiningMergingOperations():
    dfA = pd.DataFrame(["100", "200", "300", "400"],
        index=["a", "b", "c", "d"],
        columns=["A"])
    #dfA["B"] = (["Erick", "Juan", "Ernesto", "Victor"])

    df2 = pd.DataFrame()
    df2["A"] = (["100", "200", "300", "400"])
    df2["Index"] = (["a", "b", "c", "d"])
    df2 = df2.set_index(["Index"])
    df2.columns = ["A"]

    dfB = pd.DataFrame(["200", "150", "50"],
        index=["f", "b", "d"],
        columns=["B"])
    #print(dfA)
    #print(dfB)

    print("\nAppend and Concat functions:")
    print(dfA.append(dfB))
    #print(dfA.append(dfB, ignore_index=True))
    print(pd.concat((dfA, dfB), sort=False))
    #print(pd.concat((dfA, dfB), ignore_index=True))

    print("\nJoining:")
    print(dfA.join(dfB))
    print(dfA.join(dfB, how="inner"))

    dfC = pd.DataFrame()
    dfC["A"] = dfA["A"]
    dfC["B"] = dfB["B"]
    dfD = pd.DataFrame({"A": dfA["A"], "B": dfB["B"]})
    print(dfC)
    print(dfD)

    print("\nMerging:")
    


#dataFrame101()
#dataFrame102()
#basicAnalytics()
#basicVisualization()
#seriesClass()
#groupOperations()
concatenationJoiningMergingOperations()
