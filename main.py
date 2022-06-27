# importovati modul parsers iz paketa helper koji sadrzi klasu FileParser

from helper.parsers import FileParser, FileParserExtended
import json


def funkcija_1(input_list):
    # omoguciti da funkcija prihvata argument tipa lista i izvrsiti proveru da u slucaju da joj je prosledjen drugi tip,
    # ispise poruku i vrati praznu listu

    # koristeci list comprehension, izvsiti f(x) = x^2 + 1 nad svim elementima prosledjene liste
    # povratna vrednost treba da bude nova lista koju smo dobili

    if (type(input_list) is list): 
        print("Type is a list. The list was passed as an argument.")
        print("Looping Using List Comprehension")
        return [(x**2 + 1) for x in input_list]
    else:
        print("Type is not a list")
        return []


def funkcija_2(input_list, min_value):
    # omoguciti da funkcija prihvata kao argumente listu nad kojoj treba izvrsiti filtriranje sa zadatom donjom 
    # granicnom vrednosti koja je prosledjena kao drugi argument

    # povratna vrednost treba da bude lista elemenata koji odgovaraju zadatom uslovu

    if len(input_list) > 0: 
        print("List is not empty")
        #return list(filter(lambda item: item >= min_value, input_list))
        return [x for x in input_list if x >= min_value]
    else:
        print("List is empty")
        return []


def funkcija_3(input_list):
    # funkcija treba da od prosledjene liste napravi recnik tako sto ce kljuc biti index elementa liste uvecan za 1 
    # i dodatim prefiksom 'INDEX_', a vrednost ostaje nepromenjena kao u listi.
    # primer: input lista=[2, 3, 5], output recnik={'INDEX_1': 2, 'INDEX_2': 3, 'INDEX_3': 5}

    if len(input_list) > 0: 
        print("Input list is not empty")
        indices = []
        items = []
        for index, value in enumerate(input_list):
            indices.append(f"INDEX_{index+1}")
            items.append(value)
        return dict(zip(indices, items))
    else:
        print("Input list is empty")
        return {}


if __name__ == '__main__':

    # istancirati klasu FileParser kojoj prosledjujemo putanju do fajla
    # kao i tip fajla ako nije implementirano automatsko prepoznavanje tipa

    # pozvati metodu koja vraca sve vrednosti iz datoteke kao listu elemenata

    # pozvati funkciju_1 koja izvrsi funkciju f(x) = x^2 + 1 za svaki element
    # prosledjene liste i rezultate sacuvati u novoj listi

    # pozvati funkciju_2 koja vraca novu listu u kojoj su samo elementi veci
    # ili jednaki prosledjenoj vrednosti
    # ispisati rezultat

    # pozvati funkciju_3 kojoj prosledjujemo listu dobijenu izvrsavanjem funkcije_1
    # i dobijeni recnik ispisati i sacuvati u json formatu
    

    file_parser_csv = FileParser("data.csv", "csv")
    list_csv = file_parser_csv.data_to_list()

    file_parser_xlsx = FileParser("data.xlsx", "xlsx")
    list_xlsx = file_parser_xlsx.data_to_list()
    
    print("printing - main")

    list_csv_fun_1 = funkcija_1(list_csv)
    print("result list from the function_1 - csv")
    print(list_csv_fun_1)

    list_xlsx_fun_1 = funkcija_1(list_xlsx)
    print("result list from the function_1 - xlsx")
    print(list_xlsx_fun_1)

    list_csv_fun_2 = funkcija_2(list_csv, 0.3)
    print("result list from the function_2 - csv")
    print(list_csv_fun_2)

    list_xlsx_fun_2 = funkcija_2(list_xlsx, 0.3)
    print("result list from the function_2 - xlsx")
    print(list_xlsx_fun_2)

    dict_csv_fun_3 = funkcija_3(list_csv_fun_1)
    print("result dictionary from the function_3 - csv")
    print(dict_csv_fun_3)
   
    print("json")
    json_dict_csv_fun_3 = json.dumps(dict_csv_fun_3)  # convert into JSON
    print(json_dict_csv_fun_3) # the result is a JSON string

    dict_xlsx_fun_3 = funkcija_3(list_xlsx_fun_1)
    print("result dictionary from the function_3 - xlsx")
    print(dict_xlsx_fun_3)

    print("json")
    json_dict_xlsx_fun_3 = json.dumps(dict_xlsx_fun_3)  # convert into JSON
    print(json_dict_xlsx_fun_3) # the result is a JSON string


    file_parser_ext_csv = FileParserExtended("data.csv", "csv")
    dict_ext_csv = file_parser_ext_csv.data_to_dict()
    
    file_parser_ext_xlsx = FileParserExtended("data.xlsx", "xlsx")
    dict_ext_xlsx = file_parser_ext_xlsx.data_to_dict()
    
    print("printing dictionaries - ext")
    print(dict_ext_csv)
    print(dict_ext_xlsx)

