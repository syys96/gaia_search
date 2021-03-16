from astroquery.gaia import Gaia
from HTMLTable import HTMLTable
table = HTMLTable(caption='Ten stars nearest sun')
# item_list = ('name', 'source_id', 'parallax', 'ra', 'dec', 'ecl_lon', 'ecl_lat',
#                            'pm', 'pmra', 'pmdec', 'pseudocolour', 'phot_g_mean_flux',
#                            'phot_g_mean_mag', 'phot_bp_mean_flux',
#                            'phot_bp_mean_mag', 'phot_rp_mean_flux',
#                            'phot_rp_mean_mag', 'dr2_radial_velocity')
item_list = ('name', 'source_id', 'parallax', 'distance', 'ra', 'dec', 'ecl_lon', 'ecl_lat',
                            'phot_g_mean_mag', 'phot_bp_mean_mag', 'phot_rp_mean_mag')
table.append_header_rows((item_list, ))

Gaia.ROW_LIMIT = 10

query = """SELECT *
FROM gaiaedr3.gaia_source
WHERE parallax >= 300
ORDER BY parallax ASC
"""

star_name = ['Epsilon Eridani (Ran)', 'Ross 248 (HH Andromedae)', 'Ross 154 (V1216 Sagittarii)',
             'Luyten 726-8 B', 'Luyten 726-8 A', 'Sirius', 'Lalande 21185', 'Wolf 359 (CN Leonis)',
             "Barnard's Star (BD+04°3561a)", 'Proxima Centauri']
assert len(star_name) == 10

job = Gaia.launch_job_async(query)
r = job.get_results()
data = job.get_data()

for i in range(1, len(data)):
    data_list = []
    for item_name in item_list:
        if item_name == 'name':
            data_list.append(star_name[i-1])
        elif item_name == 'distance':
            data_list.append(round(3.26 / data['parallax'][i] * 1000, 2))
        else:
            data_list.append(round(data[item_name][i], 2))
    table.append_data_rows((data_list,))

table.caption.set_style({'font-size': '15px', })
table.set_style({
    'border-collapse': 'collapse',
    'word-break': 'keep-all',
    'white-space': 'nowrap',
    'font-size': '14px',
})

table.set_cell_style({
    'border-color': '#000',
    'border-width': '1px',
    'border-style': 'solid',
    'padding': '5px',
})
# 表头样式
table.set_header_row_style({
    'color': '#fff',
    'background-color': '#48a6fb',
    'font-size': '18px',
})

# 覆盖表头单元格字体样式
table.set_header_cell_style({
    'padding': '15px',
})
# 调小次表头字体大小
table[1].set_cell_style({
    'padding': '8px',
    'font-size': '15px',
})

html = table.to_html()
print(html)
print(type(html))
save_name = './table_v2.html'
with open(save_name, 'w') as f:
    f.write(html)


print(len(data))
print(data['parallax'])
print(data.colnames)
# print(r)