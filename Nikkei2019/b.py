N = int(input())  #数値入力
A = str(input())
B = str(input())
C = str(input())

count = 0
for i in range(N):
  if ( (A[i] != B[i]) & (A[i] != C[i]) & (B[i] != C[i])):
    count+=2
  else:
    if ( (A[i] != B[i]) & (A[i] == C[i]) & (B[i] != C[i]) ):
      count+=1
    if ( (A[i] != B[i]) & (A[i] != C[i]) & (B[i] == C[i]) ):
      count+=1
    if ( (A[i] == B[i]) & (A[i] != C[i]) & (B[i] != C[i]) ):
      count+=1

print(count)