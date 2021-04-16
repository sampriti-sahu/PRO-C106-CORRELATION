import plotly_express as px
import csv
import numpy as np
import pandas as pd


def Get_Data(Path, value1, value2):
    xAxis = []
    yAxis = []
    with open(Path) as f:
        df = csv.DictReader(f)
        for row in df:
            xAxis.append(float(row[value1]))
            yAxis.append(
                float(row[value2]))

    return{"x": xAxis, "y": yAxis}


def Find_CoRellation(Data):
    Corellation = np.corrcoef(Data["x"], Data["y"])
    print("Corellation = ", Corellation[0, 1])


def Plot_Graph(Path, value1, value2):
    df = pd.read_csv(Path)
    fig = px.scatter(df, x=value1, y=value2)
    fig.show()


path1 = "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Projects/Corellation/Data1.csv"
path2 = "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Projects/Corellation/Data2.csv"

valueA1 = "Coffee in ml"
valueA2 = "sleep in hours"
valueB1 = "Marks In Percentage"
valueB2 = "Days Present"


dataSource1 = Get_Data(path1, valueA1, valueA2)
print("In Data of Data1.csv file :")
Find_CoRellation(dataSource1)
print("And the Graph is as Follows")
Plot_Graph(path1, valueA1, valueA2)

dataSource2 = Get_Data(path2, valueB1, valueB2)
print("In Data of Data2.csv file :")
Find_CoRellation(dataSource2)
print("And the Graph is as Follows")
Plot_Graph(path2, valueB1, valueB2)
