import statistics
import math
from csv import reader

with open('FEH_00200521_220610143730.csv', 'r', encoding='utf-8') as csv_file:

    csv_reader = reader(csv_file)

    k = "01000"
    total = 0
    list_todohuken = []

    for row in csv_reader:
        if row[0] == k:
            total = total + int(row[2].replace(",", ""))
            list_todohuken.append(int(row[2].replace(",", "")))
            k = int(k)+1000
            k = str(k)
            if int(k) < 10000:
                k = "0"+k

    print("平均＝", int(statistics.mean(list_todohuken)))

    with open('FEH_00200521_220610143730.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = reader(csv_file)
        k = "01000"
        for row2 in csv_reader:
            if row2[0] == k:
                if int(row2[2].replace(",", "")) == max(list_todohuken):
                    max_place = row2[1]
                elif int(row2[2].replace(",", "")) == min(list_todohuken):
                    min_place = row2[1]
                elif int(row2[2].replace(",", "")) == statistics.median(list_todohuken):
                    median_place = row2[1]
                k = int(k)+1000
                k = str(k)
                if int(k) < 10000:
                    k = "0"+k

    print("中央値＝", statistics.median(list_todohuken), "場所=", median_place)
    print("最大値＝", max(list_todohuken), "場所=", max_place)
    print("最小値＝", min(list_todohuken), "場所=", min_place)
    print("分散＝", statistics.pvariance(list_todohuken))
    print("標準偏差＝", statistics.pstdev(list_todohuken))
