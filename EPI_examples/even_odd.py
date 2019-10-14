def even_odd(A):
	next_even, next_odd = 0, len(A) -1
	while next_even < next_odd:
		if A[next_even] % 2 == 0:
			next_even += 1
		else:
			A[next_even], A[next_odd] = A[next_odd], A[next_even]
			next_odd -= 1
			
A = [2,3,5,7,11,13,17,0]

print('original A: ', A)
even_odd(A)
print('after sorting: ', A)

