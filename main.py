import requests, random, json
from datetime import datetime

class Register(object):
    def __init__(self) -> None:
        self.client_id = "Y0PhbwALAAG71nw-um7G8FM64Mrn"
    
    def send_sms(self, phone_number: str):
        url = "https://www.instagram.com/accounts/send_signup_sms_code_ajax/"
        s = requests.Session()
        post = dict(s.get("https://www.instagram.com/").cookies)
        cookies = ''
        for key, value in post.items():
            cookies+=key+'='+value+";"
        headers = {
            'accept': "*/*",
            'authority': "www.instagram.com",
            'content-type': "application/x-www-form-urlencoded",
            'cookie': cookies,
            'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
            'x-csrftoken': post['csrftoken'],
        }
        sss = requests.get("https://www.instagram.com/", headers=headers).text
        self.x_instagram_ajax = sss.split('''rollout_hash":"''')[1].split('",')[0]
        self.headers = {
            'accept': "*/*",
            'authority': "www.instagram.com",
            'content-type': "application/x-www-form-urlencoded",
            'cookie': cookies,
            'origin': "https://www.instagram.com",
            'referer': "https://www.instagram.com/accounts/emailsignup/",
            'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
            'x-csrftoken': post['csrftoken'],
            'x-instagram-ajax': self.x_instagram_ajax,
            'x-asbd-id': "198387",
            'x-ig-app-id': "936619743392459",
            'x-requested-with': "XMLHttpRequest"
        }
        data = {
            'client_id': self.client_id,
            'phone_number': phone_number,
            'phone_id': "",
            'big_blue_token': "",
            'captcha_token': "",
        }
        post = requests.post(url, headers=self.headers, data=data)
        print(post.text)
        # except:
        #     pass

    def reg_account(self, phone_number: str, username: str, fullName: str,password: str, otp: str):
        time = int(datetime.now().timestamp())
        data = {
            'enc_password': password,
            'phone_number': phone_number,
            'username': username,
            'first_name': fullName,
            'month': str(random.randint(1,12)),
            'day': str(random.randint(1,30)),
            'year': str(random.randint(1989, 2002)),
            'sms_code': otp,
            "client_id": self.client_id,
            'seamless_login_enabled': "1",
            "tos_version": "row"
        }
        print(json.loads(json.dumps(data, indent=4)))
        url = "https://www.instagram.com/accounts/web_create_ajax/"
        print(requests.post(url, headers=self.headers, data=data).text)


re = Register()
phone = "+84328193448"
re.send_sms(phone)
otp = input("Nhập Code Tay: ")
#2006Tai
password = '#PWD_INSTAGRAM_BROWSER:10:1665389578:AfJQANwjxpPr458OrQXn6D6EnFbn9usVH2/iQDE3/cPEipd0xOanawkCq4TLtf60X/ZQzN0RdKxToJwJrN7Ya0XGLP0beKNa45wOcLWFkQ4s1qYC4hiLjhu/eogR0VVg1OIec3F/dtKTwpA='
re.reg_account(phone, "taile.official"+str(random.randint(1,999)), "Lê Anh Tuấn",password,otp)
