import flet as ft

def signup_view(page: ft.Page):
    def go_to_welcome(e):
        from .welcome import welcome_view
        page.views.append(welcome_view(page))
        page.update()

    return ft.View(
        "/signup", [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src="C:/Users/Isaki/Desktop/APP/flet/recursos/Icone4.png", width=110, height=110),
                        ft.Text("Bem Vindo", color="gray", size=13),
                        ft.Container(
                            content=ft.Text("Fazer Login", size=30, weight="bold", text_align=ft.TextAlign.CENTER),
                            padding=ft.padding.only(bottom=30)
                        ),
                        ft.TextField(
                            label="Usuário", 
                            width=330,
                            autofocus=True,
                            content_padding=ft.padding.symmetric(vertical=10, horizontal=12)
                        ),
                        ft.TextField(
                            label="Senha",
                            password=True,
                            can_reveal_password=True,
                            width=330,
                            content_padding=ft.padding.symmetric(vertical=10, horizontal=12),
                        ),
                        ft.Container(height=5),
                        ft.Container(
                            content=ft.Switch(label="Manter Login", scale=0.8),
                            alignment=ft.alignment.center_left,
                            padding=ft.padding.only(left=15)
                        ),
                        ft.Container(
                            content=ft.Checkbox(label="Aceito os termos de privacidade", value=False),
                            alignment=ft.alignment.center_left,
                            padding=ft.padding.only(left=23)
                        ),
                        ft.Container(
                            content=ft.ElevatedButton("Entrar", width=200, height=50, bgcolor="green", color="white"),
                            padding=ft.padding.only(top=23)
                        ),
                        ft.Container(
                            content=ft.TextButton(
                                "Esqueceu a senha?",
                                on_click=lambda e: print("Redirecionar para recuperação de senha"),
                                style=ft.ButtonStyle(
                                    padding=ft.padding.all(0),
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                    bgcolor=None
                                ),
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=0),
                        ),
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.icons.ARROW_BACK, 
                                on_click=go_to_welcome,
                                bgcolor="transparent", 
                                icon_color="white", 
                                icon_size=30,
                            ),
                            padding=ft.padding.only(left=10),
                            alignment=ft.alignment.center_left
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
