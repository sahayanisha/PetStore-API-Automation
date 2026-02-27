from pathlib import Path
import pytest
from utils.payloadLoader import *
from utils.data_factory import *
from utils.assertion import *
from utils.schema_validator import *






ROOT_DIR = Path(__file__).resolve().parents[1]
TESTDATA_DIR = ROOT_DIR/"testdata"
SCHEMA_DIR = ROOT_DIR/"schemas"

def assert_user_created(api_client,expected_user):
    username = expected_user["username"]
    res = api_client.request("GET",f"/user/{username}")

    assert_status_code(res, 200)
    assert_response_not_empty(res)

    user_json = assert_json_response(res)
    assert_field_equal(user_json["username"], expected_user["username"], "username")
    assert_field_equal(user_json["id"], expected_user["id"], "id")


@pytest.mark.parametrize("scenario_key",["single_user","multiple_users"])
def test_create_with_user_list(api_client,scenario_key,unique_id):
    data = load_json(TESTDATA_DIR/"create_list_of_user.json")
    user_type = data[scenario_key]
    user_payload = make_users_dynamic(user_type,base_id = unique_id)
    res = api_client.request("POST","/user/createWithList",user_payload)

    #HTTP validation
    assert_status_code(res, 200)
    assert_response_not_empty(res)

    res_json = assert_json_response(res)
    #Schema validation
    validate_schema(res_json, SCHEMA_DIR/"api_response_schema.json")

    #Response time
    assert_response_time(res, 4.0)

    for user in user_payload:
        assert_user_created(api_client,user)

@pytest.mark.parametrize("key",["empty_array","object_instead_of_array","null_element","missing_username"])
def test_create_with_user_list_negative(api_client,key):
    data = load_json(TESTDATA_DIR/"create_list_of_user_negative.json")
    negative_payload = data[key]
    res = api_client.request("POST","/user/createWithList",negative_payload)

    if res.status_code == 200:
        pytest.fail(f"Invalid payload {res.text} returned 200")

    assert_status_in_range(res, 400, 499)





