import os
from projherokureg.settings import REDIS_PORT_6379_TCP_ADDR

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = REDIS_PORT_6379_TCP_ADDR

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()