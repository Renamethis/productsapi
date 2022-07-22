from datetime import datetime, timedelta

def test_sales(client):
    response = client.post("/imports", json=[
        {
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a330",
            "type": "CATEGORY",
            "name": "category",
            "parentId": None,
            "price": None
        },
        {   
            "uuid": "3fa85f64-5717-4562-b3fc-2c963f66a329",
            "type": "OFFER",
            "name": "offer",
            "parentId": "3fa85f64-5717-4562-b3fc-2c963f66a330",
            "price": 155
        }
    ])
    time = (datetime.now() + timedelta(seconds=1)).isoformat()
    response = client.get('/sales?date=' + time)
    assert response.status_code == 200
    assert len(response.json) == 2
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a330")
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a329")
    response = client.delete("/delete/3fa85f64-5717-4562-b3fc-2c963f66a330")

def test_invalid_sales(client):
    response = client.get('/sales', query_string={"date": "value"})
    assert response.status_code == 400