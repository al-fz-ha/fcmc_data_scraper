from bs4 import BeautifulSoup
import requests


# configurations
case_search_URL = 'http://www.fcmcclerk.com/case/search'
case_view_URL = 'http://www.fcmcclerk.com/case/view'

# NOT USED
def get_form_data(token, case_number):
	form_data = {
		'_token': token,
		'last_name': '',
		'first_name': '',
		'middle_name': '',
		'date_of_birth': '',
		'company_name': '',
		'party_code': '',
		'case_number': case_number,
		'ticket_number': '',
		'case_type': '',
		'case_year': '',
		'case_status': '',
	}

#NOT USED
def get_form_data2(soup):
	token = soup.find("input", attrs={"name": "_token"})['value']
	case_id = soup.find("input", attrs={"name": "case_id"})['value']
	#case_id = '2020CVG000004'
	form_data = {
		'_token': token,
		'case_id': case_id,
	}

	return form_data

def main():
	print("Entering main()")
	#session = create_session()
	sess = requests.session()
	page = sess.get(case_search_URL)
	soup1 = BeautifulSoup(page.content, "lxml")
	token = soup1.find("input", attrs={"name": "_token"})['value']
	print('token: ', token)
	
	case_number = '2020CVG000004'
	form_data = {
        	'_token': token,
                'last_name': '',
                'first_name': '',
                'middle_name': '',
                'date_of_birth': '',
                'company_name': '',
                'party_code': '',
                'case_number': case_number,
                'ticket_number': '',
                'case_type': '',
                'case_year': '',
                'case_status': '',
        }
	page = sess.post(case_search_URL + '/results', data=form_data, timeout=10000)
	print('Session posted')
	stuff = page.text
	print(stuff)
	# next seesion	
	soup = BeautifulSoup(page.content, "lxml")
	#form_data = get_form_data2(soup)	
	# TEST BLOCK
	_token = soup.find("input", attrs={"name": "_token"})['value']
	print('token1: ', token)
	case_id = soup.find("input", attrs={"name": "case_id"})['value']
	print('case_id ', case_id)
	form_data = {
		'_token': token,
		'case_id': case_id,
	}
	# TEST BLOCK END
	page = sess.post(case_view_URL, data=form_data)

if __name__ == "__main__":
	main()
