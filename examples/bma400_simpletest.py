# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_bma400 import bma400

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
bma = bma400.BMA400(i2c)

while True:
    accx, accy, accz = bma.acceleration
    print("x:{:.2f}G y:{:.2f}G z:{:.2f}G".format(accx, accy, accz))
    time.sleep(0.5)
