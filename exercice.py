#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input('Add value:'))
        
    values.sort()
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        while len(words) < 2:
            words.append(str(input('Add word:')))
    


    return (sorted(words[0]) == sorted(words[1]))


def contains_doubles(items: list) -> bool:
    if len(items) == len(set(items)):
        return False
    return True


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    for k, v in student_grades.items():
        student_grades[k] = sum(v) / len(v)
    best_student = max(student_grades.items(), key = lambda x: x[1])

    return {best_student[0]: best_student[1]}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    sentence_dict = {}

    for i in sentence:
        sentence_dict[i] = sentence.count(i)
    

    return sentence_dict


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses  et enregistrer dans une structure de données
    recettes_list = []

    while True:
        recette_dict = {'Nom': None, 'Ingrédients': None}
        nom = str(input('Entrez le nom de la recette: '))

        if not len(nom):
            break

        recette_dict['Nom'] = nom
        ingrédients = []

        while True:
            ingrédient = str(input('Entrez le nom d\'un ingrédient: '))

            if not len(ingrédient):
                break

            ingrédients.append(ingrédient)

        recette_dict['Ingrédients'] = ingrédients
        recettes_list.append(recette_dict)
    
    return recettes_list


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = str(input('Entrez le nom d\'une recette: '))

    for i in ingredients:
        if i['Nom'] == nom:
            return i['Ingrédients']

    return None


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
