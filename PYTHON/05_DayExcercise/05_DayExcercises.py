#05_DayExcercise1

list()


escuela = list('Cuaderno,''lapiz,''pluma,''goma,,''zacapuntas')


length_of_list = len(escuela)
print("Length of the list:", length_of_list)


first_item = escuela[0]

middle_item = escuela[len(escuela) // 2]

last_item = escuela[-1]

print("Primer escuela:", first_item)
print("escuela del medio:", middle_item)
print("Última escuela:", last_item)


mixed_data_types = ('Gael','20','1.71','soltero','lo mas caro de mexico')
print(mixed_data_types)


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Telcel', 'Uber', 'Amazon']
print("Compañías de IT:", it_companies)


list = (it_companies)
print(list)


print("Número de compañías de IT:", len(it_companies))


first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

print("Primera compañía:", first_company)
print("Compañía del medio:", middle_company)
print("Última compañía:", last_company)


it_companies[3] = 'Samsung'
print("Compañías de IT modificadas:", it_companies)


it_companies.insert(len(it_companies) // 2, 'Tesla')
print("Compañías después de insertar Tesla:", it_companies)


it_companies = [company.upper() if company != 'IBM' else company for company in it_companies]
print("Compañías con Apple en mayúsculas:", it_companies)
  

it_companies_str = ' #; '.join(it_companies)
print("Compañías unidas con '#;':", it_companies_str)


exists = 'Google' in it_companies
print("¿Google existe en la lista?", exists)


exists = 'Spotify' in it_companies
print("¿Spotify existe en la lista?", exists)


it_companies.sort()
print("Compañías ordenadas:", it_companies)


it_companies.sort(reverse=True)
print("Compañías en orden descendente:", it_companies)


it_companies.reverse()
print("Compañías en orden invertido:", it_companies)


last_three = it_companies [3:]
print("Últimas 3 compañías:", last_three)


first_three = it_companies [3:]
print('Las primeras 3 compañias:', first_three)


first = it_companies [1:]
print('La primera compañia:', first)


the_last = it_companies [1:]
print('La ultima compañia', the_last)


All_companys = it_companies [8:]
print('Todas las compañias', All_companys)


it_companies.clear()
print("Lista de compañías vacía:", it_companies)


escuela = list('Cuaderno,''lapiz,''pluma,''goma,,''zacapuntas')
casa = list('sala,''mesa,''cogin,''tele,''puerta')

escuela_and_casa = escuela + casa

print('escuela y casa unidas',escuela_and_casa )

escuela.extend(casa)
print('escuela y casa despues de usar extend():', escuela)
