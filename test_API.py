import requests
import pytest
class TestAPI:
    def test_api_get(self):
        res = requests.get("https://jsonplaceholder.typicode.com/users/1")
        print(res.json())
        assert res.status_code == 200
        assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert res.json()['company']['bs'] == 'harness real-time e-markets'
        assert res.json()['username'] == 'Bret'
    def test_api_post(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        datas = {
            'userId': '1',
            'title': 'My blog post title',
            'body': 'This is the text of my latest blog post.',
            'Content-Type': 'application/json'
        }
        res = requests.post(url=url,data=datas)
        print(res.json())
        assert res.status_code == 201
        assert isinstance(res.json()['id'],int)


