
def test_basic_delete(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a333",
            "type": "CATEGORY",
            "name": "category",
            "parentId": None,
            "price": None
        },
    ])
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a333")
    assert response.status_code == 200
    response = client.get("/nodes/3fa85f64-5717-4562-b3fc-2c963f66a333")
    assert response.status_code == 404

def test_children_delete(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a333",
            "type": "CATEGORY",
            "name": "category",
            "parentId": None,
            "price": None
        },
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a334",
            "type": "OFFER",
            "name": "offer",
            "parentId": "3fa85f64-5717-4562-b3fc-2c963f66a333",
            "price": 151
        },
    ])
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a333")
    assert response.status_code == 200
    response = client.get("/nodes/3fa85f64-5717-4562-b3fc-2c963f66a333")
    assert response.status_code == 404
    response = client.get("/nodes/3fa85f64-5717-4562-b3fc-2c963f66a334")
    assert response.status_code == 404

def test_invalid_delete(client):
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a335")
    assert response.status_code == 404
    response = client.delete("/delete/value")
    assert response.status_code == 400

