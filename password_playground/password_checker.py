import requests
import hashlib
import sys

# url = 'https://api.pwnedpasswords.com/range/' + '3C49F'
# result = requests.get(url)
# print(result)

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching {response.status_code}, check the api and try again!')
    return response

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hassh, count in hashes:
        if hassh == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    # check password if it exists in API response
    sha1passwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1passwd[:5], sha1passwd[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... You should probably change your passweord')
        else:
            print(f'{password} was NOT found. Carry on!')

        return 'done!'


