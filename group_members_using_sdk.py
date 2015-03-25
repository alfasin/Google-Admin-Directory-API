#!/apps/python/bin/python
import json
import httplib2
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import time
# The module mydb should be implemented by you - provide your credentials
from mydb import get_path_to_p12, get_email, get_service_email

FULL_PATH_TO_P12 = get_path_to_p12()
ACCOUNT_EMAIL = get_email()
SERVICE_EMAIL = get_service_email()
GROUP = 'google-group-example@your-organization.com'


def get_group(dir, args):
    sv = dir.groups()
    return sv.get(groupKey=args['groupKey']).execute()


def get_members(dir, group):
    sv = dir.members()
    resp = sv.list(**group).execute()
    if resp.has_key('members'):
        return resp['members']
    return None


def insert_group_member(dir, body):
    sv = dir.members()
    return sv.insert(groupKey=GROUP, body=body).execute()


def del_group_member(dir, member):
    sv = dir.members()
    return sv.delete(groupKey=GROUP, memberKey=member.get('email')).execute()


def get_service():
    with open(FULL_PATH_TO_P12) as f:
        private_key = f.read()

    OAUTH_SCOPE = ['https://www.googleapis.com/auth/admin.directory.group.member',
                   'https://www.googleapis.com/auth/admin.directory.group']

    credentials = SignedJwtAssertionCredentials(SERVICE_EMAIL, private_key, OAUTH_SCOPE, sub=ACCOUNT_EMAIL)
    http = httplib2.Http()
    http = credentials.authorize(http)

    return build('admin', 'directory_v1', http=http)


# Unit tests
if __name__ == "__main__":

    start = time.time()

    directory_service = get_service()
    group = {'groupKey': GROUP}
    grp = get_group(directory_service, group)
    output = json.dumps(grp, indent=4, sort_keys=True)
    print output
    time.sleep(3)

    body = {"email": "alfasin@your-organization.com", "role": "OWNER", }
    resp = del_group_member(directory_service, body)
    output = json.dumps(resp, indent=4, sort_keys=True)
    print output
    time.sleep(3)

    resp = insert_group_member(directory_service, body)
    output = json.dumps(resp, indent=4, sort_keys=True)
    print output
    time.sleep(3)

    resp = get_members(directory_service, group)
    output = json.dumps(resp, indent=4, sort_keys=True)
    print output

    end = time.time()
    print "The job took: {0:.2f} seconds which is {1:.2f} minutes)".format(end - start, (end - start) / 60)
