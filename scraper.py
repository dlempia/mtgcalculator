import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def calculateMedian(result_list):

    float_list = []
    for item in result_list:
        if isinstance(float(item), float):
            float_list.append(float(item))
    

    final_list = []
    if (len(float_list) > 0): 
        comp = float_list[0]
        for i in float_list:
            if not i > comp * 4 or i * 4 < comp:
                final_list.append(i)
                comp = i 
    return sum(final_list)/len(final_list)


def fetchmedian(name): 

    append_to_end = name.replace(' ', '%20')

    url = 'https://shop.tcgplayer.com/productcatalog/product/show?newSearch=false&ProductType=All&IsProductNameExact=false&ProductName=' + append_to_end #need to add card name tags separated by %20

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    resultList = []
    #uncomment and indent up to next comment block for averages also change 0 to i
    #for i in range (0, len(soup.findAll('dd'))):
    one_dd = soup.findAll('dd')[0]
    cleaned = one_dd.get_text()
    if (cleaned.strip('$') != 'Unavailable'): 
        resultList.append(cleaned.strip('$'))
#push to here
    return (calculateMedian(resultList))
#uncomment below for testing? 
#fetchmedian("mox opal")
