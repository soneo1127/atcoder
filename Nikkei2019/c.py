import numpy as np

N = int(input())  #数値入力
A=[]
B=[]
for i in range(N):
  a,b=map(int, input().split())  #複数数値入力
  A.append(a)
  B.append(b)

A=np.array(A)
B=np.array(B)
# print(A)
# print(B)
A_point=0
B_point=0

count=0

for i in range( int(N/2 + 1) ):
  if (A.max() > B.max() ):
    a_index = int(A.argmax())
    A_point += A[a_index]
    A = np.delete(A, a_index)
    B = np.delete(B, a_index)
  elif (A.max() < B.max() ):
    b_index = int(B.argmax())
    A_point += A[b_index]
    A = np.delete(A, b_index)
    B = np.delete(B, b_index)
  elif (A.max() == B.max() ):
    a_index = int(A.argmax())
    A_point += A[a_index]
    A = np.delete(A, a_index)
    B = np.delete(B, a_index)
  # print("A_point")
  # print(A_point)
  count+=1
  if (N == count):
    break
  if (A.max() > B.max() ):
    a_index = int(A.argmax())
    B_point += B[a_index]
    A = np.delete(A, a_index)
    B = np.delete(B, a_index)
  elif (A.max() < B.max() ):
    b_index = int(B.argmax())
    B_point += B[b_index]
    A = np.delete(A, b_index)
    B = np.delete(B, b_index)
  elif (A.max() == B.max() ):
    b_index = int(B.argmax())
    B_point += B[b_index]
    A = np.delete(A, b_index)
    B = np.delete(B, b_index)
  # print("B_point")
  # print(B_point)
  count+=1
  if (N == count):
    break
# 最大 A,Bの小さい方

print(A_point-B_point)
