Feature: Search de Wikipedia
    Scenario: Busqueda correcta
        Given el usuario se encuentra en la pagina base de Wikipedia
        When el usuario busca el lenguaje de programacion python
        Then aparece la informacion de python con su titulo   