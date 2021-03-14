import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

Gaia.ROW_LIMIT = -1
coord = SkyCoord(ra=0, dec=-60, unit=(u.degree, u.degree), frame='icrs')
radius = u.Quantity(0.01, u.deg)
j = Gaia.cone_search_async(coord, radius)
# r = j.get_results()
# r.pprint()

data = j.get_data()
print(data.colnames)
print(len(data.colnames))
print((data[0]))
print(data['radius_val'])
# print(data['dist'])