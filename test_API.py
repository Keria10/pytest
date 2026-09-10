import requests
import pytest
class TestAPI:

    def test_api_get(self):
        res = requests.get("https://jsonplaceholder.typicode.com/users/1")
        print(res.json())
        assert res.status_code == 200
        assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert res.json()['company']['bs'] == 'harness real-time e-markets'
        assert res.json()['name'] == 'Leanne Graham'
    def test_api_post(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        datas = {
            'userId': 1,
            'title': 'My blog post title',
            'body': 'This is the text of my latest blog post.'
        }
        res = requests.post(url=url,data=datas)
        print(res.json())
        assert res.status_code == 201
        assert isinstance(res.json()['id'],int)

    @pytest.mark.parametrize("user_id,expected_name,expected_bs", [(1, "Bret", "harness real-time e-markets"),
                                                                   (2, "Ervin Howell","synergize scalable supply-chains")])
    def test_api_paramize(self,user_id,expected_name,expected_bs):
        print(user_id,expected_name,expected_bs)
        res = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        print(res.json())
        assert res.status_code == 200
        assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert res.json()['company']['bs'] == expected_bs
        assert res.json()['name'] == expected_name

    @pytest.mark.parametrize("payload,expected_status", [({'userId': 1,'title': 'My blog post title','body': 'This is the text of my latest blog post.'},201),
                                                       ({'userId': 2,'title': 'et ea vero quia laudantium autem','body': 'delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\naccusamus in eum beatae sit\nvel qui neque voluptates ut commodi qui incidunt\nut animi commodi'},201)])
    def test_api_post_params(self,payload,expected_status):
        url = 'https://jsonplaceholder.typicode.com/posts'
        # datas = {
        #     'userId': '1',
        #     'title': 'My blog post title',
        #     'body': 'This is the text of my latest blog post.',
        #     # 'Content-Type': 'application/json'  此处显示为json，则我们都会用json传参
        # }
        res = requests.post(url=url,json=payload)
        print(res.json())
        assert res.status_code == expected_status
        assert isinstance(res.json()['id'],int)