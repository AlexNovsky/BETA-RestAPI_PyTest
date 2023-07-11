import requests
def test_user_created():
    payload_new = {
                "name": "Alex",
                "job": "Engineer"
            }
    url_new = 'https://reqres.in/api/users'
    url_update = 'https://reqres.in/api/users/2'

    status = requests.get(url_new).status_code
    print(status)
    assert status == 200

    create_user = requests.post(url_new, payload_new)
    print(create_user.status_code)
    assert create_user.status_code == 201

    created_user_data = create_user.json()
    username = created_user_data['name']
    assert  username == 'Alex'
    print(created_user_data['name'])
    print(created_user_data['job'])
    payload_patch = {
        "name": username,
        "job": "updated job"
    }
    updated_user = requests.patch(url_update, payload_patch)
    print(updated_user.json())
    payload_put = {
        "name": "updated name",
        "job": "updated job"
    }
    putted_user = requests.put(url_update, payload_put)
    print(putted_user.json())