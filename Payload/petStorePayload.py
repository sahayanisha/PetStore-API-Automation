

def build_user_payload(user_id):
    user_payload = {
        "id": user_id,
        "username": f"user{user_id}",
        "firstName": "Nisha",
        "lastName": "J",
        "email": f"user{user_id}@gmail.com",
        "password": "Password123",
        "phone": "1234567890",
        "userStatus": 1
    }
    return user_payload

def build_pet_payload(pet_id):
    pet_payload = {
        "id": pet_id,
        "name": "doggie",
        "status": "available"
    }
    return pet_payload
def build_order_payload(order_id,pet_id):
    order_payload = {
        "id": order_id,
        "petId": pet_id,
        "quantity": 1,
        "shipDate": "2026-02-24T10:18:48.320Z",
        "status": "placed",
        "complete": True
    }
    return order_payload