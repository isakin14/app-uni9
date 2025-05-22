import flet as ft

def signup_view(page: ft.Page):
    def go_to_welcome(e):
        from .welcome import welcome_view
        page.views.append(welcome_view(page))
        page.update()

    def go_to_dashboard(e):
        # Referências aos campos do formulário
        username_value = username_field.value
        password_value = password_field.value
        terms_accepted = terms_checkbox.value

        # Validação dos campos obrigatórios
        error = False
        
        # Validar usuário
        if not username_value or username_value.strip() == "":
            username_field.error_text = "Usuário é obrigatório"
            error = True
        else:
            username_field.error_text = None
            
        # Validar senha
        if not password_value or password_value.strip() == "":
            password_field.error_text = "Senha é obrigatória"
            error = True
        else:
            password_field.error_text = None
            
        # Validar aceite dos termos
        if not terms_accepted:
            terms_error.visible = True
            error = True
        else:
            terms_error.visible = False
        
        # Atualizar a página para mostrar as mensagens de erro
        page.update()
        
        # Se não houver erros, navegar para o dashboard
        if not error:
            print("Login bem-sucedido!")
            from .dashboard import dashboard_view
            page.go("/dashboard")
            page.update()

    # Criação dos campos com referências para validação
    username_field = ft.TextField(
        label="Usuário", 
        width=330,
        autofocus=True,
        content_padding=ft.padding.symmetric(vertical=10, horizontal=12)
    )
    
    password_field = ft.TextField(
        label="Senha",
        password=True,
        can_reveal_password=True,
        width=330,
        content_padding=ft.padding.symmetric(vertical=10, horizontal=12),
    )
    
    terms_checkbox = ft.Checkbox(
        label="Aceito os termos de privacidade", 
        value=False
    )
    
    # Mensagem de erro para os termos (inicialmente invisível)
    terms_error = ft.Text(
        "Você deve aceitar os termos de privacidade",
        color="red",
        size=12,
        visible=False
    )

    return ft.View(
        "/signup", [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src="C:/Users/isaki/Documents/python/app-uni9/flet/meu app/assets/phishing.png", width=110, height=110),
                        ft.Container(
                            content=ft.Text("Login", size=30, weight="bold", text_align=ft.TextAlign.CENTER),
                            padding=ft.padding.only(bottom=30)
                        ),
                        username_field,
                        password_field,
                        ft.Container(height=5),
                        ft.Container(
                            content=ft.Switch(label="Manter Login", scale=0.9),
                            alignment=ft.alignment.center_left,
                            padding=ft.padding.only(left=15)
                        ),
                        ft.Container(
                            content=ft.Column([
                                terms_checkbox,
                                terms_error
                            ], spacing=0),
                            alignment=ft.alignment.center_left,
                            padding=ft.padding.only(left=23)
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                "Entrar", 
                                width=200, 
                                height=50, 
                                bgcolor="green", 
                                color="white",
                                on_click=go_to_dashboard,
                            ),
                            padding=ft.padding.only(top=23),
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
                                icon=ft.icons.ARROW_BACK if hasattr(ft, 'icons') else "arrow_back", 
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
