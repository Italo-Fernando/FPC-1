B = int(input())
T = int(input())
R1 = bool(0 < B <160 and 0 < T < 160)


if R1:
  cal = T + B
  if cal == 160:
    print(0)
  elif cal > 160:
    print(1)
  else:
    print(2)
