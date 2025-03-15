import flet as ft

def signup_view(page: ft.Page):
    return ft.View(
        "/signup", [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Bem Vindo", color="gray", size=13),
                        ft.Container(
                            content=ft.Text("Fazer Login", size=30, weight="bold", text_align=ft.TextAlign.CENTER),
                            padding=ft.Padding(left=0, top=0, right=0, bottom=30)
                        ),
                        ft.Container(
                            content=ft.TextField(label="Usuário"),
                            padding=ft.Padding(left=0, top=0, right=0, bottom=7)
                        ),
                        ft.Container(
                            content=ft.TextField(label="E-mail"),
                            padding=ft.Padding(left=0, top=0, right=0, bottom=7)
                        ),
                        ft.Container(
                            content=ft.TextField(label="Senha", password=True),
                            padding=ft.Padding(left=0, top=0, right=0, bottom=7)
                        ),
                        ft.Row([ft.Switch(label="Manter Login")], alignment=ft.MainAxisAlignment.START),
                        ft.Container(
                            content=ft.ElevatedButton("Entrar", width=200, height=50, bgcolor="green", color="white"),
                            padding=ft.Padding(left=0, top=23, right=0, bottom=0)
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
