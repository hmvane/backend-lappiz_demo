# Lappiz Demo - Backend (FastAPI)

API REST desarrollada con **FastAPI** para gestionar el registro de interesados en una demo de Lappiz LowCode.

## Descripción

Este servicio permite:

Registrar nuevos interesados (nombre y correo)
Consultar la lista de interesados
Persistir la información en un archivo JSON (simulación de almacenamiento)

La solución fue diseñada con una arquitectura modular para facilitar mantenimiento y escalabilidad.

##  Tecnologías utilizadas

**Python 3**
**FastAPI**
**Uvicorn**
**Pydantic**
**JSON (persistencia en archivo)**

##  Estructura del proyecto

```id="w0d0m7"
app/
├── main.py          # Punto de entrada de la aplicación
├── routes/          # Definición de endpoints
├── schemas/         # Modelos de datos (validación con Pydantic)
├── core/            # Lógica interna (persistencia JSON)
```

### Principios aplicados:

Separación de responsabilidades
Validación de datos con Pydantic
Organización por capas
Código limpio y mantenible

## Instalación y ejecución

### 1. Clonar repositorio

 id="qwe4lm"
git clone https://github.com/hmvane/backend-lappiz_demo.git
cd backend-lappiz_demo

### 2. Crear entorno virtual

python -m venv venv

Activar entorno:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Instalar dependencias

pip install fastapi uvicorn "pydantic[email]"

### 4. Ejecutar servidor

uvicorn app.main:app --reload

Servidor disponible en:

http://localhost:8000


## Endpoints disponibles

### Obtener personas

GET /getPeople

### Registrar persona

POST /addPerson

Body:

{
  "name": "Heidy Vanegas",
  "email": "hvanegas@gmail.com"
}

## Persistencia de datos

Los datos se almacenan en un archivo local:
people.json
Esto permite mantener la información entre ejecuciones sin necesidad de base de datos.


## Validaciones implementadas

Validación de email con `EmailStr`
Prevención de correos duplicados
Tipado estricto con Pydantic

## Documentación automática
FastAPI genera documentación interactiva en:
http://localhost:8000/docs


## Integración con Frontend

Este backend está diseñado para ser consumido por un frontend en Next.js.

Asegúrate de:

Tener habilitado CORS
Ejecutar el backend en `http://localhost:8000`

## Mejoras futuras

Persistencia en base de datos (MySql, SQLServer)
Manejo de concurrencia
Tests automatizados
Autenticación y seguridad

## Autor

Desarrollado por: **Heidy Vanegas Suazo**

## Licencia

Proyecto desarrollado como parte de una prueba técnica.
