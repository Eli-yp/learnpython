def Fbi(i):
	if i == 0:
		return 0
	if i == 1:
		return 1
	return Fbi(i-1) + Fbi(i-2)

n = int(input())
for i in range(n):
	print(Fbi(i))
