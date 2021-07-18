import requests
import json

BASE_URL = "https://api.nexmo.com"
ACCESS_TOKKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MjY2MTE2OTYsImV4cCI6MTYyNjY5ODA5NiwianRpIjoiM1VjbXRscThvcDhkIiwiYXBwbGljYXRpb25faWQiOiJlOGFkNWY0NC00NWFmLTRjMzMtODUzZC1mNDQ5NzdhM2JhYTYifQ.lvxdeKHIkY-EJoOaqcR4WcxZ_eyYjGxomrI-p-JJ4nS2mG8qYtyrnoxN9EEhEkGwrdJEjUevhzNR91JcHexMwe8hHoFHSoyAVTfQ-a8ANjU8yrapbPXHRzufSuhEXJerZV9z1EIDMSGeMk7tR4qLoiQGr_V61yOM0bu4hEgDRQGU45hfPNveyiSjQ9nPlopLh8HbqfI9x5sKLd-WsUAZ9F7kFjy90OaltpsKXz-1T43zMuECyLFfkaQQOR1RI0Nddn_PPuKdYUU63fwEwutLXEqrFgZe6HgxP0pcD6FW6TMP_9qAW2q0Smgs7TWJ1pdpXLWvw-9AMqOdgSkR3czpBA"
EXPIRED_TOKKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MjY2MTE2OTYsImV4cCI6MTYyNjY5ODA5NiwianRpIjoiM1VjbXRscThvcDhkIiwiYXBwbGljYXRpb25faWQiOiJlOGFkNWY0NC00NWFmLTRjMzMtODUzZC1mNDQ5NzdhM2JhYTYifQ.lvxdeKHIkY-EJoOaqcR4WcxZ_eyYjGxomrI-p-JJ4nS2mG8qYtyrnoxN9EEhEkGwrdJEjUevhzNR91JcHexMwe8hHoFHSoyAVTfQ-a8ANjU8yrapbPXHRzufSuhEXJerZV9z1EIDMSGeMk7tR4qLoiQGr_V61yOM0bu4hEgDRQGU45hfPNveyiSjQ9nPlopLh8HbqfI9x5sKLd-WsUAZ9F7kFjy90OaltpsKXz-1T43zMuECyLFfkaQQOR1RI0Nddn_PPuKdYUU63fwEwutLXEqrFgZe6HgxP0pcD6FW6TMP_9qAW2q0Smgs7TWJ1pdpXLWvw-9AMqOdgSkR3czpBZ"
USER_PAYLOADS = [{},{'name':'  '},{'name':''},{'name':895652},{'name':True}]
CONVERSATION_PAYLOADS = [{},{'name':'  '},{'name':''},{'name':895652},{'name':True}]
HEADERS = {
    "Authorization": "Bearer "+ACCESS_TOKKEN,
    "Content-Type": "application/json"
}
def get_users(loc_headers):
    END_POINT = "/v0.1/users"
    URL = BASE_URL+END_POINT
    res = requests.get(URL,headers=loc_headers)
    return res

def create_user(data):
    END_POINT = "/v0.1/users"
    URL = BASE_URL+END_POINT
    res = requests.post(URL,data=json.dumps(data),headers=HEADERS)
    return res

def create_conversation(data):
    END_POINT = "/v0.1/conversations"
    URL = BASE_URL+END_POINT
    res = requests.post(URL,data=json.dumps(data),headers=HEADERS)
    return res

def create_member(conversation_id, data):
    END_POINT = "/v0.1/conversations/"+conversation_id+"/members"
    URL = BASE_URL+END_POINT
    res = requests.post(URL,data=json.dumps(data),headers=HEADERS)
    return res

def delete_user(user_id):
    END_POINT = "/v0.1/users/"+user_id
    URL = BASE_URL+END_POINT
    res = requests.delete(URL,headers=HEADERS)
    return res

def delete_conversation(conversation_id):
    END_POINT = "/v0.1/conversations/"+conversation_id
    URL = BASE_URL+END_POINT
    res = requests.delete(URL,headers=HEADERS)
    return res

def delete_member(conversation_id, member_id):
    END_POINT = "/v0.1/conversations/"+conversation_id+"/members/"+member_id
    URL = BASE_URL+END_POINT
    res = requests.delete(URL,headers=HEADERS)
    return res

def test_duplicate_user_data():
    "Check same payload mulitple time for user post api."
    payload = {
        "name": "Test123",
        "display_name": "Test 123A"
    }
    res = create_user(payload)
    res_code = res.status_code
    assert res_code in range(200,300), "Failed to create user with payload: %s" % payload
    res = create_user(payload)
    res_code = res.status_code
    assert res_code not in range(200,300), "[%s]Create mulitple users for the same paylaod. Response Text: %s" % (res_code, res.text)

