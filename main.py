import src.bencode as bc
import src.bdecode as bd

def main():
    '''
    Tests each object handled by bencode/bdecode
    '''
    s = bc.encode("the quick brown fox jumps over the lazy dog")
    print(s)

    i = bc.encode(1)
    print(i)

    l = bc.encode(['a', 'b', 1, 2])
    print(l)

    d = bc.encode({'a': 1, 'b': 2})
    print(d)

    print()

    print(bd.decode(s))
    print(bd.decode(i))
    #print(bd.decode(l)) TODO
    #print(bd.decode(d)) TODO

if __name__ == "__main__":
    main()