import csv
import pandas as pd



data  = pd.read_csv("10thResult.csv")
# print(data)


listData = []

for i in data.iterrows():
    # print(i["Roll_No"])
    # print(type(i[0]))
    # print(i[0])
    # print(i[1][0])
    # print(i[1][1])
    # print(i[1][2])
    # print(i[1][3])
    # print(i[1][4])
    # print(i[1][5])
    # print(i[1][6])
    obj = {
        "Roll_No":i[1][0],
        "Name":i[1][1]

    }

    # print(obj)
    listData.append(obj)

# print(listData)
import json

with open("10thResult.json", "w+") as f:
    json.dump(listData,f)




