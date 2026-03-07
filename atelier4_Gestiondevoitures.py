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