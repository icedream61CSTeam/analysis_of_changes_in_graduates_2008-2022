from requests_html import HTMLSession
import re
import csv

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

# 打开文件准备写入
with open('output.txt', 'w', encoding='utf-8') as file:
    for url in urls:
        # 发送GET请求获取页面内容
        r = session.get(url, headers=headers)

        # 获取页面文本内容
        page_text = r.html.text

        # 将每个页面的内容写入文件
        file.write(f"URL: {url}\n")
        file.write(page_text)
        file.write("\n\n")

print("数据已保存到 output.txt 文件中")

# pattern = re.compile(r"1\.研究生\sPostgraduates.*?本\s科\sNormal\sCourses", re.DOTALL)
#
# with open('output.txt', 'r', encoding='utf-8') as file:
#     need_text = file.read()
#
# match = pattern.search(need_text)
#
# # 如果匹配成功，提取并保存文本
# if match:
#     extracted_text = match.group(0)
#
#     # 将提取的文本写入文件
#     with open('extracted_text.txt', 'w', encoding='utf-8') as file:
#         file.write(extracted_text)
#
#     print("文本已保存到 extracted_text.txt 文件中")
# else:
#     print("未找到匹配的文本")
#
#
# with open('extracted_text.txt', 'r', encoding='utf-8') as file:
#     csv_text = file.read()
#
# pattern = re.compile(r"""
#     1\.研究生\sPostgraduates\n
#     (?P<graduates_pg>\d+)\n
#     (?P<entrants_pg>\d+)\n
#     (?P<enrolment_pg>\d+)\n
#     博\s士\sDoctor´s\sDegree\n
#     (?P<graduates_phd>\d+)\n
#     (?P<entrants_phd>\d+)\n
#     (?P<enrolment_phd>\d+)\n
#     硕\s士\sMaster´s\sDegree\n
#     (?P<graduates_masters>\d+)\n
#     (?P<entrants_masters>\d+)\n
#     (?P<enrolment_masters>\d+)\n
#     2\.普通本科\sUndergraduates\n
#     (?P<graduates_ug>\d+)\n
#     (?P<entrants_ug>\d+)\n
#     (?P<enrolment_ug>\d+)\n
#     3\.职业本专科\sVocational\sUndergraduate\n
#     (?P<graduates_voc>\d+)\n
#     (?P<entrants_voc>\d+)\n
#     (?P<enrolment_voc>\d+)
# """, re.VERBOSE)
#
# match = pattern.search(csv_text)
#
# # 提取匹配的数据
# data = {
#     "Postgraduates": [
#         match.group("graduates_pg"),
#         match.group("entrants_pg"),
#         match.group("enrolment_pg")
#     ],
#     "PhD": [
#         match.group("graduates_phd"),
#         match.group("entrants_phd"),
#         match.group("enrolment_phd")
#     ],
#     "Master's": [
#         match.group("graduates_masters"),
#         match.group("entrants_masters"),
#         match.group("enrolment_masters")
#     ],
#     "Undergraduates": [
#         match.group("graduates_ug"),
#         match.group("entrants_ug"),
#         match.group("enrolment_ug")
#     ],
#     "Vocational": [
#         match.group("graduates_voc"),
#         match.group("entrants_voc"),
#         match.group("enrolment_voc")
#     ]
# }
#
# # 将数据写入 CSV 文件
# with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Category", "Graduates", "Entrants", "Enrolment"])
#     for category, numbers in data.items():
#         writer.writerow([category] + numbers)
#
# print("数据已保存到 output.csv 文件中")
