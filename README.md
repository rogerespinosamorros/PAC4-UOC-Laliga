# Programació per a la ciència de dades - PAC4

Autor: Roger Espinosa.

## Descripció

El projecte es tracta de la PAC4 de l'assignatura Programació per a la Ciència de Dades.

Hem realitzat 7 exercicis a partir d'un Dataset de Kaggle, fent un anàlisis de dades de La Liga, buscant modularitzar el projecte com a prioritat. També documentant, fent tests i controlant la qualitat del codi utilitzat.

## Estructura del projecte

```text
PAC4
├─ data
│   └─ LaLiga_Matches.csv
├─ doc
├─ img
├─ screenshots
├─ src
│   ├─ config.py
│   ├─ main.py
│   └─ exercises
│       ├─ __init__.py
│       ├─ exercise1.py
│       ├─ exercise2.py
│       ├─ exercise3.py
│       ├─ exercise4.py
│       ├─ exercise5.py
│       ├─ exercise6.py
│       └─ exercise7.py 
├─ tests
│   └─ tests_ex6.py 
├─ LICENSE
├─ README.md
└─ requirements.txt
```

## Instal·lació

Creem un entorn virtual:

```bash
python -m venv .venv
```

Activem l'entorn:

```bash
source .venv/Scripts/activate
```

Instal·lem dependències, que es troben a `requirements.txt`:

```bash
pip install -r requirements.txt
``` 

## Execució

Si volem executar tots els exercicis a la vegada:

```bash
python src/main.py
```

Podem executar els exercicis de forma incremental:

 ```bash
python src/main.py --ex 1
python src/main.py --ex 2
python src/main.py --ex 3
python src/main.py --ex 4
python src/main.py --ex 5
python src/main.py --ex 6
python src/main.py --ex 7
```

Podem veure el mode ajuda amb:

```bash
python src/main.py --help
```

## Anàlisi estàtic (linting)

Per comprovar la qualitat del codi hem utilitzat Pylint.
Per executar l'anàlisi estàtica:

```bash
pylint src/main.py
```

## Generació de la documentació

La documentació del projecte l'hem generat amb pydoc, utilitzant les comandes següents:

```bash
python -m pydoc -w src.exercises.exercise1
python -m pydoc -w src.exercises.exercise2
python -m pydoc -w src.exercises.exercise3
python -m pydoc -w src.exercises.exercise4
python -m pydoc -w src.exercises.exercise5
python -m pydoc -w src.exercises.exercise6
python -m pydoc -w src.exercises.exercise7
```

S'han generat uns fitxers HTML que s'han guardat directament a la carpeta `doc/`.

## Execució del test

Hem verificat el funcionament de la funció `fun_total_goals` de l'exercici 6 realitzant un test unitari amb `unittest`.

```bash
python tests/tests_ex6.py
```

## Comandes Git

Per inicialitzar el repositori:

```bash
git init
```

Per afegir fitxers:

```bash
git add .
```

Volem crear un commit:

```bash
git commit -m "missatge"
```

Realitzar canvis a GitHub:

```bash
git push origin main
```

## Llicència

Aquesta PAC/projecte es distribueix sota la llicència MIT.


## Fonts consultades

A continuació es poden veure els llocs webs consultats per a la realització de la PAC, sense comptar el notebook de la unitat 6.

- Simbologia de l'arbre de l'estructura per arxius md. : https://gist.github.com/GeorgeHernandez/10dcbb5fd6ca8b087d169d5a44d72cd2

- Llicència MIT trobada a: https://mit-license.org/

- Informació sobre argparse: https://docs.python.org/3/library/argparse.html

- Consulta sobre sys: https://www.w3schools.com/python/ref_module_sys.asp

- Informació sobre funció __init__.py : https://www.w3schools.com/python/python_class_init.asp

- Informació sobre arxiu __init__.py : https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/

- Informació sobre pylint: https://pylint.pycqa.org/en/latest/index.html

- Informació sobre pydoc: https://pythonology.eu/how-to-use-pydoc-to-generate-documentation-in-python/

- Informació sobre modularitat en python: https://coderivers.org/blog/modular-python/ , https://pythones.net/modularidad-en-python-oop/

- Informació sobre main.py: https://www.hrekov.com/blog/the-main-py-file

- Informació sobre un arxiu README.md : https://codingnomads.com/python-101-documentation-readme#why-have-a-good-readme

- Informació sobre l'arxiu requirements.txt : https://coderivers.org/blog/requirementstxt-python/

- Informació sobre configuracions i arxiu config.py : https://coderivers.org/blog/config-file-python/ , https://docs.python.org/3/library/configparser.html (no utilitzat finalment el configparser)

- Altres llocs webs consultats, per dubtes generals d'estructura, modalitat, codi, etc: https://docs.python-guide.org/writing/structure/ , https://dsj7419.github.io/python-learning-by-projects/05-modular-programming/ , https://networkx.org/documentation/stable/ , https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html , https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html , https://www.geeksforgeeks.org/python/matplotlib-pyplot-text-function-in-python/ .