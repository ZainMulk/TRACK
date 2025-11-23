# TRACK code to run CDS data 
import cf 
import cfplot as cfp
f=f('ff_trs_pos.new.nc)
g=f[5]
h=g[5]
cfp.mapset(proj='npstere')
cfp.traj(h)
