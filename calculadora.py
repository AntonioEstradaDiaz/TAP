import flet as ft

def main(page: ft.Page):
    # Configuración ventana
    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

    # Texto de la pantalla
    txt_pantalla = ft.Text(value="0", size=30)

    # Contenedor de la pantalla
    display = ft.Container(
        content=txt_pantalla,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0), # Derecha
        padding=10,
        width=210,
        height=70,
    )

    # Función al presionar botones
    def btn_click(e):
        valor = e.control.data
        if txt_pantalla.value == "0":
            txt_pantalla.value = valor
        else:
            txt_pantalla.value += valor
        page.update()

    # Función limpiar pantalla
    def limpiar(e):
        txt_pantalla.value = "0"
        page.update()

    # Grid para los 4 botones
    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=210,
        height=120,
        expand=False
    )

    # Datos botones (Color, Texto)
    datos = [
        (ft.Colors.PRIMARY, "1"),
        (ft.Colors.SECONDARY, "2"),
        (ft.Colors.TERTIARY, "3"),
        (ft.Colors.ERROR, "4"),
    ]

    # Crear botones y agregar al grid
    for color, texto in datos:
        grid.controls.append(
            ft.Container(
                content=ft.Text(texto, size=20, weight="bold", color="white"),
                bgcolor=color,
                border_radius=8,
                alignment=ft.alignment.Alignment(0, 0), # Centro
                on_click=btn_click,
                data=texto
            )
        )

    # Boton de limpiar
    btn_limpiar = ft.Container(
        content=ft.Text("LIMPIAR", weight="bold", color="white"),
        bgcolor=ft.Colors.GREY_700,
        border_radius=8,
        alignment=ft.alignment.Alignment(0, 0), # Centro
        width=210,
        height=50,
        on_click=limpiar
    )

    # Layout principal
    layout = ft.Column(
        controls=[display, grid, btn_limpiar],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(layout)

ft.app(target=main)