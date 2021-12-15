# TODO I can make it much smater

import os
import schedule

# get information
def brief():
    os.system('echo "\n\n\n\n" >> gpu.log')
    os.system('nvidia-smi --query-gpu=timestamp,index,utilization.gpu,memory.used,uuid --format=csv >> gpu.log')
    detailed()
def detailed():
    os.system('nvidia-smi >> gpu.log')

# execute every 30 minutes
schedule.every(30).minutes.do(brief)

print("start")
while True:
    schedule.run_pending()