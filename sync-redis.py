import redis

r = redis.StrictRedis(host='213.32.89.6', port='7644', db=0)

for key in r.scan_iter():
  try:
    value = r.hgetall(key)
    print value
    break
  except ValueError:
    print "Oops!"