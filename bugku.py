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