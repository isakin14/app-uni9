import flet as ft
from views.welcome import welcome_view
from views.signup import signup_view
from views.dashboard import dashboard_view

def main(page: ft.Page):
    page.title = "Phishing"
    page.bgcolor = "#F8F8F8"
    page.window.width = 450
    page.window.height = 750
    page.window.maximizable = False
    page.window.resizable = False

    page.fonts = {
        "MinhaFonte": "assets/Montserrat-Regular.ttf",
        "FonteNomeApp": "assets/Outfit-Medium.ttf"
    }

    page.theme = ft.Theme(font_family="MinhaFonte")

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(welcome_view(page))
        elif page.route == "/signup":
            page.views.append(signup_view(page))
        elif page.route == "/dashboard":
            page.views.append(dashboard_view(page))
        
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
