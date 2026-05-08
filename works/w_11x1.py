import requests

URL_BASE = "https://httpbin.org/get?student=Ivan&course=API"


def test_interview():
    response = requests.get(url=URL_BASE)
    data = response.json()
    # print(data)
    print(f'# Student: {data['args']['student']}')
    print(f'# Course: {data['args']['course']}')
    print(f'# origin: {data['origin'][:14]}')
    assert 'student' and 'course' in data['args']