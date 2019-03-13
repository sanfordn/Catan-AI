from subprocess import Popen, PIPE, STDOUT
p = Popen(['python3', 'catan.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
stdout_data = p.communicate(input=input("how many players: ").encode('utf-8'))[0]
print(stdout_data.decode('utf-8'))
