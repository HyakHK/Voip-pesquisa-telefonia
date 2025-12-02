#!/usr/bin/env python3

from asterisk.agi import *
from suap_client import *

# ** Código incompleto ** 

def handler():
    agi = AGI()
    agi.verbose("Inicio.")
    agi.answer()
    
    res = agi.get_data("beep", timeout=20000, max_digits=100) # captura os digitos do usuário
    digits = res

    suap = SuapClient(enrolment="", responsible_code="") # sua matrícula e código de acesso aí
    boletim = suap.get_boletim()

    agi.hangup()


if __name__ == "__main__":
    handler()
