import pytest

import bencoder as bc
import bdecoder as bd

@pytest.mark.parametrize("test_input, expected", [
    (0, b'i0e'),
    (1, b'i1e'),
    (40320, b'i40320e'),
    #(-40320, b'i-40320e'), # TODO: negative numbers

    #('', b''), # TODO: empty string
    ('a', b'1:a'),
    ('abc', b'3:abc'),
    ('the quick brown fox jumps over the lazy dog', b'43:the quick brown fox jumps over the lazy dog'),

    #([], b'le'), # TODO: empty list
    ([1, 2, 3], b'li1ei2ei3ee'),
    (['a', 'b', 1, 2], b'l1:a1:bi1ei2ee'),

    #({}, b'de'), # TODO: empty dict
    ({'a': 1, 'b': 2}, b'd1:ai1e1:bi2ee'),

    #([1, 2, 3, [4, 5, 6]], b'li1ei2ei3el4ei5ei6ee'), # TODO: list in list
    #([1, 2, 3, {'a': 1, 'b': 2}], b'li1ei2ei3d1:ai1e1:bi2eee'), TODO: dict in list

    #({'a': ['a', 'b', 1, 2]}, b'd1:a1:al1:a1:bi1ei2eee'), # TODO: list in dict
    #({'a': {'a': 1, 'b': 2}}, b'd1:a1:d1:ai1e1:bi2eee'), # TODO: dict in dict

    #([[1, 2, 3], {'a': 1, 'b': 2}], b'li1ei2ei3d1:ai1e1:bi2eee'), # TODO: list and dict in list
    #({'a': [1, 2, 3], 'b': {'a': 1, 'b': 2}}, b'd1:ai1ei2ei3d1:ai1e1:bi2eee'), # TODO: list and dict in dict

])
class Test:

    def test_encode(self, test_input, expected):
        assert bc.encode(test_input) == expected, f'Expected: {expected}, instead got {bc.encode(test_input)}'

    def test_decode(self, test_input, expected):
        assert bd.decode(expected) == test_input, f'Expected: {expected}, instead got {bd.decode(test_input)}'