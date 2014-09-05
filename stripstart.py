
import sys
for line in sys.stdin.read().strip().split('\n'):
    sys.stdout.write(', '.join(line.split(', ')[3:]) + '\n')

