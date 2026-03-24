> **Especificación de requisitos de software**

#### Proyecto: Gestión de lockers mediante datos biométricos SHD {#proyecto-gestión-de-lockers-mediante-datos-biométricos-shd .unnumbered}

##### Revisión \[99.99\] {#revisión-99.99 .unnumbered}

![](./image1.png){width="0.9582338145231846in"
height="0.4399245406824147in"}\[Mes de año\]

> **Instrucciones para el uso de este formato**
>
> Este formato es una plantilla tipo para documentos de requisitos del
> software. Está basado y es conforme con el estándar IEEE Std 830-1998.
>
> Las secciones que no se consideren aplicables al sistema descrito
> podrán de forma justificada indicarse como no aplicables (NA).
>
> Notas:
>
> Los textos en color azul son indicaciones que deben eliminarse y, en
> su caso, sustituirse por los contenidos descritos en cada apartado.
>
> Los textos entre corchetes del tipo "\[Inserte aquí el texto\]"
> permiten la inclusión directa de texto con el color y estilo adecuado
> a la sección, al pulsar sobre ellos con el puntero del ratón.
>
> Los títulos y subtítulos de cada apartado están definidos como estilos
> de MS Word, de forma que su numeración consecutiva se genera
> automáticamente según se trate de estilos "Titulo1, Titulo2 y
> Titulo3".
>
> La sangría de los textos dentro de cada apartado se genera
> automáticamente al pulsar Intro al final de la línea de título.
> (Estilos Normal indentado1, Normal indentado 2 y Normal indentado 3).
>
> El índice del documento es una tabla de contenido que MS Word
> actualiza tomando como criterio los títulos del documento.
>
> Una vez terminada su redacción debe indicarse a Word que actualice
> todo su contenido para reflejar el contenido definitivo.
>
> De la plantilla de formato del documento © & Coloriuris
> [http://www.qualitatis.org](http://www.qualitatis.org/)
>
> .

# Ficha del documento {#ficha-del-documento .unnumbered}

+--------+-------+------------------------+--------------------------+
| > **F  | > **  | > **Autor**            | > **Verificado dep.      |
| echa** | Revis |                        | > calidad.**             |
|        | ión** |                        |                          |
+========+=======+========================+==========================+
| > \[F  | > \[  | > \[Descripcion\]      | > \[Firma o sello\]      |
| echa\] | Rev\] |                        |                          |
+--------+-------+------------------------+--------------------------+

###### Documento validado por las partes en fecha: \[Fecha\] {#documento-validado-por-las-partes-en-fecha-fecha .unnumbered}

+-----------------------------------+----------------------------------+
| > Por el cliente                  | > Por la empresa suministradora  |
+===================================+==================================+
|                                   |                                  |
+-----------------------------------+----------------------------------+
| > Fdo. D./ Dña \[Nombre\]         | > Fdo. D./Dña \[Nombre\]         |
+-----------------------------------+----------------------------------+

# Contenido {#contenido .unnumbered}

#  {#section .unnumbered}

[Ficha del documento [2](#ficha-del-documento)](#ficha-del-documento)

[Contenido [4](#contenido)](#contenido)

[1 Introducción [5](#introducción)](#introducción)

[1.1 Propósito [5](#propósito)](#propósito)

[1.2 Alcance [5](#alcance)](#alcance)

[1.3 Personal involucrado
[6](#personal-involucrado)](#personal-involucrado)

[1.4 Definiciones, acrónimos y abreviaturas
[6](#definiciones-acrónimos-y-abreviaturas)](#definiciones-acrónimos-y-abreviaturas)

[1.5 Referencias [7](#referencias)](#referencias)

[1.6 Resumen [7](#resumen)](#resumen)

[2 Descripción general [8](#descripción-general)](#descripción-general)

[2.1 Perspectiva del producto
[9](#perspectiva-del-producto)](#perspectiva-del-producto)

[2.2 Funcionalidad del producto
[9](#funcionalidad-del-producto)](#funcionalidad-del-producto)

[2.3 Características de los usuarios
[9](#características-de-los-usuarios)](#características-de-los-usuarios)

[2.4 Restricciones [9](#restricciones)](#restricciones)

[2.5 Suposiciones y dependencias
[9](#suposiciones-y-dependencias)](#suposiciones-y-dependencias)

[2.6 Evolución previsible del sistema
[9](#evolución-previsible-del-sistema)](#evolución-previsible-del-sistema)

[3 Requisitos específicos
[9](#requisitos-específicos)](#requisitos-específicos)

[3.1 Requisitos comunes de los interfaces
[9](#requisitos-comunes-de-los-interfaces)](#requisitos-comunes-de-los-interfaces)

[3.1.1 Interfaces de usuario
[9](#interfaces-de-usuario)](#interfaces-de-usuario)

[3.1.2 Interfaces de hardware
[9](#interfaces-de-hardware)](#interfaces-de-hardware)

[3.1.3 Interfaces de software
[9](#interfaces-de-software)](#interfaces-de-software)

[3.1.4 Interfaces de comunicación
[9](#interfaces-de-comunicación)](#interfaces-de-comunicación)

[3.2 Requisitos funcionales
[9](#requisitos-funcionales)](#requisitos-funcionales)

[3.2.1 Requisito funcional 1
[9](#requisito-funcional-1)](#requisito-funcional-1)

[3.2.2 Requisito funcional 2
[9](#requisito-funcional-2)](#requisito-funcional-2)

[3.2.3 Requisito funcional 3
[9](#requisito-funcional-3)](#requisito-funcional-3)

[3.2.4 Requisito funcional n
[9](#requisito-funcional-n)](#requisito-funcional-n)

[3.3 Requisitos no funcionales
[9](#requisitos-no-funcionales)](#requisitos-no-funcionales)

[3.3.1 Requisitos de rendimiento
[9](#requisitos-de-rendimiento)](#requisitos-de-rendimiento)

[3.3.2 Seguridad [9](#seguridad)](#seguridad)

[3.3.3 Fiabilidad [9](#fiabilidad)](#fiabilidad)

[3.3.4 Disponibilidad [9](#disponibilidad)](#disponibilidad)

[3.3.5 Mantenibilidad [9](#mantenibilidad)](#mantenibilidad)

[3.3.6 Portabilidad [9](#portabilidad)](#portabilidad)

[3.4 Otros requisitos [9](#otros-requisitos)](#otros-requisitos)

[4 Apéndices [9](#apéndices)](#apéndices)

# Introducción

> Tenemos que definir de manera detallada los requerimientos funcionales
> y no funcionales para el desarrollo del sistema de gestión de lockers
> inteligentes con autenticación biométrica. Este documento describe el
> comportamiento esperado del sistema, las interacciones con los
> usuarios y las restricciones de diseño que regirán su implementación.
>
> Nuestro sistema propuesto busca optimizar la asignación y liberación
> de lockers en entornos institucionales, reemplazando métodos
> tradicionales basados en llaves y un registro mediante el vigilante
> asignado, esto para tener un enfoque más eficiente y automatizado
> haciendo uso de huella dactilar. Esto nos servirá como guía principal
> para el proyecto, asegurando la calidad y demás partes integradas
> durante todo el ciclo de vida del proyecto.

## Propósito

###### El propósito del documento es establecer una base para el entendimiento de todos los participantes del proyecto y lograr definir de una manera clara y concisa cada requisito a cumplir dentro del proyecto de sistema de gestión de lockers con huella biométrica, a lo largo de este documento se detallarán las funciones y las condiciones de operación que nos asegura el buen funcionamiento de proyecto final {#el-propósito-del-documento-es-establecer-una-base-para-el-entendimiento-de-todos-los-participantes-del-proyecto-y-lograr-definir-de-una-manera-clara-y-concisa-cada-requisito-a-cumplir-dentro-del-proyecto-de-sistema-de-gestión-de-lockers-con-huella-biométrica-a-lo-largo-de-este-documento-se-detallarán-las-funciones-y-las-condiciones-de-operación-que-nos-asegura-el-buen-funcionamiento-de-proyecto-final .unnumbered}

###### Este documento va dirigido a  {#este-documento-va-dirigido-a .unnumbered}

###### Equipo de desarrollo 

###### Equipo de aseguramiento de calidad

###### Gerentes de proyecto

###### Clientes 

###### Personas de soporte y mantenimiento

## Alcance

###### Nuestro proyecto a desarrollar se llama gestión de lockers mediante datos biométricos. Este sistema está compuesto por una interfaz donde el usuario interactúa de una manera sencilla desde un dispositivo con su cuenta vinculada, contiene un módulo de administrador donde se gestionan los datos de las personas registradas, el sistema contara con un lector de huella dactilar para la autenticación de los usuarios {#nuestro-proyecto-a-desarrollar-se-llama-gestión-de-lockers-mediante-datos-biométricos.-este-sistema-está-compuesto-por-una-interfaz-donde-el-usuario-interactúa-de-una-manera-sencilla-desde-un-dispositivo-con-su-cuenta-vinculada-contiene-un-módulo-de-administrador-donde-se-gestionan-los-datos-de-las-personas-registradas-el-sistema-contara-con-un-lector-de-huella-dactilar-para-la-autenticación-de-los-usuarios .unnumbered}

###### Esto se aliena con los requisitos aclarados en la descripción general del sistema a través del cual se establecieron las etapas iniciales del proyecto y en la que se logra identificar estas etapas, donde automatizamos el préstamo de lockers para mejorar la seguridad y reducir los tiempos de espera y lograr llevar un registro de los lockers disponibles, del mismo modo el documento es coherente con los requerimientos solicitados por la universidad donde se llevara a cabo la implementación de este sistema, cumpliendo con el estándar de calidad, usabilidad, confiabilidad y seguridad establecidas para estos entornos institucionales {#esto-se-aliena-con-los-requisitos-aclarados-en-la-descripción-general-del-sistema-a-través-del-cual-se-establecieron-las-etapas-iniciales-del-proyecto-y-en-la-que-se-logra-identificar-estas-etapas-donde-automatizamos-el-préstamo-de-lockers-para-mejorar-la-seguridad-y-reducir-los-tiempos-de-espera-y-lograr-llevar-un-registro-de-los-lockers-disponibles-del-mismo-modo-el-documento-es-coherente-con-los-requerimientos-solicitados-por-la-universidad-donde-se-llevara-a-cabo-la-implementación-de-este-sistema-cumpliendo-con-el-estándar-de-calidad-usabilidad-confiabilidad-y-seguridad-establecidas-para-estos-entornos-institucionales .unnumbered}

###### Además, contará con un perfil de administrador encargado de gestionar usuarios, consultar reportes y supervisar el uso del sistema. {#además-contará-con-un-perfil-de-administrador-encargado-de-gestionar-usuarios-consultar-reportes-y-supervisar-el-uso-del-sistema. .unnumbered}

######   {#section-1 .unnumbered}

######  {#section-2 .unnumbered}

## Personal involucrado

+--------------------+-------------------------------------------------+
| > Nombre           | > \[Estudiante\]                                |
+====================+=================================================+
| > Rol              | > \[Usuario del sistema\]                       |
+--------------------+-------------------------------------------------+
| > Categoría        | > \[Estudiante universitario\]                  |
| > profesional      |                                                 |
+--------------------+-------------------------------------------------+
| >                  | > \[Registrar ingreso y salida mediante         |
|  Responsabilidades | > huella\]                                      |
+--------------------+-------------------------------------------------+
| > Información de   | \[Información registrada en el sistema\]        |
| > contacto         |                                                 |
+--------------------+-------------------------------------------------+
| > Aprobación       | > \[No requiere\]                               |
+--------------------+-------------------------------------------------+

+--------------------+-------------------------------------------------+
| > Nombre           | > \[Administrador\]                             |
+====================+=================================================+
| > Rol              | > \[Administrador de sistema\]                  |
+--------------------+-------------------------------------------------+
| > Categoría        | \[Personal administrativo\]                     |
| > profesional      |                                                 |
+--------------------+-------------------------------------------------+
| >                  | > \[Gestionar usuarios, consultar reportes,     |
|  Responsabilidades | > supervisar el sistema\]                       |
+--------------------+-------------------------------------------------+
| > Información de   | \[usuario-administrador@unilibre.edu.co\]       |
| > contacto         |                                                 |
+--------------------+-------------------------------------------------+
| > Aprobación       | > \[Si\]                                        |
+--------------------+-------------------------------------------------+

+--------------------+-------------------------------------------------+
| > Nombre           | > \[Equipo de desarrollo\]                      |
+====================+=================================================+
| > Rol              | > \[Desarrollador\]                             |
+--------------------+-------------------------------------------------+
| > Categoría        | \[Estudiantes ingeniería de sistemas\]          |
| > profesional      |                                                 |
+--------------------+-------------------------------------------------+
| >                  | > \[Análisis, diseño, implementación y pruebas  |
|  Responsabilidades | > del sistema\]                                 |
+--------------------+-------------------------------------------------+
| > Información de   | \[<lindac-morenog@unilibre.edu.co>,             |
| > contacto         | <lauras-villars@unilibre.edu.co>,               |
|                    | <daniels-cortesb@unilibre.edu.co>,              |
|                    | <angele-puertor@unilibre.edu.co>\]              |
+--------------------+-------------------------------------------------+
| > Aprobación       | > \[No\]                                        |
+--------------------+-------------------------------------------------+

+--------------------+-------------------------------------------------+
| > Nombre           | > \[Técnico de soporte\]                        |
+====================+=================================================+
| > Rol              | > \[Mantenimiento\]                             |
+--------------------+-------------------------------------------------+
| > Categoría        | \[Técnico en sistemas\]                         |
| > profesional      |                                                 |
+--------------------+-------------------------------------------------+
| >                  | > \[Mantenimiento del lector biométrico,        |
|  Responsabilidades | > soporte técnico\]                             |
+--------------------+-------------------------------------------------+
| > Información de   | \[soporte@unilibre.edu.co\]                     |
| > contacto         |                                                 |
+--------------------+-------------------------------------------------+
| > Aprobación       | > \[No\]                                        |
+--------------------+-------------------------------------------------+

+--------------------+-------------------------------------------------+
| > Nombre           | > \[Gerente\]                                   |
+====================+=================================================+
| > Rol              | > \[Gerente del proyecto/Supervisor\]           |
+--------------------+-------------------------------------------------+
| > Categoría        | \[Docente universitario\]                       |
| > profesional      |                                                 |
+--------------------+-------------------------------------------------+
| >                  | > \[Supervisar el desarrollo del proyecto,      |
|  Responsabilidades | > validar entregables, evaluar el cumplimiento  |
|                    | > de requisitos\]                               |
+--------------------+-------------------------------------------------+
| > Información de   | \[alonso-guevarap@unilibre.edu.co\]             |
| > contacto         |                                                 |
+--------------------+-------------------------------------------------+
| > Aprobación       | > \[No\]                                        |
+--------------------+-------------------------------------------------+

## Definiciones, acrónimos y abreviaturas

###### \[Biometría: Método de identificación basado en características físicas propias de una única persona {#biometría-método-de-identificación-basado-en-características-físicas-propias-de-una-única-persona .unnumbered}

###### Huella dactilar: Patrón único del dedo usado para autenticación {#huella-dactilar-patrón-único-del-dedo-usado-para-autenticación .unnumbered}

###### Usuario: Persona que interactúa directamente con el sistema para utilizar sus funcionalidades, sin intervenir en configuraciones {#usuario-persona-que-interactúa-directamente-con-el-sistema-para-utilizar-sus-funcionalidades-sin-intervenir-en-configuraciones .unnumbered}

###### Administrador: Encargado de gestionar el sistema, supervisión de operaciones y control de la información {#administrador-encargado-de-gestionar-el-sistema-supervisión-de-operaciones-y-control-de-la-información .unnumbered}

###### Equipo de desarrollo: Grupo de profesionales responsables del análisis, diseño, implementación y pruebas del sistema, asegurándose de que cumpla con los requisitos establecidos {#equipo-de-desarrollo-grupo-de-profesionales-responsables-del-análisis-diseño-implementación-y-pruebas-del-sistema-asegurándose-de-que-cumpla-con-los-requisitos-establecidos .unnumbered}

###### Técnico de soporte: Persona encargada del mantenimiento y soporte de los usuarios. {#técnico-de-soporte-persona-encargada-del-mantenimiento-y-soporte-de-los-usuarios. .unnumbered}

###### Gerente: Planifica, supervisa y valida el desarrollo del proyecto. {#gerente-planifica-supervisa-y-valida-el-desarrollo-del-proyecto. .unnumbered}

###### SHD: Acrónimo de Sistema de Huella Digital {#shd-acrónimo-de-sistema-de-huella-digital .unnumbered}

######  {#section-3 .unnumbered}

###### \] {#section-4 .unnumbered}

## Referencias

+----------+-----------------+------------------+------+-------------+
| > **Refe | **Titulo**      | > **Ruta**       | > *  | > **Autor** |
| rencia** |                 |                  | *Fec |             |
|          |                 |                  | ha** |             |
+==========+=================+==================+======+=============+
| >        | > \[IEEE 830 -- | > \[[Microsoft   | >    | > \[Alonso  |
|  \[Ref.1 | > Software      | > Word -         | \[24 | > Guevara   |
|          | > Requirements  | > plan           | > de | > Perez\]   |
|          | >               | tilla_formato_ie | > M  |             |
|          | Specification\] | ee830.doc](https | arzo |             |
|          |                 | ://aulasvirtuale | >    |             |
|          |                 | s.unilibre.edu.c |  del |             |
|          |                 | o/pluginfile.php | >    |             |
|          |                 | /1261460/mod_res | 2026 |             |
|          |                 | ource/content/1/ | > \] |             |
|          |                 | plantilla_format |      |             |
|          |                 | o_ieee830.pdf)\] |      |             |
+----------+-----------------+------------------+------+-------------+
|          |                 |                  |      |             |
+----------+-----------------+------------------+------+-------------+

## Resumen

###### \[Este documento está dividido en 4 secciones principales: {#este-documento-está-dividido-en-4-secciones-principales .unnumbered}

###### Introducción: en esta sección se hace una introducción completa a todo el proyecto, teniendo como subtemas el propósito del proyecto y del documento. 

###### El alcance del proyecto que es básicamente un registro de entrada y salida a la biblioteca de la universidad con asignación de locker durante su estancia, así, mismo un sistema de administración y gestión del mismo sistema. 

###### El personal involucrado, sus roles y responsabilidades, los cuales son el usuario, el administrador, el equipo de desarrollo, el técnico de soporte (mantenimiento) y el gerente que en este caso es el docente de la materia. 

###### Las definiciones, acrónimos y abreviaturas qye puedes presentarse confusas o con su propia explicación dentro del documento. 

###### Las referencias donde sacamos información. 

###### Y un resumen del documento completo.

###### Descripción general: Aquí ya se hace una descripción más detallada sobre lo que debe contener el producto final, se divide en subsecciones. 

###### Descripción general: Presenta una visión más detallada del sistema y se divide en varias subsecciones que describen sus características principales. 

-   Perspectiva del producto: Indica desde qué punto se observa el
    sistema y si forma parte de uno mayor, apoyándose en diagramas para
    facilitar su comprensión.

-   Funcionalidad del producto: Describe las funciones principales del
    sistema de forma general, usando un lenguaje claro y entendible para
    cualquier persona.

-   Características de los usuarios: Define los tipos de usuarios que
    interactúan con el sistema, incluyendo su formación, habilidades y
    actividades.

-   Restricciones: Establece las limitaciones y herramientas que se
    utilizarán en el desarrollo del sistema.

-   Suposiciones y dependencias: Considera condiciones asumidas y
    factores externos como el mantenimiento y funcionamiento de
    herramientas físicas y digitales.

-   Evolución previsible del sistema: Analiza posibles mejoras futuras y
    oportunidades de expansión del sistema.

###### Requisitos específicos: Es la sección más extensa del documento, aquí si se descirben de manera detallada las funciones que debe hacer el sistema, requisitos funcionales y no funcionales, requerimientos del cliente, es importante que el nivel de detalle sea suficiente para que los desarrolladores y los testers sean capaces de determinar si el sistema está completo y es integrado. Se divide en subsecciones. 

###### Requisitos comunes de las interfaces, aquí se describen los requisitos de las interfaces de usuario, las interfaces de hardware, las interfaces de software y las interfaces de comunicación.

###### Los requisitos funcionales

###### Los requisitos no fucionales

###### Otros requisitos, que no encajen en ninguna de las subsecciones anteriores

###### Apéndices: aquí hay todo tipo de información relevante pero que no forme parte de las secciones anteriores

# Descripción general

## Perspectiva del producto

> El sistema de gestión de lockers es una herramienta pensada para
> funcionar dentro de una institución como la universidad. Su objetivo
> es reemplazar el uso de llaves por un sistema automático usando huella
> dactilar.
>
> Este sistema se conecta con dispositivos físicos como el lector de
> huellas y los seguros de los lockers. También trabaja con una base de
> datos donde se guarda la información de los usuarios y el estado de
> cada locker.

## Funcionalidad del producto

> El sistema permite administrar el uso de los lockers de forma
> automática usando la huella dactilar, el sitema tiene diferentes
> opciones que hacen diferentes funciones:

-   Registrar usuarios usando la huella.

-   Permitir el acceso a un locker mediante la verificación de la huella
    de un usuario registrado.

-   Asignar automáticamente un locker disponible cuando el usuario hace
    el proceso de ingreso.

-   Liberar el locker cuando el usuario termina de usarlo.

-   Mostrar cuáles lockers están disponibles o ocupados.

-   Permitir al administrador gestionar usuarios (agregar, modificar o
    eliminar).

-   Generar reportes sobre el uso de los lockers.

## Características de los usuarios

##  {#section-5 .unnumbered}

+---------------------+------------------------------------------------+
| > Tipo de usuario   | Estudiante                                     |
+=====================+================================================+
| > Formación         | Estudiante universitario                       |
+---------------------+------------------------------------------------+
| > Habilidades       | Uso básico de dispositivos digitales e         |
|                     | interfaces sencillas.                          |
+---------------------+------------------------------------------------+
| > Actividades       | Registrar su ingreso y salida de la biblioteca |
|                     | mediante huella dactilar para obtener la       |
|                     | asignación de un locker                        |
+---------------------+------------------------------------------------+

##  {#section-6 .unnumbered}

+---------------------+------------------------------------------------+
| > Tipo de usuario   | Administrador                                  |
+=====================+================================================+
| > Formación         | Personal administrativo                        |
+---------------------+------------------------------------------------+
| > Habilidades       | Manejo de sistemas de información y bases de   |
|                     | datos.                                         |
+---------------------+------------------------------------------------+
| > Actividades       | Gestionar los datos de los usuarios, gestionar |
|                     | el uso de lockers, consultas de uso, verificar |
|                     | la disponibilidad de lockers y supervisar el   |
|                     | sistema.                                       |
+---------------------+------------------------------------------------+

## Restricciones

> El sistema será construido utilizando una metodología ágil como Scrum.
> Para el backend se utilizará Python y PhP, dependiendo de los
> requerimientos del proyecto, html se implementará para el frontend.
> MySQL constituirá la base de datos central. El hardware incorporará
> sensores biométricos y controladores de lockers que se comunicarán a
> través del protocolo RS-485. Finalmente, se cumplirán las normativas
> de protección de datos vigentes, asegurando un manejo resguardado de
> la información biométrica.

## Suposiciones y dependencias

###### Para garantizar un funcionamiento óptimo del sistema, algunas acciones son necesarias: 1. Los sensores biométricos junto a sus controladores, siempre estarán disponibles. 2. Se necesitará disponer de una red LAN, que sea cableada y estable 3. Adicional a esto un censo actualizado de los usuarios, esto es crucial para el registro inicial. Si algunas de estas condiciones cambian, va a ser necesario, revisar el proyecto y rediseñar si algo quedase afectado. {#para-garantizar-un-funcionamiento-óptimo-del-sistema-algunas-acciones-son-necesarias-1.-los-sensores-biométricos-junto-a-sus-controladores-siempre-estarán-disponibles.-2.-se-necesitará-disponer-de-una-red-lan-que-sea-cableada-y-estable-3.-adicional-a-esto-un-censo-actualizado-de-los-usuarios-esto-es-crucial-para-el-registro-inicial.-si-algunas-de-estas-condiciones-cambian-va-a-ser-necesario-revisar-el-proyecto-y-rediseñar-si-algo-quedase-afectado. .unnumbered}

## Evolución previsible del sistema

> Como futuras mejoras se podría implementar:
>
> Gestión de acceso, y análisis del uso: Desarrollar un sistema para
> registrar la cantidad de veces que los usuarios ingresan y la
> necesidad de los lockers. Eso facilitara la optimización de los
> recursos, así como, la identificación de patrones de utilización.
>
> Ampliación comercial: Adaptar el sistema para usarlo en empresas y
> organizaciones también. Así no solamente en ámbitos universitarios.
> Que necesiten un registro rápido, seguro, y eficaz, para la
> administración de lockers, y el control de ingreso de personas.

# Requisitos específicos

> Esta es la sección más extensa y más importante del documento.
>
> Debe contener una lista detallada y completa de los requisitos que
> debe cumplir el sistema a desarrollar. El nivel de detalle de los
> requisitos debe ser el suficiente para que el equipo de desarrollo
> pueda diseñar un sistema que satisfaga los requisitos y los encargados
> de las pruebas puedan determinar si éstos se satisfacen.

+---------------------+------------------------------------------------+
| > Tipo de usuario   | > \[Inserte aquí el texto\]                    |
+=====================+================================================+
| > Formación         | > \[Inserte aquí el texto\]                    |
+---------------------+------------------------------------------------+
| > Habilidades       | > \[Inserte aquí el texto\]                    |
+---------------------+------------------------------------------------+
| > Actividades       | > \[Inserte aquí el texto\]                    |
+---------------------+------------------------------------------------+

> Los requisitos se dispondrán en forma de listas numeradas para su
> identificación, seguimiento, trazabilidad y validación (ej. RF 10, RF
> 10.1, RF 10.2,\...).
>
> Para cada requisito debe completarse la siguiente tabla:

+--------------------+-------------------------------------------------+
| > Número de        | > \[Inserte aquí el texto\]                     |
| > requisito        |                                                 |
+====================+=================================================+
| > Nombre de        | > \[Inserte aquí el texto\]                     |
| > requisito        |                                                 |
+--------------------+-------------------------------------------------+
| > Tipo             | > Requisito Restricción                         |
+--------------------+-------------------------------------------------+
| > Fuente del       | > \[Inserte aquí el texto\]                     |
| > requisito        |                                                 |
+--------------------+-------------------------------------------------+
| > Prioridad del    | > Alta/Esencial Media/Deseado Baja/ Opcional    |
| > requisito        |                                                 |
+--------------------+-------------------------------------------------+

> y realizar a continuación la descripción del requisito
>
> La distribución de los párrafos que forman este punto puede diferir
> del propuesto en esta plantilla, si las características del sistema
> aconsejan otra distribución para ofrecer mayor claridad en la
> exposición.

## Requisitos comunes de los interfaces

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto .unnumbered}

> Descripción detallada de todas las entradas y salidas del sistema de
> software.

### Interfaces de usuario

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-1 .unnumbered}

> Describir los requisitos del interfaz de usuario para el producto.
> Esto puede estar en la forma de descripciones del texto o pantallas
> del interfaz. Por ejemplo posiblemente el cliente ha especificado el
> estilo y los colores del producto.
>
> Describa exacto cómo el producto aparecerá a su usuario previsto.

### Interfaces de hardware

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-2 .unnumbered}

> Especificar las características lógicas para cada interfaz entre el
> producto y los componentes de hardware del sistema. Se incluirán
> características de configuración.

### Interfaces de software

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-3 .unnumbered}

> Indicar si hay que integrar el producto con otros productos de
> software. Para cada producto de software debe especificarse lo
> siguiente:

-   *Descripción del producto software utilizado*

-   *Propósito del interfaz*

-   *Definición del interfaz: contiendo y formato*

### Interfaces de comunicación

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-4 .unnumbered}

> Describir los requisitos del interfaces de comunicación si hay
> comunicaciones con otros sistemas y cuales son las protocolos de
> comunicación.

## Requisitos funcionales

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-5 .unnumbered}

> Definición de acciones fundamentales que debe realizar el software al
> recibir información, procesarla y producir resultados.
>
> En ellas se incluye:

-   *Comprobación de validez de las entradas*

-   *Secuencia exacta de operaciones*

-   *Respuesta a situaciones anormales (desbordamientos, comunicaciones,
    recuperación de errores)*

-   *Parámetros*

-   *Generación de salidas*

-   *Relaciones entre entradas y salidas (secuencias de entradas y
    salidas, formulas para la conversión de información)*

-   *Especificación de los requisitos lógicos para la información que
    será almacenada en base de datos (tipo de información, requerido)*

> Las requisitos funcionales pueden ser divididos en sub-secciones.

### Requisito funcional 1

### Requisito funcional 2

### Requisito funcional 3

### Requisito funcional n

## Requisitos no funcionales

### Requisitos de rendimiento

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-6 .unnumbered}

> Especificación de los requisitos relacionados con la carga que se
> espera tenga que soportar el sistema. Por ejemplo, el número de
> terminales, el número esperado de usuarios simultáneamente conectados,
> número de transacciones por segundo que deberá soportar el sistema,
> etc.
>
> Todos estos requisitos deben ser mesurables. Por ejemplo, indicando
> "el 95% de las transacciones deben realizarse en menos de 1 segundo",
> en lugar de "los operadores no deben esperar a que se complete la
> transacción".

### Seguridad

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-7 .unnumbered}

> Especificación de elementos que protegerán al software de accesos,
> usos y sabotajes maliciosos, así como de modificaciones o
> destrucciones maliciosas o accidentales. Los requisitos pueden
> especificar:

-   *Empleo de técnicas criptográficas.*

-   *Registro de ficheros con "logs" de actividad.*

-   *Asignación de determinadas funcionalidades a determinados módulos.*

-   *Restricciones de comunicación entre determinados módulos.*

-   *Comprobaciones de integridad de información crítica.*

### Fiabilidad

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-8 .unnumbered}

> Especificación de los factores de fiabilidad necesaria del sistema.
> Esto se expresa generalmente como el tiempo entre los incidentes
> permisibles, o el total de incidentes permisible.

### Disponibilidad

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-9 .unnumbered}

> Especificación de los factores de disponibilidad final exigidos al
> sistema. Normalmente expresados en % de tiempo en los que el software
> tiene que mostrar disponibilidad.

### Mantenibilidad

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-10 .unnumbered}

> Identificación del tipo de mantenimiento necesario del sistema.
>
> Especificación de quien debe realizar las tareas de mantenimiento, por
> ejemplo usuarios, o un desarrollador.
>
> Especificación de cuando debe realizarse las tareas de mantenimiento.
> Por ejemplo, generación de estadísticas de acceso semanales y
> mensuales.

### Portabilidad

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-11 .unnumbered}

> Especificación de atributos que debe presentar el software para
> facilitar su traslado a otras plataformas u entornos. Pueden
> incluirse:

-   *Porcentaje de componentes dependientes del servidor.*

-   *Porcentaje de código dependiente del servidor.*

-   *Uso de un determinado lenguaje por su portabilidad.*

-   *Uso de un determinado compilador o plataforma de desarrollo.*

-   *Uso de un determinado sistema operativo.*

## Otros requisitos

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-12 .unnumbered}

> Cualquier otro requisito que no encaje en ninguna de las secciones
> anteriores.
>
> Por ejemplo:
>
> Requisitos culturales y políticos Requisitos Legales

# Apéndices

###### \[Inserte aquí el texto\] {#inserte-aquí-el-texto-13 .unnumbered}

> Pueden contener todo tipo de información relevante para la SRS pero
> que, propiamente, no forme parte de la SRS.
