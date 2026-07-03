from binary_converter import Converter


def test_binary_to_decimal():
    result = Converter.binary_to_decimal('1010010 1101111 1101101 1100001')

    assert result == [82, 111, 109, 97]


def test_to_text():
    con = Converter()
    result = con.to_text('1000011 1101000 1101001 1101110 1100001')

    assert result == 'China'


def test_letter_to_decimal():
    result = Converter.letter_to_decimal('EUA')
    assert result == [69, 85, 65]


def test_to_binary():
    result = Converter.to_binary('BraSil')

    assert result == '1000010 1110010 1100001 1010011 1101001 1101100'


def test_to_binary_text():
    result = Converter.to_binary('O Rato roeu a roupa do Rei de Roma')

    assert result == ('1001111 0100000 1010010 1100001 '
                      '1110100 1101111 0100000 1110010 '
                      '1101111 1100101 1110101 0100000 '
                      '1100001 0100000 1110010 1101111 '
                      '1110101 1110000 1100001 0100000 '
                      '1100100 1101111 0100000 1010010 '
                      '1100101 1101001 0100000 1100100 '
                      '1100101 0100000 1010010 1101111 '
                      '1101101 1100001')


def test_to_text_binary():
    result = Converter.to_text('1001111 0100000 1010010 1100001 '
                               '1110100 1101111 0100000 1110010 '
                               '1101111 1100101 1110101 0100000 '
                               '1100001 0100000 1110010 1101111 '
                               '1110101 1110000 1100001 0100000 '
                               '1100100 1101111 0100000 1010010 '
                               '1100101 1101001 0100000 1100100 '
                               '1100101 0100000 1010010 1101111 '
                               '1101101 1100001')

    assert result == 'O Rato roeu a roupa do Rei de Roma'
