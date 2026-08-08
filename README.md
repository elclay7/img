# img

Repositorio personal de imágenes y GIFs con un sitio estático al estilo Giphy.

## Cómo funciona

GitHub Pages sirve el sitio desde la carpeta `/docs` en la rama `main`.

## Agregar una imagen

1. Sube tu imagen o GIF a la carpeta `docs/img/`.
2. Abre `docs/index.html` y agrega un objeto al array `IMAGES`:

   ```javascript
   {
     "name": "mi-imagen.gif",
     "url": "img/mi-imagen.gif",
     "type": "image/gif"
   }
   ```

3. Haz commit y push a `main`:

   ```bash
   git add docs/
   git commit -m "add: mi-imagen.gif"
   git push origin main
   ```

4. Espera unos segundos/minutos a que GitHub Pages actualice el sitio.

## Activar GitHub Pages

1. Ve a **Settings** → **Pages** en tu repositorio.
2. En **Build and deployment** selecciona:
   - **Source:** Deploy from a branch
   - **Branch:** `main` → `/docs` folder
3. Guarda y espera a que la URL esté disponible.

## Estructura

```
/
├── docs/              # Sitio que se sirve en GitHub Pages
│   ├── index.html     # Edita este archivo para agregar imágenes
│   ├── img/           # Tus imágenes y GIFs
│   └── CNAME          # Dominio personalizado
├── img/               # Copia de respaldo de tus imágenes (opcional)
├── CNAME              # Dominio personalizado
└── README.md
```

## Funciones del sitio

- Galería responsive al estilo Giphy.
- Hover overlay con icono de link.
- Copia el link directo de la imagen al portapapeles con un clic.
- Soporte para imágenes estáticas y GIFs animados.
