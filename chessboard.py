check = ''
pro_file = 30425624
print('  a b c d e f g h  ')
for x in range(0,8):
 for y in range(0,8):
  if x%2 == 0:
   if y%2 == 1:
    check = check + '⬛️'
   else:
    check = check + '⬜️'
  else:
   if y%2 == 0:
    check = check + '⬛️'
   else:
    check = check + '⬜️'
 print(str(8-x) + check)
 check = ''
print("\n")
print("♟️♟️♟️👑")