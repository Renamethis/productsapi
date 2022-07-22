from datetime import datetime

def testUnit(newUnit):
    assert newUnit.uuid == "3fa85f64-5717-4562-b3fc-2c963f66a333"
    assert newUnit.name == "CATEGORY"
    assert newUnit.updateTime == datetime.fromisoformat("2022-05-28T21:12:01.000")
    assert newUnit.ntype == 1
    assert newUnit.parentId == "3fa85f64-5717-4562-b3fc-2c963f66a332"
    assert newUnit.price == 100

def testHistory(newHistory):
    assert newHistory.uuid == "3fa85f64-5717-4562-b3fc-2c963f66a333"
    assert newHistory.updateTime == datetime.fromisoformat("2022-05-28T21:12:01.000")
    assert newHistory.price == 100