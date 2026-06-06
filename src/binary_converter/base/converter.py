from binary_converter import config


class Converter:
    def __init__(self):
        self.upper_letters: dict[str, int] = config.UPPER_LETTERS
        self.lower_letters: dict[str, int] = config.LOWER_LETTERS

    @staticmethod
    def _raw_text_split(bytes_: str) -> list[str]:
        return bytes_.split()

    def to_decimal(self, bytes_: str) -> list[int]:
        raw_letters = self._raw_text_split(bytes_)
        dec_list = []
        for letter in raw_letters:
            dec = 0
            for i, bit in enumerate(letter):
                dec += int(bit) * 2 ** (abs(i - (len(letter) - 1)))
            dec_list.append(dec)

        return dec_list

    def _check_case(self, value: int) -> dict[str, int] | None:
        if 65 <= value <= 90:
            return self.upper_letters
        elif 97 <= value <= 122:
            return self.lower_letters
        return None

    def to_letter(self, text: str) -> list[str]:
        values = self.to_decimal(text)
        letters = []
        for value in values:
            btw = self._check_case(value)
            for item in btw.items():
                if value == item[1]:
                    letters.append(item[0])

        return letters

    def to_text(self, num: str) -> str:
        text = ''
        for letter in self.to_letter(num):
            text += letter
        return text
