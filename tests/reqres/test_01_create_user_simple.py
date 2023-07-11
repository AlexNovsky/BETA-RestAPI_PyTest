import requests

def test_user_created():
    payload = {
                "name": "Alex",
                "job": "Engineer"
            }
    url = 'https://reqres.in/api/users'

    status = requests.get(url).status_code
    print(status)
    assert status == 200

    create_user = requests.post(url, payload)
    print(create_user.status_code)
    assert create_user.status_code == 201

    created_user_data = create_user.json()
    assert created_user_data['name'] == 'Alex'
    print(created_user_data['name'])
    assert created_user_data['job'] == payload['job']
    print(created_user_data['job'])