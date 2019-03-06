import subprocess

completed = subprocess.run(
	['ls','-al'],
	stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(
	len(completed.stdout),
	completed.stdout.decode('utf-8'))
)
