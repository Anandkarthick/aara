import json, requests

#api_url = 'https://api.foursquare.com/v2/venues/categories/'

loc_api_url = 'https://api.foursquare.com/v2/venues/search?near=Hartford,CT&Category=4bf58dd8d48988d196941735'
ll_api_url = 'https://maps.googleapis.com/maps/api/geocode/json?&address='
#emergency_room 4bf58dd8d48988d194941735
#hospital 4bf58dd8d48988d196941735


params = dict(
    client_id='XWQYFCXNEJ2J1IQKG2A1VZ5P2EA4EYSIH4NZWL1TDRTHNRXN',
    client_secret='GA2SZEBCWRU0Q5XZ1BW511X43O0PXNP553PBUOS1MOG4BWFR',
    v='20180627',
    query='hospital',
    limit=5
    )

#response = requests.get(url=loc_api_url, params=params)

response = requests.get(url=loc_api_url, params=params)
data = json.loads(response.text)
resp_code = data['meta']['code']
resp = data['response']['venues'][0]
#print(data['response']['venues'])
#print(data['meta']['code'])
print(resp)

res_name = resp['name']
#res_address = resp['formatted Address']

print(res_name)
