# img

Repositorio personal de imágenes y GIFs.

Hecho solo con **HTML y CSS**. No usa JavaScript.

## Agregar una imagen

1. Sube tu imagen o GIF a la carpeta `docs/img/`.
2. Abre `docs/index.html` y copia una tarjeta existente (`<div class="card">...</div>`).
3. Cambia el `src`, el `href` del link y el texto del nombre por los de tu nueva imagen.

## Estructura

```
├── docs/              # Sitio que se sirve en GitHub Pages
│   ├── index.html     # Edita este archivo para agregar imágenes
│   ├── img/           # Tus imágenes y GIFs
│   └── CNAME          # Dominio personalizado
└── README.md
```

## Funciones del sitio

- Galería responsive al estilo Giphy.
- Hover overlay con icono de link.
- Al hacer clic en el icono se abre la imagen para copiar su URL.
- Soporte para imágenes estáticas y GIFs animados.
