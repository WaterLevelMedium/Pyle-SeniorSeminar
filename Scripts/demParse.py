from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from urllib.request import Request
import os , wget


url = 'https://apps.nationalmap.gov/downloader/'

with open((os.path.dirname(__file__) + '\\NED3DEP.html'),'r') as f:

    soup = BeautifulSoup(f,'html.parser')

    #print(soup.prettify() , '\n\nLINKS')

    dL = list()
    for i in soup.find_all('a'):
        if i.text == 'Download Link (ZIP)' or i.text == 'Download Link (TIF)':
            print(i.get('href'))
            dL.append(i.get('href'))




    import time ,os
    os.chdir(os.path.dirname(__file__))
    print('\n')
    for j in dL:
        time.sleep(2)
        start = time.time_ns()
        print('Starting download...\n',j)
        print(os.getcwd())
        cmd = str('curl "' + j + '"  --output "' + j[-26:] + '"') # working... 28 instead of 33 char from end
        print(cmd)
        #os.system(cmd)
        #nCmd = '(New-Object System.Net.WebClient).DownloadString(' + j + ')'
        os.system(cmd)

        #reqWrite(j,j[21:])
        #wget.download(j , '\\demParse')
        #install(str(j),'autoDownload')
        end = time.time_ns()
        print('###### Download Completed in' , round(((end - start) * 0.00000001),3) , 'seconds ####################')
