class TestCreateUserAPI():
    def test_create_user_api_running(self, app):
        assert app.create_user.is_api_up() == True

    def test_create_user(self, app):
        new_payload = app.create_user.generate_new_payload()
        created_user = app.create_user.new_user(new_payload)
        assert created_user.status_code == 201
        user_details = created_user.json()
        assert user_details["name"] == new_payload["name"]
