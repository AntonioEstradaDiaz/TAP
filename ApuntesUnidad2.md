# Unidad 2: Componentes y Librerías

## 2.1 Definición Conceptual

En el desarrollo de software, la modularidad permite construir sistemas escalables, mantenibles y reutilizables. Este enfoque divide el sistema en partes independientes que facilitan su comprensión y evolución.

### Componentes

Los componentes son unidades modulares que encapsulan funcionalidades o datos específicos dentro del sistema.

* Exponen una interfaz pública bien definida.
* Ocultan los detalles de implementación (principio de encapsulamiento).
* Favorecen la reutilización de código.

**Tipos de componentes:**

* **Visuales:** Botones, tarjetas, formularios, interfaces gráficas.
* **No visuales:** Clases de lógica de negocio, controladores, gestores de estado.

---

### Librerías (Bibliotecas)

Las librerías son colecciones de código preescrito que permiten realizar tareas específicas sin necesidad de implementarlas desde cero.

* Se utilizan bajo demanda mediante importaciones.
* Reducen el tiempo de desarrollo.
* Mejoran la calidad del software al reutilizar soluciones probadas.

Ejemplos:

* Cálculos matemáticos
* Generación de números aleatorios
* Manejo de tiempo

---

### Paquetes

Un paquete es una estructura jerárquica de directorios que organiza módulos dentro de un proyecto.

* Agrupan archivos `.py`.
* Facilitan la organización del código.
* En Python, se identifican mediante un archivo `__init__.py`.

---

## 2.2 Uso de Librerías Proporcionadas por el Lenguaje

### Importación de Módulos

Python ofrece una biblioteca estándar robusta, además de permitir el uso de librerías de terceros.

```python
import flet as ft
import random
import time
```

**Descripción:**

* `flet`: Librería externa para desarrollo de interfaces gráficas.
* `random`: Generación de valores aleatorios.
* `time`: Manejo del tiempo y pausas en ejecución.

---

### Aplicación Práctica en Lógica de Juegos

En el proyecto **"Cyber RPS" (Piedra, Papel o Tijera)**, estas librerías controlan la lógica del juego.

```python
def jugar(eleccion_jugador, opciones):
    eleccion_cpu = random.choice(list(opciones.keys()))
    time.sleep(0.4)
    return eleccion_cpu
```

#### Explicación

* `random.choice(...)`: Selecciona una opción aleatoria simulando la decisión de la CPU.
* `time.sleep(0.4)`: Introduce una pausa de 400 ms para mejorar la experiencia del usuario.

---

## 2.3 Creación de Componentes Definidos por el Usuario

Para evitar la repetición de código, se emplea el principio **DRY (Don't Repeat Yourself)** junto con Programación Orientada a Objetos.

---

### Componentes No Visuales (Modelos de Datos)

```python
from dataclasses import dataclass
import flet as ft

@dataclass
class Usuario:
    nombre: str
    rol: str
    color: str = ft.Colors.BLUE
```

#### Explicación

* `@dataclass`: Automatiza la creación del constructor (`__init__`).
* Define estructuras de datos claras y reutilizables.
* Reduce código repetitivo.

---

### Componentes Visuales (Custom Widgets)

```python
class TarjetaPerfil(ft.Container):
    def __init__(self, usuario: Usuario):
        super().__init__()
        self.usuario = usuario
        
        self.content = ft.Column(
            controls=[
                ft.Text(usuario.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(usuario.rol, italic=True),
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )
        self.border = ft.border.all(2, usuario.color)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    def saludar(self, e):
        print(f"Interactuando con {self.usuario.nombre}")
```

#### Explicación

* `super().__init__()`: Inicializa el contenedor base.
* `self.content`: Define la estructura interna del componente.
* `saludar()`: Maneja eventos dentro del componente.

---

### Componente Visual Complejo: Gráficas de Progreso

```python
def crear_barra_grafica(etiqueta, peso_actual, meta, color_barra):
    ancho_max = 350
    ancho_progreso = (peso_actual / meta) * ancho_max
    
    return ft.Column([
        ft.Row([
            ft.Text(etiqueta, color="white", weight="bold", size=13),
            ft.Text(f"{peso_actual} / {meta} kg", color=color_barra, weight="bold", size=13)
        ], alignment="spaceBetween", width=ancho_max),
        
        ft.Stack([
            ft.Container(width=ancho_max, height=12, bgcolor="#0f172a", border_radius=6),
            ft.Container(width=ancho_progreso, height=12, bgcolor=color_barra, border_radius=6)
        ])
    ], spacing=5)
```

#### Explicación

* **Proporción:** Calcula el avance relativo respecto a la meta.
* **Stack:** Permite superponer elementos para crear efectos visuales.
* Simula una barra de progreso dinámica.

---

## 2.4 Creación y Uso de Paquetes/Librerías

### Modularización del Proyecto

Separar componentes en archivos mejora la escalabilidad del sistema.

---

### 1. Módulo (`ui_components.py`)

```python
import flet as ft

class ProductCard(ft.Container):
    def __init__(self, id, nombre, precio, imagen_path, on_add_cart):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.precio = precio
```

---

### 2. Uso en archivo principal (`main.py`)

```python
import flet as ft
from ui_components import ProductCard

def main(page: ft.Page):
    tarjeta = ProductCard(
        id=1,
        nombre="Laptop Pro",
        precio=25000,
        imagen_path="assets/laptop.png",
        on_add_cart=manejar_carrito
    )
    page.add(tarjeta)

ft.app(target=main)
```

#### Explicación

* Permite importar clases personalizadas.
* Mejora la organización del código.
* Facilita mantenimiento y escalabilidad.

---

## 5. Distribución Móvil: Generación de APK en Flet

### Concepto de Empaquetado

Flet utiliza Flutter para convertir aplicaciones Python en ejecutables móviles.

---

### Comando de Compilación

```bash
flet build apk
```

---

### Proceso de Construcción

1. **Análisis:** Se identifican dependencias desde `main.py`.
2. **Integración de recursos:** Se incluyen imágenes, fuentes y archivos estáticos.
3. **Compilación:** Uso del SDK de Flutter/Android.
4. **Salida:** Archivo `.apk` en `build/apk`.

---

## Bibliografía

* Flet. (2024). *Flet Documentation: Creating User Controls*.
  https://flet.dev/docs/guides/python/user-controls

* Python Software Foundation. (2024). *The Python Standard Library*.
  https://docs.python.org/3/library/

* Sommerville, I. (2015). *Software Engineering* (10th ed.). Pearson.

* Van Rossum, G., Warsaw, B., & Coghlan, N. (2001). *PEP 8 – Style Guide for Python Code*.
  https://peps.python.org/pep-0008/
