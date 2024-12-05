import pandas as pd
import requests
import lxml
from bs4 import BeautifulSoup

date = input("Write The Matches Date (MM/DD/YYYY): ")

def get_matches(date):
    
    url = f'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    global Result
    Result = pd.DataFrame(columns=('نتيجة المباراة', 'موعد المباراة', 'الفريق الثاني', 'الفريق الأول', 'البطولة'))
    
    all_champions = soup.find_all('div', {'class': 'matchCard'})
    
    for i in range(len(all_champions)):
        # Championship Name    
        championship = all_champions[i].find('div', {'class': 'title'}).find('h2').text.strip()
        all_matches = all_champions[i].find_all('div', {'class': 'item'})
        for i in range(len(all_matches)):
            # Teams Names
            first_team = all_matches[i].find('div', {'class': 'teamA'}).find('p').text.strip()
            second_team = all_matches[i].find('div', {'class': 'teamB'}).find('p').text.strip()
            # Match Time
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
            # Match Record
            score1 = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})[1].text.strip()
            score2 = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})[0].text.strip()
            full_score = str( str(score1) + ' - '  + str(score2) )
            
            full_match_data = [full_score, match_time, second_team, first_team, championship]
            Result.loc[len(Result)] = full_match_data
    print(Result)
    Result.to_excel(r'E:\webscraping\matches_by_day.xlsx')

get_matches(date)
