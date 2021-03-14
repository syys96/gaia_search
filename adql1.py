from astroquery.gaia import Gaia

query = """SELECT DISTANCE(
  POINT('ICRS', 266.41683, -29.00781),
  POINT('ICRS', ra, dec)) AS dist, *
FROM gaiaedr3.gaia_source
WHERE 1=CONTAINS(
  POINT('ICRS', 266.41683, -29.00781),
  CIRCLE('ICRS',ra, dec, 0.08333333))
ORDER BY dist ASC
"""

job = Gaia.launch_job_async(query)
r = job.get_results()
print(r)