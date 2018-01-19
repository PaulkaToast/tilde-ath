import unittest
from ath import tokenizer

class TokenizerTest(unittest.TestCase):
    def check_tokenize(self, code, itype, value, position):
        t = tokenizer.Tokenizer(code)
        result = t.tokenize()

        for i, tok in enumerate(result):
            print(str(tok) + '\n')
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

    def test_relational_opperators(self):
        code = """ 
a == b;
a != b;
a >= b;
a <= b;
"""
        itype = ["identifier", "rop", "identifier", "scolon",
                "identifier", "rop", "identifier", "scolon",
                "identifier", "rop", "identifier", "scolon",
                "identifier", "rop", "identifier", "scolon",]
        value = ["a", "==", "b", ";", "a", "!=", "b", ";",
                "a", ">=", "b", ";", "a", "<=", "b",";"]
        position = [(1,0), (1,2), (1,5), (1,6), 
                    (2,0), (2,2), (2,5), (2,6),
                    (3,0), (3,2), (3,5), (3,6),
                    (4,0), (4,2), (4,5), (4,6)]
        self.check_tokenize(code, itype, value, position)

    def test_logical_opperators(self):
        code = """
a && b;
a || b;
a = !a;
"""
        itype = ["identifier", "lop", "identifier", "scolon",
                "identifier", "lop", "identifier", "scolon",
                "identifier", "equals", "lop", "identifier", "scolon"]
        value = ["a", "&&", "b", ";", "a", "||", "b", ";",
                "a", "=", "!", "a", ";" ]
        position = [(1,0), (1,2), (1,5), (1,6),
                    (2,0), (2,2), (2,5), (2,6),
                    (3,0), (3,2), (3,4), (3,5), (3,6)]
        self.check_tokenize(code, itype, value, position)

    def test_loops(self):
        code = """
u1 = ALIVE;
u1.lifespan = HE_IS_ALREADY_HERE;

~ATH(u1) {
    > This loop will run forever. ==> ;
}EXECUTE(NULL);
THIS.DIE();
"""
        itype = ["identifier", "equals", "identifier", "scolon",
                "identifier", "dot", "identifier", "equals", "identifier",
                "scolon", "loop", "oparen", "identifier", "cparen", "obrac",
                "string", "print", "scolon", "cbrac", "execute", "oparen",
                "identifier", "cparen", "scolon", "end", "scolon"]
        value = ["u1", "=", "ALIVE", ";", "u1", ".", "lifespan", "=", 
                "HE_IS_ALREADY_HERE", ";", "~ATH", "(", "u1", ")", "{", 
                "> This loop will run forever. =", "=>", ";", "}", 
                "EXECUTE", "(", "NULL", ")", ";", "THIS.DIE()", ";"]
        position = [(1,0), (1,3), (1,5), (1,10), (2,0), (2,2), (2,3), 
                    (2,12), (2,14), (2,32), (4,0), (4,4), (4,5), (4,7),
                    (4,9), (5,4), (5,35), (5,38), (6,0), (6,1), (6,8),
                    (6,9), (6,13), (6,14), (7,0), (7,10)]        
        self.check_tokenize(code, itype, value, position)

    def test_function_factorial(self):
        code = """
ACT fac(x) {
    u1 = ALIVE;
    u1.DIE_UNLESS( x >= 1 );
    ~ATH(u1) {
        APPEARIFY REPLICATE(x, frac(SUBIFY(x, 1)));
        u1.DIE();
    }EXECUTE(u1.REVIVE());
    ~ATH(!u1) {
        APPEARIFY 1;
        u1.REVIVE();
    }EXECUTE(u1.DIE());
}
result = fac(6);
> The result is: $(result) ==> ;
THIS.DIE();
"""
        itype = ["act", "identifier", "oparen", "identifier", "cparen",
                "obrac", "identifier", "equals", "identifier", "scolon",
                "identifier", "dot", "identifier", "oparen", "identifier",
                "rop", "integer", "cparen", "scolon", "loop", "oparen", 
                "identifier", "cparen", "obrac", "return", "identifier",
                "oparen", "identifier", "cama", "identifier", "oparen",
                "identifier", "oparen", "identifier", "cama", "integer",
                "cparen", "cparen", "cparen", "scolon", "identifier",
                "dot", "identifier", "oparen", "cparen", "scolon", "cbrac",
                "execute", "oparen", "identifier", "dot", "identifier",
                "oparen", "cparen", "cparen", "scolon", "loop", "oparen",
                "lop", "identifier", "cparen", "obrac", "return", "integer",
                "scolon", "identifier", "dot", "identifier", "oparen", 
                "cparen", "scolon", "cbrac", "execute", "oparen", "identifier",
                "dot", "identifier", "oparen", "cparen", "cparen", "scolon",
                "cbrac", "identifier", "equals", "identifier", "oparen",
                "integer", "cparen", "scolon", "string", "print", "scolon",
                "end", "scolon"]
        value = ["ACT", "fac", "(", "x", ")", "{", "u1", "=", "ALIVE",
                 ";", "u1", ".", "DIE_UNLESS", "(", "x", ">=", "1", ")",
                 ";", "~ATH", "(", "u1", ")", "{", "APPEARIFY", "REPLICATE",
                 "(", "x", ",", "frac", "(", "SUBIFY", "(", "x", ",", "1",
                 ")", ")", ")", ";", "u1", ".", "DIE", "(", ")", ";", "}",
                 "EXECUTE", "(", "u1", ".", "REVIVE", "(", ")", ")", ";",
                 "~ATH", "(", "!", "u1", ")", "{", "APPEARIFY", "1", ";",
                 "u1", ".", "REVIVE", "(", ")", ";", "}", "EXECUTE", "(",
                 "u1", ".", "DIE", "(", ")", ")", ";", "}", "result", "=",
                 "fac", "(", "6", ")", ";", "> The result is: $(result) =",
                 "=>", ";", "THIS.DIE()", ";"]
        position = [(1,0), (1,4), (1,7), (1,8), (1,9), (1,11), (2,4),
                    (2,7), (2,9), (2,14), (3,4), (3,6), (3,7), (3,17),
                    (3,19), (3,21), (3,24), (3,26), (3,27), (4,4), (4,8),
                    (4,9), (4,11), (4,13), (5,8), (5,18), (5,27), (5,28),
                    (5,29),(5,31), (5,35), (5,36), (5,42), (5,43), (5,44),
                    (5,46), (5,47), (5,48), (5,49), (5,50), (6,8), (6,10),
                    (6,11), (6,14), (6,15), (6,16), (7,4), (7,5), (7,12),
                    (7,13), (7,15), (7,16), (7,22), (7,23), (7,24), (7,25),
                    (8,4), (8,8), (8,9), (8,10), (8,12), (8,14), (9,8),
                    (9,18), (9,19), (10,8), (10,10), (10,11), (10,17), 
                    (10,18), (10,19), (11,4), (11,5), (11,12), (11,13),
                    (11,15), (11,16), (11,19), (11,20), (11,21), (11,22),
                    (12,0), (13,0), (13,7),(13,9), (13,12), (13,13),
                    (13,14), (13,15), (14,0), (14,28), (14,31), (15,0),
                    (15,10)]
        self.check_tokenize(code, itype, value, position)
    
    def test_invalid_token(self):
        code = "$ = 8"

        with self.assertRaises(RuntimeError):
            t = tokenizer.Tokenizer(code)
            result = t.tokenize()