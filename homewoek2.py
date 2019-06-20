import urllib.request
import os
host=('http:www.17k.com/chapter/2933095/36699279.html')
response = urllib.request.urlopen(host)
print(response.status)

def mkdir(path):  # 创建文件夹
    is_exists = os.path.exists(path)
    if not is_exists:
        print('创建名字叫做', path, '的文件夹')
        os.makedirs(path)
        print('创建成功！')