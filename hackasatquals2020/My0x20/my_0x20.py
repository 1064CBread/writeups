import numpy as np
from numpy import genfromtxt

starlocs = genfromtxt('test.txt', delimiter=',') #reference database
nsat = np.shape(starlocs)[0] #number of challenge stars
pdist = np.zeros((nsat,nsat)) #pairwise distances
for i in range(nsat):
 for j in range(nsat):
    pdist[i,j] = np.linalg.norm(starlocs[i,0:3] - starlocs[j,0:3])

dists = np.zeros((nsat,nsat)) #sorted pairwise distances
for i in range(nsat):
 dists[i,:] = pdist[i,:]
 dists[i,:] = np.sort(dists[i,:])

def dd(row, d2): #error between "signatures"
 err = 0
 for i in d2:
    err += np.min(np.abs(row - i))
 return err

def bestrow(d2): #get the best match in the database
 errs = np.zeros(nsat)
 for i in range(nsat):
    errs[i] = dd(dists[i,:], d2)
 return (np.argmin(errs), np.min(errs))

ch = genfromtxt('chal.txt', delimiter=',') #copy-pasted the challenge from the server here.
nch = np.shape(ch)[0] #number of challenge stars
pd2 = np.zeros((nch,nch)) #pairwise distance of challenge stars
for i in range(nch):
 for j in range(nch):
    pd2[i,j] = np.linalg.norm(ch[i,0:3] - ch[j,0:3])

ans = ()
for s in range(5):
    ans += (bestrow(pd2[s,:])[0],) #compute the best match for each

print(ans) #and print