bind = "127.0.0.1:8080"

errorlog = './logs/server.logs'
accesslog = './logs/server.logs'
loglevel = 'info'

workers = 1  # to see if async really rocks
worker_class = 'aiohttp.worker.GunicornWebWorker'
worker_connections = 1000


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)
