def solution(n, customers):
    day_by_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    kiosk_q = [0 for _ in range(n)]
    kiosk = [0 for _ in range(n)]
    current_date, current_time, w = (customers.pop(0)).split()
    current_date = list(map(int, current_date.split('/')))
    chour, cminute, csec = list(map(int, current_time.split(':')))
    current_time = chour*3600 + cminute*60 + csec
    kiosk_q[0] = int(w)*60
    kiosk[0] += 1
    answer = 0
    for customer in customers:
        date, time, work = customer.split()
        date = list(map(int, date.split('/')))
        hour, minute, sec = list(map(int, time.split(':')))
        time = hour*3600 + minute*60 + sec 
        gap = 0
        if date == current_date:
            gap = time - current_time
        else:   # not the same day
            if (date[0] == current_date[0] and date[1] - current_date[1] == 1) or (date[0]-current_date[0] == 1 and date[1] == 1 and current_date[1]== day_by_month[current_date[0]]): # one day gap
                gap = time + (24*3600 - current_time)
            else:   # many day gap
                gap = 1000000000
        current_time = time
        
        print(kiosk_q, gap)

        minKioskIdx = 0
        minKiosk = kiosk_q[minKioskIdx]
        while minKiosk > 0:
            for i in range(n):
                kiosk_q[i] -= gap
                if kiosk_q[i] < minKiosk:
                    minKioskIdx = i
                    minKiosk = kiosk_q[i]
                if kiosk_q[i] < 0:
                    kiosk_q[i] = 0
            gap = minKiosk
        kiosk[minKioskIdx] += 1
        kiosk_q[minKioskIdx] = int(work)*60
        print(kiosk)

    for k in kiosk:
        answer = max(answer, k)
    return answer

n=3
c=["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24"
, "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]
print(solution(n,c))

            
        

