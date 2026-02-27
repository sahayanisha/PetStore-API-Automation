import pytest



@pytest.mark.negative
def test_invalid_order_id(api_client):
    res = api_client.request("GET","/store/order/9999999")
    assert res.status_code in [400,404]

@pytest.mark.negative
def test_create_pet_with_invalidStatus(api_client,unique_id):
    pet_id = unique_id+1
    pet_payload = {
        "id": pet_id,
        "name": "doggie",
        "status": "invalid"
    }
    res = api_client.request("POST","/store/pet",pet_payload)
    assert res.status_code in [404, 200]
