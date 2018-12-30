import unittest
from game import number_game

test.assert_equals(number_game(2,12), [3, 5, 7, 9, 11])
test.assert_equals(number_game(0,0), [])
test.assert_equals(number_game(2,12), [3, 5, 7, 9, 11])
test.assert_equals(number_game(200,180), [180, 182, 184, 186, 188, 190, 192, 194, 196, 198])
test.assert_equals(number_game(180,200), [181, 183, 185, 187, 189, 191, 193, 195, 197, 199])
