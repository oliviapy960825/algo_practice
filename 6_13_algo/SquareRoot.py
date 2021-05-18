"""
写一个函数，求平方根，函数参数为目标数字和精度，测试案例 fn(4.1,0.001) 
fn(501.1,0.001) fn(0.045,0.001) 
"""

def fn(num, decimal):
	l=0
	r=num/2
	while l<r:
		mid=l+(r-l)/2
		diff=mid**2-decimal
		if abs(diff)<=decimal:
			return mid
		if diff>0:
			r=mid
		else:
			l=mid
	if abs(l**2-num)<=decimal:
		return l
	return r

print(fn(4.1, 0.001))
