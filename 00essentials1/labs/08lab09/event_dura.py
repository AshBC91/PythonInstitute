hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

dura_hours = (mins + dura) / 60
final_hour = (dura_hours + hour) % 24
final_mins = (mins + dura) % 60

print(str(int(final_hour)) + ":" + str(final_mins))

