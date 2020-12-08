import os
import json
import jsonschema
from jsonschema import validate


def get_schemas(folder):
    """
    ENG
        This function creates a generator with the name of the schemas

        Parameters
        ----------
        folder : str
            name of folder that contains schemas

    RU
        Это функция создает генератор с названием схем

        Аргументы
        ---------
        folder : str
            Название папки в которой хранятся схемы
    """

    folder_name_with_schemas = folder + "/"
    list_of_schemas = os.listdir(folder)

    for schema in list_of_schemas:
        with open(folder_name_with_schemas + schema, 'r') as file:
            schema = json.load(file)
            yield schema


def get_json(folder):
    """
    ENG
        This function creates a generator with the name of the json files 

        Parameters
        ----------
        folder : str
            name of folder that contains json files

    RU
        Это функция создает генератор с названием json файлов

        Аргументы
        ---------
        folder : str
            Название папки в которой хранятся json файлы для обработки
    """

    folder_name_with_json = folder + "/"
    list_of_json = os.listdir(folder)

    for json in list_of_json:
        with open(folder_name_with_json + json, 'r') as file:
            json = file.read()
            yield json


def write_down_invalid_json(err):
    """
    ENG
        This function write down invalid json files in error.log 

        Parameters
        ----------
        err : str
            discription of error

    RU
        Это функция записывает неверные json файлы в error.log

        Аргументы
        ---------
        err : str
            описание ошибки
    """

    with open("error.log", "a") as file:
        file.write(str(err))


def remove_old_error_log(file):
    if os.path.isfile(file):
        os.remove(file)


def validate_json(json_data, schemas):
    """
    ENG
        This function get data from to parameters 'json_data' and 'schemas'
        and then in the loop each json file checks for valid or invalid 
        for each schema

        Parameters
        ----------
        json_data : yeild
            generator with json data 
        schemas : yeild
            generator with schemas
    RU
        Эта функция получает данные из параметров 'json_data' и 'schemas', 
        а затем в цикле каждый файл json проверяет валидность или невалидность
        для каждой схемы

        Аргументы
        ---------
        json_data : yeild
            генератор с json данными 
        schemas : yeild
            генератор с схемами
    """

    # Clean error.log 
    # if you wish remove this code
    remove_old_error_log("error.log")

    for schema in schemas:
        for json in json_data:
            try:
                validate(instance=json, schema=schema)
            except jsonschema.exceptions.ValidationError as err:
                write_down_invalid_json(err)


# Call the main function to run script
validate_json(get_json("json"), get_schemas("schema"))
