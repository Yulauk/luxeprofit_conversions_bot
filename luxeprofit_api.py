import requests
import collections_for_import
from config import luxeprofit_api_key
from datetime import datetime
import pytz


# set time and time zone
time_zone = pytz.timezone('Europe/Madrid')
time_now = datetime.now(time_zone)

# API-Key
api_key = luxeprofit_api_key
headers = {'API-Key': api_key}

# URL
base_url = 'https://api-luxeprofit.affise.com'
not_base_url = f'/3.0/stats/conversions?date_from={time_now.date()}&date_to={time_now.date()}&timezone={time_zone}'
html = requests.get(f'{base_url}{not_base_url}', headers=headers)

# if status code == 200 html give response, this response read in json format
response_read = html.json()
length_conversions = f"You have: {len(response_read['conversions'])} conversions"

# made request for response self balance
url_for_balance = '/3.1/partner/me'
balance_requests = requests.get(f'{base_url}{url_for_balance}', headers=headers)
read_balance_requests = balance_requests.json()


def conversionsResponse():
    lst = [length_conversions]
    str_result = ''

    for offer in range(len(response_read['conversions'])):
        if response_read['conversions'][offer]['goal_value'] == '2':
            lst.append(f"[{response_read['conversions'][offer]['updated_at'][11:16]}]"
                       f"🤑{response_read['conversions'][offer]['revenue']}$"
                       f"{collections_for_import.country_flags[response_read['conversions'][offer]['country']]}"
                       f"{response_read['conversions'][offer]['city']}"
                       f"{response_read['conversions'][offer]['offer']['title']} "[:20]+'...')
        else:
            lst.append(f"[{response_read['conversions'][offer]['updated_at'][11:16]}] "
                       f"{collections_for_import.country_flags[response_read['conversions'][offer]['country']]} "
                       f"{response_read['conversions'][offer]['city']} "
                       f"{response_read['conversions'][offer]['offer']['title']} "[:25]+'...')

    for k, v in read_balance_requests['user']['central_balance']['USD'].items():
        lst.append(f"{k}:{v}$")

    for _ in lst:
        str_result += (_+'\n')
    yield str_result


if __name__ == '__main__':
    if len(response_read['conversions']) > 0:
        for i in range(len(response_read['conversions'])):
            print(response_read['conversions'][i]['created_at'][11:16][:35])
    else:
        print('not have conversions')
