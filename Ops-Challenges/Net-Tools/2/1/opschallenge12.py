#! Python3

import psutil

times = psutil.cpu_times()

print("----------system info--------")
print(f" [~] user time: {times.user}")
print(f" [~] user time: {times.system}")
print(f" [~] user time: {times.interrupt}")
print(f" [~] user time: {times.idle}")
print(f" [~] user time: {times.}")
print("----------end system info--------")
