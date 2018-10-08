fruits = ['яблоко', 'банан', 'киви', 'арбуз']
i = 0
while i < len(fruits):
  print('{}{}{:>7}'.format(i + 1, '.', fruits[i]))
  i = i + 1
