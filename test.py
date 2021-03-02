import pytest

@pytest.mark.parametrize("test_input,expected", [("hello", False),
                                                 ("HELLO", True),
                                                 ("HeLlO", False),
                                                 (" \n", False),
                                                 ("1337 5P34K", True),
                                                 ("42", False),
                                                 ("", False)])
def test_str_uppercase_check(test_input, expected):
    assert test_input.isupper() == expected


def test_str_substring_replace():
    str = "War is not peace. Freedom is not slavery. Ignorance is not strength."
    assert str.replace(" not", "") == "War is peace. Freedom is slavery. Ignorance is strength."


def test_str_text_formatting():
    str = "My name is {name}. " \
          "My weight is {weight:.1f} lbs. " \
          "English is{native_language} my native language".format(name = "Dmitry Yaskovich",
                                                                  weight = 176.37,
                                                                  native_language = "" if False else " not")
    assert str == "My name is Dmitry Yaskovich. " \
                  "My weight is 176.4 lbs. " \
                  "English is not my native language"


def test_tuple_element_position():
    tpl = ("Google Inc.", "Apple Inc.", "Microsoft Corp.")
    try:
        assert tpl.index("Dimini Inc.")
    except ValueError:
        pass


def test_tuple_elements_count():
    tpl = ("dimini.tk", "dmni.tk",
           "dimini.ml", "dmni.ml",
           "dimini.cf", "dmni.cf",
           "dimini.ga", "dmni.ga",
           "dimini.gq", "dmni.gq",
           "dimini-inc.com",
           "dimini.dev")
    assert len(tpl) == 12


def test_tuple_join():
    tpl_1 = ("Dmitry Yaskovich", 176.37, False)
    tpl_2 = ("Яскович Дмитрий", 80, True)
    assert tpl_1 + tpl_2 == ("Dmitry Yaskovich", 176.37, False,
                             "Яскович Дмитрий", 80, True)
