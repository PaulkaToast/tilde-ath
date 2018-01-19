import unittest
from ath import tokenizer

class TokenizerTest(unittest.TestCase):
    def check_tokenize(self, code, itype, value, position):
        t = tokenizer.Tokenizer(code)
        result = t.tokenize()
        for i, tok in enumerate(result):
            self.assertEqual(tok.itype, itype[i])
            self.assertEqual(tok.value, value[i])
            self.assertEqual(tok.position, position[i])

    def test_declaration_nums(self):
        code = "var = 5;"
        itype = ["identifier", "equals", "integer", "scolon"]
        value = ["var", "=", "5", ";"]
        position = [(0,0), (0,4), (0,6), (0,7)]
        self.check_tokenize(code, itype, value, position)


