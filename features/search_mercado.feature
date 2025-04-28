Feature: Search de Mercado Libre
    Scenario: Busqueda correcta
        Given el usuario se encuentra en la pagina base de mercado libre
        When el usuario busca el producto iphone13
        Then aparecen todos los productos disponibles  