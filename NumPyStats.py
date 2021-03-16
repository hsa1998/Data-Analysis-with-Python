import numpy as np

def calculate(list):
  if len(list) != 9:
     raise ValueError('List does not have 9 elements. ')
  oldlist = np.array(list)
  newlist = oldlist.reshape((3,3))
  calculations = {}

  hmean = newlist.mean(axis = 0)
  vmean = newlist.mean(axis = 1)
  fmean = newlist.mean()

  calculations['mean'] = [hmean.tolist(), vmean.tolist(), fmean]

  hvar = newlist.var(axis = 0)
  vvar = newlist.var(axis = 1)
  fvar = newlist.var()

  calculations['variance'] = [hvar.tolist(), vvar.tolist(), fvar]

  hstd = newlist.std(axis = 0)
  vstd = newlist.std(axis = 1)
  fstd = newlist.std()

  calculations['standard deviation'] = [hstd.tolist(), vstd.tolist(), fstd]

  hmax = newlist.max(axis = 0)
  vmax = newlist.max(axis = 1)
  fmax = newlist.max()

  calculations['max'] = [hmax.tolist(), vmax.tolist(), fmax]

  hmin = newlist.min(axis = 0)
  vmin = newlist.min(axis = 1)
  fmin = newlist.min()

  calculations['min'] = [hmin.tolist(), vmin.tolist(), fmin]

  hsum = newlist.sum(axis = 0)
  vsum = newlist.sum(axis = 1)
  fsum = newlist.sum()

  calculations['sum'] = [hsum.tolist(), vsum.tolist(), fsum]

  return calculations

print(calculate([0,1,2,3,4,5,6,7]))

