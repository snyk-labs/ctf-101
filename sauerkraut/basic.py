import os
import subprocess

print('---about to execute os.system---')
output = os.system('whoami')
print(output)

print('---about to execute subprocess.check_output---')
output = subprocess.check_output(['whoami'])
print(output)

