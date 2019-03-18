zone_id = [87, 106, 118, 121, 122, 127, 129]

sql = """
INSERT INTO `itl_return_visit_cfg` 
(gmt_create, gmt_modified, zone_id, type, st, et, operator_id)
VALUES 
('2019-03-12 00:00:00', '2019-03-12 00:00:00', '{z}', 'POST_THING', null, null, '431'),
('2019-03-12 00:00:00', '2019-03-12 00:00:00', '{z}', 'REPAIR', null, null, '431'),
('2019-03-12 00:00:00', '2019-03-12 00:00:00', '{z}', 'COMPLAIN', null, null, '431'),
('2019-03-12 00:00:00', '2019-03-12 00:00:00', '{z}', 'PRAISE', null, null, '431');
"""

for zId in zone_id:
    print(sql.format(z=zId))