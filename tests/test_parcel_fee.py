# Unit tests for delivery_fee() in src/parcel_fee.py
import pytest
from src.parcel_fee import delivery_fee


# ---------- Valid inputs: 1 to 1000 grams costs 500 cents ----------

@pytest.mark.parametrize("weight_grams", [
    1,      # lower boundary of band 1
    500,    # middle of band 1
    1000,   # upper boundary of band 1
])
def test_weight_1_to_1000_grams_returns_500_cents(weight_grams):
    # Act
    result = delivery_fee(weight_grams)
    # Assert
    assert result == 500


# ---------- Valid inputs: 1001 to 20000 grams costs 1000 cents ----------

@pytest.mark.parametrize("weight_grams", [
    1001,   # lower boundary of band 2
    10000,  # middle of band 2
    20000,  # upper boundary of band 2
])
def test_weight_1001_to_20000_grams_returns_1000_cents(weight_grams):
    # Act
    result = delivery_fee(weight_grams)
    # Assert
    assert result == 1000


def test_valid_weight_returns_int():
    # Arrange
    weight_grams = 500
    # Act
    result = delivery_fee(weight_grams)
    # Assert
    assert type(result) is int


# ---------- Correct type, outside permitted range: ValueError ----------

@pytest.mark.parametrize("weight_grams", [
    0,      # just below lower limit
    -1,     # negative weight
    20001,  # just above upper limit
])
def test_weight_outside_range_raises_value_error(weight_grams):
    # Act & Assert
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)


# ---------- Invalid data type: TypeError ----------

@pytest.mark.parametrize("weight_grams", [
    500.0,  # float
    "500",  # string
    None,   # None
    True,   # bool is not a valid integer
    False,  # bool is not a valid integer
])
def test_invalid_weight_type_raises_type_error(weight_grams):
    # Act & Assert
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)
