'''
handles per-object encoding
'''

def encode_int(i):
    assert isinstance(i, int)
    return b'i%de' % i

def encode_string(s):
    assert isinstance(s, str)
    return b'%d:%b' % (len(s), s.encode())

def encode_list(l):
    assert isinstance(l, list)
    return b'l%be' % b"".join([encode(o) for o in l])

def encode_dict(d):
    assert isinstance(d, dict)
    return b'd%be' % b"".join([encode(k) + encode(v) for k, v in d.items()])


def encode(o):
    assert isinstance(o, (int, str, list, dict))
    if isinstance(o, int):
        return encode_int(o)
    elif isinstance(o, str):
        return encode_string(o)
    elif isinstance(o, list):
        return encode_list(o)
    elif isinstance(o, dict):
        return encode_dict(o)
    else:
        raise TypeError(f'{type(o)} is not a valid type')