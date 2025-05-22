import flet as ft

def create_account_view(page: ft.Page):
    def go_to_welcome(e):
        from .welcome import welcome_view
        page.views.append(welcome_view(page))
        page.update()
    
    def validate_and_create_account(e):
        # Referências aos campos do formulário
        username_value = username_field.value
        email_value = email_field.value
        password_value = password_field.value
        confirm_password_value = confirm_password_field.value
        terms_accepted = terms_checkbox.value

        # Validação dos campos obrigatórios
        error = False
        
        # Validar usuário
        if not username_value or username_value.strip() == "":
            username_field.error_text = "Usuário é obrigatório"
            error = True
        else:
            username_field.error_text = None
            
        # Validar e-mail
        if not email_value or email_value.strip() == "":
            email_field.error_text = "E-mail é obrigatório"
            error = True
        elif "@" not in email_value or "." not in email_value:
            email_field.error_text = "E-mail inválido"
            error = True
        else:
            email_field.error_text = None
            
        # Validar senha
        if not password_value or password_value.strip() == "":
            password_field.error_text = "Senha é obrigatória"
            error = True
        else:
            password_field.error_text = None
            
        # Validar confirmação de senha
        if not confirm_password_value or confirm_password_value.strip() == "":
            confirm_password_field.error_text = "Confirmação de senha é obrigatória"
            error = True
        elif password_value != confirm_password_value:
            confirm_password_field.error_text = "As senhas não coincidem"
            error = True
        else:
            confirm_password_field.error_text = None
            
        # Validar aceite dos termos
        if not terms_accepted:
            terms_error.visible = True
            error = True
        else:
            terms_error.visible = False
        
        # Atualizar a página para mostrar as mensagens de erro
        page.update()
        
        # Se não houver erros, criar a conta e navegar para a tela de boas-vindas
        if not error:
            print("Conta criada com sucesso!")
            # Aqui seria implementada a lógica para criar a conta
            # Por enquanto, apenas volta para a tela de boas-vindas
            go_to_welcome(e)

    # Criação dos campos com referências para validação
    username_field = ft.TextField(
        label="Usuário", 
        width=330,
        autofocus=True,
        content_padding=ft.padding.symmetric(vertical=10, horizontal=12)
    )
    
    email_field = ft.TextField(
        label="E-mail",
        width=330,
        content_padding=ft.padding.symmetric(vertical=10, horizontal=12)
    )
    
    password_field = ft.TextField(
        label="Senha",
        password=True,
        can_reveal_password=True,
        width=330,
        content_padding=ft.padding.symmetric(vertical=10, horizontal=12),
    )
    
    confirm_password_field = ft.TextField(
        label="Confirmar Senha",
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
                            content=ft.Text("Criar Conta", size=30, weight="bold", text_align=ft.TextAlign.CENTER),
                            padding=ft.padding.only(bottom=30)
                        ),
                        username_field,
                        email_field,
                        password_field,
                        confirm_password_field,
                        ft.Container(height=5),
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
                                "Cadastrar", 
                                width=200, 
                                height=50, 
                                bgcolor="green", 
                                color="white",
                                on_click=validate_and_create_account
                            ),
                            padding=ft.padding.only(top=23)
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
