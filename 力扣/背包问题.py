def package(bagWeight, value, weight):
    line = [] # 每个 weight 对应的价值

    # 第一行
    for i in range(0,bagWeight):
        if i >= weight[0]:
            line.append(value[0])
        else:
            line.append(0)

    # 剩下行
    r = len(value)
    for i in range(1, r +1):
        next = [0]*r

        for j in range(bagWeight+1):
            if j < weight[i]:
                next[j] = line[j]
            else:
                a= value[i] + line[j - weight[i]]
                b = line[j]
                next[j] = max(a, b)

        line = next


    return line[bagWeight]




value = [5, 10,3,6,3]
weight = [2,5,1,4,3]
bagWeight = 6

print(package(bagWeight, value, weight)) # 13