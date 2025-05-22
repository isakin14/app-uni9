import flet as ft

def dashboard_view(page: ft.Page):
    # Função para voltar à tela anterior
    def go_back(e):
        from .welcome import welcome_view
        page.views.append(welcome_view(page))
        page.update()
    
    # Função para atualizar o dashboard (simulação)
    def refresh_dashboard(e):
        # Aqui seria implementada a lógica para atualizar os dados
        # Por enquanto, apenas mostra uma mensagem
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Dashboard atualizado!"),
            bgcolor="#4CAF50"
        )
        page.snack_bar.open = True
        page.update()
    
    # Função para exibir detalhes da máquina (simulação)
    def show_machine_details(e, machine_name):
        # Aqui seria implementada a navegação para a tela de detalhes
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Detalhes da {machine_name}"),
            bgcolor="#2196F3"
        )
        page.snack_bar.open = True
        page.update()
    
    # Função para criar um card de máquina
    def create_machine_card(name, infected, suspicious, status):
        # Definir cores baseadas no status
        if status == "Segura":
            status_color = "#4CAF50"  # Verde
            circle_color = "#4CAF50"
        elif status == "Em observação":
            status_color = "#FFC107"  # Amarelo
            circle_color = "#FFC107"
        else:  # Crítica
            status_color = "#F44336"  # Vermelho
            circle_color = "#F44336"
        
        return ft.Container(
            content=ft.Column([
                # Cabeçalho do card
                ft.Row([
                    ft.Container(
                        content=ft.Text(""),
                        width=15,
                        height=15,
                        border_radius=50,
                        bgcolor=circle_color
                    ),
                    ft.Text(
                        name,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    )
                ], alignment=ft.MainAxisAlignment.START, spacing=10),
                
                # Linha separadora
                ft.Container(
                    height=1,
                    bgcolor="#424242",
                    margin=ft.margin.only(top=10, bottom=10)
                ),
                
                # Corpo do card - Informações
                ft.Row([
                    ft.Icon(name="warning", color="#F44336", size=16),
                    ft.Text("Arquivos contaminados:", size=14, color="#BDBDBD"),
                    ft.Text(str(infected), size=14, weight=ft.FontWeight.BOLD, color="white")
                ], alignment=ft.MainAxisAlignment.START, spacing=5),
                
                ft.Row([
                    ft.Icon(name="help_outline", color="#FFC107", size=16),
                    ft.Text("Arquivos suspeitos:", size=14, color="#BDBDBD"),
                    ft.Text(str(suspicious), size=14, weight=ft.FontWeight.BOLD, color="white")
                ], alignment=ft.MainAxisAlignment.START, spacing=5),
                
                # Rodapé do card - Status
                ft.Container(
                    content=ft.Text(
                        f"Status: {status}",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),
                    bgcolor=status_color,
                    border_radius=5,
                    padding=10,
                    margin=ft.margin.only(top=15),
                    alignment=ft.alignment.center
                )
            ]),
            width=320,
            border_radius=10,
            bgcolor="#212121",
            padding=15,
            margin=10,
            ink=True,  # Efeito de clique
            on_click=lambda e, name=name: show_machine_details(e, name)
        )
    
    # Dados de exemplo para as máquinas
    machines_data = [
        {"name": "Máquina 01", "infected": 0, "suspicious": 0, "status": "Segura"},
        {"name": "Máquina 02", "infected": 0, "suspicious": 3, "status": "Em observação"},
        {"name": "Máquina 03", "infected": 2, "suspicious": 5, "status": "Crítica"},
        {"name": "Máquina 04", "infected": 0, "suspicious": 1, "status": "Segura"},
        {"name": "Máquina 05", "infected": 4, "suspicious": 2, "status": "Crítica"},
        {"name": "Máquina 06", "infected": 0, "suspicious": 2, "status": "Em observação"}
    ]
    
    # Criar cards para cada máquina
    machine_cards = []
    for machine in machines_data:
        machine_cards.append(
            create_machine_card(
                machine["name"],
                machine["infected"],
                machine["suspicious"],
                machine["status"]
            )
        )
    
    # Organizar cards em uma lista com layout de wrap
    card_row_1 = ft.Row(
        controls=[machine_cards[0], machine_cards[1], machine_cards[2]],
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )
    
    card_row_2 = ft.Row(
        controls=[machine_cards[3], machine_cards[4], machine_cards[5]],
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )
    
    # Retornar a view completa
    return ft.View(
        "/dashboard",
        [
            # Barra superior com título e botão de voltar
            ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.icons.ARROW_BACK if hasattr(ft, 'icons') else "arrow_back",
                    on_click=go_back
                ),
                title=ft.Text("Dashboard de Segurança"),
                bgcolor="#1E1E1E",
                center_title=True
            ),
            
            # Conteúdo principal
            ft.Container(
                content=ft.Column([
                    # Subtítulo
                    ft.Text(
                        "Status das Máquinas",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),
                    
                    # Resumo geral
                    ft.Container(
                        content=ft.Row([
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("Total de Máquinas", size=14, color="#BDBDBD"),
                                    ft.Text(str(len(machines_data)), size=24, weight=ft.FontWeight.BOLD, color="white")
                                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                                bgcolor="#212121",
                                border_radius=10,
                                padding=15,
                                expand=True,
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("Máquinas Seguras", size=14, color="#BDBDBD"),
                                    ft.Text(
                                        str(sum(1 for m in machines_data if m["status"] == "Segura")),
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color="#4CAF50"
                                    )
                                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                                bgcolor="#212121",
                                border_radius=10,
                                padding=15,
                                expand=True,
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("Máquinas Críticas", size=14, color="#BDBDBD"),
                                    ft.Text(
                                        str(sum(1 for m in machines_data if m["status"] == "Crítica")),
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color="#F44336"
                                    )
                                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                                bgcolor="#212121",
                                border_radius=10,
                                padding=15,
                                expand=True,
                                alignment=ft.alignment.center
                            )
                        ], spacing=10),
                        margin=ft.margin.only(top=10, bottom=20)
                    ),
                    
                    # Cards de máquinas organizados em linhas com wrap
                    ft.Text("Detalhes por Máquina", size=16, color="#BDBDBD"),
                    card_row_1,
                    card_row_2,
                    
                    # Botão de atualização
                    ft.Container(
                        content=ft.ElevatedButton(
                            "ATUALIZAR DASHBOARD",
                            on_click=refresh_dashboard,
                            bgcolor="#4CAF50",
                            color="white",
                            width=250,
                            height=50
                        ),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=20, bottom=20)
                    ),
                ], scroll=ft.ScrollMode.AUTO),
                expand=True,
                padding=20
            )
        ],
        bgcolor="#121212",
        padding=0
    )
