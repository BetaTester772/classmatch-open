from random import randint
import requests
import reqConfig as info
from bs4 import BeautifulSoup

def login(login_id, login_pw):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    headers = {'User-Agent': user_agent,
               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}

    session = requests.Session()
    session.headers.update(headers)

    url_login_page = 'https://hi.hana.hs.kr/member/login.asp'
    session.get(url_login_page)

    url_login_proc = 'https://hi.hana.hs.kr/proc/login_proc.asp'
    login_data = {'login_id': login_id, 'login_pw': login_pw, 'x': str(randint(10, 99)), 'y': str(randint(10, 99))}
    res = session.post(url_login_proc, headers={'Referer': url_login_page}, data=login_data)
    if '로그인 정보가 잘못되었습니다.' in res.text:
        return False
    return session

def get_Id_Name(session):
    soup = BeautifulSoup(session.get('https://hi.hana.hs.kr/SYSTEM_Member/Member/MyPage/mypage.asp').text, 'html.parser')
    return soup.find_all(style='float:right;')[1].text.split(':')[1][1:6], soup.select('[name="MUsr_Name"]')[0].get('value')

def get_Timetable(session):
    soup = BeautifulSoup(session.get('https://hi.hana.hs.kr/SYSTEM_Sugang/Sugang_info/Subject_timeTale/sugang_timetable.asp').text, 'html.parser')
    timetable = soup.find_all('tr')
    timetable_edit=[]
    cls={}
    for i in timetable:
        for j in i.find_all('td'):
             if '교시' not in j.text:
                 timetable_edit.append(j.text.lstrip().split())
    for i in timetable_edit:
        if len(i) != 0:
            del i[-2]
            tot=''
            for j in range(len(i[:-1])):
                tot+=str(i[:-1][j])
                if j+1 < len(i[:-1]):
                    tot+=' '
            cls[tot] = i[-1].split('/')[0].split(':')[1]
    return cls