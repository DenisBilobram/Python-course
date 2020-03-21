seconds = int(input("Enter a time in seconds: "))
print(f"{(seconds // 3600):02}:{(seconds - ((seconds // 3600) * 3600)) // 60:02}:{seconds - ((seconds // 60) * 60):02}")