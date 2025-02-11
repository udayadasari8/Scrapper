import requests
import re
import bs4
import csv
url = "https://www.agroinfomedia.com/index.php"
res = requests.get(url)
# html_content = res.text
hlinks=[]
links = re.findall(r'(category\.php\?id=(.*?)&amp;&amp;idd=0)(.*?)strong',res.text)
for link in links:
    a=re.sub("amp;","",link[0])
    b=re.sub(" ","%20",a)
    hlinks.append("https://www.agroinfomedia.com/"+b)

# print(hlinks[6])
slinks=[]
for i in hlinks:
    print(i,"scraping this header link")
    res2=requests.get(i)
    link2=re.findall(r'(company-info\.php\?\d{3}\/(.*?))style',res2.text)
    for link in link2:
        a=(re.sub("\"","",link[0]))
        b=("https://www.agroinfomedia.com/"+a)
        slinks.append(b)
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    

    headerscsv = ['URL Scraped', 'Label', 'Value']
    writer.writerow(headerscsv) 
    for j in slinks:
        print(j,"scraping this sublink")
        res3=requests.get(j)
            # soup=bs4.BeautifulSoup(res.text,'html.parser')
            # data=soup.find_all(class_="style2")
            # print(data)
        h=re.findall(r'<strong>((.*?)):(.*?)\s(.*?)\s(.*?)class="style2">((.*?))<',res3.text)
        # print(i[0],i[5])

        for i in h:
            row=[j,i[0],i[5]]
            writer.writerow(row)


    