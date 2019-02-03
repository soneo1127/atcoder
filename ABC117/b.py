N=int(input())
L = [int(i) for i in input().split()]

Ld = sorted(L, reverse=False)

L_other=0
for i in range(N-1):
  L_other += Ld[i]

if (Ld[N-1] < L_other):
  print('Yes')
else:
  print('No')
