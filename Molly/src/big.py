import pandas
import pyecharts.options as opts
from pyecharts.charts import Line

#计算不同学历的比例
def rate_calculation(path):            
    result={}
    for year in range(1995, 2023):
        file_path = f"{path}{year}.csv"
        read_csv= pandas.read_csv(file_path)       #读取csv文件  
        sum_graduates=read_csv.iloc[:,1].sum()   #算每年总人数
        
        for i in range(1,5):                   #算不同学历(4种)比例
            degree=f'Category{i}'                
            result[f'{year}_{degree}_比例']=
    return result


#创建Line图表对象
line = Line()

# 添加年份数据到 x 轴
line.add_xaxis(read_csv['年份'].tolist())

# 添加不同学历比例的数据到折线图上，并实现堆叠效果
for column in read_csv.columns[1:]:
    line.add_yaxis(column, read_csv[column].tolist(), is_smooth=True, is_stack=True)

# 设置全局
line.set_global_opts(
    title_opts=opts.TitleOpts(title="26年来不同学历比例变化")
    xaxis_opts=opts.AxisOpts(name="年份"), yaxis_opts=opts.AxisOpts(name="比例")
    )

# 生成html文件
line.render("stacked_line_chart.html")



    