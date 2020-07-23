time = int(input("Enter a number of seconds: "))

if time < 0:
    exit()

hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time - minutes * 60 - hours * 3600

print("%d second(s) is equivalent to %02d:%02d:%02d." % (time, hours, minutes, seconds))
