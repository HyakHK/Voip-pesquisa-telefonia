class AgiHandler:
    def __init__(self, agi: object):
        self.agi = agi
        self.default_timeout = 60000 * 2
    
    def ask_enrolment_and_access_code(self):
        enrolment = self.agi.get_data("beep", timeout=20000, max_digits=100)
        access_code = ""
        
        for _ in range(5):
            selection_digit = ""     
            while selection_digit not in ["1", "2"]:
                self.agi.verbose("número ou letra, aguardando escolha do usuário...")
                selection_digit = self.agi.wait_for_digit(timeout=self.default_timeout)

            char = self._process_responsible_code_entry(selection_digit)
            access_code += char

        return enrolment, access_code.lower()
    
    def _process_responsible_code_entry(self, selection_digit):
        if selection_digit == "1":
            self.agi.verbose("selecionado: número.")
            self.agi.verbose("aguardando entrada...")
                
            char = self.agi.wait_for_digit(timeout=self.default_timeout)
            self.agi.verbose(f"Num: {char} ")     

        elif selection_digit == "2":
            self.agi.verbose("selecionado: caractere.")
            self.agi.verbose("aguardando entrada...")
                
            char = self._decode_t9( self.agi.get_data(filename="beep", timeout=self.default_timeout, max_digits=5) )
            self.agi.verbose(f"Char: {char}")
        
        return char


    def _decode_t9(self, seq):
        mapping = {
            "2": "A",  "22": "B",  "222": "C",
            "3": "D",  "33": "E",  "333": "F",
            "4": "G",  "44": "H",  "444": "I",
            "5": "J",  "55": "K",  "555": "L",
            "6": "M",  "66": "N",  "666": "O",
            "7": "P",  "77": "Q",  "777": "R",  "7777": "S",
            "8": "T",  "88": "U",  "888": "V",
            "9": "W",  "99": "X",  "999": "Y",  "9999": "Z",
        }

        return mapping.get(seq, "?")
