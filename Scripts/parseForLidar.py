from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from urllib.request import Request
import os , wget


url = 'https://apps.nationalmap.gov/downloader/'

with open((os.path.dirname(__file__) + '\\TNM Download v2.html'),'r') as f:

    soup = BeautifulSoup(f,'html.parser')

    print(soup.prettify() , '\n\nLINKS')

    dL = list()
    for i in soup.find_all('a'):
        if i.text == 'Download Link (LAZ)':
            print(i.get('href'))
            dL.append(i.get('href'))



    u = dL[3]

    import time
    print('\n\n')
    for j in dL:
        time.sleep(2)
        start = time.time_ns()
        print('Starting download...\n',j)
        wget.download(j , 'Data\\autoDownload')
        end = time.time_ns()
        print('###### Download Completed in' , round(((end - start) * 0.000000001),3) , 'seconds ####################')


"""
def reqWrite():

    import requests

    downloaded_obj = requests.get(url)

    with open("python_logo.png", "wb") as file:
        file.write(downloaded_obj.content)

"""
