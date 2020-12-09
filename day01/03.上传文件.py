'''
接口的功能是上传文件，比如上传头像，附件等
'''
import requests
url = "http://www.httpbin.org/post"

file = r"D:\test.txt"
with open(file, 'r') as f:
    #字典，上传的文件：文件相关参数组成的元祖
    # text/plain 是文件的类型
    load = {"file1": (file, f, "text/plain")}
    r = requests.post(url, files = load)
    #print(r.text)

#上传图片
file1 = r"D:\a.jpg"
with open(file1,'rb') as d:
    load = {"file2":(file1,d,"image/jpg")}
    #文件名：file-tuple
    #file-tuple 可以是二元组、三元组、四元组
    #img/png MIME类型，文件类型，application/json application/
    r = requests.post(url,files =load)
    # print(r.text)

#可以一次上传多个文件，文本和图片一起上传
with open(file,'r') as f1:
    with open(file1,'rb') as f2:
        load = {"file1": (file, f1, "text/plain"), "file2": (file1, f2, "image/jpg")}
        r = requests.post(url, files=load)
        print(r.text)