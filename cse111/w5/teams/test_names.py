from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    full_name = make_full_name("Isaac", "Asiedu")
    assert isinstance(full_name, str)

    assert make_full_name("Kwaku", "James") == "James; Kwaku"
    # assert make_full_name("Isaac", "Asiedu") == "Asiedu; Isaac"


def test_extract_family_name():
    family_name = extract_family_name("James; Isaac")
    assert isinstance(family_name, str)

    assert extract_family_name("James; Kwaku") == "James"
    # assert extract_family_name("Isaac; Asiedu") == "Asiedu"


def test_extract_given_name():
    given_name = extract_given_name("James; Isaac")
    assert isinstance(given_name, str)

    assert extract_given_name("James; Kwaku") == "Kwaku"
    # assert extract_given_name("Isaac; Asiedu") == "Asiedu"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
