import random

def solution(ar):
	ar.sort()

	for i in xrange(2, len(ar)):
		if ar[i] < ar[i-2] + ar[i-1]:
			print i
			return 1
	return 0



A = [random.randint(-100, 100) for i in range(10)]
A = [-1] * 10
# print A
print solution(A)
print A