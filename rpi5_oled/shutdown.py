# 前面省略，从下面直奔主题，举个代码例子：
#!/usr/bin/python3

import logging
import subprocess
import re
import smbus
import time

address         = 0x2D
shutdown_reg    = 0x45
test_commond    = 0x00
bus = smbus.SMBus(0)
"""
logging.basicConfig(
    filename = '/home/pi/Desktop/pistatus.log',
    level = logging.DEBUG,
    format = '%(asctime)s %(message)s',
    datefmt = '%d/%m/%Y %H:%M:%S')
"""


sysJobTargets = subprocess.check_output(["sudo","systemctl","list-jobs"]).decode('utf-8')
# if re.search('reboot.target.*start',sysJobTargets) == None:
if re.search('reboot.target*',sysJobTargets) == None:
    logging.info('Raspberry Pi power off')
    # bus.write_byte_data(address,test_commond,test_commond)
    # bus.write_byte_data(address,shutdown_reg,0x88)
    bus.write_i2c_block_data(address, 0x00, [0xFF, 0xFF])
    time.sleep(0.1)  # Wait a bit to ensure the signal is sent
    bus.write_i2c_block_data(address, 0x00, [0xFF, 0xFE])
    time.sleep(0.1)  # Wait a bit to ensure the signal is sent


