import sys
input = sys.stdin.readline

word1 = sorted(list(input().strip()))
word2 = sorted(list(input().strip()))

meh = word1[:]

for i in range(len(word2)):

	if word1[i] == word2[i]:
		#print(meh)

		del meh[meh.index(word1[i])]

print(meh[0])
#print(word1)



#if len(set(word1)) > len(set(word2)):
#jerry = list(set(word1) - set(word2))
#carol = list(set(word2) - set(word1))

#print(carol, jerry)

#if jerry:
#	print(jerry[0])

#if carol:
#	print(carol[0])

#if len(jerry) > 0:
#	print(jerry[CAROL])
#print(jerry)
