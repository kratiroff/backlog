import redis
import json

r = redis.StrictRedis(host='213.32.89.6', port='7644', db=0)

for key in r.scan_iter():
  try:
    value = r.hgetall(key)
    parsed = ''
    if type(value) is str:
      parsed = json.dumps(json.loads(value), sort_keys=True, indent=4)
    else:
      parsed = json.dumps(value, sort_keys=True, indent=4)
    print parsed
    break
  except ValueError:
    print "Oops!"
