

#to assign job for each day
days=[]
for i in range(len(data)):
    dayy=day(jobs[i].job_due_date,jobs[i].job_name)
    days.append(dayy)

print(days[0].day_name,days[0].job)