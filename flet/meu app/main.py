import flet as ft
from views.welcome import welcome_view
from views.signup import signup_view

def main(page: ft.Page):
    page.title = "Phishing"
    page.bgcolor = "#F8F8F8"
    page.window.width = 450
    page.window.height = 750
    page.window.maximizable = False
    page.window.resizable = False
    
    page.fonts = {
        "MinhaFonte": "C:/Users/isaki/Desktop/APP/flet/recursos/Montserrat-Regular.ttf"
    }

    page.theme = ft.Theme(font_family="MinhaFonte")

    page.views.append(welcome_view(page))
    page.update()
    
ft.app(target=main)