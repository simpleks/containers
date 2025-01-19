# script.py
print("🎉 Witaj w kontenerze!")
with open("data.txt", "r") as f:
    print(f"Zawartość pliku data.txt: {f.read()}")
