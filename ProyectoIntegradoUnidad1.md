# Sistema de Registro de Estudiantes - Flet 

Este proyecto fue desarrollado para la materia de Tópicos Avanzados de Programación utilizando Python y el framework Flet.

La aplicación implementa una interfaz gráfica en modo oscuro con estilo tipo "terminal tecnológica", validación de formularios y un sistema de confirmación visual mediante overlay.

El proyecto demuestra:

- Uso del framework Flet para desarrollo de interfaces modernas
- Aplicación de Dark Mode y personalización de estilos
- Validación de formularios en tiempo real
- Manejo de eventos con funciones callback
- Uso de overlays para mostrar resultados
- Organización estructurada de componentes visuales

---

## Código Completo

```python
import flet as ft

def main(page: ft.Page):
    # Configuración "Tech" / Dark Mode
    page.title = "Registro de Estudiantes - Terminal Mode"
    page.bgcolor = "#0F172A"  
    page.padding = 30
    page.theme_mode = ft.ThemeMode.DARK

    # Paleta de colores "Cyber"
    color_base = "#00E5FF"  
    color_error = "#FF453A" 
    color_texto = "#E2E8F0" 

    # --- CONTROLES DE ENTRADA ---
    txt_nombre = ft.TextField(label="Nombre", border_color=color_base, color=color_texto, cursor_color=color_base, expand=True)
    txt_control = ft.TextField(label="Número de control", border_color=color_base, color=color_texto, cursor_color=color_base, expand=True)
    txt_email = ft.TextField(label="Email", border_color=color_base, color=color_texto, cursor_color=color_base)

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color=color_base,
        color=color_texto,
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color=color_base,
        color=color_texto,
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    rg_genero = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="masculino", label="Masculino", fill_color=color_base),
        ft.Radio(value="femenino", label="Femenino", fill_color=color_base)
    ]))

    txt_error_genero = ft.Text(value="", color=color_error, size=12)

    row_genero = ft.Column([
        ft.Row([
            ft.Text("Género:", color=color_base, weight=ft.FontWeight.BOLD, size=16),
            rg_genero
        ], alignment=ft.MainAxisAlignment.START),
        txt_error_genero
    ])

    # --- FUNCIÓN PARA MOSTRAR DATOS Y VALIDAR ---
    def enviar_datos(e):
        txt_nombre.error_text = None
        txt_nombre.border_color = color_base
        
        txt_control.error_text = None
        txt_control.border_color = color_base
        
        txt_email.error_text = None
        txt_email.border_color = color_base
        
        dd_carrera.error_text = None
        dd_carrera.border_color = color_base
        
        dd_semestre.error_text = None
        dd_semestre.border_color = color_base
        
        txt_error_genero.value = ""
        
        es_valido = True

        valor_nombre = txt_nombre.value.strip() if txt_nombre.value else ""
        if not valor_nombre:
            txt_nombre.error_text = "El nombre es obligatorio."
            txt_nombre.border_color = color_error
            es_valido = False
        elif any(char.isdigit() for char in valor_nombre):
            txt_nombre.error_text = "El nombre no puede contener números."
            txt_nombre.border_color = color_error
            es_valido = False

        valor_control = txt_control.value.strip() if txt_control.value else ""
        if not valor_control:
            txt_control.error_text = "El número de control es obligatorio."
            txt_control.border_color = color_error
            es_valido = False
        elif not valor_control.isdigit():
            txt_control.error_text = "Solo se permiten números."
            txt_control.border_color = color_error
            es_valido = False

        valor_email = txt_email.value.strip() if txt_email.value else ""
        if not valor_email:
            txt_email.error_text = "El email es obligatorio."
            txt_email.border_color = color_error
            es_valido = False
        elif not valor_email.endswith("@gmail.com"):
            txt_email.error_text = "El email debe terminar en @gmail.com"
            txt_email.border_color = color_error
            es_valido = False

        if not dd_carrera.value:
            dd_carrera.error_text = "Selecciona una carrera."
            dd_carrera.border_color = color_error
            es_valido = False
            
        if not dd_semestre.value:
            dd_semestre.error_text = "Selecciona un semestre."
            dd_semestre.border_color = color_error
            es_valido = False

        if not rg_genero.value:
            txt_error_genero.value = "Por favor, selecciona un género."
            es_valido = False

        page.update()

        if not es_valido:
            return

        def cerrar_dialogo(e):
            if overlay_container in page.overlay:
                page.overlay.remove(overlay_container)
            
            txt_nombre.value = ""
            txt_control.value = ""
            txt_email.value = ""
            dd_carrera.value = None
            dd_semestre.value = None
            rg_genero.value = None
            
            page.update()

        overlay_container = ft.Container(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("DATOS TRANSMITIDOS", weight=ft.FontWeight.BOLD, color=color_base, size=20),
                    ft.Divider(color=color_base),
                    ft.Text(f"Nombre: {valor_nombre}", size=15, color=color_texto),
                    ft.Text(f"Número de control: {valor_control}", size=15, color=color_texto),
                    ft.Text(f"Email: {valor_email}", size=15, color=color_texto),
                    ft.Text(f"Carrera: {dd_carrera.value}", size=15, color=color_texto),
                    ft.Text(f"Semestre: {dd_semestre.value}", size=15, color=color_texto),
                    ft.Text(f"Género: {rg_genero.value}", size=15, color=color_texto),
                    ft.Container(height=10),
                    ft.ElevatedButton(
                        content=ft.Text("Cerrar Conexión", color="#0F172A", weight=ft.FontWeight.BOLD),
                        bgcolor=color_base,
                        on_click=cerrar_dialogo,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                bgcolor="#1E293B", 
                border=ft.border.all(2, color_base), 
                border_radius=10,
                padding=30,
                width=400,
                shadow=ft.BoxShadow(blur_radius=30, color=ft.Colors.with_opacity(0.3, color_base)), 
            ),
            bgcolor=ft.Colors.with_opacity(0.8, "black"), 
            alignment=ft.Alignment(0, 0),
            expand=True,
        )

        page.overlay.append(overlay_container)
        page.update()

    btn_enviar = ft.ElevatedButton(
        content=ft.Text("EJECUTAR REGISTRO", color="#0F172A", size=16, weight=ft.FontWeight.BOLD),
        bgcolor=color_base,
        on_click=enviar_datos,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
        )
    )

    # --- CONSTRUCCIÓN DE LA INTERFAZ ---
    page.add(
        ft.Column([
            ft.Text("SISTEMA DE REGISTRO", size=24, weight=ft.FontWeight.BOLD, color=color_base),
            ft.Divider(color=color_base),
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([
                dd_carrera,
                dd_semestre
            ], spacing=10),
            row_genero,
            ft.Container(height=10),
            btn_enviar
        ], spacing=15)
    )

ft.run(main, view=ft.AppView.WEB_BROWSER)
```

---

## Funcionamiento General

1. Se configura la página en modo oscuro con una paleta estilo "cyber".
2. Se crean campos de texto, dropdowns y radio buttons.
3. Se valida cada campo al presionar el botón.
4. Si existen errores, se muestran mensajes personalizados.
5. Si todo es válido, se muestra un overlay con los datos capturados.
6. El botón "Cerrar Conexión" limpia el formulario y cierra el overlay.

---

## Conceptos Aplicados

- Programación orientada a eventos
- Validación de formularios
- Componentes visuales en Flet
- Manejo dinámico de estilos
- Uso de contenedores y layouts (Row, Column)
- Implementación de overlays
- Separación lógica entre interfaz y validación

---

## Ejecución

```python
pip install flet
python nombre_del_archivo.py
```

La aplicación se abrirá en el navegador usando el modo WEB_BROWSER.
