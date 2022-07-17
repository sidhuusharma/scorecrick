import requests
import bs4
import sqlite3
conn = sqlite3.connect('score.db')
c = conn.cursor()

c.execute('''CREATE TABLE crscore(live TEXT)''')
link='https://www.cricbuzz.com/live-cricket-scores/38321/eng-vs-ind-3rd-odi-india-tour-of-england-2022'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text ,'html.parser')
details = soup.select('.cb-col-100 .cb-col .cb-col-scores')
c.execute('''INSERT INTO crscore VALUES(?)''',(str(details[0]),))

conn.commit()
#print('completed')
c.execute('''SELECT * FROM crscore''')
results = c.fetchall()[0]
print(results)

conn.close()
