import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    rf = '../../Data/raw_data/MAWI/dat/SB-F-202004090759.cnt2'
    rf = '../../Data/raw_data/MAWI/dat/SB-F-202201021400.cnt2'
    rf = '../../Data/raw_data/MAWI/dat/SB-G-202004080800.cnt2'

    x = []

    x = list(range(0, 101, 10))
    x.insert(1,1)
    x.insert(2,5)
    ox = x


    print(x)

    c_list = []
    with open(rf, 'r') as f:
        lines = f.readlines()
        for line in lines:
            c_list = [int(x) for x in line.split()]
    # print(c_list[:222])
    total = sum(c_list)

    nums = len(c_list)

    step_sum = 0
    y = []
    for v in c_list:
        step_sum += v
        y.append(step_sum / total)

    x = [nums * i //100 for i in x]
    print(x)
    print(nums)
    x[-1] -= 1
    print(x)
    y = [y[i] for i in x]

    plt.figure()
    plt.figure(figsize=(8, 6))
    # 显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.xticks(np.arange(1, len(x)+1, 1), ox, rotation=0)
    # plt.plot(x,y_real,'s-')
    plt.plot([i + 1 for i in range(len(x))], [i * 100 for i in y], 's-')

    # 设置标题
    plt.title('分布')

    # 设置 x 和 y 轴名称
    plt.xlabel('流数量百分比')
    plt.ylabel('包数量百分比')

    # 设置 x 和 y 轴标尺最大最小值
    for x, y in zip([i + 1 for i in range(len(x))], [i * 100 for i in y]):
        plt.text(x, y, '%.0f' % y + "%", fontdict={'fontsize': 14})

    plt.xlim(1, 12)
    plt.ylim(0, 100)

    # plt.savefig("../../Data/figure/insert_reduction.png")
    plt.show()
