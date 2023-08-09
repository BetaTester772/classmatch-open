from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
import utils
import reqConfig as info
from random import randint
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import os
from pathlib import Path
import pymysql

db_config = {
    "host": "",
    "user": "",
    "password": "",
    "database": ""
}

# MySQL에 연결
connection = pymysql.connect(**db_config)

# 커서 생성
cursor = connection.cursor()

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
root = os.path.dirname(os.path.abspath(__file__))
app = FastAPI()
class resisterData(BaseModel):
  id: str
  pw: str

class matchData(BaseModel):
  id1: str
  id2: str

app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

@app.post("/resister")
def index(userInfo:resisterData):
  session = utils.login(userInfo.id, userInfo.pw)
  if session == 'fail':
    return '계정이 잘못되었습니다'

  res = session.post('https://go.hana.hs.kr/json/userTimeTable.ajax', headers=info.headers, data={'mcode': '106'})
  timetable = eval(res.content)["resultList"]
  cls1 = {}

  for i in timetable:
    cls1[i['scodeName']] = i['divCode']

  userid, username = utils.get_Id_Name(userInfo.id,userInfo.pw)
  query = f'SELECT * FROM table WHERE var="{userid}"'
  cursor.execute(query)
  if len(cursor.fetchall()) != 0:
    query = f'UPDATE table SET var="{cls1}" WHERE var="{userid}"'
    cursor.execute(query)
    connection.commit()
  else:
    query = f'INSERT INTO table VALUES ("{userid}", "{username}", "{cls1}")'
    cursor.execute(query)
    connection.commit()
  return 'success'


@app.post("/match")
def index(userInfo:matchData):
  query = f'SELECT * FROM table WHERE var="{userInfo.id1}"'
  cursor.execute(query)
  cls1 = cursor.fetchall()
  if len(cls1) == 0:
    return '이름1은 등록되지 않은 이름입니다'
  cls1 = eval(cls1[0][2])

  query = f'SELECT * FROM table WHERE var="{userInfo.id2}"'
  cursor.execute(query)
  cls2 = cursor.fetchall()
  if len(cls2) == 0:
    return '이름2는 등록되지 않은 이름입니다'
  cls2 = eval(cls2[0][2])
  match = []
  for i in cls1.keys():
    try:
      if cls1[i] == cls2[i]:
        match.append(i + '(' + cls1[i] + '분반)')
    except:
      print('두번째 유저는 과목', i + '이(가) 없습니다')
  print(match)
  return match