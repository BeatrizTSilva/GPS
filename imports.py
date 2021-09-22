# https://stackoverflow.com/questions/28867795/reading-i2c-data-from-gps
import smbus
import time

bus = smbus.SMBus(1)
address = 0x42
bus.read_byte_data(address,0x00)
bus.read_byte(address)
