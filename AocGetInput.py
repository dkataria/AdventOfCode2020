import collections
import requests

# response = requests.get(url)
def getInput(day):
    url = 'https://adventofcode.com/2020/day/' + str(day) + '/input'

    # set cookie below as your session id from your browser session to AOC
    cookie = ''

    headers = {'session': cookie}
    session = requests.Session()
    resp = session.get(url, cookies=headers)
    inputaoc = []
    for each in resp.text.splitlines():
        inputaoc.append(each)
    return inputaoc