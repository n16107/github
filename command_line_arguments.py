import sys

print(sys.argv)

print('Hello python')
print('open logfile...')

sys.stderr.write('WARNING: log file not found starting a new one\n')


print('finish')