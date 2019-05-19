S = input()
num_be = int(S[:2])
num_af = int(S[2:])

if ( ((num_be > 12) & (num_af > 12)) or ( (num_be == 0) & (num_af == 0) ) or ( (num_be == 0) & (num_af > 12) ) or ( (num_be > 12) & (num_af == 0)) ) :
  print('NA')
elif ( ((num_be > 0) & (num_be < 13)) & ((num_af > 0) & (num_af < 13)) ):
  print('AMBIGUOUS')
elif((num_be > 12) or (num_be == 0) ):
  print('YYMM')
else:
  print('MMYY')