import requests
import hashlib
import sys

def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error {res.status_code} occured!\nCheck API and try again')
    return res

def get_pass_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    ''' Check password is it exists in API response '''
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    response = req_api_data(first5)
    return get_pass_leaks(response,tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"'{password}' was found {count} times.. You should change your password ASAP.")
        else:
            print(f"'{password}' was NOT found. Good to go!")
    return 'Sayonara!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
