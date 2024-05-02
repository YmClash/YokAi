import pyfirmata2
from pyfirmata import util, Arduino
import serial
import serial.tools.list_ports as stool


import time

# PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino('COM4')


print(board)

#
it = pyfirmata2.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    sw = digital_input.read()
    if sw is True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)

















ports =  stool.comports()
for port, desc,hwid in sorted(ports):
    print(f'Port {port}:{desc} : {hwid}')
#
# # import time
# #
# port ='COM4'
# ard_board = Arduino(port)
# #
# board = serial.Serial("COM4",9600)
#
#
# it = util.Iterator(ard_board)
#
#
# it.run()
# print(ard_board)
#
# digital_pin =  ard_board.get_pin('d:10:i')
# led_pin = ard_board.get_pin('d:13:o')
#
# while True:
#
#     sw = digital_pin.read
#     if sw is True:
#         led_pin.write(1)
#     else:
#         led_pin.write(0)
#         time.sleep(0.1)