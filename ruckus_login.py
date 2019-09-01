import requests
import os

def get_credentials(filepath='credentials.txt', debug=0):
    with open(filepath, "r") as f:
        data = f.readlines()
        username = data[0].strip()
        password = data[1].strip()

    if (debug):
        print("Fetched username [%r] and password [%r]" % (username, password))

    return username, password


def main():
    username, password = get_credentials()

    login_url = 'https://scg.ruckuswireless.com:9998/forms/user_login?username=%s&password=%s&ok=Log+In' % (
        username, password)

    try:
        r = requests.post(login_url, verify=False, timeout=1)
        print("Request Succesful at endpoint:\n\n>>> ", r.url)

    #TODO: Proper error handling
    except:
        print('Already logged in.')

if __name__ == "__main__":
    main()
