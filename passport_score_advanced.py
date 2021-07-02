import requests
import json
import csv

def indexreq():
    vcode = 1
    while vcode == 1:
        countrycode1 = str(input('\nplease input the country code1\n'))
        countrycode2 = str(input('\nplease input the country code2\n'))

        url = "https://www.henleyglobal.com/proxy?url=https://www.henleypassportindex.com/fetch?url=passports%2F" + countrycode1  +"%2Frankings"
        payload={}
        headers = {
            'Cookie': 'PHPSESSID=mudu2s3s60hn9git1l94pgao9t'
        }
        response1 = requests.request("GET", url, headers=headers, data=payload)

        url = "https://www.henleyglobal.com/proxy?url=https://www.henleypassportindex.com/fetch?url=passports%2F" + countrycode2  +"%2Frankings"
        payload={}
        headers = {
            'Cookie': 'PHPSESSID=mudu2s3s60hn9git1l94pgao9t'
        }
        response2 = requests.request("GET", url, headers=headers, data=payload)

        try:
            wellshow1 = json.loads(response1.text)
            wellshow2 = json.loads(response2.text)
            square_num1=int(0)
            square_num2=int(0)
            square_tot1=len(wellshow1)
            square_tot2=len(wellshow2)

            print("\n" + countrycode1)

            while square_num1 < square_tot1:
                print( 'country ' + countrycode1  + ' year ' + str(wellshow1[square_num1]['year']) + ' score is ' + str(wellshow1[square_num1]['score']))
                square_num1 = square_num1 +1
                vcode = vcode +1

            print("\n" + countrycode2)
            
            while square_num2 < square_tot2:
                print( 'country ' + countrycode2  + ' year ' + str(wellshow2[square_num2]['year']) + ' score is ' + str(wellshow2[square_num2]['score']))
                square_num2 = square_num2 +1
                vcode = vcode +1

            square_num1=int(0)
            square_num2=int(0)
            print("\n" + countrycode1 + " and " + countrycode2 + " comparison  ")

            try:
                while square_num1 < square_tot1 or square_num2 < square_tot2:
                    print( 'country ' + countrycode1 + ' compete ' + countrycode2   + ' year ' + str(wellshow2[square_num2]['year'])  +' power result  is ' )
                    print(int(wellshow1[square_num1]['score']) - int(wellshow2[square_num2]['score']))
                    square_num1 = square_num1 +1
                    square_num2 = square_num2 +1
                    vcode = vcode +1
            except TypeError:
                print("No Score")

        except json.decoder.JSONDecodeError:
            print('\nwrong country code, please try again\n')
            break

def country_code_search(country_name):
    while True:
        with open('country_hen.csv',newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            try:
                abb_show = [row[country_name] for row in rows]
                abb_refine = str(abb_show[0])
                print('\nthe country code of ' + country_name + " is "  +abb_refine)
                break
            except KeyError:
                print('\nCountry'+ country_name  +'is not in the database\n')

while True:
    country_name=str(input("please input the country name to search the country code \n"))
    country_code_search(country_name)
    print("\n==========Please use the country code returned by the script to search==========\n")
    indexreq()
