# for counting the number of times a programming language was used in ideone
import requests
import datetime
import csv
from bs4 import BeautifulSoup

# global variables
programming_languages_used = {}
counter = 1
ideoneString = "https://ideone.com"

def get_content(path):
    r = requests.get(path)
    content = r.content
    print(r.url)
    soup = BeautifulSoup(content,'html.parser')
    return soup

def count_programming_languages_used(soup):
    languagesResult = soup.find_all(class_ = "header")
    for elem in languagesResult:
        spanElement = elem.find('span')
        language = spanElement.string

        if language not in programming_languages_used:
            programming_languages_used[language] = 1
        else:
            programming_languages_used[language] += 1


if __name__ == "__main__":

    contents = get_content(ideoneString + '/recent/'+str(counter))    
    count_programming_languages_used(contents)
    date_variable = datetime.date.today()
    print(date_variable.strftime("%d-%b-%Y"))
    print("Languages used ->",programming_languages_used)

    with open('programs_used_by_ideone.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['date'])
    csvFile.close()

with open('person.csv', 'w') as csvFile2:
    writers = csv.writer(csvFile2)
    writers.writerow(['date'])

csvFile2.close()