from astroquery.gaia import Gaia

gaiadr2_table = Gaia.load_table('gaiadr2.gaia_source')
for column in (gaiadr2_table.columns):
    print(column.name)