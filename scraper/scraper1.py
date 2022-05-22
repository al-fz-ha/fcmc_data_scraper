import sys
from bs4 import BeautifulSoup
import requests
import reader
import generator
import time

# Scraping Program.

# !---CONFIGURATIONS---! #
case_search_URL = 'http://www.fcmcclerk.com/case/search'
case_view_URL = 'http://www.fcmcclerk.com/case/view'

# Set DEBUG to True for debugging messages
DEBUG = True
# Set VERBOSE to True for fuller outputs
VERBOSE = False

# Scrape data for one case
def scrape(case_num):
    if DEBUG:
        print('fetching: ', case_num)

    s = requests.session()
    page = s.get(case_search_URL)

    soup1 = BeautifulSoup(page.content, "lxml")
    token = soup1.find("input", attrs={"name": "_token"})['value']
    if DEBUG:
        print('token: ', token)
    form_data = {
        '_token': token,
        'last_name': '',
        'first_name': '',
        'middle_name': '',
        'date_of_birth': '',
        'company_name': '',
        'party_code': '',
        'case_number': case_num,
        'ticket_number': '',
        'case_type': '',
        'case_year': '',
        'case_status': '',
    }

    # POST request with search criteria
    page = s.post(case_search_URL + '/results', data=form_data)
    if VERBOSE:
        print(page.text)
        print()

    # Find POST params used for full case results
    soup = BeautifulSoup(page.content, "lxml")
    token = soup.find("input", attrs={"name": "_token"})['value']
    case_id = soup.find("input", attrs={"name": "case_id"})['value']
    form_data = {
        '_token': token,
        'case_id': case_id,
    }
    if DEBUG:
        print('token: ', token)
        print('case_id: ', case_id)
        print()

    # POST request for full case results
    page = s.post("http://www.fcmcclerk.com/case/view", data=form_data)
    
    # Scrape time
    soup = BeautifulSoup(page.content, "lxml")
    case_data_list = []
    case_data_list.append(case_num)

    # Scrape and store attorney data
    atty_table_soup = soup.find(id='atty_table')
    atty_table_data_soup = atty_table_soup.find_all("td", attrs={"class": "data"})

    for atty_data in atty_table_data_soup:
        if VERBOSE:
            print("data: ", atty_data.get_text())
        case_data_list.append(atty_data.get_text())

    # Scrape and store party data
    pty_table_soup = soup.find(id='pty_table')
    pty_table_data_soup = pty_table_soup.find_all("td", attrs={"class": "data"})
    for pty_data in pty_table_data_soup:
        if VERBOSE:
            print("data: ", pty_data.get_text())
        case_data_list.append(pty_data.get_text())
    
    return case_data_list

def main(path):
    #path = 'input.xlsx'
    print('reading file ', path)
    case_num_list = reader.read(path)
    case_data_list = []
    print('scraping...')
    for case_num in case_num_list:
        try:
            case_data_list.append(scrape(case_num))
        except: 
            print('Error in: ', case_num)
            print('Skipping')
            print()
        print('sleeping...')
        # adjust sleep time here
        time.sleep(5)
    print("Finished!")
    generator.generate(case_data_list)

if __name__ == "__main__":
        # pass input file here
	main('input.xlsx')


