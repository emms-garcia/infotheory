#!/usr/bin/python
def generate_worst_case(n, pattern):
  repeat_string = pattern[0:len(pattern)-1] + "d"
  string = ""
  for i in range(n-1):
    string += repeat_string
  string += pattern
  return string

def find_string(sub, alpha):
  curr = 0
  at = []
  i = 0
  cont = 0
  while i != len(alpha):
    curr = 0
    if len(sub) > len(alpha[i:len(alpha)]):
      print "Number of Comparations: %s"%cont
      return at
    for j in range(len(sub)):
      cont += 1
      if j + i < len(alpha):
        if alpha[i+j] == sub[j]:
          inicio = i
          curr += 1
        else:
          break
    if curr > 0: i += curr
    else: i += 1
    if curr == len(sub):
      at.append(inicio)
  print "Number of Comparations: %s"%cont
  return at

alpha = "gcagagadgcagagadgcagagadgcagagadgcagagag"
sub = "gcagagag"
alpha = generate_worst_case(1000, sub)
print "Positions found by algorithm: %s"%find_string(sub, alpha)
print "Positions found by python function: %s"%alpha.find(sub)

