from binary_converter import Converter

def test_to_decimal():
    con = Converter()
    result = con.to_decimal('1010010 1101111 1101101 1100001')

    assert result == [82, 111, 109, 97]


def test_to_letter():
    con = Converter()
    text = '1000001 1010010 1000111 1000101 1001110 1010100 1001001 1001110 1000001'
    result = con.to_letter(text)

    assert result == ['A', 'R', 'G', 'E', 'N', 'T', 'I', 'N', 'A']


def test_to_text_upper():
    con = Converter()
    text = '1010100 1000101 1011000 1000001 1010011'
    result = con.to_text(text)

    assert result == 'TEXAS'


def test_to_text_lower():
    con = Converter()
    text = '1100011 1101000 1101001 1101110 1100001'
    result = con.to_text(text)

    assert result == 'china'


def test_to_text_mixed():
    con = Converter()
    text = '1000010 1110010 1100001 1010011 1101001 1101100'
    result = con.to_text(text)

    assert result == 'BraSil'
