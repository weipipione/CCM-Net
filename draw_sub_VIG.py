import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
              '21', '22', '23']  # 类别

acc = [0.895668549905838, 0.8983050847457628, 0.9457627118644067, 1.0,
       0.8836158192090395, 0.8885122410546139, 0.9427495291902072, 0.9902071563088513,
       0.9355932203389831, 0.9694915254237289, 0.9446327683615819, 0.9694915254237289,
       0.9408662900188324, 0.9619585687382297, 0.9645951035781545, 0.8587570621468926,
       0.9261770244821093, 0.9325800376647835, 0.9412429378531073, 0.8821092278719397,
       0.9728813559322034, 0.9510357815442562, 0.888135593220339
       ]  # 对应类别的值

acc = np.array(acc) * 100

# 计算acc和f1的均值
acc_mean = np.mean(acc)
# f1_mean = np.mean(f1)
# 设置柱状图的宽度
bar_height = 0.8
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
plt.text(acc_mean - 3.3, len(categories)+0.1, f' {acc_mean:.2f}',
         color=(239 / 255, 83 / 255, 71 / 255), fontsize=20, weight='bold')
# plt.text(f1_mean + 0.1, len(categories) - 0.2, f' {f1_mean:.2f}',
#          color=(61 / 255, 101 / 255, 81 / 255), fontsize=9.5)

# 设置刻度标签
# 设置刻度标签（每隔两个显示一次数值，最后一个刻度也显示）
# 设置刻度标签（每隔两个显示一次数值，最后一个也显示）
show_ticks_indices = [r for r in range(0, len(categories), 2)]  # 每隔两个刻度显示一次
show_ticks_indices.append(len(categories) - 1)  # 最后一个也显示
show_ticks_labels = [categories[i] for i in show_ticks_indices]  # 对应的刻度标签

plt.yticks([r + bar_height / 2 for r in show_ticks_indices], show_ticks_labels, fontsize=20)

# plt.yticks(len(categories) + bar_height / 2 )
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
plt.savefig('C://Users//weiyayun//Desktop//论文写作//论文图//subject//SEED_VIG1.png', dpi=800)

# 显示图表
plt.show()
