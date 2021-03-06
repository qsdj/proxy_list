# -*- coding: UTF-8 -*-
import config

if config.PERSISTENCE['type'] == 'redis':
    from persistence.redis_impl import Redis as persister
elif config.PERSISTENCE['type'] == 'mongo':
    from persistence.mongo_impl import Mongo as persister
else:
    from persistence.redis_impl import Redis as persister
db = persister()


def worker(queue_persistence):
    while True:
        db.add(queue_persistence.get())
