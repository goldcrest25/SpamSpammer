import random
import string

def _get_random_item(arr):
    idx = random.randint(1, len(arr)) - 1
    return arr[idx]

class Inputifier:
    domains = ["co", "com", "co.ck", "net", "org"]
    separator_chars = ['_', '-', '.']

    def __init__(self):
        # TODO: make this configurable
        with open("nasty-things-to-say.txt") as file:
            data = file.read().splitlines()
        self.lines = [datum for datum in data if datum != ""]
        print(f"{len(self.lines)} line(s) read from datafile")

    # TODO: refactor such that lines/domain/separator are gathered together
    def GetRandomEmailAddress(self):
        line1 = _get_random_item(self.lines).lower()
        line2 = _get_random_item(self.lines).lower()
        domain = _get_random_item(self.domains)
        separator_char = _get_random_item(self.separator_chars)

        line1 = line1.replace(' ', separator_char)
        line2 = line2.replace(' ', separator_char)

        return f"{line1}@{line2}.{domain}"
    
    def GetRandomPassword(self):
        substitution_chars = [
            ( 'o', '0' ),
            ( 'i', '1' ),
            ( 'z', '2' ),
            ( 'e', '3' ),
            ( 's', '5' ),
            ( 'a', '@' ),
        ]
        
        line = _get_random_item(self.lines)
        separator_char = _get_random_item(self.separator_chars)

        for schar in substitution_chars:
            do_substitution = random.randint(0, 1) == 1
            if(do_substitution):
                line = line.replace(schar[0], schar[1])
        
        line.replace(' ', separator_char)

        return line
