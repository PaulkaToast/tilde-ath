from collections import namedtuple
import re

class Tokenizer:
    TOKEN_TYPES = [
        ("act",        r"\bACT\b"),
        ("end",        r"\bTHIS\.DIE()\b"),
        ("return",     r"\bAPPEARIFY\b"),
        ("execute",    r"\bEXECUTE\b"),
        ("loop",       r"~ATH"),
        ("oparen",     r"\("),
        ("cparen",     r"\)"),
        ("cbrac",      r"\}"),
        ("obrac",      r"\{"),
        ("dot",        r"\."),
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
                return Token(itype, value)
        raise RuntimeError('Could not match token to "{}"'.format(self.code))

    def tokenize(self):
        tokens = []
        while self.code != "":
            tokens.append(self.tokenize_single_token())
            self.code = self.code.strip()
        return tokens

Token = namedtuple('Token', ['itype', 'value'])