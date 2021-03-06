import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
import numpy as np

radius_limit = 1
radius = u.Quantity(radius_limit, u.deg)

au2ly = 3.26
Gaia.ROW_LIMIT = 10

total_data = []
for ra in range(1):
    for dec in range(-90, -89):
        print('ra %f, dec %f' % (ra, dec))
        coord = SkyCoord(ra=ra, dec=dec, unit=(u.degree, u.degree), frame='icrs')
        j = Gaia.cone_search_async(coord, radius)
        data = j.get_data()
        print(len(data))
        arr = list(np.array(data))
        arr_new = []
        for item in arr:
            assert data.colnames[2] == 'source_id'
            assert data.colnames[96] == 'dist'
            assert data.colnames[9] == 'parallax'
            arr_new.append([item[2], item[96], item[9]])
        # print(type(arr))
        # print(len(list(arr)))
        # print(list(arr))
        total_data.extend(arr_new)

print(total_data)
np.save('./total_data_v2.npy', total_data)
