from random import randint
import requests
import reqConfig as info
from bs4 import BeautifulSoup

def login(login_id, login_pw):
    session = requests.Session()
    session.headers.update(info.headers)

    url_login_page = 'https://go.hana.hs.kr/login.do'
    session.get(url_login_page)

    url_login_proc = 'https://go.hana.hs.kr/json/loginProc.ajax'
    login_data = {'mUsr_ID': login_id, 'mUsr_PW': login_pw, 'loginArr': 'test1,test2,test6,teste,teste10,teste11,teste12,teste13,teste2,teste3,teste4,teste5,teste7,teste8,testest,testI,testm,testo,testp,tests,tests1,tests2,tests22,tests3', 'push_Token': ''}
    res = session.post(url_login_proc, headers=info.headers, data=login_data)
    if res.text.split('"')[3] == 'fail':
        return 'fail'
    while res.text.split('"')[3] == 'loginCheck':
        res = session.post(url_login_proc, headers=info.headers, data=login_data)
    return session

def get_Id_Name(login_id, login_pw):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    headers = {'User-Agent': user_agent,
               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}

    session = requests.Session()
    session.headers.update(headers)

    url_login_page = 'https://hi.hana.hs.kr/member/login.asp'
    session.get(url_login_page)

    url_login_proc = 'https://hi.hana.hs.kr/proc/login_proc.asp'
    login_data = {'login_id': login_id, 'login_pw': login_pw, 'x': str(randint(10, 99)), 'y': str(randint(10, 99))}
    session.post(url_login_proc, headers={'Referer': url_login_page}, data=login_data)

    soup = BeautifulSoup(session.get('https://hi.hana.hs.kr/SYSTEM_Member/Member/MyPage/mypage.asp').text, 'html.parser')
    return soup.find_all(style='float:right;')[1].text.split(':')[1][1:6], soup.select('[name="MUsr_Name"]')[0].get('value')

