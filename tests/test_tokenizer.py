import unittest
from ath import tokenizer

class TokenizerTest(unittest.TestCase):
    def check_tokenize(self, code, itype, value, position):
        t = tokenizer.Tokenizer(code)
        result = t.tokenize()
        print(str(result) + '\n')
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

        code = "num1 = 123;"
        itype = ["identifier", "equals", "integer", "scolon"]
        value = ["num1", "=", "123", ";"]
        position = [(0,0), (0,5), (0,7), (0,10)]
        self.check_tokenize(code, itype, value, position)

        code = "var=5;"
        itype = ["identifier", "equals", "integer", "scolon"]
        value = ["var", "=", "5", ";"]
        position = [(0,0), (0,3), (0,4), (0,5)]
        self.check_tokenize(code, itype, value, position)
    
    def test_declaration_strings(self):
        code = "str = >hello=;"
        itype = ["identifier", "equals", "string", "scolon" ]
        value = ["str", "=", ">hello=", ";"]
        position = [(0,0), (0,4), (0,6), (0,13)]
        self.check_tokenize(code, itype, value, position)

        code = "> hello, world!\\n ==> ;"
        itype = ["string", "print", "scolon"]
        value = ["> hello, world!\\n =", "=>", ";"]
        position = [(0,0), (0,19), (0,22)]
        self.check_tokenize(code, itype, value, position)

    def test_function_declaration(self):
        code = """
ACT func() {
    APPEARIFY 0;
}
"""
        itype = ["act", "identifier", "oparen", "cparen", 
                "obrac", "return", "integer", "scolon", 
                "cbrac"]
        value = ["ACT", "func", "(", ")", "{", "APPEARIFY",
                "0", ";", "}"]
        position = [(1,0), (1,4), (1,8), (1,9), (1,11), (2,4), 
                    (2,14), (2,15), (3,0)]
        self.check_tokenize(code, itype, value, position)

