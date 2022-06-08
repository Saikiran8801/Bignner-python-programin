n=int(input())
reminder=n % 11
result_reminder_0= reminder == 0
result_reminder_1=reminder == 1
if result_reminder_0 or result_reminder_1:
    print("Special Eleven")
else:
    print("Normal Number")
