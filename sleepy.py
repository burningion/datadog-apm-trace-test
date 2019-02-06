from ddtrace import tracer
from ddtrace.ext.priority import USER_KEEP
import time

import argparse

parser = argparse.ArgumentParser(description='Trace Duration Generator')
parser.add_argument('timeseconds', type=int, help='Number of seconds to wait for trace')

args = parser.parse_args()
# uncomment below if running in a container
# tracer.configure(hostname='agent')

with tracer.trace("web.request",service="trace-length-test") as span:
    span.context.sampling_priority = USER_KEEP
    time.sleep(args.timeseconds)
    span.set_tag('time', args.timeseconds)

# wait for the trace to flush afterwards
time.sleep(5)
