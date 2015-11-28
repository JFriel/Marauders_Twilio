from redis import Redis
r = Redis()


def gerData():
    listofMmachines = r.lrange("drillhall-machines",0,-1
