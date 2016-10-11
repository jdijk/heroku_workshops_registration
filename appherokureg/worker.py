import os
import redis
from rq import Worker, Queue, Connection

# REDIS settings, local or docker if we have the right env var:
REDIS_PORT_6379_TCP_ADDR = 'redis://redis:6379'

if 'REDIS_PORT_6379_TCP_PORT' in os.environ:
    REDIS_PORT_6379_TCP_ADDR = os.environ['REDIS_PORT_6379_TCP_ADDR ']
else:
    print ('REDIS_PORT_6379_TCP_ADDR not in environ')

# else we're on Heroku
if 'REDIS_URL' in os.environ:
    REDIS_PORT_6379_TCP_ADDR  = os.environ['REDIS_URL']
else:
    print ('REDIS_URL not in environ - so not in Heroku')


listen = ['high', 'default', 'low']

redis_url = REDIS_PORT_6379_TCP_ADDR

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()