import matplotlib.pyplot as plt

pairs_cases = [
    ("Diego", "Dora"),
    ("Maya", "Miguel"),
    ("El Chavo Animado", "Quico"),
    ("Pato", "Pocoyo"),
    ("Mortadelo", "Filemon"),
    ("Tokio", "Rio"),
    ("Zorro", "Bernardo"),
    ("Don Quijote", "Sancho Panza"),
    ("Zipi", "Zape"),
    ("Fidel Castro", "Che Guevara"),
    ("Isabel I of Castile", "Ferdinand II of Aragon"),
    ("Frida Kahlo", "Diego Rivera"),
    ("Messi", "Di Maria"),
    ("Penelope Cruz", "Javier Bardem"),
    ("Chino", "Nacho")
]

pairs = [
    ("diego", "dora"),
    ("maya", "miguel"),
    ("el chavo", "quico"),
    ("pato", "pocoyo"),
    ("mortadelo", "filemon"),
    ("tokio", "rio"),
    ("zorro", "bernardo"),
    ("don quijote", "sancho panza"),
    ("zipi", "zape"),
    ("fidel castro", "che guevara"),
    ("isabel i de castilla", "fernando ii de aragon"),
    ("frida kahlo", "diego rivera"),
    ("lionel messi", "angel di maria"),
    ("penelope cruz", "javier bardem"),
    ("chino", "nacho")
]

pairs_first_names = [
    ("diego", "dora"),
    ("maya", "miguel"),
    ("el", "quico"),
    ("pato", "pocoyo"),
    ("mortadelo", "filemon"),
    ("tokio", "rio"),
    ("zorro", "bernardo"),
    ("don", "sancho"),
    ("zipi", "zape"),
    ("fidel", "che"),
    ("isabel", "fernando"),
    ("frida", "diego"),
    ("lionel", "angel"),
    # ("penelope", "javier"),
    ("chino", "nacho")
]

def show_img(orig_name):
    name = orig_name.split()[0] # search by first only
    path = "imgs/" + name + ".jpg"
    try:
        img = plt.imread(path)
        plt.imshow(img)
        plt.axis("off")
        plt.title(orig_name)
        plt.show()
    except FileNotFoundError:
        print("file " + path + " doesn't exist")

while True:
    guess = input("Adivina un par (separados por una coma):\n")

    if ',' not in guess:
        print("Olvidaste la COMA, inténtalo de nuevo ;)")
        continue

    person1, person2 = guess.split(sep=',')
    person1 = person1.strip()
    person2 = person2.strip()

    p1_ready = person1.lower()
    p2_ready = person2.lower()

    if p2_ready == "img":
        show_img(p1_ready)
    else:
        if (p1_ready, p2_ready) in pairs or (p1_ready, p2_ready) in pairs_first_names or (p2_ready, p1_ready) in pairs or (p2_ready, p1_ready) in pairs_first_names:
            print(f"Sí, {person1} y {person2} son una parecha!")
        else:
            print(f"No, {person1} y {person2} no son una parecha:(")