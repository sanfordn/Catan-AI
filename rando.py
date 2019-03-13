#from subprocess import Popen, PIPE, STDOUT
import subprocess
# p = Popen(['python3', 'catan.py'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
# stdout_data = p.communicate(input=input("How many people are playing? ").encode('utf-8'))[0]
# regOut = stdout_data.decode('utf-8')
def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

def read(process):
    return process.stdout.readline().rstrip().decode("utf-8")


def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()


def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)


proc = subprocess.Popen(['python3','catan.py'],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
write(proc,input("How many people are playing?"))
while True:
    line = read(proc)
    if line != '':
        #the real code does filtering here
        print(line)
    else:
        break
write(proc,input(read(proc)))

# def slicer(my_str,sub):
#     index=my_str.find(sub)
#     if index !=-1 :
#         return my_str[index:]
#     else :
#         raise Exception('Sub string not found!')
#
# print(slicer(stdout_data.decode('utf-8'),"Player"))
