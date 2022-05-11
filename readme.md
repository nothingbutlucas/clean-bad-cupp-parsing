
# Clean bad parsen spanish dictionary's

I made this little script to clean up a Spanish dictionary, which I got from the [cupp tool](https://github.com/Mebus/cupp).

I hope you find it useful.

## Prerequisites

* Python3
* pip
* [pwntools](https://pypi.org/project/pwntools/)

#### [Python3 and pip installation](https://realpython.com/installing-python/)

#### pwntools installation

```bash
pip install pwntools
```

## Usage

First, clone the repo:
```bash
git clone https://github.com/nothingbutlucas/clean-spanish-dictionary
```
Move the script somewhere in your path:
```bash
cd clean-spanish-dictionary
mv clean_spanish.py /usr/bin/
```
Then use it by passing it 2 arguments
```bash
clean_spanish.py [file to fix] [fixed file]
```

#### Example:

You can find the badly parsed Spanish dictionary, at this url -> ftp.funet.fi/pub/unix/security/passwd/crack/dictionaries/spanish/words.spanish.gz
It is the same as the one downloaded from [cupp](https://github.com/Mebus/cupp)
Since you downloadit, unzip it with gunzip:
```bash
gunzip words.spanish.gz
```
```bash
clean_spanish.py words.spanish words.spanish.fix
```
---


# Limpiar diccionarios en español mal parseados

Hice este pequeño script para limpiar un diccionario en español, que obtuve apartir de la herramienta [cupp](https://github.com/Mebus/cupp).

Ojala te sea útil.

## Prerequisitos

* Python3
* pip
* [pwntools](https://pypi.org/project/pwntools/)

#### [Instalación de Python3 y pip](https://realpython.com/installing-python/)

#### Instalación de pwntools 

```bash
pip install pwntools
```

## Uso

Primero, clona este repositorio:
```bash
git clone https://github.com/nothingbutlucas/clean-spanish-dictionary
```
Move el script a algún lugar de tu PATH:
```bash
cd clean-spanish-dictionary
mv clean_spanish.py /usr/bin/
```
Después ejecutalo pasandole 2 argumentos
```bash
clean_spanish.py [archivo a arreglar] [archivo arreglado]
```

#### Ejemplo:

Podes encontrar el diccionario mal parseado en esta url -> ftp.funet.fi/pub/unix/security/passwd/crack/dictionaries/spanish/words.spanish.gz
Es el mismo que se descarga desde [cupp](https://github.com/Mebus/cupp)
Una vez descargado, descomprimilo con gunzip
```bash
gunzip words.spanish.gz
```
Y luego ejecuta el script
```bash
clean_spanish.py words.spanish words.spanish.fix
```

