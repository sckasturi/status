#status
Status is a simple python based applet that allows for any sysadmin to see the status of their server. It shows some information including load average, uptime, users logged in, and memory available.

How to run
----------
```
$ git clone https://github.com/sckasturi/status  
$ cd status
$ pip install -r requirements.txt --user
$ ./run.py # note, it is advised to run in screen/tmux
```


API
---
There is a simple JSON API. All commands are accessed through GET requests. 

###`/api`
This will return a list of every value that the script is aware of. Fairly simple to use.

####Example:

`GET http://localhost/api`

```
{
  "hostname": "rio",
  "loadaverage": {
    "15m": "0.06",
    "1m": "0.18",
    "5m": "0.06"
  },
  "memory": {
    "available": "187.9 MB",
    "percent": "68.2",
    "total": "591.5 MB"
  },
  "uptime": {
    "day": "44",
    "hour": "8",
    "min": "19"
  },
  "users": [
    "skasturi"
  ]
}
```

###`/api/<value>`
If you replace `value` with what ever you wish to look up (i.e. `hostname`, `uptime`, etc.) you can get the specific value without any of the other values.

####Example:

`GET http://localhost/api/memory`

```
{
  "memory": {
    "available": "187.9 MB",
    "percent": "68.2",
    "total": "591.5 MB"
  }
}
```
