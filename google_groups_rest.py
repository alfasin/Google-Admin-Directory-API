#!/usr/bin/python
import httplib2
import json
from oauth2client.client import SignedJwtAssertionCredentials
from urllib import urlencode
# The module mydb should be implemented by you - provide your credentials
from mydb import get_path_to_p12, get_email, get_service_email

FULL_PATH_TO_P12 = get_path_to_p12()
ACCOUNT_EMAIL = get_email()
SERVICE_EMAIL = get_service_email()


def get_group_members(group):
    url = 'https://www.googleapis.com/admin/directory/v1/groups/{}/members'.format(group['email'])
    return call_google_api("GET", url)


def add_group_members(group, payload=False):
    url = 'https://www.googleapis.com/admin/directory/v1/groups/{}/members'.format(group)
    return call_google_api("POST", url, payload)


def call_google_api(method, url, payload=False):
    content = {}
    try:
        http = get_conn()
        if payload:
            (resp, content) = http.request(uri=url, method=method, body=json.dumps(payload), headers={'Content-type':'application/json'})
        else:
            (resp, content) = http.request(uri=url, method=method, headers={'Content-type':'application/json'})
    except Exception as e:
        print "Failed to post request to [{}] due to: {}".format(url, e)
    return json.loads(content)


def get_conn():
    with open(FULL_PATH_TO_P12) as f:
        private_key = f.read()

    OAUTH_SCOPE = ['https://www.googleapis.com/auth/admin.directory.group.member',
                   'https://www.googleapis.com/auth/admin.directory.group']

    credentials = SignedJwtAssertionCredentials(SERVICE_EMAIL, private_key, OAUTH_SCOPE, sub=ACCOUNT_EMAIL)
    http = httplib2.Http()
    return credentials.authorize(http)    


# Unit test
if __name__ == '__main__':
    payload = {
        "email": "alfasin@your-organization.com'",
        "role": "MEMBER",
    }
    print "\n ---------------------------------- \n"
    print "calling add_group_member('alfasin@your-organization.com', 'google-group-example@your-organization.com')"
    res = get_group_members({'email': 'google-group-example@your-organization.com'})
    print json.dumps(res, indent=4, sort_keys=True)
    print "\n ---------------------------------- \n"
