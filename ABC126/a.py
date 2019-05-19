N, K = map(int, input().split())  #複数数値入力
S = input()
S = S[:K-1] + S[K-1].lower() + S[K:]
print(S)
