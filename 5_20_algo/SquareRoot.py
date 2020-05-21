"""
Good morning! Here's your coding interview problem for today.

Given a real number n, find the square root of n. For example, given 
n = 9, return 3.

"""

def square_root(n):
	left=0
	right=n-1
	while left+1<right:
		mid=left+(right-left)//2
		if mid**2==n:
			return mid
		elif mid**2>n:
			right=mid
		elif mid**2<n:
			left=mid

	if right**2>n:
		return left
	else:
		return right

print(square_root(23))