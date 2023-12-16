import random

class NPC:
    def __init__(self, nom, race, espèce, profession):
        self.nom = nom
        self.race = race
        self.espèce = espèce
        self.profession = profession
        self.force = self.roll_dice()
        self.agilité = self.roll_dice()
        self.constitution = self.roll_dice()
        self.intelligence = self.roll_dice()
        self.sagesse = self.roll_dice()
        self.charisme = self.roll_dice()
        self.classe_armure = random.randint(1, 12)
        self.point_de_vie = random.randint(1, 20)

    def roll_dice(self):
        return sum(sorted([random.randint(1, 6) for _ in range(4)])[1:])

    def afficher_caracteristiques(self):
        print(f"Nom: {self.nom}")
        print(f"Race: {self.race}")
        print(f"Espèce: {self.espèce}")
        print(f"Profession: {self.profession}")
        print(f"Force: {self.force}")
        print(f"Agilité: {self.agilité}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Sagesse: {self.sagesse}")
        print(f"Charisme: {self.charisme}")
        print(f"Classe d'armure: {self.classe_armure}")
        print(f"Point de vie: {self.point_de_vie}")

class Kobold(NPC):
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} !")

    def subir_dommage(self, dommage):
        print(f"{self.nom} subit {dommage} points de dommage !")

class Héros(NPC):
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} !")
        roll = random.randint(1, 20)
        if roll == 20:
            print(f"Coup critique ! {cible.nom} subit {random.randint(1, 8)} points de dommage !")
        elif roll == 1:
            print(f"Attaque ratée !")
        elif roll >= cible.classe_armure:
            print(f"{cible.nom} est touché ! {cible.nom} subit {random.randint(1, 6)} points de dommage !")
        else:
            print(f"{cible.nom} esquive l'attaque !")

    def subir_dommage(self, dommage):
        print(f"{self.nom} subit {dommage} points de dommage !")