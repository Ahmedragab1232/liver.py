import requests
from bs4 import BeautifulSoup as bss4

url = ("https://www.winwin.com/%D9%83%D8%B1%D8%A9-%D9%82%D8%AF%D9%85/%D8%A7%D9%84%D9%81%D8%B1%D9%82/%D9%84%D9%8A%D9%81%D8%B1%D8%A8%D9%88%D9%84/%D8%A7%D9%84%D9%84%D8%A7%D8%B9%D8%A8%D9%88%D9%86")
page=requests.get(url)
print(page)
soup = bss4(page.content, 'html.parser')

players= soup.findAll('div' , {'class' : 'squad-top'})
# print(players)

for player in players:
    player_name = player.find('div','field field--name-node-title field--type-ds field--label-hidden field__item')
    name = player_name.text
    player_position = player.find('div','field field--name-taxonomy-term-title field--type-ds field--label-hidden field__item')
    position = player_position.text
    player_number = player.find('div' , 'field field--name-field-number field--type-integer field--label-hidden field__item')
    number = player_number.text
    club_name = player.find('div','field field--name-field-team field--type-entity-reference field--label-hidden field__item')
    club = club_name.text
    player_nationality = player.find('div','field field--name-field-country-code field--type-string field--label-hidden field__item')
    nationality = player_nationality.text
    info = [name,position,number,club,nationality]
    print(info)
