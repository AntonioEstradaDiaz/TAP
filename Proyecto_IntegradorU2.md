# Catálogo de Productos con Carrito en Flet

## 1. Descripción General

Este programa implementa una aplicación tipo catálogo de productos con carrito de compras utilizando la librería `Flet`.

Se estructura en tres partes principales:

- Componente reutilizable (`ProductCard`)
- Lógica del carrito
- Interfaz gráfica principal

---

## 2. Componente Reutilizable: `ProductCard`

### Definición

Se define una clase `ProductCard` que hereda de `ft.Container`, representando una tarjeta de producto.

### Constructor

```python
def __init__(self, id, nombre, descripcion, precio, imagen_path, on_add_cart):
```

#### Parámetros

- `id`: Identificador del producto
- `nombre`: Nombre del producto
- `descripcion`: Descripción breve
- `precio`: Precio del producto
- `imagen_path`: Ruta de la imagen
- `on_add_cart`: Función callback para agregar al carrito

### Estado Local

```python
self.es_favorito = False
```

Controla si el producto está marcado como favorito.

---

### Controles Interactivos

#### Botón de favorito

```python
self.btn_favorito = ft.IconButton(...)
```

- Alterna entre iconos:
  - `FAVORITE_BORDER`
  - `FAVORITE`
- Llama a `toggle_favorito`

#### Botón de carrito

```python
self.btn_carrito = ft.Button(...)
```

- Ejecuta `agregar_carrito`

---

### Estructura Visual

La tarjeta contiene:

1. Imagen del producto  
2. Nombre  
3. Descripción  
4. Precio  
5. Botones de acción  

Se organiza con:

```python
ft.Column([...])
```

---

### Métodos

#### `toggle_favorito`

```python
def toggle_favorito(self, e):
```

- Cambia el estado `es_favorito`
- Actualiza el icono dinámicamente

---

#### `agregar_carrito`

```python
def agregar_carrito(self, e):
```

- Ejecuta el callback `on_add_cart`
- Muestra un `SnackBar` como retroalimentación visual

---

## 3. Función Principal: `main(page: ft.Page)`

### Configuración Inicial

```python
page.title = "TechStore - Catálogo"
page.theme_mode = ft.ThemeMode.LIGHT
page.bgcolor = ft.Colors.GREY_50
```

- Define tema, colores y comportamiento de scroll

---

## 4. Lógica del Carrito

### Estructura de Datos

```python
articulos_carrito = []
```

Lista que almacena los productos agregados.

---

### Función `update_cart_badge`

Responsabilidades:

- Actualizar contador del carrito  
- Renderizar lista de productos en el diálogo  
- Calcular total  
- Habilitar/deshabilitar botón de pago  

---

### Función `handle_add_cart`

```python
def handle_add_cart(id_prod, nombre, precio):
```

- Agrega un producto al carrito  
- Llama a `update_cart_badge`  

---

## 5. Diálogo de Carrito

### Componentes

- `listado_carrito`: Lista de productos  
- `dialog_carrito`: Ventana modal (`AlertDialog`)  
- `btn_pagar`: Botón de pago  

---

### Funciones Asociadas

#### `abrir_carrito`

- Muestra el diálogo  
- Actualiza contenido  

#### `cerrar_carrito`

- Cierra el diálogo  

#### `procesar_pago`

- Vacía el carrito  
- Muestra confirmación con `SnackBar`  

---

## 6. Barra de Navegación (AppBar)

```python
page.appbar = ft.AppBar(...)
```

Incluye:

- Ícono principal  
- Título "TechStore"  
- Botón de carrito con contador dinámico  

---

## 7. Modelo de Datos

Lista de productos:

```python
productos = [
    {"id": 1, "nombre": "Laptop Pro 15\"", "desc": "Potente equipo para desarrollo y diseño.", "precio": 25000, "img": "laptop.png"},
    {"id": 2, "nombre": "Smartphone Z", "desc": "Pantalla OLED, Cámara de 108MP.", "precio": 12000, "img": "phone.png"},
    {"id": 3, "nombre": "Audífonos ANC", "desc": "Cancelación de ruido activa. Batería 30h.", "precio": 3500, "img": "headphones.png"},
    {"id": 4, "nombre": "Monitor 4K UHD", "desc": "32 pulgadas IPS, HDR10, colores precisos.", "precio": 8000, "img": "monitor.png"},
    {"id": 5, "nombre": "Teclado Mecánico", "desc": "RGB personalizable, Switch Blue Táctil.", "precio": 1500, "img": "keyboard.png"},
    {"id": 6, "nombre": "Mouse Gamer", "desc": "16000 DPI con botones programables.", "precio": 900, "img": "mouse.png"},
]
```

Cada producto contiene:

- id  
- nombre  
- descripción  
- precio  
- imagen  

---

## 8. Interfaz Principal

### Catálogo Responsivo

```python
catalogo_grid = ft.ResponsiveRow(...)
```

- Usa `ResponsiveRow` para adaptarse a distintos tamaños de pantalla  
- Cada producto se renderiza como `ProductCard`  

---

### Distribución

Columnas según tamaño:

- sm: 12  
- md: 6  
- lg: 4  
- xl: 3  

---

## 9. Renderizado Final

```python
page.add(...)
```

Se agregan:

- Título  
- Grid de productos  

---

## 10. Ejecución

```python
ft.run(main, assets_dir="assets")
```

- Define la carpeta `assets` para imágenes  
- Ejecuta la aplicación  

---

## 11. Conceptos Clave Aplicados

- Programación orientada a objetos (POO)  
- Componentes reutilizables  
- Manejo de estado  
- Callbacks (eventos)  
- Diseño responsivo  
- Separación de lógica y UI  
