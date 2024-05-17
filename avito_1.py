a = 1
b = 2
c = 3
d = 4
k = 0
m = 2
N = 1_000

step = (m - k) / N
integral = 0

for i in range(N):
    x = k + step * i
    integral += (a * x**3 + b * x**2 + c * x + d) * step

print(round(integral, 3))


