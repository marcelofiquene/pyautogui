from datetime import datetime
import pandas as pd
import pyautogui
import time
import webbrowser, os
import sys
import pyperclip

# -------------------------
# VERIFICAÇÃO DE RESOLUÇÃO
# -------------------------
resolucao_esperada = (1920, 1080)

if pyautogui.size() != resolucao_esperada:
    print(f"[ERRO] Resolucao atual {pyautogui.size()} não é {resolucao_esperada}.")
    sys.exit()

# -------------------------
# FUNÇÃO PYPERCLIP
# -------------------------
def write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    
# -------------------------
# ABRE O FORMULÁRIO HTML
# -------------------------
webbrowser.open(f"file://{os.path.abspath('form.html')}")
time.sleep(2)

# -------------------------
# LÊ A PLANILHA
# -------------------------
df = pd.read_csv("clientes.csv", encoding="utf-8")

# -------------------------
# COORDENADAS
# -------------------------
coords = {
    "first_name": (394, 265),
    "education": {
        "High School": (337, 516),
        "College": (336, 542),
        "Grad School": (338, 566)
    },
    "sex": {
        "Male": (339, 642),
        "Female": (337, 667)
    },
    "experience_dropdown": (367, 744),
    "submit": (363, 882)
}

# -------------------------
# LOOP PARA PREENCHER TODOS OS CLIENTES
# -------------------------
for index, cliente in df.iterrows():
    print(f"[INFO] Preenchendo cliente {index + 1}...")

    # --- Campo: First Name ---
    pyautogui.click(coords["first_name"])
    write(cliente["first_name"])
    time.sleep(0.5)

    # --- Campo: Last Name ---
    pyautogui.press("tab")
    write(cliente["last_name"])
    time.sleep(0.5)

    # --- Campo: Job Title ---
    pyautogui.press("tab")
    write(cliente["job_title"])
    time.sleep(0.5)

    # --- Education ---
    educ = cliente["education"]
    if educ in coords["education"]:
        pyautogui.click(coords["education"][educ])
        time.sleep(0.5)

    # --- Sexo ---
    sexo = cliente["sex"]
    if sexo in coords["sex"]:
        pyautogui.click(coords["sex"][sexo])
        time.sleep(0.5)

    # --- Dropdown: Years of experience ---

    down_presses = {
    "0-1": 1,
    "2-5": 2,
    "6+": 3
    }

    pyautogui.click(coords["experience_dropdown"])
    exp = cliente["experience"]
    if exp in down_presses:
        for _ in range(down_presses[exp]):
            pyautogui.press('down')
            time.sleep(0.3)
        pyautogui.press('enter')

    # --- Campo de Data ---
    pyautogui.press("tab")
    try:
        data_formatada = datetime.strptime(cliente["date"], "%Y-%m-%d").strftime("%d/%m/%Y")
        pyautogui.write(data_formatada, interval=0.1)
    except ValueError:
        print(f"[ERRO] Data inválida no cliente {index + 1}: {cliente['date']}")
        pyautogui.write("01/01/2000", interval=0.1)
    time.sleep(0.5)

    # --- Submit ---
    pyautogui.click(363, 882)
    print(f"[OK] Cliente {index + 1} enviado.")
    time.sleep(2)
