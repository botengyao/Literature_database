import requests
from bs4 import BeautifulSoup
import csv

def get_issn_aqi(journal):
    '''
    :param journal:
    :return: results of every journal
    '''
    url = 'http://sci.justscience.cn/index.html?q=' + journal +'&sci=1'
    r = requests.get(url, timeout = 60)
    print(r.status_code)
    Soup = BeautifulSoup(r.text,'lxml')
    ids = Soup.select('.tb1 > tr > td')

    result = {}
    result['journal_name'] = journal
    result['abbreviation'] = ids[2].string
    result['ISSN'] = ids[3].string
    result['num_per_year'] = ids[4].string
    result['5_year_avg_IF'] = ids[5].string
    result['no_self_citation_IF'] = ids[6].string
    result['IF'] = ids[7].string
    return result

def main():
    #get_issn_aqi('CA-A CANCER JOURNAL FOR CLINICIANS')

    with open(r'xxxxx\journal_ISSN.csv', 'w', newline='', encoding='UTF-8') as f2,\
            open(r'xxxxxxx\journal_name.txt', 'r') as f1:

            fieldnames = ['journal_name', 'abbreviation','ISSN','num_per_year','5_year_avg_IF','no_self_citation_IF','IF']
            writer = csv.DictWriter(f2, fieldnames=fieldnames)
            writer.writeheader()

            lines = f1.readlines()
            for line in lines:
                try:
                    result = get_issn_aqi(line.strip())
                except:
                    result['journal_name'] = line.strip()
                    result['ISSN'] = 0
                    result['abbreviation'] = ''
                    result['num_per_year'] = ''
                    result['5_year_avg_IF'] = ''
                    result['no_self_citation_IF'] = ''
                    result['IF'] = ''
                writer.writerow(result)

if __name__ == '__main__':
    main()
    print("Finished")