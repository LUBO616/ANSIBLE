# Metodología de investigación y automatización

[← Volver al portafolio](../README.md)

Este documento define la forma de trabajo que estoy desarrollando en el laboratorio. Es una guía de aplicación progresiva; cada proyecto identifica qué etapas ya realizó y cuáles siguen pendientes.

## Un problema antes que una herramienta

Cada práctica comienza con un problema concreto. La descripción debe explicar quién necesita el resultado, qué operación se quiere mejorar y qué queda fuera del alcance.

La solución debe poder evaluarse con criterios observables: un módulo devuelve el resultado esperado, una configuración cumple un valor definido o un servicio responde a una prueba concreta.

## Ciclo de trabajo

| Etapa | Registro mínimo |
|---|---|
| Investigación | Problema, documentación consultada y preguntas abiertas |
| Diseño | Alcance, componentes, dependencias y criterios de aceptación |
| Comprobaciones previas | Estado inicial, conectividad y permisos necesarios |
| Implementación | Código o procedimiento y justificación de las decisiones |
| Validación | Prueba realizada, resultado esperado, resultado obtenido y limitaciones |
| Recuperación | Procedimiento aplicable a los cambios introducidos |
| Documentación | Evidencias revisadas, conclusiones y próximos pasos |

## Qué significa una validación útil

Una prueba debe resolver una duda concreta. Que un contenedor esté en ejecución no demuestra que una aplicación responda; que exista una credencial no demuestra que un Job pueda utilizarla.

En el Proyecto 001 distinguimos entre acceso SSH manual, ejecución del módulo `ping` desde AAP y recopilación de facts con `setup`. Cada resultado responde a una pregunta diferente.

Para automatizaciones que modifican estado, una segunda ejecución puede ayudar a comprobar idempotencia. También deben considerarse fallos relevantes y recuperación. Las pruebas se eligen según el riesgo y el objetivo; no se añaden por cumplir una lista vacía.

## Registro de evidencia

Cada evidencia publicada debe identificar:

- Proyecto, actividad y entorno de ejemplo.
- Procedimiento o comando ejecutado.
- Resultado esperado y observado.
- Fecha de ejecución cuando se disponga de ella.
- Alcance de lo demostrado y lo que sigue pendiente.
- Transformaciones realizadas para anonimizarla.

Las capturas o animaciones recreadas se etiquetan como demostraciones. No se presentan como registros originales.

## Convenciones

La documentación, los nombres de tareas y los comentarios se redactan en español. Los módulos, parámetros y palabras reservadas conservan la sintaxis de Ansible.

Los proyectos se organizan por carpetas con un identificador estable. Los títulos describen su objetivo. Una práctica planificada no se marca como completada por tener una carpeta o un README.

## Datos y permisos

Los ejemplos públicos utilizan identificadores ficticios. Las credenciales se administran mediante los mecanismos previstos por la plataforma y quedan fuera del repositorio.

Se solicita únicamente el acceso necesario para cada actividad. La pertenencia a un grupo de inventario organiza el alcance, pero no sustituye la autorización ni los permisos de acceso.

## Recuperación

Para una consulta de descubrimiento, el procedimiento puede consistir en diagnosticar y repetir una lectura fallida; no hay que inventar un rollback si no se introdujeron cambios.

Para modificar sistemas, la recuperación se diseña antes de ejecutar. Debe señalar qué puede restaurarse, qué información es necesaria y en qué casos se requiere intervención manual.

## Fuentes de referencia

- [Ansible: módulo ping](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html).
- [Ansible: módulo setup](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/setup_module.html).
- [Documentación de Red Hat Ansible Automation Platform 2.7](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7).

[Continuar con el Proyecto 001 →](../02-proyectos/proyecto-001-descubrimiento-linux/README.md)
