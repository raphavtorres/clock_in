from create import hit_point

import time
from RPLCD import CharLCD
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

leitorRfid = SimpleMFRC522()

# Raspberry Pi pin setup
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=18, pins_data=[16, 11, 12, 15])

lcd.clear()
lcd.write_string("Registro Ponto")

print("Aproxime o cartao da leitora...")

try:
    id, ra = leitorRfid.read()
    print("ID do aluno: ", id)
    lcd.clear()

    if id == 383529815217:
        hit_point(id)
        lcd.write_string("Tag RFID válida")
        time.sleep(5)
    else:
        lcd.write_string("Tag RFID nao permitida!")
        time.sleep(5)
         
finally:
    GPIO.cleanup()
