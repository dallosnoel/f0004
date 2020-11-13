név =input('Mi a neved? ')
kor =input('Hány éves vagy? ')
év =input('Melyik év-ben vagyunk? ')

év =int(év)
kor = int(kor)
születési_év = év - kor
print(f'{név}, kend {születési_év}-ban született.')
