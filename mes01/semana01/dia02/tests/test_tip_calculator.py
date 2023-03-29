def test_calculate_tip():
    bill = 100.0
    share = 4
    tip_percentage = 10
    expected_total = 27.5
    
    tip = bill * (tip_percentage / 100)
    total = (bill + tip) / share
    
    assert total == expected_total
