import flet as ft
import requests
 
def main(page: ft.Page):

    def ConectarAPI(moeda):
        url= 'https://open.er-api.com/v6/latest/' + moeda

        resposta= requests.get(url)

        if resposta.status_code== 200:
            dados= resposta.json()
            return (dados['rates']['BRL'])

    def convert_currency(e):
        cotacao= ConectarAPI ('USD')
        if valor_input.value.isdecimal() and cotacao!= None:
            dollars = float(valor_input.value)
            reais = dollars * cotacao
            result.value = f"BRL {reais:.2f}"
        else:
            result.value = "Por favor, insira um número válido"
        page.update()
   
    # Título
    page.title = "Conversor de Moeda (USD para BRL)"
 
    # Campo de entrada para BRL
    valor_input = ft.TextField(label="Valor em Dólares (USD)", width=200)
 
    # Botão para acionar a conversão
    convert_button = ft.ElevatedButton(text="Converter", on_click=convert_currency)
 
    # Texto para exibir o resultado
    result = ft.Text(value="BRL 0.00", size=20)
 
    # Adicionando componentes à página
    page.add(
        ft.Column(
            [
                ft.Text("Conversor de Moeda (BRL para USD)", size=30),
                valor_input,
                convert_button,
                result,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
# Executar o aplicativo
ft.app(target=main)