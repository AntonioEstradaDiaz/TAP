1. Interfaz Gráfica de Usuario

Una Interfaz Gráfica de Usuario (GUI, Graphical User Interface) es el medio visual mediante el cual un usuario interactúa con un sistema informático a través de elementos gráficos como botones, ventanas, formularios, menús y campos de texto.

La GUI se basa en la programación orientada a eventos, donde el sistema responde a acciones del usuario como clics, escritura o selección de opciones. Este modelo mejora la experiencia del usuario y permite construir aplicaciones dinámicas e interactivas.

En esta unidad se utiliza el framework Flet para el desarrollo de interfaces gráficas con Python, permitiendo crear aplicaciones web, de escritorio y móviles con una misma base de código.

1.1 Creación de interfaz gráfica para usuarios

La creación de una interfaz gráfica implica:

Configurar la ventana principal.

Definir controles visuales.

Organizar componentes mediante contenedores.

Asignar eventos a los controles interactivos.

En Flet, la interfaz se construye agregando controles a un objeto Page.

Ejemplo 1: Calculadora básica (Uso de GridView y Container)

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

    txt_pantalla = ft.Text(value="0", size=30)

    display = ft.Container(
        content=txt_pantalla,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
    )

    def btn_click(e):
        valor = e.control.data
        if txt_pantalla.value == "0":
            txt_pantalla.value = valor
        else:
            txt_pantalla.value += valor
        page.update()

    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=210,
        height=120,
        expand=False
    )

    datos = [
        (ft.Colors.PRIMARY, "1"),
        (ft.Colors.SECONDARY, "2"),
        (ft.Colors.TERTIARY, "3"),
        (ft.Colors.ERROR, "4"),
    ]

    for color, texto in datos:
        grid.controls.append(
            ft.Container(
                content=ft.Text(texto, size=20, weight="bold", color="white"),
                bgcolor=color,
                border_radius=8,
                alignment=ft.alignment.Alignment(0, 0),
                on_click=btn_click,
                data=texto
            )
        )

    page.add(ft.Column([display, grid]))

ft.app(target=main)
```
En esta práctica se aplicó:

Uso de contenedores.

Uso de GridView.

Manejo de eventos on_click.

Actualización dinámica con page.update().

1.2 Tipos de eventos

Un evento es una acción que ocurre dentro de la aplicación y que puede ser procesada por el sistema.

Tipos principales:

Eventos de clic (on_click)

Eventos de cambio (on_change)

Eventos de envío (on_submit)

Eventos personalizados mediante pubsub

Ejemplo 2: Chat con sistema de eventos y pubsub

```python
from dataclasses import dataclass
import flet as ft

@dataclass
class Message:
    user: str
    text: str
    message_type: str

def main(page: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(
            Message(
                user="Usuario",
                text=new_message.value,
                message_type="chat_message",
            )
        )
        new_message.value = ""

    page.add(chat, ft.Row([new_message, ft.Button("Send", on_click=send_click)]))

ft.app(target=main)
```
En esta práctica se aplicó:

Manejo de eventos personalizados.

Comunicación entre usuarios con pubsub.

Actualización dinámica de controles.

1.3 Manejo de eventos

El manejo de eventos consiste en asociar funciones a acciones específicas del usuario.

Ejemplo aplicado en un sistema tipo casino con cambio de vistas:
```python
import flet as ft
import random

def main(page: ft.Page):
    page.title = "Casino Demo"

    resultado = ft.Text("")

    def lanzar_dado(e):
        resultado.value = f"Dado: {random.randint(1,6)}"
        page.update()

    def dado_view():
        return ft.Column(
            [
                ft.Text("Dado"),
                ft.ElevatedButton("Lanzar", on_click=lanzar_dado),
                resultado
            ]
        )

    page.add(dado_view())

ft.app(target=main)
```
Aquí se observa:

Eventos de botón.

Modificación de valores dinámicos.

Uso de funciones para cambiar vistas.

1.4 Manejo de componentes gráficos de control

Los componentes gráficos permiten la entrada y validación de datos.

Ejemplo 4: Formulario con validaciones
```python
import flet as ft

def main(page: ft.Page):

    txt_nombre = ft.TextField(label="Nombre")
    txt_email = ft.TextField(label="Email")

    def enviar_datos(e):
        if not txt_nombre.value:
            txt_nombre.error_text = "El nombre es obligatorio."
        if not txt_email.value:
            txt_email.error_text = "El email es obligatorio."
        page.update()

    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar_datos)

    page.add(ft.Column([txt_nombre, txt_email, btn_enviar]))

ft.app(target=main)
```
En esta práctica se aplicó:

Uso de TextField.

Validación de datos.

Manejo de mensajes de error.

Interacción dinámica con el usuario.

Conclusión

Durante la Unidad I se desarrollaron múltiples prácticas que permitieron comprender los fundamentos de las interfaces gráficas y la programación orientada a eventos.

Se aplicaron conceptos como:

Creación de interfaces.

Manejo de eventos.

Uso de contenedores y layouts.

Validación de datos.

Comunicación entre componentes.

Cambio dinámico de vistas.

El framework Flet permitió integrar estos elementos de forma estructurada y modular, facilitando el desarrollo de aplicaciones interactivas en Python.

Bibliografía

Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1995). Design patterns: Elements of reusable object-oriented software. Addison-Wesley.

Lutz, M. (2013). Learning Python (5th ed.). O’Reilly Media.

Shneiderman, B., Plaisant, C., Cohen, M., Jacobs, S., Elmqvist, N., & Diakopoulos, N. (2016). Designing the user interface: Strategies for effective human-computer interaction (6th ed.). Pearson.

Sommerville, I. (2016). Software engineering (10th ed.). Pearson.

Flet Dev. (2024). Flet documentation. Recuperado de https://flet.dev/docs
