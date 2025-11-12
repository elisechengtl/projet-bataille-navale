class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        """Crée une grille vide avec les dimensions données."""
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.vide = '∿' 
        self.touche = 'x' 
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)

    def tirer(self, ligne, colonne):
        """Marque un tir sur la grille à la position."""
        if 0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes:
            index = ligne * self.nombre_colonnes + colonne
            self.matrice[index] = self.touche
        else:
            print("Coordonnées invalides")
