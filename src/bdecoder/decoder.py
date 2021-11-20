import re

'''
handles per-object decoding
'''

match_num = re.compile('(\d+)')
match_int = re.compile('i(\d+)e')
match_str = re.compile('(\d+):.')
match_list = re.compile('l(.*)ee')
match_dict = re.compile('d(.*)ee')

def decode_int(x):
    return int(x[1:][:-1])

def decode_string(x):
    length = match_num.match(x)
    if not length:
        raise Exception('Invalid bencoded string')
    return x[len(length.group())+1:]

def decode_list(x):
    l =  []
    tok = ''

    for char in str(x)[1:]:
        tok += char
        if match_int.match(tok):
            l.append(decode_int(tok))
            tok = ''
            continue
        elif match_str.match(tok):
            l.append(decode_string(tok))
            tok = ''
            continue
    return l

def decode_dict(x):
    d = {}
    tok = ''
    key = True
    last_key = ''
    for char in str(x)[1:]:
        tok += char
        if key:
            if match_int.match(tok):
                d[decode_int(tok)] = None
                last_key = decode_int(tok)
                tok = ''
                key = False
                continue
            elif match_str.match(tok):
                d[decode_string(tok)] = None
                last_key = decode_string(tok)
                tok = ''
                key = False
                continue
        else:
            if match_int.match(tok):
                d[last_key] = decode_int(tok)
                tok = ''
                key = True
                continue
            elif match_str.match(tok):
                d[last_key] = decode_string(tok)
                tok = ''
                key = True
                continue
    return d

def decode(x):
    '''
    decode a bencoded object
    '''
    assert isinstance(x, bytes)

    case = str(x, 'utf-8')
    if match_int.match(case):
        return decode_int(case)

    elif match_str.match(case):
        return decode_string(case)
    
    elif match_list.match(case):
        return decode_list(case)
    
    elif match_dict.match(case):
        return decode_dict(case)
    
    else:
        raise Exception('Invalid bencoded object')
    