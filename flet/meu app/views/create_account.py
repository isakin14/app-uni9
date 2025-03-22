import flet as ft

def create_account_view(page: ft.Page):
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
                        ft.Container(
                            content=ft.Text("Criar Conta", size=30, weight="bold", text_align=ft.TextAlign.CENTER),
                            padding=ft.padding.only(bottom=30)
                        ),
                        ft.TextField(
                            label="Usuário", 
                            width=330,
                            autofocus=True,
                            content_padding=ft.padding.symmetric(vertical=10, horizontal=12)
                        ),
                        ft.TextField(
                            label="E-mail",
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
                        ft.TextField(
                            label="Confirmar Senha",
                            password=True,
                            can_reveal_password=True,
                            width=330,
                            content_padding=ft.padding.symmetric(vertical=10, horizontal=12),
                        ),
                        ft.Container(height=5),
                        ft.Container(
                            content=ft.Checkbox(label="Aceito os termos de privacidade", value=False),
                            alignment=ft.alignment.center_left,
                            padding=ft.padding.only(left=23)
                        ),
                        ft.Container(
                            content=ft.ElevatedButton("Cadastrar", width=200, height=50, bgcolor="green", color="white"),
                            padding=ft.padding.only(top=23)
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
