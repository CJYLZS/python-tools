'''

POST https://www.qingline.net/api/pc/login HTTP/1.1
Host: www.qingline.net
Connection: keep-alive
Content-Length: 37
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
Accept: application/json, text/plain, */*
Content-Type: application/json;charset=UTF-8
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnFpbmdsaW5lLm5ldFwvYXBpXC93ZWNoYXRcL3Rva2VuLWxvZ2luIiwiaWF0IjoxNjQwMDAxNTU5LCJleHAiOjE2NDUxODU1NTksIm5iZiI6MTY0MDAwMTU1OSwianRpIjoiTklrVTlmV2VTSDVYRWNHYyIsInN1YiI6MTk1MTM2LCJwcnYiOiI1MWNkNmVjNzA0YWY3NjhkODYzZWQ5MGU1ZjQyZmU4NjM5MDU1NmZlIn0.cKKv4HIf08oRku1ZvJf-FRjdflnwZl7BX_kxUk9nXak
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: https://www.qingline.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.qingline.net/login/email
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=17cfd56bcd0ceb-0f7749aace1fcc-c343365-384000-17cfd56bcd1af1; CNZZDATA1279193991=1285448396-1636336609-%7C1639998429; token=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnFpbmdsaW5lLm5ldFwvYXBpXC93ZWNoYXRcL3Rva2VuLWxvZ2luIiwiaWF0IjoxNjQwMDAxNTU5LCJleHAiOjE2NDUxODU1NTksIm5iZiI6MTY0MDAwMTU1OSwianRpIjoiTklrVTlmV2VTSDVYRWNHYyIsInN1YiI6MTk1MTM2LCJwcnYiOiI1MWNkNmVjNzA0YWY3NjhkODYzZWQ5MGU1ZjQyZmU4NjM5MDU1NmZlIn0.cKKv4HIf08oRku1ZvJf-FRjdflnwZl7BX_kxUk9nXak; userinfo={%22id%22:95098%2C%22verified%22:null%2C%22student_number%22:%22201908010417%22%2C%22grade%22:3%2C%22university_id%22:2054%2C%22phone%22:18640311811%2C%22avatar_url%22:%22https://thirdwx.qlogo.cn/mmopen/vi_32/p3mKOvThoqsnZqx4ZMEPdfOnicphibk2pQne1iaFQC2922ibibK40LklSqkmGCDxLyMmSmZFYZlbviazuhibicm6cRTYcA/132%22%2C%22email%22:%22691086891@qq.com%22%2C%22real_name%22:%22%E5%BC%A0%E6%99%8B%22%2C%22rank%22:%22%22%2C%22university_name%22:%22%E6%B9%96%E5%8D%97%E5%A4%A7%E5%AD%A6%22%2C%22position%22:%22%22%2C%22teacher_number%22:%22%22%2C%22identity_number%22:%22%22%2C%22nick_name%22:%22YLZS%22%2C%22user_type%22:2%2C%22department%22:%22%E4%BF%A1%E6%81%AF%E7%A7%91%E5%AD%A6%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%22%2C%22major%22:%22%E8%AE%A1%E7%A7%91%22}

{"account":"1@a.cn","password":"abc"}

CONVERT TO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

req_url = 'https://www.qingline.net/api/pc/login'
req_headers = {
    'Host':'www.qingline.net',
    'Connection':'keep-alive',
    'Content-Length':'37',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'Accept':'application/json, text/plain, */*',
    'Content-Type':'application/json;charset=UTF-8',
    'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnFpbmdsaW5lLm5ldFwvYXBpXC93ZWNoYXRcL3Rva2VuLWxvZ2luIiwiaWF0IjoxNjQwMDAxNTU5LCJleHAiOjE2NDUxODU1NTksIm5iZiI6MTY0MDAwMTU1OSwianRpIjoiTklrVTlmV2VTSDVYRWNHYyIsInN1YiI6MTk1MTM2LCJwcnYiOiI1MWNkNmVjNzA0YWY3NjhkODYzZWQ5MGU1ZjQyZmU4NjM5MDU1NmZlIn0.cKKv4HIf08oRku1ZvJf-FRjdflnwZl7BX_kxUk9nXak',
    'sec-ch-ua-mobile':'?0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform':'"Windows"',
    'Origin':'https://www.qingline.net',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Dest':'empty',
    'Referer':'https://www.qingline.net/login/email',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'UM_distinctid=17cfd56bcd0ceb-0f7749aace1fcc-c343365-384000-17cfd56bcd1af1; CNZZDATA1279193991=1285448396-1636336609-%7C1639998429; token=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnFpbmdsaW5lLm5ldFwvYXBpXC93ZWNoYXRcL3Rva2VuLWxvZ2luIiwiaWF0IjoxNjQwMDAxNTU5LCJleHAiOjE2NDUxODU1NTksIm5iZiI6MTY0MDAwMTU1OSwianRpIjoiTklrVTlmV2VTSDVYRWNHYyIsInN1YiI6MTk1MTM2LCJwcnYiOiI1MWNkNmVjNzA0YWY3NjhkODYzZWQ5MGU1ZjQyZmU4NjM5MDU1NmZlIn0.cKKv4HIf08oRku1ZvJf-FRjdflnwZl7BX_kxUk9nXak; userinfo={%22id%22:95098%2C%22verified%22:null%2C%22student_number%22:%22201908010417%22%2C%22grade%22:3%2C%22university_id%22:2054%2C%22phone%22:18640311811%2C%22avatar_url%22:%22https://thirdwx.qlogo.cn/mmopen/vi_32/p3mKOvThoqsnZqx4ZMEPdfOnicphibk2pQne1iaFQC2922ibibK40LklSqkmGCDxLyMmSmZFYZlbviazuhibicm6cRTYcA/132%22%2C%22email%22:%22691086891@qq.com%22%2C%22real_name%22:%22%E5%BC%A0%E6%99%8B%22%2C%22rank%22:%22%22%2C%22university_name%22:%22%E6%B9%96%E5%8D%97%E5%A4%A7%E5%AD%A6%22%2C%22position%22:%22%22%2C%22teacher_number%22:%22%22%2C%22identity_number%22:%22%22%2C%22nick_name%22:%22YLZS%22%2C%22user_type%22:2%2C%22department%22:%22%E4%BF%A1%E6%81%AF%E7%A7%91%E5%AD%A6%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%22%2C%22major%22:%22%E8%AE%A1%E7%A7%91%22}'
    }
req_body = '{"account":"1@a.cn","password":"abc"}'

req = requests.post(url = req_url, headers = req_headers, data = req_body, verify = False)
print(req.text)

'''


