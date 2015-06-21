import pprint
from requests_oauthlib import OAuth2Session


# Credentials you get from registering a new application
client_id = 'my_client_id'
client_secret = 'my_secret'

# OAuth endpoints given in the Rdio API documentation
authorization_base_url = 'https://www.rdio.com/oauth2/authorize'
token_url = 'https://services.rdio.com/oauth2/token'

rdio = OAuth2Session(client_id, redirect_uri='http://127.0.0.1')

# Redirect user to Rdio for authorization
authorization_url, state = rdio.authorization_url(authorization_base_url)
print 'Please go here and authorize,', authorization_url

# Get the authorization verifier code from the callback url
redirect_response = raw_input('Paste the full redirect URL here:')

# Fetch the access token
rdio.fetch_token(token_url, client_secret=client_secret,
                     authorization_response=redirect_response)

# Fetch a protected resource, i.e. user profile
pprint.pprint(rdio.post('http://api.rdio.com/1',
                        data={'method': 'getTopCharts', 'type': 'Artist'}).json())
