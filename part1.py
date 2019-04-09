import requests
from bs4 import BeautifulSoup
import csv

# global variables
counter = 1
test_data = [4]
test_data2 = [5,15]
result_set = set()
ideoneString = "https://ideone.com"
languageList = []


def get_content(path):
    r = requests.get(path)
    content = r.content
    print(r.url)
    soup = BeautifulSoup(content,'html.parser')
    return soup


def populate_languages_used(soup):
    languagesResult = soup.find_all(class_ = "header")
    for elem in languagesResult:
        spanElement = elem.find('span')
        language = spanElement.string
        languageList.append(language)

def get_links_from_content(soup):
    allResults = soup.find_all("strong")
    for index,result in enumerate(allResults):
        link = result.find("a")
        if (languageList[index] == "C++" or languageList[index] == "C++14" or languageList[index] == "Java"):
            result_set.add(ideoneString+link.get('href'))
    print(result_set) 
    print("Length of result :",len(result_set))


def check_standard_output(test_data_sent,test_data2):
    for item in result_set:
        r = requests.get(item)
        content = r.content
        soup = BeautifulSoup(content,'html.parser')
        output = soup.find_all(id = 'output-text')
        liste = []
        for x in output:
            liste.append(str(x))
        checkList = liste[0].splitlines()
        #to check the output manually
        # print(checkList) 
        test_data_sent = [str(item) for item in test_data_sent]
        test_data2 = [str(item) for item in test_data2]
        setA = set(test_data)
        setC = set(test_data2)
        setB = set(checkList)
        if (setA.issubset(setB) or setC.issubset(setB)):
            print("Matches ->",r.url,"->",setA.issubset(setB))
            print("matches 2 ->",r.url,"->",setC.issubset(setB))


if __name__ == "__main__":
    # # initialize csv file
    # with open('programs_used_by_ideone.csv','a') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writrerows(['date','programs'])
    #     writer.close()

    while True:
        contents = get_content(ideoneString + '/recent/'+str(counter))
        populate_languages_used(contents)
        get_links_from_content(contents)
        check_standard_output(test_data,test_data2)
        result_set.clear()
        counter += 1




# with open(filename,'a+',newline = '') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writrerow()