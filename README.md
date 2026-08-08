# img

Repositorio personal de imágenes y GIFs con un sitio estático al estilo Giphy, listo para GitHub Pages desde la carpeta `/docs` en la rama `main`.

## Cómo funciona

- Subes tus imágenes a la carpeta `img/` en la raíz del repo y haces push a `main`.
- Un **GitHub Action** genera automáticamente la carpeta `docs/` con:
  - `docs/index.html`
  - `docs/images.js` (catálogo)
  - `docs/img/` (copia de tus imágenes)
- GitHub Pages sirve el sitio desde `/docs` en la rama `main`.
- No necesitas ejecutar `build.py` en tu máquina ni tocar la carpeta `docs/`.

## Subir una nueva imagen

1. Copia tu imagen o GIF a la carpeta `img/` (en la raíz del repo).
2. Haz commit y push a `main`:

   ```bash
   git add img/nueva-imagen.gif
   git commit -m "add: nueva imagen"
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

- `index.html` — Plantilla del sitio.
- `build.py` — Script que escanea imágenes y genera `images.js`.
- `img/` — **Agrega tus imágenes aquí.**
- `docs/` — Sitio generado automáticamente por GitHub Actions.
- `.github/workflows/build.yml` — Workflow que genera `docs/` en cada push.

## Funciones del sitio

- Galería responsive al estilo Giphy.
- Buscador por nombre de archivo.
- Hover overlay con icono de link.
- Copia el link directo de la imagen al portapapeles con un clic.
- Soporte para imágenes estáticas y GIFs animados.
