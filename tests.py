
from subprocess import Popen, PIPE, STDOUT
p = Popen(['python3', 'catan.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
stdout_data = p.communicate(input='4'.encode('utf-8'))[0]
print(stdout_data)
