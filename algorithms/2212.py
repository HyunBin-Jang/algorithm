import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

sensors.sort()

length = sensors[-1] - sensors[0]
dif_sensor = []
for i in range(N-1):
    dif_sensor.append(sensors[i+1] - sensors[i])
dif_sensor.sort()
for i in range(K-1):
    if dif_sensor:
        length -= dif_sensor.pop()
print(length)
