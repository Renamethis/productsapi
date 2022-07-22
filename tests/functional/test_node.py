
def test_get_node(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a332",
            "type": "CATEGORY",
            "name": "category",
            "parentId": None,
            "price": None
        },
        {   
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a331",
            "type": "OFFER",
            "name": "offer",
            "parentId": "3fa85f64-5717-4562-b3fc-2c963f66a332",
            "price": 155
        }
    ])
    response = client.get("/nodes/3fa85f64-5717-4562-b3fc-2c963f66a332")
    assert response.status_code == 200
    assert response.json["uuid"] == "3fa85f64-5717-4562-b3fc-2c963f66a332"
    assert response.json["type"] == "CATEGORY"
    assert response.json["parentId"] is None
    assert response.json["price"] == 155
    assert len(response.json["children"]) == 1
    response = client.get("/nodes/3fa85f64-5717-4562-b3fc-2c963f66a331")
    assert response.status_code == 200
    assert response.json["price"] == 155
    assert response.json["parentId"] == "3fa85f64-5717-4562-b3fc-2c963f66a332"
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a332")

def test_invalid_get_node(client):
    response = client.get("/nodes/3fa85f64-5717-4562-b3fc-2c963f66a335")
    assert response.status_code == 404
    response = client.get("/nodes/value")
    assert response.status_code == 400
