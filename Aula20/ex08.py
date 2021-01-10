def area(largura, comprimento):
    tot = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {tot:.1f}m².')

print()
print('  CONTROLE DE TERRENO')
print(25*'-')
area(largura=float(input('LARGURA (m): ')), comprimento=float(input('COMPRIMENTO (m): ')))