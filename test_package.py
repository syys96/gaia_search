from astroquery.simbad import Simbad

ret = Simbad.query_object("m1")
ret.pprint(show_unit=True)