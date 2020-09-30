def contracting(l):
  for i in range(1, len(l) - 1):
    if abs(l[i] - l[i-1]) > abs(l[i + 1] - l[i]):
      continue
    else:
      return(False)
  return(True)
