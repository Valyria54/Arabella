def schoener(s):
    return input("> " + s + "\n* ")

# Bot spricht mit Mensch
mensch = schoener("Hallo")

if "hallo" in mensch or "hi" in mensch:
    mensch = schoener("Wie geht es dir?")
else:
    mensch = schoener("Was willst du mir sagen?")

if "gut" in mensch:
    mensch = schoener("Super!")
elif "schlecht" in mensch or "nicht gut" in mensch:
                      mensch = schoener("Oh, was ist passiert?")

if "was" in mensch or "nichts" in mensch:
    mensch = schoener ("Du kannst mir deine Probleme erzählen, wenn welche hast.")
elif "krank" in mensch or "nicht gut" in mensch:
    mensch = schoener ("Oh, ich wünsche dir gute Besserung!")
    
else:
    mensch = schoener("Ich verstehe dich nicht.")

print ("Auf Wiedersehen! Bis zum nächsten Mal!")
