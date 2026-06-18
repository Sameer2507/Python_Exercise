def convertMillis(millis):
    seconds = millis // 1000
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours}:{minutes}:{seconds}"

millis = int(input("Enter milliseconds: "))
print(convertMillis(millis))