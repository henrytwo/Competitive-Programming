import sys
input = sys.stdin.readline

thing = input()

print(thing.index('java') if 'java' in thing else len(thing))
