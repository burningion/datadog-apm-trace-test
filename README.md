# Datadog APM Trace Test

This is just a quick test repo to see how long of traces Datadog's APM infrastructure can handle. I ran it for 6.5 hours, and still had traces. 

You're welcome to add a language to test with a PR.

## How it works

Rather than using threads, `runsleepy.py` runs a bunch of instances of a Ruby and Python script via the command line. It assumes you have the Datadog Agent running locally, with APM enabled. If you're running from within a container instead, check each file for the line to uncomment.

The script itself uses Python's `subprocess.Popen` function, spinning up a child program for each duration in a new process without waiting.

Running it looks like this:

```bash
$ python3 runsleepy.py
Opening subprocess for 6000 seconds
Opening subprocess for 6300 seconds
Opening subprocess for 6600 seconds
Opening subprocess for 6900 seconds
Opening subprocess for 7200 seconds
Opening subprocess for 7500 seconds
....
$ ps aux
PID   USER     TIME  COMMAND
 3412 root      0:00 python3 sleepy.py 10200
 3413 root      0:00 python3 sleepy.py 10500
 3414 root      0:00 python3 sleepy.py 10800
 3415 root      0:00 python3 sleepy.py 11100
 3416 root      0:00 python3 sleepy.py 11400
 3417 root      0:00 python3 sleepy.py 11700
 3418 root      0:00 python3 sleepy.py 12000
...
```

You'll see the traces start showing up later. If for any reason you want to stop everything, assuming you're not running other Python/Ruby processes...:

```bash
$ killall -9 python3
$ killall -9 ruby
```
