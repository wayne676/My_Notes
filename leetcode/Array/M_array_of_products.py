'''
"array": [5, 1, 4, 2] ->
[8, 40, 10, 20]
// 8 = 1x4x2
//40 = 5x4x2
//10 = 5x1x2
//20 = 5x1x4
'''
# method 1 o(n*n)
def arrayOfProducts(array):
	r=[]
	for i in range(array):
		x=1
		for j in range(array):
			if j==i:
				continue
			x=array[j]*x
		r.append(x)
	return r

# method 2 o(n)
def arrayOfProducts(array):
	# Write your code here.
	zeros=[]
	productsWithoutZero=1
	for i,v in enumerate(array):
		if v ==0:
			zeros.append(i)
		else:
			productsWithoutZero*=v
	result=[]
	for i,v in enumerate(array):
		if v==0:
			if len(zeros)>1:
				result.append(0)
			else:
				result.append(productsWithoutZero)
		else:
			if len(zeros)>0:
				result.append(0)
			else:
				result.append(productsWithoutZero/v)
	return result