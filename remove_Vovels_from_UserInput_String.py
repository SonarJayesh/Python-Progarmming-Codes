text = input("Enter the String: ")
result = ""
for ch in text:
    if ch.lower() not in "aeiou":
        result = result + ch

print("String  without vowels:",result)        