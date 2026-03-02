import pyautogui
import time

link = 'https://www.spotify.com/'

pyautogui.press('win')        # ou 'winright'
pyautogui.write('brave')          # nome do navegador
pyautogui.press('enter')
time.sleep(2)                     # aguarda o navegador abrir

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(5)                     # aguarda a página carregar

pyautogui.click(x=683, y=149)
time.sleep(1)
pyautogui.write('Tyler, the creator')
pyautogui.press('enter')