import os

SOUNDS_PATH = '/var/lib/asterisk/agi-bin/Voip-pesquisa-telefonia/sounds'

class AgiHandler:
    def __init__(self, agi: object):
        self.agi = agi
        self.default_timeout = 60000 * 2
    
    def home_menu(self):
        welcome_audio_file = self._get_sound_file_path('boas_vindas')
        menu_audio_file = self._get_sound_file_path('menu')
        try_again_audio_file = self._get_sound_file_path('tentar_novamente')
        
        self.agi.stream_file(welcome_audio_file)
        
        digit = ""
        options = ['1', '2']   
        
        while digit not in options:
            self.agi.stream_file(menu_audio_file)
            digit = self.agi.wait_for_digit(timeout=self.default_timeout)
            
            if digit not in options:
                self.agi.stream_file(try_again_audio_file)
        
        return digit

    def ask_enrolment_and_access_code(self):
        self.agi.stream_file(self._get_sound_file_path("solicita_matricula"))
        enrolment = self.agi.get_data("beep", timeout=20000, max_digits=14)
        
        self.agi.stream_file(self._get_sound_file_path("informe_codigo"))
        access_code = ""
        
        options = ['1', '2']

        for count in range(5):
            selection_digit = ""     
            while selection_digit not in options:
                if count != 0:
                    self.agi.stream_file(self._get_sound_file_path("tipo_char"))
                
                self.agi.stream_file("beep")
                self.agi.verbose("número ou letra, aguardando escolha do usuário...")
                selection_digit = self.agi.wait_for_digit(timeout=self.default_timeout)
            
            char = self._process_responsible_code_entry(selection_digit)
            access_code += char

            if count != 4:
                self.agi.stream_file(self._get_sound_file_path("proximo_char"))

        self.agi.stream_file(self._get_sound_file_path("realizando_consulta"))
        return enrolment, access_code.lower()
    
    def _get_sound_file_path(self, file_name):
        return os.path.join(SOUNDS_PATH, file_name)

    def _process_responsible_code_entry(self, selection_digit):
        if selection_digit == "1":
            self.agi.stream_file(self._get_sound_file_path("selecionado_numero"))
            self.agi.verbose("aguardando entrada...")
            
            self.agi.stream_file("beep")
            char = self.agi.wait_for_digit(timeout=self.default_timeout)
            self.agi.verbose(f"Num: {char} ")     

        elif selection_digit == "2":
            self.agi.stream_file(self._get_sound_file_path("selecionado_letra"))
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
