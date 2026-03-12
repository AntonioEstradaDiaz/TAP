import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "Cyber RPS"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.bgcolor = "#0B0C10"
    page.padding = 20
    
    page.fonts = {"Orbitron": "https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap"}
    page.theme = ft.Theme(font_family="Orbitron")

    estado = {"hp_jugador": 100, "hp_cpu": 100, "juego_activo": True}
    daño_por_golpe = 25

    opciones = {
        "Piedra": {"emoji": "🪨", "color": "#FF007F", "vence": "Tijeras"},
        "Papel": {"emoji": "📄", "color": "#00F0FF", "vence": "Piedra"},
        "Tijeras": {"emoji": "✂️", "color": "#CCFF00", "vence": "Papel"}
    }

    barra_jugador = ft.ProgressBar(value=1.0, color="#00F0FF", bgcolor="#1F2833", height=12)
    barra_cpu = ft.ProgressBar(value=1.0, color="#FF007F", bgcolor="#1F2833", height=12)

    hud = ft.Column([
        ft.Row([ft.Text("JUGADOR", color="#00F0FF"), ft.Text("CPU", color="#FF007F")], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([ft.Container(barra_jugador, expand=True), ft.Container(width=10), ft.Container(barra_cpu, expand=True)]),
    ])

    resultado_texto = ft.Text("READY?", size=28, color="#FFFFFF", weight=ft.FontWeight.BOLD)

    batalla_jugador = ft.Text("⚡", size=70, animate_scale=ft.Animation(duration=300, curve="bounceOut"))
    batalla_cpu = ft.Text("⚡", size=70, animate_scale=ft.Animation(duration=300, curve="bounceOut"))
    
    zona_batalla = ft.Container(
        content=ft.Row([batalla_jugador, ft.Text("VS", color="#45A29E"), batalla_cpu], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=30, border=ft.border.all(2, "#1F2833"), border_radius=15, bgcolor="#111217"
    )

    def jugar(e):
        if not estado["juego_activo"]: return
        
        eleccion_jugador = e.control.data
        eleccion_cpu = random.choice(list(opciones.keys()))

        batalla_jugador.value = opciones[eleccion_jugador]["emoji"]
        batalla_cpu.value = "❓"
        page.update()
        time.sleep(0.3)

        batalla_cpu.value = opciones[eleccion_cpu]["emoji"]
        if eleccion_jugador == eleccion_cpu:
            resultado_texto.value = "BLOQUEADO"
        elif opciones[eleccion_jugador]["vence"] == eleccion_cpu:
            estado["hp_cpu"] -= daño_por_golpe
            barra_cpu.value = max(0, estado["hp_cpu"] / 100)
            resultado_texto.value = "¡GOLPE!"
        else:
            estado["hp_jugador"] -= daño_por_golpe
            barra_jugador.value = max(0, estado["hp_jugador"] / 100)
            resultado_texto.value = "¡DAÑO!"

        if estado["hp_jugador"] <= 0 or estado["hp_cpu"] <= 0:
            estado["juego_activo"] = False
            resultado_texto.value = "GAME OVER" if estado["hp_jugador"] <= 0 else "VICTORIA"

        page.update()

    botones = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        controls=[
            ft.Container(
                content=ft.Text(d["emoji"], size=30),
                on_click=jugar, data=n, padding=15, border_radius=50,
                border=ft.border.all(2, d["color"])
            ) for n, d in opciones.items()
        ]
    )

    page.add(hud, ft.Container(height=20), zona_batalla, ft.Row([resultado_texto], alignment="center"), ft.Container(expand=True), botones)

app = ft.app(target=main, export_asgi=True)
