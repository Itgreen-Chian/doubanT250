import urllib.request


# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")  # urlopen方法可以直接一个网址打开一个网页（解析网页）
# print(response.read().decode('utf-8'))   # 对获取的网页信息进行utf-8解码

# 获取一个post请求
import urllib.parse   # parse 解析器


# date = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")  #bytes方法把数据转换为二进制
# response = urllib.request.urlopen("http://httpbin.org/post",data=date)
# print(response.read().decode("utf-8"))

# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)  # timeout:超时设置防止程序超时卡死
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("timeout")


# response = urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)  # urllib.error.HTTPError: HTTP Error 418: 状态码418是指“我是一个茶壶”
# # print(response.getheaders())  # getheaders获取网页的头部信息
# print(response.getheader("server"))  # 获取网页头部信息里的server

# 模拟浏览器访问
urls = "http://httpbin.org/post"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"

}
date = bytes(urllib.parse.urlencode({"name":"eric"}), encoding="utf-8")
req = urllib.request.Request(url=urls, data=date, headers=header)  # 构建请求对象
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

# urls = "https://www.douban.com"
# header = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
#
# }
# req = urllib.request.Request(url=urls, headers=header)  # 构建请求对象
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
