import sender_stand_request
import data



def new_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def negative_assert(first_name):
    user_body = new_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400



def test_posit_assert_new_users():
    response = sender_stand_request.post_new_user(data.user_body)
    assert response.status_code == 200

def test_neg_assert_new_users():
    negative_assert("")

