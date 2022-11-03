import requests
import fake_useragent
import time
import xml.etree.ElementTree as ET


payload_n = []
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'}
session = requests.Session()
link = 'http://med-demo.bars-open.ru/med2/getmodule.php?Form=System/login&modal=1&baseForm=System/login&theme=bars&cache=c5bdc9d63676b5f7be4b6477c94874a07&cache_enabled=0&session_cache=1&FormCache=59fb4951150e441c9287c8b2a18fe8d8'
link2 = 'http://med-demo.bars-open.ru/med2/getmodule.php?Form=System/lpu&modal=1&baseForm=System/lpu&theme=bars&cache=c5bdc9d63676b5f7be4b6477c94874a07&cache_enabled=0&session_cache=1&FormCache=83b0fd6b469ddbb5e7f324ce350fda3a'
mis = 'http://med-demo.bars-open.ru/med2/getdata.php?Form=PatientSearch/patient_search&baseForm=PatientSearch/patient_search&theme=bars&cache=c5bdc9d63676b5f7be4b6477c94874a07&cache_enabled=0&session_cache=1&FormCache=9b2da650c308bdea2d3b6a5d09911360'
user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

data ={
  "DBPassword": "aaa",
  "DBLogin": "AAA",
  "action": "action",
  "LPU": "10903",
  "EMPLOYER": "21195602",
  "lpu_id": "10903",
  "CABLAB": "21805483",
  "Module": "Authorization",
  "DataSet": "DS_PATIENTS",
  "SURNAME_g0": "иван",
  "FIRSTNAME_g1": "иван",
  "LASTNAME_g2": "иван"
}

responce = session.post(link, data=data, headers=header).text
time.sleep(2)
responce2 = session.post(link2, data=data, headers=header).text

mis_inf = session.post(mis, data=data, headers=header).text

with open('patinfo.xml', 'w', encoding='utf-8') as f:
    f.write(str(mis_inf))

tree = ET.parse('patinfo.xml')
root = tree.getroot()

tree.write('patinf.xml', encoding='utf-8')

for pat in root.findall('row'):
    id = pat.find('ID').text
    fio = pat.find('FULLNAME').text
    card = pat.find('CARD_NUMB').text
    payload = {
        "id": id,
        "fio": fio,
        "card": card
    }
    payload_n.append(payload)

with open('patinf.xml', 'w', encoding='utf-8') as f:
  f.write(str(payload_n))



