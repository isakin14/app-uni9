import flet as ft

def welcome_view(page: ft.Page):
    def go_to_signup(e):
        from .signup import signup_view
        page.views.append(signup_view(page))
        page.update()

    def go_to_create_account(e):
        from .create_account import create_account_view
        page.views.append(create_account_view(page))
        page.update()
    
    def login_sso(e):
        KEYCLOAK_AUTH_URL = "https://seu-keycloak.com/realms/sua-realm/protocol/openid-connect/auth"
        CLIENT_ID = "seu-client-id"
        REDIRECT_URI = "https://seu-backend.com/callback"

        url = (
            f"{KEYCLOAK_AUTH_URL}"
            f"?client_id={CLIENT_ID}"
            f"&redirect_uri={REDIRECT_URI}"
            f"&response_type=code"
            f"&scope=openid"
        )
        page.launch_url(url)

    return ft.View(
        "/", [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src="assets/phishing.png",
                            width=230,
                            height=230
                        ),
                        ft.Text(
                            "Nome do App",
                            size=44,
                            weight=ft.FontWeight.BOLD,
                            font_family="FonteNomeApp"
                        ),
                        ft.Column(
                            controls=[],
                            height=35,
                        ),
                        ft.ElevatedButton(
                            "ENTRAR", 
                            on_click=go_to_signup, 
                            bgcolor="green", 
                            color="white",
                            width=200,
                            height=50,
                        ),
                        ft.ElevatedButton(
                            "CRIAR CONTA", 
                            on_click=go_to_create_account, 
                            bgcolor="blue", 
                            color="white",
                            width=200,
                            height=50,
                        ),
                        ft.Text("Login SSO:", color="gray", size=13),
                        ft.Container(
                            content=ft.Image(
                                src="assets/e-learning-svgrepo-com.svg",
                                width=40,
                                height=40
                            ),
                            on_click=login_sso,
                            border_radius=10,
                            padding=5,
                            ink=True
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

