class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInfo(self):
        print(self.nom, self.prenom, self.numeroPermis)

        if self.voitureService:
            print("Voiture:", self.voitureService.marque, self.voitureService.matricule)
        else:
            print("Pas de voiture de service")

    def affecterVoiture(self, voiture):
        if self.voitureService :
            print("Cet employé a déjà une voiture")
        elif voiture.chauffeur:
            print("Cette voiture est déjà attribuée")
        else:
            self.voitureService = voiture
            voiture.chauffeur = self

    def retirerVoiture(self):
        if self.voitureService:
            self.voitureService.chauffeur = None
            self.voitureService = None


class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInfor(self):
        print(self.marque, self.matricule, self.annee)

        if self.chauffeur:
            print("Chauffeur:", self.chauffeur.nom, self.chauffeur.prenom)
        else:
            print("Aucun chauffeur")


v1 = Voiture("ABC123", 2025, "DODGE", 50000)
v2 = Voiture("23452015", 2022, "DACIA", 20000)

e1 = Employe("P12345", "RAMZI", "SAADI")
e2 = Employe("P67890", "BASSEM", "SAADI")

e1.afficherInfo()
e2.afficherInfo()

v1.afficherInfor()
v2.afficherInfor()

e1.affecterVoiture(v1)
e2.affecterVoiture(v2)
e1.afficherInfo()
e2.afficherInfo()

e1.retirerVoiture()
e1.afficherInfo()

e2.affecterVoiture(v1)
