class TestUpdateUser():
    def test_is_api_running(self, app):
        assert app.update_user.is_update_api_up() == True

    def test_patch_user(self, app):
        new_payload = app.create_user.generate_new_payload()
        created_user = app.create_user.new_user(new_payload)
        assert created_user.status_code == 201
        user_details = created_user.json()
        assert user_details["job"] == new_payload["job"]
        patched_user = app.update_user.patch_user(user_details["name"])
        updated_details = patched_user.json()
        assert updated_details["job"] == "updated job"

    def test_put_user(self, app):
        new_payload = app.create_user.generate_new_payload()
        created_user = app.create_user.new_user(new_payload)
        assert created_user.status_code == 201
        user_details = created_user.json()
        assert user_details["job"] == new_payload["job"]
        patched_user = app.update_user.patch_put_user(user_details["name"])
        updated_details = patched_user.json()
        assert updated_details["name"] == "updated name"
        assert updated_details["job"] == "updated job"