def test_different_user_payloads():
    """Test different type of paylaod/schema for user post api."""
    failed_schemas = []
    for user in USER_PAYLOADS:
        # res = requests.post(URL,data=json.dumps(user),headers=HEADERS)
        res = create_user(user)
        res_code = res.status_code
        print("Requested Payload: %s" % str(user))
        print("Response Code: %s." % res_code)
        print("Response Text: %s" % res.text)
        if res_code in range(200,300):
            o_user = {}
            o_user.update({
                'Status': 'Failed',
                'Payload': dict(user),
                'Response': res_code,
                'Response Text': res.text
            })
            failed_schemas.append(o_user)
    assert len(failed_schemas) == 0, "Failed for these payload: %s" % str(failed_schemas)

def test_different_conversation_payloads():
    """Test different type of paylaod/schema for conversation post api."""
    failed_schemas = []
    for conv in CONVERSATION_PAYLOADS:
        # res = requests.post(URL,data=json.dumps(conv),headers=HEADERS)
        res = create_conversation(conv)
        res_code = res.status_code
        print("Requested Payload: %s" % str(conv))
        print("Response Code: %s." % res_code)
        print("Response Text: %s" % res.text)
        if res_code in range(200,300):
            o_conv = {}
            o_conv.update({
                'Status': 'Failed',
                'Payload': dict(conv),
                'Response': res_code,
                'Response Text': res.text
            })
            failed_schemas.append(o_conv)
    assert len(failed_schemas) == 0, "Failed for these payloads: %s" % str(failed_schemas)

def test_invalid_token():
    """Test user get api with invalid token."""
    loc_headers = {
        "Authorization": "Bearer "+"AiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MjY2MTE2OTYsImV4cCI.AiOiJKV1QiLCJhbGciOiJSUzI1NiJ9"
    }
    res = get_users(loc_headers)
    res_code = res.status_code
    print("For invalid token, got a response Code: %s." % res_code)
    print("Response Text: %s" % res.text)
    assert res_code not in range(200,300), "Failed for invalid token, getting a response code(%s)." % res.status_code

def test_empty_token():
    """Test user get api with without token."""
    loc_headers = {
        "Authorization": "Bearer "+""
    }
    res = get_users(loc_headers)
    res_code = res.status_code
    print("For empty token, got a response Code: %s." % res_code)
    print("Response Text: %s" % res.text)
    assert res_code not in range(200,300), "Failed for empty token, getting a response code(%s)." % res.status_code

def test_without_token():
    """Test user get api with without token."""
    END_POINT = "/v0.1/users"
    URL = BASE_URL+END_POINT
    res = requests.get(URL)
    res_code = res.status_code
    print("For without token, got a response Code: %s." % res_code)
    print("Response Text: %s" % res.text)
    assert res_code not in range(200,300), "Failed for without token, getting a response code(%s)." % res.status_code

def test_expired_token():
    """Test user get api with expired token."""
    loc_headers = {
        "Authorization": "Bearer "+EXPIRED_TOKKEN
    }
    res = get_users(loc_headers)
    res_code = res.status_code
    assert res_code not in range(200,300), "Failed for expired token, getting a response code(%s)." % res.status_code

def test_app_flow_test_case_1():
    """Complete flow scenario"""
    user_id, conversation_id, member_id = None, None, None
    # Create user
    user_data = {
        "name": "test_user_name12",
        "display_name": "Test User Name12"
    }
    user_res = create_user(user_data)
    res_data = user_res.json()
    assert user_res.status_code in range(200,300), "Failed to create user with payload: %s" % user_data
    assert res_data.get('id'), "Couldn't get user ID in response."
    user_id = res_data['id']
    # create conversation
    conversation_data = {
        "name": "test_user_name1_chat2",
        "display_name": "Test User Name1 Chat2",
    }
    conv_res = create_conversation(conversation_data)
    res_data = conv_res.json()
    assert conv_res.status_code in range(200,300), "Failed to create conversation with payload: %s" % conversation_data
    assert res_data.get('id'), "Couldn't get conversation ID in response."
    conversation_id = res_data['id']
    # Create members
    member_data = {
        "user_id": user_id,
    }
    mem_res = create_member(conversation_id, member_data)
    res_data = mem_res.json()
    assert mem_res.status_code in range(200,300), "Failed to create member with payload: %s and conversation ID: %s" % (member_data, conversation_id)
    assert res_data.get('id'), "Couldn't get member ID in response."
    member_id = res_data['id']
    # Delete members
    res = delete_member(conversation_id. member_id)
    assert res.status_code in range(200,300), "Failed to delete the member."
    # Delete conversation
    res = delete_conversation(conversation_id)
    assert res.status_code in range(200,300), "Failed to delete the conversation."
    # Delete User
    res = delete_user(user_id)
    assert res.status_code in range(200,300), "Failed to delete the user."

