
def test_category_import(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a333",
            "type": "CATEGORY",
            "name": "category",
            "parentId": None,
            "price": None
        },
    ])
    assert response.status_code == 200
    assert response.json[0]['uuid'] == "3fa85f64-5717-4562-b3fc-2c963f66a333"
    assert response.json[0]['type'] == "CATEGORY"
    assert response.json[0]['name'] == "category"
    assert response.json[0]['parentId'] is None
    assert response.json[0]['price'] == -1
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a333")

def test_offer_import(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a334",
            "type": "OFFER",
            "name": "offer",
            "parentId": None,
            "price": 151
        },
    ])
    assert response.status_code == 200
    assert response.json[0]['uuid'] == "3fa85f64-5717-4562-b3fc-2c963f66a334"
    assert response.json[0]['type'] == "OFFER"
    assert response.json[0]['name'] == "offer"
    assert response.json[0]['parentId'] is None
    assert response.json[0]['price'] == 151
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a334")

def test_invalid_data_category(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a334",
            "type": "CATEGORY",
            "name": "offer",
            "parentId": None,
            "price": 151
        },
    ])
    assert response.status_code == 400

def test_invalid_data_offer(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a334",
            "type": "OFFER",
            "name": "offer",
            "parentId": None,
            "price": None
        },
    ])
    assert response.status_code == 400

def test_invalid_price(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a334",
            "type": "OFFER",
            "name": "offer",
            "parentId": None,
            "price": -123
        },
    ])
    assert response.status_code == 400