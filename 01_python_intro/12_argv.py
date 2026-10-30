import sys


# Addiert übergebene Werte. Aufrufbar über: python 12_argv.py 3 9

print(sys.argv)

zahl1 = float(sys.argv[1])
zahl2 = float(sys.argv[2])

print(zahl1 + zahl2)