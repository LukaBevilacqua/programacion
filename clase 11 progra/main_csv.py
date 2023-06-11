import csv

lista_personajes = []

with open("personas.csv", "r") as file:
    persona = {}
    for linea in file:
        print(linea.split(","))