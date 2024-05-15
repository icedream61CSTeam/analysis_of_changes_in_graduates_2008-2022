import pandas as pd
import matplotlib.pyplot as plt

# 定义输入文件名
input_file = '../output/postgraduates_data.csv'

# 读取CSV文件
df = pd.read_csv(input_file)

# 准备数据
years = list(range(2004, 2019))
graduates = df['Graduates']

#匹配年份顺序

graduates = graduates.iloc[::-1]

# 创建折线图
plt.figure(figsize=(10, 6))
plt.plot(years, graduates, marker='o', linestyle='-', color='b')

# 添加标题和标签
plt.title('Number of Postgraduates Graduates (2004-2019)')
plt.xlabel('Year')
plt.ylabel('Number of Graduates')
plt.xticks(years, rotation=45)
plt.grid(True)

# 显示图表
plt.tight_layout()
plt.show()
