import requests
import json
import csv

def indexreq():
    vcode = 1
    while vcode == 1:
        countrycode = str(input('\nplease input the country code\n'))
        url = "https://www.henleyglobal.com/proxy?url=https://www.henleypassportindex.com/fetch?url=passports%2F" + countrycode  +"%2Frankings"
        payload={}
        headers = {
            'Cookie': 'PHPSESSID=mudu2s3s60hn9git1l94pgao9t'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        try:
            wellshow = json.loads(response.text)
            square_num=int(0)
            square_tot=len(wellshow)
            while square_num < square_tot:
                print( 'country ' + countrycode  + ' year ' + str(wellshow[square_num]['year']) + ' score is ' + str(wellshow[square_num]['score']))
                square_num = square_num +1
                vcode = vcode +1
        except json.decoder.JSONDecodeError:
            print('\nwrong country code, please try again\n')
            break

while True:
    indexreq()
