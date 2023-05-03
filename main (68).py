import requests

# Enter your Walk Score API key here
API_KEY = 'your_api_key_here'

# Generate a walk score for a given address
def get_walk_score(address):
    url = 'http://api.walkscore.com/score'
    params = {
        'address': address,
        'format': 'json',
        'transit': '1',
        'bike': '1',
        'wsapikey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    walk_score = data['walkscore']
    return walk_score

# Query an address and get its walk score
address = input('Enter an address: ')
walk_score = get_walk_score(address)
print('Walk Score for {}: {}'.format(address, walk_score))
