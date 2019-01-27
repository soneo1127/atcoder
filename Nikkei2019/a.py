N,A,B=map(int, input().split())  #複数数値入力

# 最大 A,Bの小さい方
Max = min(A,B)

x = A+B-N
Min = max(x,0)

print(Max, Min)
