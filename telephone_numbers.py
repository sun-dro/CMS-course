def as_numeric(text):
    """

    :param text:
    :return:
    """
    text = text.lower()
    encoding = {
        'a': '2',
        'b': '2',
        'c': '2',
        'd': '3',
        'e': '3',
        'f': '3',
        'g': '4',
        'h': '4',
        'i': '4',
        'j': '5',
        'k': '5',
        'l': '5',
        'm': '6',
        'n': '6',
        'o': '6',
        'p': '7',
        'q': '7',
        'r': '7',
        's': '7',
        't': '8',
        'u': '8',
        'v': '8',
        'w': '9',
        'x': '9',
        'y': '9',
        'z': '9'
    }
    decoded_str = ''
    for char in text:
        if char.isdigit():
            decoded_str += char
        elif char == ' ':
            decoded_str += ' '
        else:
            decoded_str += encoding[char]
    return decoded_str


print(as_numeric('12wz'))


