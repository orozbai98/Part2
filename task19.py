ves_in_earth = int(input("vash ves: "))
ves_in_moon = ves_in_earth*0.165
kol_let_moon = int(input("skolko let vy na lune: "))
if kol_let_moon <= 1:
    print(ves_in_moon)
else:
    print(ves_in_moon+kol_let_moon)