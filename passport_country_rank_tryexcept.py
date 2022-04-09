import requests
import json


def country_rank_printing(country_abbr):

    # define the request process

    url = "https://www.henleyglobal.com/proxy?url=https://www.henleypassportindex.com/api/passports/" + country_abbr + "/rankings"
    response = requests.request("GET", url)
    
    struct_response = json.loads(response.text)

    # prepare the length of response
   
    len_structure_sum = len(struct_response)
    len_start = int(0)

    # prepare the empty lists

    list_year = []
    list_rank = []
    list_multi = []

    # data writing into the lists

    while len_start < len_structure_sum:
        ranking_show = str(struct_response[len_start]['rank'])
        year_show = str(struct_response[len_start]['year'])
        conbining_show = year_show + " year ranking " + ranking_show
        list_multi.append(conbining_show)
        len_start = len_start + 1

    # sorting and preparing the data list

    list_multi.sort(reverse = False)
    list_start = int(0)
    list_num = len(list_multi)

    # print the sorted list

    while list_start < list_num:
        print(list_multi[list_start])
        list_start = list_start + 1

# running the program

while True:
    try:
        real_inside = input("please input the country abbreviation that you want to search \n")
        print("country " + real_inside + " passport ranking is")
        country_rank_printing(real_inside)
    except json.JSONDecodeError:
        print(str(real_inside) +  " is Not a Country code or country code not found, please try again\n")
