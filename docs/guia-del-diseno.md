# Guía del diseño del README

[← Volver al portafolio](../README.md)

## Propósito

La portada presenta un laboratorio de investigación en español con un diseño de terminal: fondo oscuro, jerarquía tipográfica clara y acentos de color. El movimiento destaca la identidad y explica el flujo de trabajo. Los documentos mantienen texto seleccionable y enlaces para explorar el contenido.

## Archivos principales

| Archivo | Función |
|---|---|
| `README.md` | Portada con animaciones y navegación |
| `README-sin-animacion.md` | Mismo contenido con imágenes estáticas |
| `recursos/animaciones/portada.gif` | Cabecera animada |
| `recursos/animaciones/terminal.gif` | Demostración técnica recreada |
| `recursos/animaciones/arquitectura.gif` | Diagrama conceptual animado |
| `recursos/imagenes/` | Alternativas estáticas y recursos SVG |
| `herramientas/generar_recursos.py` | Generador reproducible de los recursos visuales |

Todos los recursos visuales se alojan en el repositorio. No se requieren servicios externos para generar imágenes al abrir la página.

## Compatibilidad y accesibilidad

El README utiliza Markdown, imágenes y una sección desplegable con `details`. No depende de JavaScript ejecutado dentro de GitHub.

Las imágenes tienen texto alternativo. Las animaciones cuentan con equivalentes estáticos y con explicaciones en texto. El enlace a la versión sin animación aparece al principio.

Los diseños con fondo oscuro conservan su propio fondo al mostrarse en otros temas. El contenido principal permanece en Markdown para adaptarse a la interfaz del lector.

La presentación de un README puede variar entre GitHub, editores y previsualizadores. La vista previa incluida con la entrega es una aproximación visual; debe revisarse también en la pestaña de previsualización de GitHub antes de publicar.

## Cómo mantenerlo

1. Actualiza primero los textos y los estados de avance.
2. Repite la misma modificación en `README-sin-animacion.md`.
3. Si cambian textos o estados dentro de una imagen, modifica el generador.
4. Regenera los recursos con Python 3.10 o posterior y Pillow, siguiendo el bloque de abajo.
5. Comprueba legibilidad, enlaces, tamaño de archivo y correspondencia entre imágenes y texto.
6. Revisa el contenido antes de incorporarlo al repositorio remoto.

Desde la raíz del repositorio, en Linux con fuentes DejaVu instaladas:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r herramientas/requisitos-diseno.txt
.venv/bin/python herramientas/generar_recursos.py
```

La generación de las imágenes se realiza localmente. La instalación inicial de Pillow puede requerir conexión a Internet. La opción `--solo-estaticas` regenera únicamente PNG y SVG. El script también puede utilizar las fuentes Arial y Consolas instaladas en Windows, aunque la apariencia tipográfica puede variar.

El generador no necesita acceso al laboratorio ni credenciales de Red Hat. Sus datos son ilustrativos.

## Significado de las animaciones

La terminal es una **recreación didáctica con datos de ejemplo**. No debe describirse como una grabación o una nueva ejecución realizada por AAP.

El diagrama distingue el estado comprobado de desarrollo y lo pendiente en Git y QA. Una línea animada representa una relación conceptual, no tráfico de red medido.

Las tarjetas y etiquetas de estado se mantienen manualmente. No son métricas en vivo ni comprobaciones de integración continua.

## Límites editoriales

- Mantener un proyecto en desarrollo y los demás como planificados.
- No convertir una prueba satisfactoria en una garantía general.
- Publicar evidencias sanitizadas con procedencia y alcance.
- Evitar datos reales de infraestructura, secretos e información de terceros.
- No añadir indicadores de certificación, cobertura o CI sin respaldo verificable.
- Conservar la versión estática como alternativa de lectura.

## Referencias primarias

- [GitHub: sintaxis básica de escritura y formato, incluidas imágenes y enlaces relativos](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- [GitHub: organizar información en secciones desplegables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections).
- [GitHub: trabajar con archivos que no son código e imágenes](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files).
- [GitHub Markup: procesamiento y saneamiento del contenido renderizado](https://github.com/github/markup).
- [Ansible: módulo ping](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html).
- [Ansible: módulo setup](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/setup_module.html).

## Publicación

La entrega prepara los archivos para revisión. No implica que el repositorio remoto ya se haya modificado. Para conservar rutas relativas, los recursos y documentos deben publicarse con la misma estructura de carpetas que el README.
