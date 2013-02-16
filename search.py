#!/usr/bin/python
def generate_worst_case(P, n):
  repeat_string = P[0:len(P)-1] + "d"
  T = ""
  for i in range(n-1):
    T += repeat_string
  T += P
  return T  

#Do a simple search of a sub-string P in a string T.
#P = Pattern to search.
#T = Text potentially containing the pattern.
def naive_search(P, T):
  at = []
  i = 0
  cont = 0
  for i in range(len(T)):
    curr = 0
    for j in range(len(P)):
      cont += 1
      if j + i < len(T):
        if T[i+j] == P[j]:
          inicio = i
          curr += 1
        else: 
          inicio = 0
    if curr == len(P):
      at.append(inicio)
  print "Number of Comparations: %s"%cont
  return at

def kmp(P, T):
  curr = 0
  at = []
  i = 0
  cont = 0
  while i != len(T):
    curr = 0
    if len(P) > len(T[i:len(T)]):
      print "Number of Comparations: %s"%cont
      return at
    for j in range(len(P)):
      cont += 1
      if j + i < len(T):
        if T[i+j] == P[j]:
          match = i
          curr += 1
        else:
          break
    if curr > 0: i += curr
    else: i += 1
    if curr == len(P):
      at.append(match)
  print "Number of Comparations: %s"%cont
  return at

def MAX(a, b):
  if a > b: return a
  else: return b

def zeros(n):
  vect = []
  for i in range(n):
    vect.append(0)
  return vect

def preBmBc(T, P):
  m = len(P)
  n = len(T)
  bmBc = {}

  for i in range( n - 1):
    if T[i] not in P:
      bmBc[T[i]] = m

  for i in range( m - 1):
    bmBc[P[i]] = m - i - 1

  return  bmBc

def suffixes(P, m):
  suff = zeros(m)
  suff[m - 1] = m
  g = m - 1
  f = 0
  for i in range(m-2, -1, -1):
    if i > g and suff[i + m - 1 - f] < i - g:
      suff[i] = suff[i + m - 1 - f]
    else:
      if (i < g):
        g = i
      f = i
      while (g >= 0 and P[g] == P[g + m - 1 - f]):
        g -= 1
      suff[i] = f - g
  return suff


def preBmGs(P, m):
  suff = suffixes(P, m)
  print "Sufixes: %s"%suff
  bmGs = []
  for i in range(m):
    bmGs.append(m)
  j = 0
  for i in range(m - 2, -1, -1):
    if (suff[i] == i + 1):
     for j in range(m - 1 - 1):
        if (bmGs[j] == m):
           bmGs[j] = m - 1 - i
  for i in range(m - 1):
    bmGs[m - 1 - suff[i]] = m - 1 - i
  return bmGs


def BM(P, T):
  n = len(T)
  m = len(P)
  bmGs = preBmGs(P, m)
  bmBc = preBmBc(T, P)
  print bmGs
  print bmBc
  j = 0
  matches = []
  while (j <= n - m):
    i = m - 1
    while True:
      if i >= 0 and P[i] == T[i + j]:
        i -= 1
      else:
        break
    if i < 0: 
      matches.append(j)
      j += bmGs[0]
    else:
      j += max(bmGs[i], bmBc[T[i + j]] - m + 1 + i)

  return matches

T = "gcatcgcagagagtatacagtacg"
P = "gcagagag"
#T = generate_worst_case(P, 1000)
#print "Positions found by algorithm: %s"%kmp(P, T)
print "Positions found by algorithm: %s"%BM(P, T)
print "Positions found by python function: %s"%T.find(P)
