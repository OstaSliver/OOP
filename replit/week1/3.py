h_in, min_in, h_out, min_out = map(int, input().split())

time_in = h_in * 60 + min_in
time_out = h_out * 60 + min_out

calulate_time = time_out - time_in


if calulate_time <= 15:
    cost = 0
elif 15 < calulate_time <= 180: 
    cost = (calulate_time // 60) * 10
elif 240 < calulate_time <= 360:  # 6 ชั่วโมง
    cost = 4 * 10 + ((calulate_time - 240) // 60) * 20
else: 
    cost = 200

print(cost)
