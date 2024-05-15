import csv

# 定义输入和输出文件名
input_file = 'output.txt'
output_file = 'postgraduates_data.csv'

# 打开并读取txt文件
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 准备存储数据的列表
data = []

# 查找并提取数据
for i in range(len(lines)):
    if 'Postgraduates' in lines[i] or 'Postgraduates*' in lines[i]:
        # 获取下一行的数据并添加到列表
        if i + 1 < len(lines):
            cleaned_line = lines[i + 1].strip()
            if cleaned_line:
                values = cleaned_line.split()
                # 逐一添加每个值
                for value in values:
                    data.append(('Postgraduates', value))

# 将数据写入CSV文件
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 写入CSV文件的标题
    writer.writerow(['Degree', 'Graduates'])

    # 写入每一行数据
    for row in data:
        writer.writerow(row)

print(f"Data has been successfully written to {output_file}")
