import finesql


def test_pending_repr():
    assert str(finesql._main.Pending) == "FineSQLPending"