def test_app_flow_test_case_2():
    """Create user and conversation and delete user then try to create member."""
    user_id, conversation_id, member_id = None, None, None
    # Create user
    user_data = {
        "name": "test_user_name22",
        "display_name": "Test User Name22"
    }
    user_res = create_user(user_data)
    res_data = user_res.json()
    assert user_res.status_code in range(200,300), "Failed to create user with payload: %s" % user_data
    assert res_data.get('id'), "Couldn't get user ID in response."
    user_id = res_data['id']
    # create conversation
    conversation_data = {
        "name": "test_user_name2_chat2",
        "display_name": "Test User Name2 Chat2",
    }
    conv_res = create_conversation(conversation_data)
    res_data = conv_res.json()
    assert conv_res.status_code in range(200,300), "Failed to create conversation with payload: %s" % conversation_data
    assert res_data.get('id'), "Couldn't get conversation ID in response."
    conversation_id = res_data['id']
    # Delete User
    res = delete_user(user_id)
    assert res.status_code in range(200,300), "Failed to delete the user."
    # Create members
    member_data = {
        "user_id": user_id
    }
    mem_res = create_member(conversation_id, member_data)
    res_data = mem_res.json()
    assert mem_res.status_code not in range(200,300), "Member is created by using the user id of deleted user."
    assert res_data.get('id'), "Couldn't get member ID in response."
    member_id = res_data['id']

    # Removing the test data
    # Delete members
    res = delete_member(conversation_id. member_id)
    assert res.status_code in range(200,300), "Failed to delete the member."
    # Delete conversation
    res = delete_conversation(conversation_id)
    assert res.status_code in range(200,300), "Failed to delete the conversation."

def test_app_flow_test_case_3():
    """Create user and conversation and delete conversation then try to create member."""
    user_id, conversation_id, member_id = None, None, None
    # Create user
    user_data = {
        "name": "test_user_name32",
        "display_name": "Test User Name32"
    }
    user_res = create_user(user_data)
    res_data = user_res.json()
    assert user_res.status_code in range(200,300), "Failed to create user with payload: %s" % user_data
    assert res_data.get('id'), "Couldn't get user ID in response."
    user_id = res_data['id']
    # create conversation
    conversation_data = {
        "name": "test_user_name3_chat2",
        "display_name": "Test User Name3 Chat2",
    }
    conv_res = create_conversation(conversation_data)
    res_data = conv_res.json()
    assert conv_res.status_code in range(200,300), "Failed to create conversation with payload: %s" % conversation_data
    assert res_data.get('id'), "Couldn't get conversation ID in response."
    conversation_id = res_data['id']

    # Delete conversation
    res = delete_user(conversation_id)
    assert res.status_code in range(200,300), "Failed to delete the conversation."

    # Create members
    member_data = {
        "user_id": user_id
    }
    mem_res = create_member(conversation_id, member_data)
    res_data = mem_res.json()
    assert mem_res.status_code not in range(200,300), "Member is created by using the user id of deleted user."
    assert res_data.get('id'), "Couldn't get member ID in response."
    member_id = res_data['id']

    # Removing demo data
    # Delete members
    res = delete_member(conversation_id. member_id)
    assert res.status_code in range(200,300), "Failed to delete the member."

    # Delete User
    res = delete_user(user_id)
    assert res.status_code in range(200,300), "Failed to delete the user."

def test_app_flow_test_case_4():
    """Create user and conversation and delete both the user and conversation then try to create member."""
    user_id, conversation_id, member_id = None, None, None
    # Create user
    user_data = {
        "name": "test_user_name42",
        "display_name": "Test User Name42"
    }
    user_res = create_user(user_data)
    res_data = user_res.json()
    assert user_res.status_code in range(200,300), "Failed to create user with payload: %s" % user_data
    assert res_data.get('id'), "Couldn't get user ID in response."
    user_id = res_data['id']
    # create conversation
    conversation_data = {
        "name": "test_user_name4_chat2",
        "display_name": "Test User Name4 Chat2",
    }
    conv_res = create_conversation(conversation_data)
    res_data = conv_res.json()
    assert conv_res.status_code in range(200,300), "Failed to create conversation with payload: %s" % conversation_data
    assert res_data.get('id'), "Couldn't get conversation ID in response."
    conversation_id = res_data['id']

    # Delete conversation
    res = delete_user(conversation_id)
    assert res.status_code in range(200,300), "Failed to delete the conversation."

    # Delete User
    res = delete_user(user_id)
    assert res.status_code in range(200,300), "Failed to delete the user."

    # Create members
    member_data = {
        "user_id": user_id
    }
    mem_res = create_member(conversation_id, member_data)
    res_data = mem_res.json()
    assert mem_res.status_code not in range(200,300), "Member is created by using the user id of deleted user."
    assert res_data.get('id'), "Couldn't get member ID in response."
    member_id = res_data['id']

    # Removing demo data
    # Delete members
    res = delete_member(conversation_id. member_id)
    assert res.status_code in range(200,300), "Failed to delete the member."
