# img

Repositorio personal de imágenes y GIFs con un sitio estático al estilo Giphy, listo para GitHub Pages desde la carpeta `/docs` en la rama `main`.

## Cómo funciona

- Subes tus imágenes a la carpeta `img/` en la raíz del repo y haces push a `main`.
- Un **GitHub Action** genera automáticamente la carpeta `docs/` con:
  - `docs/index.html` (con las imágenes embebidas directamente)
  - `docs/img/` (copia de tus imágenes)
  - `docs/CNAME` (para tu dominio personalizado)
- GitHub Pages sirve el sitio desde `/docs` en la rama `main`.
- **No toques la carpeta `docs/` manualmente.** Se regenera automáticamente.

## Subir una nueva imagen

1. Copia tu imagen o GIF a la carpeta `img/` (en la raíz del repo).
2. Haz commit y push a `main`:

   ```bash
   git pull origin main
   cp mi-imagen.gif img/
   git add img/mi-imagen.gif
   git commit -m "add: mi-imagen.gif"
   git push origin main
   ```

3. GitHub Actions regenerará la carpeta `docs/` y hará push del cambio a `main`.
4. Espera unos segundos/minutos a que GitHub Pages actualice el sitio.

> **Importante:** como GitHub Actions modifica `main` con la carpeta `docs/` actualizada, antes de tu próximo cambio local ejecuta:
>
> ```bash
> git pull origin main
> ```

## Activar GitHub Pages

Tu repo ya está configurado para servir desde `/docs` en `main`. Si necesitas verificarlo:

1. Ve a **Settings** → **Pages** en tu repositorio.
2. En **Build and deployment** debe decir:
   - **Source:** Deploy from a branch
   - **Branch:** `main` → `/docs` folder
3. Guarda y espera a que la URL esté disponible.

## Estructura

```
/
├── .github/workflows/build.yml   # GitHub Action que genera docs/
├── img/                          # TUS IMÁGENES (agrega aquí)
├── src/                          # Código fuente del sitio
│   ├── index.html
│   └── build.py
├── docs/                         # Sitio generado (NO editar manualmente)
│   ├── index.html
│   ├── img/
│   └── CNAME
├── CNAME                         # Dominio personalizado
└── README.md
```

## Funciones del sitio

- Galería responsive al estilo Giphy.
- Hover overlay con icono de link.
- Copia el link directo de la imagen al portapapeles con un clic.
- Soporte para imágenes estáticas y GIFs animados.
