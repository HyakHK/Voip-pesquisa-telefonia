#!/usr/bin/env python3

from asterisk.agi import *
from suap_client import *
from utils import *
from agi_handler import AgiHandler
from text_to_speech import text_to_speech

# Incompleto

def handler():
   try:
        agi = AGI()
        agi_handler = AgiHandler(agi)
        
        agi.verbose("Inicio.")
        agi.answer()

        agi_handler.home_menu()
        
        agi.verbose("A obter matrícula e código de acesso...")
       
        enrolment, access_code = agi_handler.ask_enrolment_and_access_code()
        agi.verbose(f"Matrícula: {enrolment}, Código de acesso: {access_code}")

        suap = SuapClient(
          enrolment=enrolment, 
          responsible_code= access_code
        ) 
        
        boletim = suap.get_boletim()
        text_boletim = format_boletim(boletim)
        audio_wav = text_to_speech(text_boletim)
        audio_gsm = wav_to_gsm(audio_wav)

        agi.stream_file(audio_gsm.split(".gsm")[0])

        agi.send_command
        agi.hangup()
    
   except Exception as e:
        agi.verbose(f"Erro: {e}")

if __name__ == "__main__":
    handler()
