import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing'

pyautogui.hotkey('ctrl','t')
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(10)

pyautogui.click(484, 299, clicks=2)
time.sleep(2)
pyautogui.click(467, 382)
time.sleep(2)
pyautogui.click(1162, 186)
time.sleep(2)
pyautogui.click(986, 565)
time.sleep(10)



import pandas as pd

df= pd.read_excel(r'C:\Users\gabri\Downloads\Vendas - Dez.xlsx')
display(df)
faturamento = df['Valor Final'].sum()
quantidade = df['Quantidade'].sum()


pyautogui.hotkey('ctrl','t')
pyautogui.write('mail.google.com')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(129, 192)
time.sleep(1)
pyautogui.write('gabriel.rodrigues250306+diretoria@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
assunto = 'Relatório de Vendas de Ontem'
pyperclip.copy(assunto)
pyautogui.press('ctrl','v')
pyautogui.press('tab')
pyautogui.write(f'''Prezados, bom dia

O faturamento de ontem foi de R${faturamento:,.2f}
A quantidade de produtos foi de {quantidade:,}

abs:
BatistaPython
''')
pyautogui.hotkey('ctrl','enter')







#time.sleep(5)
#pyautogui.position()