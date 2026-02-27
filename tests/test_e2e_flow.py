from Payload.petStorePayload import *



def test_pet_order_flow(unique_id,api_client):
    user_id = unique_id
    pet_id = unique_id+1
    order_id = unique_id+2
    # Create user

    user_payload = build_user_payload(user_id)
    res = api_client.request("POST","/user",user_payload)
    response_json = res.json()
    print(response_json)
    assert res.status_code == 200
    assert "code" in res.text

    #Create pet
    pet_payload = build_pet_payload(pet_id)
    res = api_client.request("POST","/pet",pet_payload)
    response_json = res.json()
    print(response_json)
    assert res.status_code == 200
    assert res.json()["id"] == pet_id

    #Create Order

    order_payload = build_order_payload(order_id,pet_id)
    res = api_client.request("POST","/order",order_payload)
    res = api_client.request("POST","/store/order",order_payload)
    response_json = res.json()
    print(response_json)
    assert res.status_code == 200
    assert response_json["id"] == order_id
    assert response_json["status"] == "placed"
    assert response_json["complete"] is True

  #get placed order
    res = api_client.request("GET",f"/store/order/{order_id}")
    assert res.status_code == 200
    assert res.json()["petId"] == pet_id



