import pytest

from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('string, result', [
    ('lesson', 'Lesson'),
    ('Task', 'Task'),
    ('stRing', 'String'),
    ('from import', 'From import')
    ])
def test_capitalize_positive(string, result):
    res = string_utils.capitalize(string)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize('string, result', [
    ('123abc', '123abc'),
    ('', ''),
    (''   '', ''   '')
    ])
def test_capitalize_negative(string, result):
    res = string_utils.capitalize(string)
    assert res == result


@pytest.mark.positive
@pytest.mark.parametrize('string, result', [
    (' lesson', 'lesson'),
    ('     Task', 'Task'),
    ('line  ', 'line  ')
    ])
def test_trim_positive(string, result):
    res = string_utils.trim(string)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize('string, result', [
    (' ', ''),
    ('     ', ''),
    ('String', 'String')
    ('', '')
    ])
def test_trim_negative(string, result):
    res = string_utils.trim(string)
    assert res == result


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, result', [
    ('lesson', 's', True),
    ('Task', 'T', True),
    ('5225', '2', True),
    ('Task!', '!', True),
    ('lesson, yes', ',', True),
    ('String', 'ing', True),
    ('new lesson', ' ', True)
    ])
def test_contains_positive(string, symbol, result):
    res = string_utils.contains(string, symbol)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, result', [
    ('lesson', 'h', False),
    ('Task', 't', False),
    ('5225', '6', False),
    ('', 'f', False),
    ('lesson', 'lisson', False),
    ('52256', '52256 ', False)
    ])
def test_contains_negative(string, symbol, result):
    res = string_utils.contains(string, symbol)
    assert res == result


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, result', [
    ('lesson', 's', 'leon'),
    ('Task', 'Tas', 'k'),
    ('5225', '2', '55'),
    ('Good day', ' ', 'Goodday'),
    ('Time?line', '?', 'Timeline'),
    ('calculator', 'calculator', '')
    ])
def test_delete_symbols_positive(string, symbol, result):
    res = string_utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, result', [
    ('lesson', 'sun', 'lesson'),
    ('Task', 't', 'Task'),
    ('5225', '8', '5225'),
    ('skypro', 'skypro cool', 'skypro')
    ])
def test_delete_symbols_negative(string, symbol, result):
    res = string_utils.delete_symbol(string, symbol)
    assert res == result
