import flet as ft

def welcome_view(page: ft.Page):
    def go_to_signup(e):
        from .signup import signup_view
        page.views.append(signup_view(page))
        page.update()
    
    return ft.View(
        "/", [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src="C:/Users/Isaki/Desktop/APP/flet/recursos/Icone4.png", width=230, height=230),
                        ft.Column(
                            controls=[],
                            height=25,
                        ),
                        ft.ElevatedButton(
                            "ENTRAR", 
                            on_click=go_to_signup, 
                            bgcolor="green", 
                            color="white",
                            width=200,
                            height=50,
                        ),
                        ft.Container(
                            content=ft.TextButton(
                                "Criar conta",
                                on_click=lambda e: print("Redirecionar para criação de conta"),
                                style=ft.ButtonStyle(
                                    padding=ft.padding.all(0),
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                    bgcolor=None
                                ),
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=0),
                        ),
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
