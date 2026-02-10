# 🧮 Calculadora Básica con Flet y Python

> **Materia:** Tópicos Avanzados de Programación (TAP)  
> **Práctica:** 0 - Introducción a Flet

Este proyecto consiste en el desarrollo de una interfaz gráfica de usuario (GUI) para una calculadora funcional, utilizando **Python** como lenguaje base y **Flet** como framework visual.

---

## 📸 Vista Previa
*(Aquí puedes subir una captura de tu calculadora funcionando si deseas)*

---

## 📝 Apunte de Desarrollo

### 1. Preparación del Entorno
Para este proyecto utilizamos **Flet**, una librería que permite construir aplicaciones web, de escritorio y móviles con el mismo código base en Python.

**Instalación:**
Se requiere ejecutar el siguiente comando en la terminal para instalar la librería:
```bash
pip install flet
```
2. Estructura de la Interfaz (UI)
El diseño se construye mediante la composición de "Controles" (Widgets). Los principales utilizados fueron:

ft.Container: El bloque constructor fundamental.

Se utilizó para crear la pantalla (display) con alineación a la derecha.

Se utilizó para crear cada botón, asignando colores, bordes redondeados y dimensiones fijas.

ft.GridView: Un organizador automático.

Permite acomodar los botones en una rejilla (filas y columnas) sin tener que calcular coordenadas manuales (runs_count=2).

ft.Column: El layout principal.

Apila verticalmente el display, la rejilla de botones y el botón de "Limpiar".

3. Lógica y Eventos (Backend)
La interactividad se logra conectando la interfaz con funciones de Python mediante eventos.

A. El Evento on_click y data
En lugar de crear una función diferente para cada número, usamos una propiedad inteligente llamada data:
```
# Ejemplo de configuración del botón
boton = ft.Container(
    content=ft.Text("1"),
    on_click=agregar_numero,  # Todos llaman a la misma función
    data="1"                  # Cada uno lleva su propio valor
)
```
B. Función de Captura
La función agregar_numero(e) recupera el valor del botón presionado:

Obtiene el valor con e.control.data.

Actualiza la variable de texto del display.

Ejecuta page.update() para refrescar la pantalla (paso crítico en Flet).

C. Función Limpiar
Una función simple que restablece el valor del display a "0".

🚀 Cómo ejecutar el proyecto
Asegúrate de estar en la carpeta del proyecto.

Ejecuta el archivo principal:
```
python main.py
```
