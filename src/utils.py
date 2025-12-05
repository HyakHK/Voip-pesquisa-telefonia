import subprocess, os

def format_boletim(boletim: dict):
    text = []
    for i in boletim['results']:
        disciplina = i.get('disciplina').split("TEC")[1]
        text.append(f"Disciplina: {disciplina},")
        text.append(f"Media Final: {i.get('media_final_disciplina')},")
        text.append(f"Situação: {i.get('situacao')},")
    
    return ''.join(text)

def run_cmd(command):
    subprocess.run(command, check=False)

def wav_to_gsm(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo: {path} não existe.")
    
    fname = "rep.gsm"
    out_dir = os.path.dirname(os.path.abspath(path))
    gsm_out = os.path.join(out_dir, fname)
    wav_to_gsm_cmd = ["sox", path, "-r", "8000", "-c", "1", gsm_out]

    run_cmd(wav_to_gsm_cmd)

    return gsm_out
