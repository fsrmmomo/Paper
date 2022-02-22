import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dat_file_folder = "../../Data/cnt/"
    x = [1, 200, 500, 1000, 2000, 5000, 10000, 20000]
    y = [[] for i in range(len(x))]
    i = 1
    for file in os.listdir(dat_file_folder):
        if file[-3:] == "res":
            num = int(file[:-4])
            print("Process: ", dat_file_folder + file)
            with open(dat_file_folder + file, 'rb') as f:
                str = f.readline().split()
                i = x.index(num)
                y[i] = list(map(int, str))
    y_real = [1]
    for list in y[1:]:
        print(list)
        y_real.append(np.mean(list))
    print(y_real)
    y_real = [1-y_real[i]/x[i] for i in range(len(x))]
    print(y_real)



    plt.figure()
    plt.figure(figsize=(8, 6))
    # 显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.xticks(np.arange(1,9, 1),x,rotation=0)
    # plt.plot(x,y_real,'s-')
    plt.plot([i+1 for i in range(len(x))],[i*100 for i in y_real],'s-')

    # 设置标题
    plt.title('插入量减少')

    # 设置 x 和 y 轴名称
    plt.xlabel('窗口大小')
    plt.ylabel('减少百分比')

    # 设置 x 和 y 轴标尺最大最小值
    for x, y in zip([i+1 for i in range(len(x))],[i*100 for i in y_real]):
        plt.text(x, y, '%.0f' % y+"%", fontdict={'fontsize': 14})

    plt.xlim(1, 8.5)
    plt.ylim(0, 80)

    plt.savefig("../../Data/figure/insert_reduction.png")
    plt.show()


