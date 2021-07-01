'''
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
distances=[5,25,15,10,15]
fuel = [1,2,1,0,3]
mpg=10
'''
def validStartingCity(distances, fuel, mpg):
    fuel = [v*mpg for v in fuel]
    if sum(distances)<sum(fuel):
        return -1
    else:
        i=gas=distance=start_city=0

        while i < len(fuel):
            gas+=fuel[i]
            distance += distances[i]
            if gas<distance:
                gas=0
                distance=0
                start_city = i+1
            i+=1
        return start_city