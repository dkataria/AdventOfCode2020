import collections
import requests

# response = requests.get(url)
def getInput(day):
    url = 'https://adventofcode.com/2020/day/' + str(day) + '/input'

    # set cookie below as your session id from your browser session to AOC
    cookie = '53616c7465645f5f7a2362b2e67fc9ca3ad6f34e84359616c7097d5e7f116bb18b37ca30b4b1fcb387475e063af2e7ae'

    headers = {'session': cookie}
    session = requests.Session()
    resp = session.get(url, cookies=headers)
    inputaoc = []
    for each in resp.text.splitlines():
        inputaoc.append(each)
    return inputaoc