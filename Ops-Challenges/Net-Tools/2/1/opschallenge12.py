#! Python3

import psutil

times = psutil.cpu_times()

print("----------system info--------")
print(f" [~] user time: {times.user}")
print(f" [~] system time: {times.system}")
print(f" [~] interrupt time: {times.interrupt}")
print(f" [~] idle time: {times.idle}")
print("----------end system info--------")
