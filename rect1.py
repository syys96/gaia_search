import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
import numpy as np

Gaia.ROW_LIMIT = -1
coord = SkyCoord(ra=301, dec=-60, unit=(u.degree, u.degree, u.pc), frame='icrs')
width = u.Quantity(0.1, u.deg)
height = u.Quantity(0.1, u.deg)
radius = u.Quantity(0.02, u.deg)
r = Gaia.query_object_async(coordinate=coord, width=width, height=height, radius=radius)
print((r['dist']))
print(type(r['designation']))
print(r.colnames)
# print(r['source_id'])
arr = np.array(r)
print(arr.shape)
