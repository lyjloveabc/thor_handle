select
itl_launch_task.content,  u1.name, itl_post_thing_log.created_time,
itl_post_thing_log.status,
itl_launch_task.is_received, itl_do_task.status,
u2.name, itl_launch_task.created_time, itl_do_task.modified_time
from itl_post_thing_log
left join itl_launch_task on itl_launch_task.id = itl_post_thing_log.launch_task_id
left join itl_do_task on itl_do_task.launch_task_id = itl_launch_task.id
left join user u1 on u1.id = itl_post_thing_log.user_id
left join user u2 on u2.id = itl_do_task.executor_user_id
where itl_post_thing_log.zone_id in (2, 76, 82)
and itl_post_thing_log.created_time >= '2017-12-01 00:00:00'
and itl_post_thing_log.created_time <= '2018-02-03 23:59:59'