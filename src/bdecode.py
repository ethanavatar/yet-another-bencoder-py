import re

'''
handles per-object decoding
'''

def decode_int(x):
    assert isinstance(x, bytes)
    return int(x[1:][:-1])

def decode_string(x):
    assert isinstance(x, bytes)
    l = re.match(b'(\d+)', x)
    if not l:
        raise Exception('Invalid bencoded string')
    s = x[len(l.group())+1:]
    return str(s, 'utf-8')

def decode_list(x):
    raise NotImplementedError
    assert isinstance(x, bytes)
    return [decode(i) for i in x]

def decode_dict(x):
    raise NotImplementedError
    assert isinstance(x, bytes)
    return {decode(x): decode(x) for x in x}

def decode(x):
    '''
    decode a bencoded object
    '''
    assert isinstance(x, bytes)

    match = str(x, 'utf-8')[0]
    if match in '0123456789':
        return decode_string(x)

    elif match == 'i':
        return decode_int(x)
    
    elif match == 'l':
        return decode_list(x)
    
    elif match == 'd':
        return decode_dict(x)
    
    else:
        raise Exception('Invalid bencoded object')
    