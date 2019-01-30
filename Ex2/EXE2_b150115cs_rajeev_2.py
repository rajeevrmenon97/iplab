n = int(input("Enter value of n (length of sequence A): "))
m = int(input("Enter value of m (length of sequence B): "))
a = []
b = []
c = []
print("Enter elements of sequence A: ")
a = list(map(int, input().rsplit()))
print("Enter elements of sequence B: ")
b = list(map(int, input().rsplit()))
b = list(reversed(b))

"""
b =
for i in range(n):
	p = i - n//2
	if p < 0:
		p = 0
	q = n//2 - i
	if q < 0:
		q = 0
	con = 0
	while p < n and q < n:
		con += a[p] * b[q]
		p += 1
		q += 1
	c.append(con)
"""

a = [0]*(m-1) + a + [0]*(m-1)
for k in range(n + m - 1):
	j = k
	sum = 0
	for i in range(m):
		 sum += a[j] * b[i]
		 j += 1
	c.append(sum)


print("Convolution A*B")
print(*c)
