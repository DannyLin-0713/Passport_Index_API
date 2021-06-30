import csv

def country_code_search():
    while True:
        with open('country_hen.csv',newline='') as csvfile:
            country_name=str(input("please input the country name to search the country code \n"))
            rows = csv.DictReader(csvfile)
            try:
                abb_show = [row[country_name] for row in rows]
                abb_refine = str(abb_show[0])
                print('\nthe country code of ' + country_name + " is "  +abb_refine)
                break
            except KeyError:
                print('\nCountry is not in the database\n')

while True:
    country_code_search()
