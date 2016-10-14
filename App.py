import sys
import csv
import Stemmer
import operator

""" 
Este script permite leer un archivo de texto y
limpiarlo permitiendo su posterior uso para la
herramienta Weka.
"""

#Abrimos el archivo.
doc_file = open('In/Datos_Proyecto.txt', 'r', encoding='utf-8')

#Volcamos su contenido en una variable.
file_content = doc_file.read()

#Ponemos la totalidad del contenido en minusculas.
file_content = file_content.lower()
file_content = file_content[3:]
file_content = file_content.replace('`', '\'')
file_content = file_content.replace(', \n\n', '\n', 1)
file_content = file_content.replace(', \n', ',')
file_content = file_content.replace('\n\n\n', '\n')
file_content = file_content.replace('\n\n', '\n')
file_content = file_content.replace('.\'\n\'', '.\',\'')
file_content = file_content.replace('.\',\n\'', '.\',\'')
file_content = file_content.replace('\',\n\'trabajo', '\',\'trabajo')
file_content = file_content.replace('\'trabajo especial de grado (tecnologia educativa)\',', '\'trabajo especial de grado (tecnologia educativa)\'')
file_content = file_content.replace('\'trabajo especial de grado (aplicaciones internet)\',', '\'trabajo especial de grado (aplicaciones internet)\'')
file_content = file_content.replace('\'trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)\',', '\'trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)\'')
file_content = file_content.replace('\'trabajo especial de grado (ingenieria de software)\',', '\'trabajo especial de grado (ingenieria de software)\'')
file_content = file_content.replace('\'trabajo especial de grado (base de datos)\',', '\'trabajo especial de grado (base de datos)\'')
file_content = file_content.replace('\'trabajo especial de grado (sistemas distribuidos y paralelos)\',', '\'trabajo especial de grado (sistemas distribuidos y paralelos)\'')
file_content = file_content.replace('\'trabajo especial de grado (inteligencia artificial)\',', '\'trabajo especial de grado (inteligencia artificial)\'')
file_content = file_content.replace('\'trabajo especial de grado (sistemas de informacion)\',', '\'trabajo especial de grado (sistemas de informacion)\'')
file_content = file_content.replace('\'trabajo especial de grado (computacion grafica)\',', '\'trabajo especial de grado (computacion grafica)\'')
file_content = file_content.replace('\',\n\'', '\',\'')
file_content = file_content.replace('\'\n\n\'', '\'\n\'')
file_content = file_content.replace('\', \'', '\',\'')
file_content = file_content.replace('\n\'trabajo especial de grado (tecnologia educativa)\'', '\'trabajo especial de grado (tecnologia educativa)\'')
file_content = file_content.replace('\n\'trabajo especial de grado (aplicaciones internet)\'', '\'trabajo especial de grado (aplicaciones internet)\'')
file_content = file_content.replace('\n\'trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)\'', '\'trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)\'')
file_content = file_content.replace('\n\'trabajo especial de grado (ingenieria de software)\'', '\'trabajo especial de grado (ingenieria de software)\'')
file_content = file_content.replace('\n\'trabajo especial de grado (base de datos)\'', '\'trabajo especial de grado (base de datos)\'')
file_content = file_content.replace('\n\'trabajo especial de grado (sistemas distribuidos y paralelos)\'', '\'trabajo especial de grado (sistemas distribuidos y paralelos)\'')
file_content = file_content.replace('\n\'trabajo especial de grado (inteligencia artificial)\'', '\'trabajo especial de grado (inteligencia artificial)\'')
file_content = file_content.replace('\n\'trabajo especial de grado (sistemas de informacion)\'', '\'trabajo especial de grado (sistemas de informacion)\'')
file_content = file_content.replace('\n\'trabajo especial de grado (computacion grafica)\'', '\'trabajo especial de grado (computacion grafica)\'')
file_content = file_content.replace('\',\n \'', '\',\'')
file_content = file_content.replace('\',  \n\'', '\',\'')
file_content = file_content.replace('. \'trabajo especial de grado (tecnologia educativa)\'', '\',\'trabajo especial de grado (tecnologia educativa)\'')
file_content = file_content.replace('. \'trabajo especial de grado (aplicaciones internet)\'', '\',\'trabajo especial de grado (aplicaciones internet)\'')
file_content = file_content.replace('. \'trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)\'', '\'trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)\'')
file_content = file_content.replace('. \'trabajo especial de grado (ingenieria de software)\'', '\',\'trabajo especial de grado (ingenieria de software)\'')
file_content = file_content.replace('. \'trabajo especial de grado (base de datos)\'', '\',\'trabajo especial de grado (base de datos)\'')
file_content = file_content.replace('. \'trabajo especial de grado (sistemas distribuidos y paralelos)\'', '\',\'trabajo especial de grado (sistemas distribuidos y paralelos)\'')
file_content = file_content.replace('. \'trabajo especial de grado (inteligencia artificial)\'', '\',\'trabajo especial de grado (inteligencia artificial)\'')
file_content = file_content.replace('. \'trabajo especial de grado (sistemas de informacion)\'', '\',\'trabajo especial de grado (sistemas de informacion)\'')
file_content = file_content.replace('. \'trabajo especial de grado (computacion grafica)\'', '\',\'trabajo especial de grado (computacion grafica)\'')
file_content = file_content.replace('. \n\'', '.\',\'')
file_content = file_content.replace('\'\'trabajo especial de grado (tecnologia educativa)\'', '\',\'trabajo especial de grado (tecnologia educativa)\'')
file_content = file_content.replace('\'\'trabajo especial de grado (aplicaciones internet)\'', '\',\'trabajo especial de grado (aplicaciones internet)\'')
file_content = file_content.replace('\'\'trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)\'', '\'trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)\'')
file_content = file_content.replace('\'\'trabajo especial de grado (ingenieria de software)\'', '\',\'trabajo especial de grado (ingenieria de software)\'')
file_content = file_content.replace('\'\'trabajo especial de grado (base de datos)\'', '\',\'trabajo especial de grado (base de datos)\'')
file_content = file_content.replace('\'\'trabajo especial de grado (sistemas distribuidos y paralelos)\'', '\',\'trabajo especial de grado (sistemas distribuidos y paralelos)\'')
file_content = file_content.replace('\'\'trabajo especial de grado (inteligencia artificial)\'', '\',\'trabajo especial de grado (inteligencia artificial)\'')
file_content = file_content.replace('\'\'trabajo especial de grado (sistemas de informacion)\'', '\',\'trabajo especial de grado (sistemas de informacion)\'')
file_content = file_content.replace('\'\'trabajo especial de grado (computacion grafica)\'', '\',\'trabajo especial de grado (computacion grafica)\'')
file_content = file_content.replace('. \n','. ')
file_content = file_content.replace(' \n','\n')
file_content = file_content.replace('\"', '$COMILLAS$')
file_content = file_content.replace('\'', '"')
file_content = file_content.replace('$COMILLAS$', '\'')

