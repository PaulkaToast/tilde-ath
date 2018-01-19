from collections import namedtuple
import re

class Tokenizer:
    TOKEN_TYPES = [
        ("act",        r"\bACT\b"),
        ("end",        r"\bTHIS\.DIE\(\)"),
        ("return",     r"\bAPPEARIFY\b"),
        ("execute",    r"\bEXECUTE\b"),
        ("loop",       r"~ATH"),
        ("oparen",     r"\("),
        ("cparen",     r"\)"),
        ("cbrac",      r"\}"),
        ("obrac",      r"\{"),
        ("dot",        r"\."),
        ("cama",       r","),
        ("scolon",     r";"),
        ("print",      r"=>"),
        ("rop",        r"==|!=|>=|<="),
        ("string",     r">\s*(.*?)="),
        ("rop",        r">|<"),
        ("equals",     r"="),
        ("lop",        r"&&|\|\||!"),
        ("identifier", r"\b[a-zA-Z][a-zA-Z_0-9]*\b"),
        ("integer",    r"\b[0-9]+\b")
    ]

    def __init__(self, code):
        self.code = code
        self.linenos = 0
        self.col = 0

    def tokenize_single_token(self):
        for itype, regex in Tokenizer.TOKEN_TYPES: 
            regex = r"\A(" + regex + ")"

            if itype == "string":
                regex = r"\A" + regex 

            regex = re.compile(regex)
            match = regex.match(self.code)

            if match:
                value = match.group(1)
                self.code = self.code[match.end():]
                
                position = (self.linenos, self.col)
                self.col += match.end()

                return Token(itype, value, position)
        raise RuntimeError('Could not match token to "{}"'.format(self.code))

    def clear_whitespace(self):
        num_to_remove = 0
        for c in self.code:
            if c == '\n':
                self.col = 0
                self.linenos += 1
                num_to_remove += 1
            elif c.isspace():
                self.col += 1
                num_to_remove += 1
            else:
                break
        self.code = self.code[num_to_remove:]

    def tokenize(self):
        tokens = []
        self.clear_whitespace()
        while self.code != "":
            tokens.append(self.tokenize_single_token())
            self.clear_whitespace()
        return tokens

Token = namedtuple('Token', ['itype', 'value', 'position'])