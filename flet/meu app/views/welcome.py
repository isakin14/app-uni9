import flet as ft
from .signup import signup_view

def welcome_view(page: ft.Page):
    def go_to_signup(e):
        page.views.append(signup_view(page))
        page.update()
    
    return ft.View(
        "/", [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src="C:/Users/Isaki/Downloads/icone.png", width=210, height=210),
                        ft.Column(
                            controls=[],
                            height=20,
                        ),
                        ft.ElevatedButton(
                            "ENTRAR", 
                            on_click=go_to_signup, 
                            bgcolor="green", 
                            color="white",
                            width=200,
                            height=50,
                        ),
                        ft.Text("Clique para entrar", color="gray", size=12),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True,
            )
        ],
        padding=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
