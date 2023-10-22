from collections import deque

food_portions = deque([int(num) for num in input().split(", ")])
stamina = deque([int(num) for num in input().split(", ")])
peaks_info = deque([["Vihren", 80], ["Kutelo", 90], ["Banski Suhodol", 100], ["Polezhan", 60], ["Kamenitza", 70]])
conquered_peaks = []

for _ in range(7):
    daily_food_portion = food_portions.pop()
    daily_stamina = stamina.popleft()
    daily_sum = daily_food_portion + daily_stamina

    if daily_sum >= peaks_info[0][1]:
        conquered_peaks.append(peaks_info[0][0])
        peaks_info.popleft()

        if len(peaks_info) == 0:
            print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
            break
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep="\n")
  
