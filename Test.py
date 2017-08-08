from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.indeed.com/jobs?q=&l=Clovis%2C+NM'

#Opens up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML Parser
page_soup = soup(page_html, "html.parser")

#Grabs each product
row_result = page_soup.findAll('div',{'class':'row result'})
#print(row_result)
print(len(row_result))

#rresult = row_result[0]
rresults = row_result[0]
for rresults in row_result:
    Job_Title = rresults.a['title']

    location = rresults.findAll('span',{'class':'location'})
    Location = location[0].text

    summary = rresults.findAll('span',{'class':'summary'})
    Summary = summary[0].text

    print('Job_Title: ' + (Job_Title))
    print(Location)
    print('Summary: ' + (Summary))
