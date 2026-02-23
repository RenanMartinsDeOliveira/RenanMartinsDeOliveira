#programa básico para dizer o tipo primitivo do que foi digitado e todas as informações possiveís sobre ele.

q = input('digite algo: ')
t = type(q)


print('este caractér é do tipo {}'.format(t))
print('{} é númerico?'.format(q),q.isalnum())
print('{} é formado somente por espaços?'.format(q),q.isspace())
print('{} é alfabético?'.format(q),q.isalpha())
print('{} é alfanúmerico?'.format(q),q.isalnum())
print('{} é decimal?'.format(q),q.isdecimal())
print('{} é somente formado por letras maiusculas?'.format(q),q.isupper())
print('{} é somente formado por letras minusculas?'.format(q),q.islower())
print('{} está capitalizado?'.format(q),q.istitle())
print('{} é ascii?'.format(q),q.isascii())
print('{} é de 0 a 9?'.format(q),q.isdigit())
print('{} é um identificador válido?'.format(q),q.isidentifier())
print('{} contém apenas caractérs imprimiveis?',q.isprintable())
