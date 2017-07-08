update
user left join zones on zones.id = user.zone_id
set user.company_id = zones.company_id;