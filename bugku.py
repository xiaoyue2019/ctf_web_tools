import tool
import re
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

tool=tool.tool()
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

_=tool.get_webs('http://123.206.87.240:8002/web3/',ifline=True)
for i in _:
	print(i)