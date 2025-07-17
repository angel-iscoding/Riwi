# Ticket de Desarrollo: Página de Login y Registro - Proyecto Riwi

## Descripción

Como desarrollador Frontend, se me ha asignado la tarea de implementar las páginas de **Login** y **Registro** para el proyecto Riwi, siguiendo el diseño proporcionado en Figma:

[Figma - Riwi Login/Register UI](https://www.figma.com/design/lTlTgdLOqovSnhUE3TNKQh/Riwi-Studing?node-id=0-1&t=uYUh0rlcsftqLNrn-1)

El diseño incluye todos los assets, guías de estilo, fuentes y colores necesarios para la correcta implementación visual y de experiencia de usuario.

---

## Requerimientos

### 1. **Responsividad**
- La página debe ser completamente responsive, adaptándose a dispositivos móviles, tablets y escritorio.
- En pantallas pequeñas, el formulario y el logo deben estar centrados y la imagen de fondo debe ocultarse.

### 2. **Formulario de Login**
- Debe recoger los datos de usuario: **email** y **contraseña**.
- Validar que los campos no estén vacíos y que el email tenga formato válido.
- Al enviar, realizar una petición GET a la siguiente URL de Supabase:

  ```
  https://qmcvwjhihwuoepzcprmv.supabase.co/rest/v1/users?email=eq.{email}
  ```

  Usando el siguiente token en los headers:

  ```
  apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtY3Z3amhpaHd1b2VwemNwcm12Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MjcxMzIyNywiZXhwIjoyMDY4Mjg5MjI3fQ.wHepnufDopMGzpVrk86-q4oN8W27rEmuNdmSJyE7Xos
  ```

- Estructura esperada de los datos recibidos:

  ```json
  [
    {
      "id": 1,
      "email": "usuario@ejemplo.com",
      "password": "contraseña123"
    }
  ]
  ```

- Validar que el usuario y contraseña coincidan con los datos devueltos por la base de datos. Si no coinciden, mostrar mensaje de error y no permitir el acceso.

### 3. **Formulario de Registro**
- Recoger los datos: **email**, **contraseña**, **confirmar contraseña**.
- Validar que los campos no estén vacíos, el email tenga formato válido y las contraseñas coincidan.
- Antes de registrar, verificar que el email no esté ya registrado (GET a la misma URL).
- Si el email es nuevo, realizar una petición POST a la misma URL con la siguiente estructura JSON:

  ```json
  {
    "email": "usuario@ejemplo.com",
    "password": "contraseña123"
  }
  ```

- Usar los mismos headers y token que en el login.

---

## Consideraciones Técnicas

- El proyecto debe seguir buenas prácticas de desarrollo: modularidad, legibilidad y comentarios donde sea necesario.
- Los formularios deben manejar los estados de carga y error de forma clara para el usuario.
- El código debe estar preparado para cambiar fácilmente entre Supabase y un backend local (por ejemplo, JSON Server).
- Los assets y estilos deben seguir fielmente el diseño de Figma.

---

## Sugerencias

- Utilizar validaciones nativas de HTML5 y complementarlas con validaciones en JavaScript.
- Centralizar la configuración de endpoints y tokens en un archivo para facilitar cambios futuros.
- Documentar el código y los endpoints utilizados en este README para referencia de otros desarrolladores.

---

## Estructura de Carpetas

```
public/
    icons.jpg...
src/
    script.supabase.js
    script.local.js
    login/
        login.html
        login.css
        login.js
    register/
        register.html
        register.css
        register.js
README.md
```

---

