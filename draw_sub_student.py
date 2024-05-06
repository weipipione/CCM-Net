import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              '11']  # 类别

acc = [0.9200626959247649, 0.9767008387698043, 0.9743384121892542, 0.9702194357366771,
       0.9876847290640394, 0.9377394636015326, 0.9793103448275862, 0.9900383141762452,
       0.9562657695542472, 0.9630541871921182, 0.9797160243407708
       ]  # 对应类别的值
acc = np.array(acc) * 100
# f1 = [0.9452789699570815, 0.9877149877149877, 0.9847182425978989, 0.9833333333333332,
#       0.9930264993026499, 0.9491790461297889, 0.9878542510121457, 0.9947853991175291,
#       0.9737108190091002, 0.9777117384843982, 0.9893390191897655
#       ]
# f1 = np.array(f1) * 100
# acc_min_max = [[0.9655172413793104, 0.9568965517241379,
#                 0.9396551724137931, 0.9568965517241379,
#                 0.9741379310344828, 0.9482758620689655,
#                 0.9482758620689655, 0.9482758620689655,
#                 0.9137931034482759, 0.9310344827586207],
#                [1.0, 1.0, 1.0, 1.0, 1.0,
#                 1.0, 1.0, 1.0, 1.0, 1.0]]  # 箱线图的数据
# f1_min_max = [[0.9629629629629629, 0.9640287769784172,
#                0.9333333333333332, 0.9565217391304348,
#                0.9615384615384616, 0.9494949494949494,
#                0.9541284403669724, 0.9333333333333333,
#                0.9180327868852458, 0.948051948051948],
#               [1.0, 1.0, 1.0, 1.0, 1.0,
#                1.0, 1.0, 1.0, 1.0, 1.0]]  # 箱线图的数据
# 计算acc和f1的均值
acc_mean = np.mean(acc)
# f1_mean = np.mean(f1)
# 设置柱状图的宽度
bar_height = 0.4
# 计算每个柱状图的中心位置
bar_centers = [r + bar_height / 2 for r in range(len(categories))]

# 创建横向柱状图
plt.figure(figsize=(8, 8))  # 设置图表大小
# 绘制小于均值的柱状图（颜色不同）
for i, value in enumerate(acc):
    if value < acc_mean:
        plt.barh(bar_centers[i], value, color=(242 / 255, 121 / 255, 112 / 255), height=bar_height)  # 设置小于均值的柱状图颜色为红色
    else:
        plt.barh(bar_centers[i], value, color=(98 / 255, 178 / 255, 176 / 255), height=bar_height)  # 设置大于等于均值的柱状图颜色为黄色

# plt.barh(r1, acc, color=(242 / 255, 204 / 255, 142 / 255), height=bar_height, label='Accuracy')  # 绘制第一个柱状图，设置颜色和标签
# plt.barh(r2, f1, color=(165 / 255, 165 / 255, 141 / 255), height=bar_height, label='F1 Score')  # 绘制第二个柱状图，设置颜色和标签
# plt.barh(r2, f1, color=(130 / 255, 178 / 255, 154 / 255), height=bar_height, label='F1 Score')  # 绘制第二个柱状图，设置颜色和标签

# 计算acc和f1的均值（与之前的代码相同）

# 绘制垂直虚线（acc均值）和（f1均值）（与之前的代码相同）
plt.axvline(x=acc_mean, color=(239 / 255, 83 / 255, 71 / 255), linestyle='--', linewidth=2.5,label='Acc Mean')
# plt.axvline(x=f1_mean, color=(61 / 255, 101 / 255, 81 / 255), linestyle='--', label='F1 Mean')

# 在垂直虚线上标注均值
plt.text(acc_mean - 3.35, len(categories) - 0.4, f' {acc_mean:.2f}',
         color=(239 / 255, 83 / 255, 71 / 255), fontsize=20, weight='bold')
# plt.text(f1_mean + 0.1, len(categories) - 0.2, f' {f1_mean:.2f}',
#          color=(61 / 255, 101 / 255, 81 / 255), fontsize=9.5)

# 设置刻度标签
# 设置刻度标签（每隔两个显示一次数值）
plt.yticks([r + bar_height / 2 for r in range(len(categories))], categories, fontsize=20)

plt.ylabel('Subjects', fontsize=20, ha='center', weight='bold')
# 设置标题和标签
plt.xlabel('Values', fontsize=20, ha='center', weight='bold')  # 设置X轴标签

# 隐藏图表的上边框和右边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 加粗横坐标刻度标签
plt.xticks(fontsize=20)
# 设置横坐标范围
plt.xlim(80, 100)  # 设置横坐标范围
plt.locator_params(axis='x', integer=True)
# plt.ylim(-1.6, 32.5)  # 设置横坐标范围

# 显示图例（位置设置为左上角）
plt.legend(loc='upper left',fontsize=20)

# 保存图片到指定路径
plt.savefig('C://Users//weiyayun//Desktop//论文写作//论文图//subject//Self_made1.png', dpi=800)

# 显示图表
plt.show()
