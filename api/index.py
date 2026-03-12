import flet as ft
import random
import time

def main(page: ft.Page):
    # Configuración de ventana (Estilo Mobile)
    page.title = "Cyber RPS"
    page.window_width = 400
    page.window_height = 750
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.bgcolor = "#0B0C10" # Fondo oscuro profundo
    page.padding = 20
    
    # Fuente futurista de Google Fonts
    page.fonts = {"Orbitron": "https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap"}
    page.theme = ft.Theme(font_family="Orbitron")

    # Estado del juego (Vida)
    estado = {"hp_jugador": 100, "hp_cpu": 100, "juego_activo": True}
    daño_por_golpe = 25

    opciones = {
        "Piedra": {"emoji": "🪨", "color": "#FF007F", "vence": "Tijeras"},
        "Papel": {"emoji": "📄", "color": "#00F0FF", "vence": "Piedra"},
        "Tijeras": {"emoji": "✂️", "color": "#CCFF00", "vence": "Papel"}
    }

    # HUD (Head-Up Display) - Barras de vida
    barra_jugador = ft.ProgressBar(value=1.0, color="#00F0FF", bgcolor="#1F2833", height=12, border_radius=5)
    barra_cpu = ft.ProgressBar(value=1.0, color="#FF007F", bgcolor="#1F2833", height=12, border_radius=5)

    hud = ft.Column([
        ft.Row([ft.Text("JUGADOR", color="#00F0FF", size=14), ft.Text("CPU", color="#FF007F", size=14)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([ft.Container(barra_jugador, expand=True), ft.Container(width=10), ft.Container(barra_cpu, expand=True)]),
    ])

    resultado_texto = ft.Text("READY?", size=28, color="#FFFFFF", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    # Zona de combate
    batalla_jugador = ft.Text("⚡", size=70, animate_scale=ft.Animation(duration=300, curve="bounceOut"))
    batalla_cpu = ft.Text("⚡", size=70, animate_scale=ft.Animation(duration=300, curve="bounceOut"))
    
    zona_batalla = ft.Container(
        content=ft.Row(
            [batalla_jugador, ft.Text("VS", size=20, color="#45A29E"), batalla_cpu],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=30,
        border=ft.border.all(2, "#1F2833"),
        border_radius=15,
        bgcolor="#111217",
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color="black12")
    )

    def reiniciar_juego(e):
        estado["hp_jugador"] = 100
        estado["hp_cpu"] = 100
        estado["juego_activo"] = True
        barra_jugador.value = 1.0
        barra_cpu.value = 1.0
        batalla_jugador.value = "⚡"
        batalla_cpu.value = "⚡"
        resultado_texto.value = "READY?"
        resultado_texto.color = "#FFFFFF"
        btn_reinicio.visible = False
        page.update()

    btn_reinicio = ft.ElevatedButton("JUGAR DE NUEVO", on_click=reiniciar_juego, visible=False, color="#0B0C10", bgcolor="#66FCF1")

    def jugar(e):
        if not estado["juego_activo"]:
            return

        eleccion_jugador = e.control.data
        eleccion_cpu = random.choice(list(opciones.keys()))

        # Animación de carga
        batalla_jugador.scale = 0.8
        batalla_cpu.scale = 0.8
        batalla_jugador.value = opciones[eleccion_jugador]["emoji"]
        batalla_cpu.value = "❓"
        resultado_texto.value = "FIGHT!"
        page.update()
        
        time.sleep(0.4) 

        # Revelación y golpe
        batalla_jugador.scale = 1.2
        batalla_cpu.scale = 1.2
        batalla_cpu.value = opciones[eleccion_cpu]["emoji"]

        # Lógica de daño
        if eleccion_jugador == eleccion_cpu:
            resultado_texto.value = "BLOQUEADO"
            resultado_texto.color = "#C5C6C7"
        elif opciones[eleccion_jugador]["vence"] == eleccion_cpu:
            resultado_texto.value = "¡GOLPE CRÍTICO!"
            resultado_texto.color = "#00F0FF"
            estado["hp_cpu"] -= daño_por_golpe
            barra_cpu.value = max(0, estado["hp_cpu"] / 100) # Evita que la barra de vida sea negativa
        else:
            resultado_texto.value = "¡DAÑO RECIBIDO!"
            resultado_texto.color = "#FF007F"
            estado["hp_jugador"] -= daño_por_golpe
            barra_jugador.value = max(0, estado["hp_jugador"] / 100)

        # Chequear Fin del Juego
        if estado["hp_jugador"] <= 0 or estado["hp_cpu"] <= 0:
            estado["juego_activo"] = False
            btn_reinicio.visible = True
            if estado["hp_jugador"] <= 0:
                resultado_texto.value = "GAME OVER"
                resultado_texto.color = "#FF007F"
            else:
                resultado_texto.value = "¡VICTORIA!"
                resultado_texto.color = "#CCFF00"

        page.update()
        time.sleep(0.2)
        batalla_jugador.scale = 1.0
        batalla_cpu.scale = 1.0
        page.update()

    # Botones estilo "Consola/Arcade"
    botones = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        controls=[
            ft.Container(
                content=ft.Text(datos["emoji"], size=35),
                bgcolor="#111217",
                border=ft.border.all(2, datos["color"]),
                padding=20,
                border_radius=50,
                ink=True,
                on_click=jugar,
                data=nombre,
                shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color=datos["color"], offset=ft.Offset(0, 0))
            ) for nombre, datos in opciones.items()
        ]
    )

    # Ensamblar la pantalla (Corregido el contenedor del resultado_texto)
    page.add(
        hud,
        ft.Container(height=30),
        zona_batalla,
        # Solución: Usamos un Row centrado en lugar de ft.alignment.center
        ft.Row([resultado_texto], alignment=ft.MainAxisAlignment.CENTER), 
        ft.Row([btn_reinicio], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(expand=True),
        botones,
        ft.Container(height=10)
    )

#ft.app(target=main)
ft.app(target=main,view=ft.AppView.WEB_BROWSER)