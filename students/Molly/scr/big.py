import pandas
import pyecharts.options as opts
from pyecharts.charts import Bar

#此处代码本来用于计算26年来不同学历比例变化中的不同学历比例
""" #计算不同学历的比例
def rate_calculation(path):            
    result={}
    for year in range(1995, 2023):
        file_path = f"{path}{year}.csv"
        read_csv= pandas.read_csv(file_path)       #读取csv文件  
        sum_graduates=read_csv.iloc[:,1].sum()   #算每年总人数
        
        for i in range(1,5):                   #算不同学历(4种)比例
            degree=f'Category{i}'                
            result[f'{year}_{degree}_比例']=
    return result """

read_csv=pandas.read_csv("C:\\Users\\tzy25\\Downloads\\postgraduates_data.csv")

x_data = ["2008", "2009", "2010","2011", "2012", "2013","2014", "2015", "2016","2017", "2018", "2019", "2020", "2021", "2022",]
y_data = read_csv["Graduates"].tolist()[::-1]

#创建Line图表对象
bar = Bar()

# x 轴
bar.add_xaxis(xaxis_data=x_data)

# 添加年份数据到 y 轴
bar.add_yaxis("本科学历毕业人数", y_data)

# 设置全局
bar.set_global_opts(title_opts=opts.TitleOpts(title="08~22研究生毕业人数变化柱状图"),
                    xaxis_opts=opts.AxisOpts(name="年份"), 
                    yaxis_opts=opts.AxisOpts(name="毕业人数"))

# 生成html文件
bar.render("D:\\FirstProject\\little_project\\python_test\\drawing.html")




    