import pyperclip


def post_convert(lines):
    url_code = 'req_url = \'' + lines[0].split(' ')[1] + '\'\n'
    lines = lines[1:]
    # {"":""}
    head_code = 'req_headers = {\n    '
    for i in range(len(lines)):
        if lines[i] == '':
            lines = lines[i+1:]
            break
        elif lines[i+1] != '':
            part_head = '\'' + \
                lines[i].split(':')[0]+'\':\'' + \
                ':'.join(lines[i].split(':')[1:]).strip()+'\',\n    '
            head_code += part_head
        else:
            part_head = '\'' + \
                lines[i].split(':')[0]+'\':\'' + \
                ':'.join(lines[i].split(':')[1:]).strip()+'\'\n    '
            head_code += part_head
    head_code += '}\n'
    body_code = 'req_body = \''
    for line in lines:
        body_code += line
    body_code += '\'\n'
    return url_code + head_code + body_code


def get_convert(lines):
    url_code = 'req_url = \'' + lines[0].split(' ')[1] + '\'\n'
    lines = lines[1:]
    # {"":""}
    head_code = 'req_headers = {\n    '
    for i in range(len(lines)):
        if lines[i] == '':
            lines = lines[i+1:]
            break
        elif lines[i+1] != '':
            part_head = '\'' + \
                lines[i].split(':')[0]+'\':\'' + \
                ':'.join(lines[i].split(':')[1:]).strip()+'\',\n    '
            head_code += part_head
        else:
            part_head = '\'' + \
                lines[i].split(':')[0]+'\':\'' + \
                ':'.join(lines[i].split(':')[1:]).strip()+'\'\n    '
            head_code += part_head
    head_code += '}\n'
    return url_code + head_code


all_text = pyperclip.paste()

lines = all_text.split("\r\n")

code_start = 'import requests\nimport urllib3\nurllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)\n\n'

# get request mode
request_mode = lines[0].split(' ')[0]
if request_mode == 'POST':
    code_end = '\nreq = requests.post(url = req_url, headers = req_headers, data = req_body, verify = False)\nprint(req.text)'
    pyperclip.copy(code_start + post_convert(lines) + code_end)
elif request_mode == 'GET':
    code_end = '\nreq = requests.get(url = req_url, headers = req_headers, verify = False)\nprint(req.text)'
    pyperclip.copy(code_start + get_convert(lines) + code_end)

# print(sourse)
