from random import randint

# # the size of a tile, in pxels
# W, H = 5, 5

# # the game size, in tiles
# X, Y = 100, 100

#nbr de salles et leur taille
nbrdesalles = randint(1, 5)
tailles = []
for j in range (nbrdesalles):
    tailles.append([randint(3,11),randint(3,11)])

# coordonées de chaque salle 
coordonées = []
for j in range (nbrdesalles):
    coordonées.append([randint(1,39),randint(1,39)])
a,b = 0,1
while a < nbrdesalles-1 or b < nbrdesalles :
    if (abs(coordonées[a][0] - coordonées[b][0]) <= tailles[a][0]) or (abs(coordonées[a][1] - coordonées[b][1]) <= tailles[a][1]) :
        coordonées[b] = [randint(1,39),randint(1,39)]
        a = 0
        b = 1
    else:
        b+=1
    if b == nbrdesalles :
        a += 1
        b = a+1


# le joueur
# ligne_player = randint(0,tailles[-1][1] - 2)
# colonne_player = randint(0,tailles[-1][0] - 2)
# player = '@'

#création des salles
# def create_salle_avec_player(largeur,hauteur):
#     salle = '-'*largeur
#     for i in range (hauteur-2) :
#         if i == ligne_player :
#             salle +=  'n|' + '.'*colonne_player + player + '.'*(largeur-3-colonne_player) + '|'
#         else:
#             salle += 'n|' + '.'*(largeur-2) + '|'

    # salle += 'n' + '-'*largeur
    # return salle
        
def create_salle_sans_player(largeur,hauteur):
    salle = '-'*largeur
    for i in range (hauteur-2) :
        salle += 'n|' + '.'*(largeur-2) + '|'

    salle += 'n' + '-'*largeur
    return salle


salles = [ create_salle_sans_player(tailles[i][0],tailles[i][1]) for i in range (nbrdesalles) ] 

# création des portes
def nbr_de_pr(salle):
    res = 0
    for i in range (len(salle)):
        if salle[i] == '+':
            res += 1
    return res

nbr_de_c = randint(nbrdesalles-1, (nbrdesalles)*(nbrdesalles-1)/2)
c_créés = 0
while c_créés < nbr_de_c :
    for j in range (len(salles)) :
        ps_plus = 1
        ps_réelle = randint(1 , 2*(tailles[j][0] + tailles[j][1] - 2) - nbr_de_pr(salles[j]))
        for i in range (len(salles[j])):
            if salles[j][i] == '|' or salles[j][i] == '-':
                ps_plus += 1
                if ps_plus == ps_réelle :
                    salles[j] = salles[j][:i] + '+' + salles[j][i+1 :]
                    c_créés += 0.5


#initialisation de l'espace de jeu
new_salles = [salle.split('n') for salle in salles]
positions=[]
for i in range(len(new_salles)) :
    cp = 0
    for j in range(len(new_salles[i])):
        positions.append((coordonées[i][1]-1)*50 + coordonées[i][0] + 50*cp)
        cp += 1
new_salles_1 = []
for i in range (len(new_salles)):
    new_salles_1 += new_salles[i]

ref = {}
for i in range (len(positions)):
    ref[positions[i]] = new_salles_1[i]
ps_sorted = sorted(ref.keys())

cp_ecr = ps_sorted[0]-1
espace = ' '*(ps_sorted[0]-1)
for j in range(len(ps_sorted)-1):
    espace += ref[ps_sorted[j]] 
    cp_ecr = ps_sorted[j] + len(ref[ps_sorted[j]])
    espace += (ps_sorted[j+1] - cp_ecr -1)*' '
    cp_ecr = ps_sorted[j+1] 
espace += ref[ps_sorted[-1]] + ' '* (2500-ps_sorted[-1]-len(ref[ps_sorted[-1]]))
for n in range (50):
    espace = espace[:(n+1)*50 ] +'\n' + espace[(n+1)*50  :]
# initialize pygame
# need to do it early so screen and clock are defined
# pg.init()
# screen = pg.display.set_mode((X*W, Y*H))
# clock = pg.time.Clock()

print(espace)