import src.bencode as bc
import src.bdecode as bd

def test():

    s = "the quick brown fox jumps over the lazy dog"
    i = 40320
    l = ['a', 'b', 1, 2]
    d = {'a': 1, 'b': 2}

    print('forward:\n')
    print(f'original: {s}\nencoded: {bc.encode(s)}\n')
    print(f'original: {i}\nencoded: {bc.encode(i)}\n')
    print(f'original: {l}\nencoded: {bc.encode(l)}\n')
    print(f'original: {d}\nencoded: {bc.encode(d)}\n')
    print('backward:\n')
    print(f'encoded: {bc.encode(s)}\ndecoded: {bd.decode(bc.encode(s))}\n')
    print(f'encoded: {bc.encode(i)}\ndecoded: {bd.decode(bc.encode(i))}\n')
    print(f'encoded: {bc.encode(l)}\ndecoded: {bd.decode(bc.encode(l))}\n')
    print(f'encoded: {bc.encode(d)}\ndecoded: {bd.decode(bc.encode(d))}\n')

if __name__ == "__main__":
    test()