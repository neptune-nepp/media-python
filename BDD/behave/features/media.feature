Feature: Soma dois números e dividir por 2
    Sceneario: Realizar uma soma e divisão simples
        Given eu tenho dois números inteiros: 2 e 4
        When eu somo os dois números e dividido por 2
        Then o resultado deve ser 3


    Scenario: Valores não inteiros não são aceitos
        Given eu tenho dois números que não são inteiros: 2.5 e 4.2
        When eu tento somar os dois números e dividir por 2
        Then uma exceção TypeError deve ser levantada