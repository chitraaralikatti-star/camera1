from camera import bookingDecision

def test_booking_approved():
    assert bookingDecision(2, 2, 2, 10) == "APPROVED"

def test_booking_conditional():
    assert bookingDecision(5, 1, 3, 10) == "CONDITIONAL"

def test_booking_rejected():
    assert bookingDecision(8, 0, 5, 10) == "REJECTED"

def test_invalid_capacity():
    assert bookingDecision(2, 1, 2, 0) == "INVALID_CAPACITY"
