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
    
    filename = key.replace('/', '')
    with open(filename + '.json', 'w') as f:
     json.dump(json.loads(parsed), f, indent=4, sort_keys=True)

    break 
  except ValueError:
    print "Oops!"
