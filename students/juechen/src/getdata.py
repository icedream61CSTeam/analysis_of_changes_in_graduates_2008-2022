from requests_html import HTMLSession # type: ignore
import os

# 创建HTMLSession对象
session = HTMLSession()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 "
                  "Safari/537.36"
}

# 定义15年(2008-2022)URL列表
urls = [
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/2022/quanguo/202401/t20240110_1099539.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/2021/quanguo/202301/t20230104_1038067.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/2020/quanguo/202108/t20210831_556364.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/jytjsj_2019/qg/202006/t20200611_464803.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/jytjsj_2018/qg/201908/t20190812_394239.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/jytjsj_2017/qg/201808/t20180808_344698.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/jytjsj_2016/2016_qg/201708/t20170823_311668.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/jytjsj_2015/2015_qg/201610/t20161012_284510.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/jytjsj_2014/2014_qg/201509/t20150902_205106.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/s8492/s8493/201412/t20141215_181593.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/s7567/201309/t20130904_156896.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/s7382/201305/t20130529_152564.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/s6200/201201/t20120117_129518.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/s4958/s4959/201012/t20101229_113484.html',
    'http://www.moe.gov.cn/jyb_sjzl/moe_560/s4628/s4631/201010/t20101021_109983.html'
]

# 构建目标文件的相对路径
output_file_path = '../output/output.txt'

# 确保目标目录存在，如果不存在则创建
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# 打开文件准备写入
with open(output_file_path, 'w', encoding='utf-8') as file:
    for url in urls:
        try:
            # 发送GET请求获取页面内容
            r = session.get(url, headers=headers)

            # 检查响应状态码和内容
            if r.status_code == 200 and r.html:
                # 获取页面文本内容
                page_text = r.html.text

                # 将每个页面的内容写入文件
                file.write(f"URL: {url}\n")
                file.write(page_text)
                file.write("\n\n")
            else:
                print(f"无法获取内容，URL: {url}")
        except Exception as e:
            print(f"请求失败，URL: {url}, 错误: {e}")

print(f"数据已保存到 {output_file_path} 文件中")