# Filtramos los datos pre prosesados para centrarnos en los datos utiles.
data_formated = []
palabras_clave_moda = {'aplicaciones internet':{}, 'tecnologias en comunicaciones y redes de computadoras':{}, 'base de datos':{}, 'inteligencia artificial':{}, 'sistemas de informacion':{}}
file_content = file_content.split('\n')
registros_procesados = 0;
registros_descartados = 0;
for line_content in file_content:
	line = line_content.split('","')
	ignorar = False
	if len(line) >= 3:
		titulo = line[0].replace('"', '')
		descripcion = line[1].replace('"', '')
		palabras_clave = ""
		mencion = ""
		if len(line) == 3:
			mencion = line[2].replace('"', '')
			if "trabajo especial de grado (aplicaciones internet)" in mencion:
				mencion = "aplicaciones internet"
			elif "trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)" in mencion:
				mencion = "tecnologias en comunicaciones y redes de computadoras"
			elif "trabajo especial de grado (base de datos)" in mencion:
				mencion = "base de datos"
			elif "trabajo especial de grado (inteligencia artificial)" in mencion:
				mencion = "inteligencia artificial"
			elif "trabajo especial de grado (sistemas de informacion)" in mencion:
				mencion = "sistemas de informacion"
			else:
				ignorar = True
		elif len(line) == 4:
			palabras_clave = line[2].replace('"', '')
			mencion = line[3].replace('"', '')
			if "trabajo especial de grado (aplicaciones internet)" in mencion:
				mencion = "aplicaciones internet"
			elif "trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)" in mencion:
				mencion = "tecnologias en comunicaciones y redes de computadoras"
			elif "trabajo especial de grado (base de datos)" in mencion:
				mencion = "base de datos"
			elif "trabajo especial de grado (inteligencia artificial)" in mencion:
				mencion = "inteligencia artificial"
			elif "trabajo especial de grado (sistemas de informacion)" in mencion:
				mencion = "sistemas de informacion"
			else:
				ignorar = True
		else:
			palabras_clave = line[2].replace('"', '')
			for section in line[3:]:
				if "trabajo especial de grado (aplicaciones internet)" in section:
					mencion = "aplicaciones internet"
				elif "trabajo especial de grado (tecnologias en comunicaciones y redes de computadoras)" in section:
					mencion = "tecnologias en comunicaciones y redes de computadoras"
				elif "trabajo especial de grado (base de datos)" in section:
					mencion = "base de datos"
				elif "trabajo especial de grado (inteligencia artificial)" in section:
					mencion = "inteligencia artificial"
				elif "trabajo especial de grado (sistemas de informacion)" in section:
					mencion = "sistemas de informacion"
				else:
					ignorar = True
		if not ignorar:
			registros_procesados += 1
			for palabra in palabras_clave.split(', '):
				if palabra in palabras_clave_moda[mencion]:
					palabras_clave_moda[mencion][palabra] += 1
				else:
					palabras_clave_moda[mencion][palabra] = 1
			if palabras_clave == '':
				sorted_moda = sorted(palabras_clave_moda[mencion].items(), key=operator.itemgetter(1))
				palabras_clave = [x[0] for x in sorted_moda][0:5]
				palabras_clave_generado = ''
				for palabra in palabras_clave:
					palabra = palabra.replace(',', '')
					palabra = palabra.replace('.', '')
					palabras_clave_generado += palabra + ', '
				palabras_clave = palabras_clave_generado
			data_formated.append([titulo, descripcion, palabras_clave, mencion])
		else:
			registros_descartados += 1
