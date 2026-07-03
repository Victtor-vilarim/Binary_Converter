from binary_converter import config


class Converter:

    @staticmethod
    def binary_to_decimal(bytes_: str) -> list[int]:
        bytes_ = bytes_.split()
        dec_list = []
        for byte_ in bytes_:
            dec = 0
            for i, bit in enumerate(byte_):
                dec += int(bit) * 2 ** (abs(i - (config.ASCII_BYTE_SIZE - 1)))
            dec_list.append(dec)

        return dec_list

    @classmethod
    def to_text(cls, bytes_: str) -> str:
        text = ''
        for num in cls.binary_to_decimal(bytes_):
            text += chr(num)
        return text

    @staticmethod
    def letter_to_decimal(text: str) -> list[int]:
        return [ord(letter) for letter in text]

    @classmethod
    def to_binary(cls, text: str) -> str:
        nums = cls.letter_to_decimal(text)
        bytes_ = ''
        for num in nums:
            bytes_ += f'{num:b}'.rjust(config.ASCII_BYTE_SIZE, '0')
            bytes_ += ' '

        return bytes_[0:len(bytes_) - 1]
