#!/usr/bin/env python3

from asterisk.agi import *
from suap_client import *
from agi_handler import AgiHandler

# Incompleto

def handler():
    agi = AGI()
    agi_handler = AgiHandler(agi)
    
    agi.verbose("Inicio.")
    agi.answer()
    
    agi.verbose("A obter matrícula e código de acesso...")
    try:
        enrolment, access_code = agi_handler.ask_enrolment_and_access_code()
        agi.verbose(f"Matrícula: {enrolment}, Código de acesso: {access_code}")

    except Exception as e:
        agi.verbose(f"Erro: {e}")

    suap = SuapClient(
        enrolment= enrolment, 
        responsible_code = access_code
    ) 
    
    boletim = suap.get_boletim()

    agi.hangup()


if __name__ == "__main__":
    handler()
