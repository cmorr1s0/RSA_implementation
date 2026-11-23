# significant thanks to James Lim on StackOverflow

import codecs

_encode_emoji = {
    "\U0001F5FF": b'\x00',                                                         # null
    "\U0001f92f": b'\x01', "\U0001f60d": b'\x02', "\U0001f911": b'\x03',           # tc 1-3
    "\U0001F636": b'\x04', "\U0001f62d": b'\x05', "\U0001F642": b'\x06',           # tc 4-6
    "\U0001f514": b'\x07',                                                         # bell
    "\U0001F353": b'\x08', "\U0001F36C": b'\x09', "\U0001F3B2": b'\x0a',           # fe 0-2
    "\u23F3": b'\x0b', "\U0001F48E": b'\x0c', "\U0001F4A9": b'\x0d',               # fe 3-5
    "\u270c": b'\x0e', "\u270b": b'\x0f', "\U0001f978": b'\x10',                   # so, si, tc7
    "\u2600": b'\x11', "\u2601": b'\x12', "\u26a1": b'\x13', "\u2b50": b'\x14',    # dc 1-4
    "\U0001F641": b'\x15', "\U0001F634": b'\x16', "\U0001f9ca": b'\x17',           # tc 8-10
    "\U0001f383": b'\x18', "\U0001f384": b'\x19',                                  # cancel, end of medium
    "\U0001f389": b'\x1a', "\U0001f37e": b'\x1b',                                  # substitute, escape
    "\u2660": b'\x1c', "\u2663": b'\x1d', "\u2665": b'\x1e', "\u2666": b'\x1f',    # is 1-4
    "\U0001F480": b'\x7f',                                                         # delete
}

_decode_emoji = {
    b'\x00': "\U0001F5FF",                                                         # null
    b'\x01': "\U0001f92f", b'\x02': "\U0001f60d", b'\x03': "\U0001f911",           # tc 1-3
    b'\x04': "\U0001F636", b'\x05': "\U0001f62d", b'\x06': "\U0001F642",           # tc 4-6
    b'\x07': "\U0001f514",                                                         # bell
    b'\x08': "\U0001F353", b'\x09': "\U0001F36C", b'\x0a': "\U0001F3B2",           # fe 0-2
    b'\x0b': "\u23F3", b'\x0c': "\U0001F48E", b'\x0d': "\U0001F4A9",               # fe 3-5
    b'\x0e': "\u270c", b'\x0f': "\u270b", b'\x10': "\U0001f978",                   # so, si, tc7
    b'\x11': "\u2600", b'\x12': "\u2601", b'\x13': "\u26a1", b'\x14': "\u2b50",    # dc 1-4
    b'\x15': "\U0001F641", b'\x16': "\U0001F634", b'\x17': "\U0001f9ca",           # tc 8-10
    b'\x18': "\U0001f383", b'\x19': "\U0001f384",                                  # cancel, end of medium
    b'\x1a': "\U0001f389", b'\x1b': "\U0001f37e",                                  # substitute, escape
    b'\x1c': "\u2660", b'\x1d': "\u2663", b'\x1e': "\u2665", b'\x1f': "\u2666",    # is 1-4
    b'\x7f': "\U0001F480",                                                         # delete
}


# _encode_ascii_bytes = [num.to_bytes() for num in range(128)]
# _encode_ascii = {str(byte.decode("ascii")): byte for byte in _encode_ascii_bytes}

_encode_ascii = {num.to_bytes().decode("ascii"): num.to_bytes() for num in range(128)}

# _decode_ascii_bytes = [num.to_bytes() for num in range(32, 127)]
# _decode_ascii = {byte: str(byte.decode("ascii")) for byte in _decode_ascii_bytes}

_decode_ascii = {num.to_bytes().decode("ascii"): num.to_bytes() for num in range(32, 127)}

_encode_table = {**_encode_ascii, **_encode_emoji}

_decode_table = {**_decode_emoji, **_decode_ascii}

def emoji_encode(text: str) -> tuple:
    # example encoder that converts ints to letters
    # see https://docs.python.org/3/library/codecs.html#codecs.Codec.encode
    return b''.join(_encode_table[x] for x in text), len(text)

def emoji_decode(binary: bytes) -> tuple:
    # example decoder that converts letters to ints
    # see https://docs.python.org/3/library/codecs.html#codecs.Codec.decode
    return ''.join(_decode_table[x.to_bytes()] for x in binary), len(binary)

def emoji_search_function(encoding_name):
    return codecs.CodecInfo(emoji_encode, emoji_decode, name="emoji_ascii")

codecs.register(emoji_search_function)