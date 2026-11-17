import pytest
from src.parcel_acceptance import is_parcel_accepted


# ---------- Both limits met: returns True ----------

@pytest.mark.parametrize("weight_grams, length_cm", [
    (1, 1),         # both at lower boundary
    (10000, 100),   # both in the middle
    (20000, 200),   # both at upper boundary
    (20000, 1),     # weight upper, length lower
    (1, 200),       # weight lower, length upper
])
def test_weight_and_length_within_limits_returns_true(weight_grams, length_cm):
    # Act
    result = is_parcel_accepted(weight_grams, length_cm)
    # Assert
    assert result is True


# ---------- Zero or above a limit: returns False ----------

@pytest.mark.parametrize("weight_grams, length_cm", [
    (0, 100),       # zero weight
    (20001, 100),   # weight just above limit
    (10000, 0),     # zero length
    (10000, 201),   # length just above limit
    (0, 0),         # both zero
    (20001, 201),   # both above limit
])
def test_weight_or_length_zero_or_above_limit_returns_false(weight_grams, length_cm):
    # Act
    result = is_parcel_accepted(weight_grams, length_cm)
    # Assert
    assert result is False


# ---------- Negative measurement: ValueError ----------

@pytest.mark.parametrize("weight_grams, length_cm", [
    (-1, 100),      # negative weight
    (10000, -1),    # negative length
    (-1, -1),       # both negative
])
def test_negative_weight_or_length_raises_value_error(weight_grams, length_cm):
    # Act & Assert
    with pytest.raises(ValueError):
        is_parcel_accepted(weight_grams, length_cm)


# ---------- Invalid data type: TypeError ----------

@pytest.mark.parametrize("weight_grams, length_cm", [
    (500.0, 100),   # weight is float
    ("500", 100),   # weight is string
    (None, 100),    # weight is None
    (True, 100),    # weight is bool (not a valid integer)
    (500, 100.0),   # length is float
    (500, "100"),   # length is string
    (500, None),    # length is None
    (500, True),    # length is bool (not a valid integer)
])
def test_invalid_weight_or_length_type_raises_type_error(weight_grams, length_cm):
    # Act & Assert
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)