print('Registros procesados: ', registros_procesados, '\nRegistros ignorados: ', registros_descartados)
csv_file = open('Out/Datos_Proyecto.csv', 'w', encoding='utf-8')
csv_file = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
for row in data_formated:
	csv_file.writerow(row)

# Reducimos las palabras a su minima exprecion para su posterior prosesamiento.
csv_file_stemmer = open('Out/Datos_Proyecto_Stemmer.csv', 'w', encoding='utf-8')
csv_file_stemmer = csv.writer(csv_file_stemmer, quoting=csv.QUOTE_ALL)
stemmer = Stemmer.Stemmer('spanish')
for row in data_formated:
	titulo_in = row[0]
	titulo_in = titulo_in.replace(',', '')
	titulo_in = titulo_in.replace('.', '')
	titulo_in = titulo_in.replace('-', '')
	titulo_in = titulo_in.replace('(', '')
	titulo_in = titulo_in.replace(')', '')
	titulo_in = titulo_in.replace('[', '')
	titulo_in = titulo_in.replace(']', '')
	titulo_out = stemmer.stemWords(titulo_in.split(' '))
	resumen_in = row[1]
	resumen_in = resumen_in.replace(',', '')
	resumen_in = resumen_in.replace('.', '')
	resumen_in = resumen_in.replace('-', '')
	resumen_in = resumen_in.replace('(', '')
	resumen_in = resumen_in.replace(')', '')
	resumen_in = resumen_in.replace('[', '')
	resumen_in = resumen_in.replace(']', '')
	resumen_out = stemmer.stemWords(resumen_in.split(' '))
	key_words_in = row[2]
	key_words_in = key_words_in.replace(',', '')
	key_words_in = key_words_in.replace('.', '')
	key_words_in = key_words_in.replace('-', '')
	key_words_in = key_words_in.replace('(', '')
	key_words_in = key_words_in.replace(')', '')
	key_words_in = key_words_in.replace('[', '')
	key_words_in = key_words_in.replace(']', '')
	key_words_out = stemmer.stemWords(key_words_in.split(' '))
	csv_file_stemmer.writerow([' '.join(titulo_out), ' '.join(resumen_out), ' '.join(key_words_out), row[3]])
