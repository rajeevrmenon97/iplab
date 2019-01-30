def conv(a,b,m,n):
	c = []
	b = list(reversed(list(map(list,list(map(reversed,b))))))
	for i in range(m):
		a[i] = [0]*(n-1) + a[i] + [0]*(n-1)
	a = [[0] * (m + 2 * (n - 1))]*(n-1) + a + [[0] * (m + 2 * (n - 1))]*(n-1)
	for i in range(m + n - 1):
		row = []
		for j in range(m + n - 1):
			p = i
			sum = 0
			for s in range(n):
				q = j
				for t in range(n):
					sum += a[p][q] * b[s][t]
					q += 1
				p += 1
			row.append(sum)
		c.append(row)
	return c

"""
def conv(a,b,m,n):
  a = list(reversed(list(map(list,list(map(reversed,a))))))
  c = []
  mid = m//2
  for p in range(n):
	  row = []
	  for q in range(n):
		  s = 0
		  i = p - m//2
		  if i < 0:
			  i = 0
		  j = q - m//2
		  if j < 0:
			  j = 0
		  k = m//2 - p
		  if k < 0:
			  k = 0
		  l = m//2 - q
		  if l < 0:
			  l = 0
		  while i < n and k < m:
			  while j < n and l < m:
				  s += b[i][j] * a[k][l]
				  j += 1
				  l += 1
			  i += 1
			  k += 1
		  row.append(s)
	  c.append(row)
  return c
"""

a = []
b = []
c = []
m = int(input("Enter dimension m of A(mxm) matrix: "))
print("Enter matrix A:")
for _ in range(m):
	a.append(list(map(int, input().rsplit())))
n = int(input("Enter dimension m of B(nxn) matrix: "))
for _ in range(n):
	b.append(list(map(int, input().rsplit())))
c1 = conv(a.copy(),b.copy(),m,n)
c2 = conv(b.copy(),a.copy(),n,m)
print("Convolution A*B")
for i in range(m + n - 1):
	print(*c1[i], sep = "\t")
print("Convolution B*A")
for i in range(m + n - 1):
	print(*c2[i], sep = "\t")
