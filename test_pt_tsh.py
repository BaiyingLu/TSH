import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 4, "normal thyroid function"),
    (0.5, 3, "hyperthyroidism"),
    (2, 5, "hypothyroidism"),
    (2, 3, "normal thyroid function"),
    (3, 4, "normal thyroid function"),
    (0, 4, "hyperthyroidism"),
    (1, 10, "hypothyroidism"),
])
def test_Diagnosis(a, b, expected):
    from pt_tsh import Diagnosis
    answer = Diagnosis(a, b)
    assert answer == expected


@pytest.mark.parametrize("a, expected", [
    (['Anne Boynton', '45', 'Female',
      'TSH,3.5,3.6,1.8,2.8,1.9,3.4,3,3.6,3,4',
      'END'],
     [{'First Name': 'Anne', 'Last Name': 'Boynton',
       'Age': 45,
       'Gender': 'Female',
       'Diagnosis': 'normal thyroid function',
       'TSH': [1.8, 1.9, 2.8, 3.0, 3.0, 3.4, 3.5, 3.6, 3.6, 4.0]}]),
    (['Jennie Kim', '24', 'Female',
      'TSH,3.7,0.2,1.8,2.8',
      'Lisa Manoban', '22', 'Female',
      'TSH,3.7,5.2,1.8,2.8',
      'END'],
     [{'First Name': 'Jennie', 'Last Name': 'Kim',
       'Age': 24,
       'Gender': 'Female',
       'Diagnosis': 'hyperthyroidism',
       'TSH': [0.2, 1.8, 2.8, 3.7]},
      {'First Name': 'Lisa', 'Last Name': 'Manoban',
       'Age': 22,
       'Gender': 'Female',
       'Diagnosis': 'hypothyroidism',
       'TSH': [1.8, 2.8, 3.7, 5.2]}]),
])
def test_tsh_info_process(a, expected):
    from pt_tsh import tsh_info_process
    answer = tsh_info_process(a)
    assert answer == expected
