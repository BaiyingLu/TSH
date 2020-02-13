import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 4, "normal thyroid function"),
    (0.5, 3, "hyperthyroidism"),
    (2, 5, "hypothyroidism"),
    (2, 3, "normal thyroid function"),
])
def test_is_tachycardic(a, b, expected):
    from pt_tsh import Diagnosis
    answer = Diagnosis(a, b)
    assert answer == expected
