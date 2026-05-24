print("Hello, I am an AI robot. What is your name?")
name= input()
print(f"Nice to meet you, {name}. How are you feeling today?")
print("1. Happy")
print("2. Sad")

feeling=input().lower()
if feeling=="happy":
    print("Thats great to hear! Keep smiling!")
elif feeling=="sad":
    print("I'm sorry to hear that.")
else:
    print("I see its hared to put feelings into words. I hope you feel better soon!")

print(f"It was nice meeting you, {name}. Take care!")