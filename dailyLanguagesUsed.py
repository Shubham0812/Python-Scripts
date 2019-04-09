# for counting the number of times a programming language was used in ideone
import requests
import datetime
import csv
import os
import time
from bs4 import BeautifulSoup

# global variables
programming_languages_used = {}
counter = 1
ideoneString = "https://ideone.com"
dir_path = os.path.dirname(os.path.realpath(__file__))
file_name =  dir_path + "/" +"programming_language_used.csv"

def get_content(path):
    r = requests.get(path)
    content = r.content
    print(r.url)
    soup = BeautifulSoup(content,'html.parser')
    return soup

def count_programming_languages_used(soup):
    line_count = 0
    if os.path.isfile(file_name):   
        print("File exists") 
        with open(file_name,'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',') 
            for row in csv_reader:
                print("test row ->",row[1])
                if line_count == 0:
                    pass
                else:
                    programming_languages_used[row[1]] = int(row[2])
                line_count += 1
        print("After reading file",programming_languages_used)


    languagesResult = soup.find_all(class_ = "header")
    for elem in languagesResult:
        spanElement = elem.find('span')
        language = spanElement.string

        if language not in programming_languages_used:
            programming_languages_used[language] = 1
        else:
            programming_languages_used[language] += 1


def write_data_in_csvfile(programming_language_dictionary):
    date_variable = datetime.date.today()

    programming_languages = list(programming_language_dictionary.keys())
    programming_languages_count = list(programming_language_dictionary.values())
    print(date_variable.strftime("%d-%b-%Y"))

    if os.path.isfile(file_name):
        with open(file_name,'w+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['Date','Programming Language','Count'])
    
    for index in range(0,len(programming_languages)):
        write_in_excel = []
        write_in_excel.append(date_variable)
        write_in_excel.append(programming_languages[index])
        write_in_excel.append(programming_languages_count[index])

        with open(file_name,'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(write_in_excel)


if __name__ == "__main__":
    t1 = time.time()
    if not os.path.isfile(file_name):
        with open(file_name,'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['Date','Programming Language','Count'])

    contents = get_content(ideoneString + '/recent/'+str(counter))    
    count_programming_languages_used(contents)
    write_data_in_csvfile(programming_languages_used)
    print("Languages used ->",programming_languages_used)
    t2 = time.time()
    print("Task done in : ",str(datetime.timedelta(seconds=t2 - t1)))


