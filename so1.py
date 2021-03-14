import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

Gaia.ROW_LIMIT = -1
coord = SkyCoord(ra=0, dec=20, unit=(u.degree, u.degree), frame='icrs')
radius = u.Quantity(1.0, u.deg)
j = Gaia.cone_search_async(coord, radius)
r = j.get_results()
r.pprint()
