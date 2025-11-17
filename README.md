# 🔧 Módulo Odoo – Gestión de Tareas

Este módulo ha sido desarrollado como parte del **Laboratorio 5 del módulo de Sistemas de Gestión Empresarial**.  
Su objetivo es demostrar la creación, instalación y funcionamiento de un módulo personalizado dentro de Odoo.

---

## 📌 Características del módulo

El módulo **Gestión de Tareas** permite:

- Crear tareas con un nombre.
- Definir la prioridad (0–100).
- Marcar las tareas como realizadas.
- Determinar automáticamente si una tarea es urgente.
- Listar todas las tareas en una vista tipo lista.
- Editar cada tarea mediante un formulario.

---

## 🧠 Modelo de datos (`gestion.tareas`)

El modelo contiene los siguientes campos:

| Campo      | Tipo        | Descripción |
|-----------|-------------|-------------|
| `nombre`   | Char        | Nombre de la tarea. |
| `prioridad` | Integer    | Nivel de prioridad (0 a 100). |
| `realizada` | Boolean    | Indica si la tarea está completada. |
| `urgente`  | Boolean (compute) | Valor calculado dependiendo de la prioridad. |

La urgencia se calcula automáticamente cuando la prioridad es **mayor o igual a 80**.

---

## 🖼️ Vistas

El módulo incluye:

### ✔ Vista Lista (`list`)
Muestra:
- Nombre  
- Prioridad  
- Realizada  
- Urgente  

### ✔ Vista Formulario (`form`)
Permite editar una tarea mostrando todos los campos relevantes.

---

## 📁 Estructura del módulo

