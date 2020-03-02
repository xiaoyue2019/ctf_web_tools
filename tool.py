import re,requests,math,base64

class tool():

    def __init__(self):
        self.val=requests.Session()

    def get_webs(self,url,baochi=False,ifline=False,fhgeshi='text',bmgeshi='utf8'):
        '''
        获取网页源码
        baochi设置是否维持session
        ifline设置是否逐行返回，默认不 如果不逐行返回那么将返回一个对象，转文本这里给个demo：
        .text.encode('raw_unicode_escape' ).decode(bmgeshi)
        fhgeshi设置是否返回字节集数据，如需要下载图片
        bmgeshi设置编码格式，默认utf8
        '''
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
        }
        if fhgeshi=='text':
            if baochi:
                if ifline:
                    res=[]
                    for i in self.val.get(url).text.encode('raw_unicode_escape' ).decode(bmgeshi).split('\n'):
                        #raw_unicode_escape 将含有byte格式的字符串转换成byte格式。再用utf8对其decode为文本。
                        res.append(i)
                    return res
                else:
                    return self.val.get(url)
            else:
                if ifline:
                    res=[]
                    for i in requests.get(url,headers).text.encode('raw_unicode_escape' ).decode(bmgeshi).split('\n'):
                        #raw_unicode_escape 将含有byte格式的字符串转换成byte格式。再用utf8对其decode为文本。
                        res.append(i)
                    return res
                else:
                    return requests.get(url,headers)
        elif fhgeshi=='byte':
            return requests.get(url,headers).content

    def get_post(self,url,method,data,baochi=False,ifcom=True,bmgeshi='utf8'):
        '''
        get_post
        ifcom设置是否启用headers 默认启用
        baochi设置是否维持session
        bmgeshi设置编码格式，默认utf8
        '''
        if ifcom:
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
                }
        if baochi:
            if method=='get':
                res=self.val.get(url,params=data,headers=headers).text.encode('raw_unicode_escape' ).decode(bmgeshi)
            else:
                res=self.val.post(url,data=data,headers=headers).text.encode('raw_unicode_escape' ).decode(bmgeshi)
            return res
        else:
            if method=='get':
                res=requests.get(url,params=data,headers=headers).text.encode('raw_unicode_escape' ).decode(bmgeshi)
            else:
                res=requests.post(url,data=data,headers=headers).text.encode('raw_unicode_escape' ).decode(bmgeshi)
            return res

    def bm_unic2acs(self,data,geshi="&#"):
        '''
        Unicode转str
        geshi设置Unicode的三种格式：
        1.&#
        2.&#*
        3.u
        '''

        if geshi=='&#':
            data=re.findall('&#([0-9]+);',data,re.S)
            _=[chr(int(i)) for i in data]
        if geshi=='&#x':
            data=re.findall('&#x([0-9a-zA-Z]+);',data,re.S)
            _=[chr(int(i,16)) for i in data]
        if geshi=='u':
            data=re.findall('u([0-9A-Za-z]+)',data,re.S)
            print(data)
            _=[chr(int(i,16)) for i in data]
        return ''.join(_)

    def bm_zhalan(self,data,ifencode=True):
        '''
        栅栏密码加密解密
        ifencode设置是否为加密 默认是加密
        '''
        data=data.strip()
        if ifencode and data is not None:
            result=[]
            for j in range(2,len(data)+1):
                dd={}
                cc=""
                for i in range(0,len(data),j):
                    for ii in range(0,j):
                        try:
                            data[i:i+j:][ii]
                            try:
                                dd[str(ii)]+=data[i:i+j:][ii]
                            except Exception:
                                dd[str(ii)]=data[i:i+j:][ii]
                        except Exception:
                            pass
                for i in range(len(dd)):
                        cc+=dd[str(i)]
                result.append('第'+str(i+1)+"栏:  "+cc)
            return result
            # 13524  135 24
            # 135246  135 246
        else:
            res=[]
            for group_number in range(2,len(data)+1):
                def cut_string(string,length):
                    textArr=re.findall('.{'+str(length)+'}',string)
                    textArr.append(string[len(textArr)*length:])
                    return textArr
                group_char_number=int(math.floor(len(data)/group_number))
                add_char_number=len(data)%group_number
                TS_list1=cut_string(data[:((group_char_number+1)*add_char_number)],group_char_number+1)
                TS_list2=cut_string(data[((group_char_number+1)*add_char_number):],group_char_number)
                TS_list=TS_list1+TS_list2
                result_str=''
                for i in range(group_char_number+1):
                    for j in range(len(TS_list)):
                        try:
                            result_str=result_str+TS_list[j][i]
                        except:
                            pass
                res.append('第'+str(group_number)+'栏:  '+result_str) 
            return res

    def bm_base64_decode(self,data):
        '''
        64,32,16的贝斯转换。
        输出按照16,32,64从左往右
        加密同
        '''
        res16_='转换失败'.encode()
        res32_='转换失败'.encode()
        res64_='转换失败'.encode()
        try:
            res16_=base64.b16decode(data.encode())
        except Exception:
            pass
        try:
            res64_=base64.b64decode(data.encode())
        except Exception:
            pass
        try:
            res32_=base64.b32decode(data.encode())
        except Exception:
            pass
        return res16_.decode(),res32_.decode(),res64_.decode()
        
    def bm_base64_encode(self,data):
        res16='转换失败'
        res32='转换失败'
        res64='转换失败'
        try:
            res16=base64.b16encode(data.encode())
            res64=base64.b64encode(data.encode())
            res32=base64.b32encode(data.encode())
        except Exception:
            pass
        return res16,res32,res64

    def bm_mors(self,data,sign):
        '''
        莫斯解密
        sign设置分隔符
        '''
        res=''
        MorseList = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
        "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
        "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
        "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
        "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
        "....": "&", ".--.-.": "@", ".-.-.": "+",
                }
        # 分割，字符串string，分割标识符sign
        lists = data.split(sign)
        for code in lists:
            res+=MorseList.get(code)
        return res

if __name__ == "__main__":
    # tool=tool()
    # print(tool.bm_mors('...--/.----/..---/..-./--./.-/..-./--.','/'))
    # _=tool.bm_unic2acs(r'\u0064\u0066\u0061\u0064\u0073\u0066\u0061\u0067\u516c\u79c1\u517c\u987e','u')
    # _=tool.bm_unic2acs('&#x7F16;&#x7801;&#x89E3;&#x7801;','&#x')
    # print(tool.bm_zhalan('123456789'))
    # _=tool.bm_zhalan(r'KYsd3js2E{a2jda}',False)
    # for i in _:
    #     print(i)
    # print(_)
    # print(tool.get_webs('https://img-blog.csdnimg.cn/20190927151053287.png',True,'byte'))
    # with open('e:/大学生活/网络安全课/Python脚本/1.jpg','wb') as f:
    #     f.write(tool.get_webs('https://img-blog.csdnimg.cn/20190927151053287.png',True,'byte'))
    # print(tool.bm_base64_encode('dfasdfsdffasdf'))
    # print(tool.bm_base64_decode('ZGZhc2Rmc2RmZmFzZGY='))
    pass
    