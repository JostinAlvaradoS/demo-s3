# 🎨 Design System Adyacente — Sofka Technologies

> Transformamos organizaciones con tecnología, agilidad y talento humano

## 1. Identidad de Marca

Empresa colombiana de consultoría y desarrollo de software fundada en 2000, con presencia en Colombia, México, Brasil, España y otros países de Latinoamérica. Especializada en transformación digital, desarrollo ágil, QA, DevOps, arquitectura cloud e inteligencia artificial.

**Personalidad de marca:** innovadora, ágil, confiable, humana, tecnológica, latinoamericana, experta, colaborativa

---

## 2. Paleta de Colores

### Primarios

| Token | Hex | Uso |
|---|---|---|
| Sofka Orange | `#FF6B2B` | Color principal de marca, CTAs primarios, botones de acción, acentos destacados, íconos activos y enlaces hover |
| Sofka Orange Dark | `#E55A1C` | Estado hover y pressed de botones primarios, énfasis en texto sobre fondo claro |

### Secundarios

| Token | Hex | Uso |
|---|---|---|
| Sofka Navy | `#1C1C3C` | Fondo principal de secciones oscuras, navbar, footer, fondos de hero y bloques de alto contraste |
| Sofka Navy Mid | `#2A2A5A` | Fondos de cards en tema oscuro, estados hover de elementos de navegación sobre fondo navy |
| Sofka Blue Accent | `#3B3B7A` | Bordes de cards en tema oscuro, separadores, elementos decorativos secundarios |

### Neutrales

| Token | Hex | Uso |
|---|---|---|
| White | `#FFFFFF` | Fondos de secciones claras, texto sobre fondos oscuros, backgrounds de cards en tema claro |
| Light Gray | `#F5F5F7` | Fondos alternativos de secciones, backgrounds de cards secundarias y áreas de contenido |
| Mid Gray | `#9B9BA8` | Texto secundario, placeholders, subtítulos, metadata y etiquetas de menor jerarquía |
| Dark Gray | `#3D3D4E` | Texto de cuerpo sobre fondos claros, párrafos y descripciones |
| Border Gray | `#E2E2E8` | Bordes de inputs, separadores de secciones, divisores de contenido en tema claro |

### Semánticos

| Token | Hex | Uso |
|---|---|---|
| Success | `#22C55E` | Mensajes de éxito, indicadores de estado positivo, badges de confirmación |
| Warning | `#F59E0B` | Alertas de advertencia, indicadores de atención, estados pendientes |
| Error | `#EF4444` | Mensajes de error, validaciones negativas, estados de fallo en formularios |
| Info | `#3B82F6` | Mensajes informativos, tooltips de ayuda, estados de carga e información neutral |

### Gradientes

| Nombre | CSS | Uso |
|---|---|---|
| Hero Gradient | `linear-gradient(135deg, #1C1C3C 0%, #2A2A5A 50%, #1C1C3C 100%)` | Fondo del hero principal de la homepage y secciones de impacto alto |
| Orange Accent Gradient | `linear-gradient(90deg, #FF6B2B 0%, #FF8C5A 100%)` | Botones primarios con efecto degradado, banners de CTA y highlights de sección |
| Dark Overlay Gradient | `linear-gradient(180deg, rgba(28,28,60,0) 0%, rgba(28,28,60,0.85) 100%)` | Overlay sobre imágenes de fondo en hero y cards con imagen de fondo |
| Section Transition | `linear-gradient(180deg, #FFFFFF 0%, #F5F5F7 100%)` | Transición visual suave entre secciones de fondo claro en la homepage |

---

## 3. Tipografía

### Familias Tipográficas

- **Poppins** — Fuente principal para headings, subheadings, botones, navegación y etiquetas de UI | Pesos: 400 Regular, 500 Medium, 600 SemiBold, 700 Bold, 800 ExtraBold | Fuente: Google Fonts
- **Poppins** — Fuente de cuerpo de texto, párrafos, descripciones y contenido editorial | Pesos: 400 Regular, 500 Medium | Fuente: Google Fonts
- **monospace (system)** — Fragmentos de código, snippets técnicos en el blog y contenido de developer relations | Pesos: 400 Regular | Fuente: System stack: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas

### Escala Tipográfica

| Token | Tamaño | Line Height | Uso |
|---|---|---|---|
| Display XL | 72px / 4.5rem | 1.1 | Headline principal del hero en desktop, statement de impacto máximo |
| Display LG | 56px / 3.5rem | 1.15 | Títulos de sección principales en desktop, hero en tablet |
| H1 | 48px / 3rem | 1.2 | Títulos de página internas, hero en mobile, encabezados de primer nivel |
| H2 | 36px / 2.25rem | 1.25 | Títulos de secciones secundarias, encabezados de bloques de contenido |
| H3 | 28px / 1.75rem | 1.3 | Títulos de cards, subtítulos de servicios, encabezados de artículos del blog |
| H4 | 22px / 1.375rem | 1.35 | Encabezados de subsecciones, nombres de servicios, títulos de testimonios |
| H5 | 18px / 1.125rem | 1.4 | Etiquetas de sección, títulos de items en listas, nombres de equipo |
| Body LG | 18px / 1.125rem | 1.6 | Párrafo principal del hero, texto introductorio de secciones clave |
| Body MD | 16px / 1rem | 1.65 | Texto de cuerpo estándar en párrafos, descripciones de servicios y contenido general |
| Body SM | 14px / 0.875rem | 1.6 | Texto secundario, metadata, fechas de blog, etiquetas de categoría |
| Caption | 12px / 0.75rem | 1.5 | Pie de foto, disclaimers, notas al pie, texto legal |
| Button LG | 16px / 1rem | 1.25 | Texto de botones primarios y secundarios de tamaño grande |
| Button MD | 14px / 0.875rem | 1.25 | Texto de botones de tamaño estándar y chips |
| Overline | 12px / 0.75rem | 1.4 | Etiquetas sobre títulos de sección (ej: 'NUESTROS SERVICIOS'), todo en mayúsculas con letter-spacing amplio |

---

## 4. Espaciado

**Unidad base:** 4px (base-4 system compatible con Tailwind CSS)

| Token | Valor | Uso |
|---|---|---|
| space-1 | 4px | Separación mínima entre elementos inline, padding de badges y chips |
| space-2 | 8px | Padding interno de elementos pequeños, gap entre icono y texto en botones |
| space-3 | 12px | Padding de inputs y selects, separación entre items de lista |
| space-4 | 16px | Padding base de cards, espaciado entre elementos de navegación |
| space-5 | 20px | Padding de botones, separación entre campos de formulario |
| space-6 | 24px | Padding de cards estándar, gap entre columnas de grid en mobile |
| space-8 | 32px | Margen entre secciones pequeñas, padding horizontal de containers en mobile |
| space-10 | 40px | Padding vertical de secciones compactas, separación entre grupos de contenido |
| space-12 | 48px | Padding de secciones medianas, separación entre cards en grid |
| space-16 | 64px | Padding vertical estándar de secciones en tablet y desktop |
| space-20 | 80px | Padding de secciones de alto impacto, separación mayor entre bloques |
| space-24 | 96px | Padding vertical de hero y secciones premium en desktop |
| space-32 | 128px | Padding del hero principal en desktop, secciones de máximo espaciado |

---

## 5. Componentes UI

### Primary Button

Botón de acción principal con fondo naranja Sofka Orange (#FF6B2B), texto blanco en Poppins SemiBold, bordes redondeados. Usado para CTAs principales como 'Contáctanos', 'Conoce más'.

- **Variantes:** Default, Hover (Orange Dark #E55A1C con sombra), Active, Disabled (opacidad 50%), Large (padding 16px 32px), Medium (padding 12px 24px), con gradiente naranja
- **Props:** size: lg|md|sm, disabled: boolean, loading: boolean, icon: left|right|none, fullWidth: boolean

### Secondary Button

Botón con borde naranja y texto naranja sobre fondo transparente (outlined). Alternativa al botón primario para acciones secundarias. En fondos oscuros puede aparecer con borde blanco.

- **Variantes:** Default, Hover (fondo naranja con texto blanco), Disabled, sobre fondo claro, sobre fondo oscuro
- **Props:** size: lg|md|sm, disabled: boolean, icon: left|right|none, theme: light|dark

### Navigation Bar

Barra de navegación superior con fondo navy oscuro (#1C1C3C) o transparente sobre hero. Contiene logo Sofka a la izquierda, links de navegación centrados o a la derecha, y CTA button. Se vuelve sticky con fondo sólido al hacer scroll.

- **Variantes:** Transparent (sobre hero), Solid Navy (sticky on scroll), Mobile (hamburger menu), con megamenu dropdown
- **Props:** sticky: boolean, theme: transparent|solid, mobileOpen: boolean

### Hero Section

Sección principal de la homepage con fondo gradient navy oscuro, titular Display XL en blanco, subtítulo Body LG en gris claro, y botones CTA. Puede incluir imagen o ilustración a la derecha en layout de dos columnas.

- **Variantes:** Full-width con imagen de fondo, Split layout (texto + imagen), Solo texto centrado, con video de fondo
- **Props:** layout: full|split|centered, hasVideo: boolean, hasImage: boolean, ctaCount: 1|2

### Service Card

Card de servicio con fondo blanco o navy, ícono de servicio en la parte superior, título H3, descripción Body MD, y link 'Saber más' en naranja. Bordes redondeados (8-12px), sombra sutil, efecto hover con elevación.

- **Variantes:** Light theme, Dark theme (fondo navy), con imagen, solo icono, featured (borde naranja)
- **Props:** theme: light|dark, hasImage: boolean, icon: string, featured: boolean

### Statistics Counter

Bloque de estadísticas con número grande animado, etiqueta descriptiva y posible ícono. Usados en secciones de impacto para mostrar años de experiencia, clientes, colaboradores y países.

- **Variantes:** Sobre fondo oscuro con número en naranja, sobre fondo claro, horizontal, vertical, con icono
- **Props:** value: string, label: string, icon: string, animated: boolean

### Blog Post Card

Card de artículo del blog con imagen de portada, categoría/tag en naranja, título H4, extracto Body SM, fecha y autor. Efecto hover con sombra y ligero scale.

- **Variantes:** Horizontal (featured), Vertical (grid), Compacto (lista), con video thumbnail
- **Props:** layout: horizontal|vertical|compact, hasImage: boolean, category: string

### Team Member Card

Card de miembro del equipo con foto circular o cuadrada, nombre H4, cargo Body SM en naranja, y links a redes sociales. Usado en secciones de equipo y liderazgo.

- **Variantes:** Con foto, sin foto (avatar placeholder), con redes sociales, sin redes
- **Props:** hasPhoto: boolean, socialLinks: array, size: sm|md|lg

### Testimonial Card

Card de testimonio con cita en comillas, nombre del cliente, empresa y cargo. Fondo blanco con borde izquierdo naranja o diseño con foto del cliente. Usado en sección de casos de éxito.

- **Variantes:** Con foto de cliente, sin foto, con logo de empresa, carrusel, grid
- **Props:** hasPhoto: boolean, hasCompanyLogo: boolean, layout: card|featured

### Footer

Pie de página con fondo navy oscuro (#1C1C3C), logo blanco de Sofka, columnas de links de navegación, información de contacto, redes sociales (LinkedIn, Instagram, Twitter, YouTube), y copyright. Layout de 4-5 columnas en desktop.

- **Variantes:** Desktop (multi-columna), Tablet (2 columnas), Mobile (accordion), con newsletter form
- **Props:** showNewsletter: boolean, columns: number

### Input Field

Campo de texto con label flotante o estático, borde gris claro, fondo blanco, esquinas redondeadas (6px). Estado focus con borde naranja (#FF6B2B). Incluye mensaje de error en rojo.

- **Variantes:** Default, Focus (borde naranja), Error (borde rojo + mensaje), Disabled, con icono prefijo/sufijo, textarea
- **Props:** type: text|email|tel|textarea, error: string, disabled: boolean, icon: left|right

### Contact Form

Formulario de contacto con campos de nombre, empresa, email, teléfono, servicio de interés (select) y mensaje (textarea). CTA button primario naranja. Validación inline con mensajes de error.

- **Variantes:** Completo (página de contacto), Compacto (widget), Modal, en sidebar
- **Props:** variant: full|compact|modal, showServiceSelect: boolean

### Tag / Badge

Etiqueta pequeña para categorías de blog, tecnologías, servicios o estados. Fondo con baja opacidad del color de categoría, texto en el mismo color, bordes redondeados completos (pill).

- **Variantes:** Orange (categorías Sofka), Blue (tecnología), Green (disponible), Gray (neutro), Dark (tema oscuro)
- **Props:** color: orange|blue|green|gray, size: sm|md

### Dropdown / Select

Menú desplegable para selección de servicios, países o categorías. Estilizado con borde gris, esquinas redondeadas, icono de chevron en naranja. Panel de opciones con fondo blanco y hover en naranja claro.

- **Variantes:** Default, Open, Disabled, con búsqueda interna, multiselect
- **Props:** searchable: boolean, multi: boolean, disabled: boolean

### Mega Menu

Panel de navegación expandido que aparece al hover sobre items del navbar como 'Servicios' o 'Soluciones'. Contiene ícono, título y descripción de cada sub-servicio organizado en grid de columnas.

- **Variantes:** 2 columnas, 3 columnas, con imagen destacada, con categorías agrupadas
- **Props:** columns: 2|3|4, hasFeaturedImage: boolean

### Accordion

Componente de preguntas frecuentes o contenido expandible. Encabezado con título y ícono + en naranja que rota a x al abrirse. Contenido que se despliega con animación suave.

- **Variantes:** Default (borde inferior), Card style (con fondo), Flush, múltiple open, solo uno abierto
- **Props:** allowMultiple: boolean, defaultOpen: number|null

### Section Divider

Separador visual entre secciones. Puede ser una línea de gradiente naranja-transparente, un wave SVG que crea transición entre secciones de diferente color, o simplemente espacio en blanco.

- **Variantes:** Wave (de dark a light), Wave (de light a dark), Línea gradiente, Angular cut
- **Props:** type: wave|line|angle, fromColor: string, toColor: string

---

## 6. Layout & Grid

**Sistema de Grid:** 12 columnas con gutter de 24px en desktop, 16px en tablet y 16px en mobile. Sistema basado en Tailwind CSS grid con clases grid-cols-12, gap-6 y contenedor centrado.

**Contenedores:** max-width: 1280px con padding horizontal de 16px en mobile, 32px en tablet y 64px en desktop. Algunas secciones de hero y footer son full-width (100vw) con contenido interno contenido en el container estándar.

### Breakpoints

| Nombre | Valor |
|---|---|
| xs | 375px |
| sm | 640px |
| md | 768px |
| lg | 1024px |
| xl | 1280px |
| 2xl | 1536px |

**Patrones de Layout:** Hero full-width con overlay oscuro y contenido centrado o split 50/50, Grid de 3 columnas para cards de servicios en desktop, 2 en tablet, 1 en mobile, Grid de 4 columnas para estadísticas y métricas de impacto, Grid de 3 columnas para cards del blog, 1 featured grande + 2 secundarias, Layout alternado de sección (imagen izquierda + texto derecha, luego inverso) para showcases, Footer en 4-5 columnas en desktop, colapsado en mobile con acordeón, Secciones con fondo alternado (blanco, gris claro, navy) para crear ritmo visual, Sticky navbar con transición de transparente a sólido al hacer scroll, Scroll horizontal en mobile para carruseles de testimonios y logos de clientes

---

## 7. Motion & Animaciones

**Principios:** Movimiento sutil y funcional que no distrae del contenido, Transiciones suaves para cambios de estado de UI (hover, focus, active), Animaciones de entrada de contenido al hacer scroll (fade-in + slide-up), Contadores animados para estadísticas al entrar en viewport, Easing ease-in-out para la mayoría de transiciones, Duración corta (150-300ms) para micro-interacciones de UI, Duración media (400-600ms) para transiciones de sección y modales

| Token | Valor | Uso |
|---|---|---|
| duration-fast | 150ms | Cambios de color en hover de botones, links e inputs |
| duration-base | 250ms | Transiciones de estado de componentes (open/close de dropdowns, focus de inputs) |
| duration-slow | 400ms | Animaciones de entrada de secciones al hacer scroll, apertura de modales |
| duration-slower | 600ms | Animaciones de contadores, transiciones de página y efectos de hero |
| easing-default | cubic-bezier(0.4, 0, 0.2, 1) | Easing estándar para la mayoría de transiciones (equivale a ease-in-out de Tailwind) |
| easing-in | cubic-bezier(0.4, 0, 1, 1) | Elementos que salen del viewport o se ocultan |
| easing-out | cubic-bezier(0, 0, 0.2, 1) | Elementos que entran al viewport o aparecen |
| easing-bounce | cubic-bezier(0.34, 1.56, 0.64, 1) | Micro-interacciones con efecto de rebote sutil en íconos y badges |

---

## 8. Iconografía

- **Estilo:** Iconos de línea (outline) con grosor de trazo de 1.5-2px, esquinas levemente redondeadas, estilo minimalista y geométrico. En contextos de énfasis se usan versiones filled o con fondo circular de color naranja con baja opacidad.
- **Librería:** Heroicons (Tailwind Labs) como biblioteca principal compatible con el stack Next.js + Tailwind. Complementado con íconos personalizados para servicios específicos de Sofka (agile, DevOps, cloud, AI).
- **Tamaños:** 16px (inline, caption), 20px (botones, inputs, navegación), 24px (items de lista, navegación principal), 32px (cards de servicio compactas), 48px (cards de servicio estándar, sección de servicios), 64px (iconos de características, sección de valores), 96px (ilustraciones de hero, secciones vacías)

---

## 9. Imágenes & Media

**Estilo:** Fotografía profesional de personas trabajando en entornos tecnológicos modernos, colaboración en equipo y espacios de oficina contemporáneos. Tratamiento de color con ligero tono cálido o overlay de marca. Ilustraciones vectoriales para conceptos abstractos de tecnología (cloud, AI, agile). Imágenes con diversidad étnica y de género representando el equipo latinoamericano.

- Fotografías de alta resolución con personas reales del equipo Sofka o representativas
- Overlay de color navy semi-transparente sobre imágenes de fondo para garantizar legibilidad del texto
- Ilustraciones vectoriales flat/semi-flat para conceptos de servicios y tecnología
- Aspect ratio 16:9 para imágenes de blog y hero, 1:1 para fotos de equipo y testimonios
- Logos de clientes en escala de grises sobre fondo claro o blanco sobre fondo oscuro
- Evitar imágenes de stock genéricas y preferir fotografías originales del equipo
- Iconos de tecnología y logos de partners en sus colores originales con fondo neutro
- Uso de gradiente naranja-navy como reemplazo creativo cuando no hay imagen disponible

---

## 10. Accesibilidad

**Estándar:** WCAG 2.1 Nivel AA como referencia de cumplimiento. Contraste mínimo 4.5:1 para texto normal y 3:1 para texto grande. El naranja #FF6B2B sobre navy #1C1C3C y blanco sobre navy cumplen ratios de contraste adecuados.

- Contraste de color: texto blanco sobre navy #1C1C3C cumple ratio 12.6:1 (AAA)
- Contraste de color: texto oscuro #3D3D4E sobre blanco #FFFFFF cumple ratio 8.9:1 (AAA)
- Navegación por teclado con focus visible usando outline naranja (#FF6B2B) de 2px
- Atributos aria-label en iconos decorativos y botones sin texto descriptivo visible
- Alt text descriptivo en todas las imágenes de contenido
- Tamaño mínimo de área táctil de 44x44px para elementos interactivos en mobile
- Formularios con labels explícitos asociados mediante for/id, no solo placeholder
- Estructura semántica con HTML5 landmarks (header, nav, main, section, footer)
- Soporte para preferencia de movimiento reducido (prefers-reduced-motion) desactivando animaciones
- Videos con subtítulos y transcripciones disponibles
- Links de salto al contenido principal (skip-to-content) para navegación por teclado

---

## 11. Patrones de Diseño

### Hero CTA Pattern

Sección hero con headline grande, subtítulo explicativo y 1-2 botones de llamada a la acción (primario naranja + secundario outlined). Fondo navy con gradiente o imagen con overlay.

**Uso:** Página principal, páginas de servicio, landing pages de campañas

### Feature Grid

Grid de 3-4 columnas con cards de características o servicios, cada una con ícono, título y descripción corta. Puede alternar entre tema claro y oscuro según el contexto de la sección.

**Uso:** Sección de servicios en homepage, páginas de servicio, sección de beneficios

### Social Proof Strip

Franja con logos de clientes o partners en escala de grises sobre fondo claro, con scroll automático o estático. Acompañada de texto como 'Empresas que confían en nosotros'.

**Uso:** Bajo el hero de homepage, páginas de servicios, landing pages

### Stats Impact Section

Sección con fondo navy oscuro mostrando 4 métricas clave (años de experiencia, colaboradores, clientes, países) con números grandes animados en blanco o naranja.

**Uso:** Sección de 'Por qué Sofka' en homepage y página About

### Alternating Content Sections

Patrón de secciones que alternan el layout imagen-texto y texto-imagen, con fondo alternado blanco/gris claro. Cada sección tiene un overline, H2, párrafo y CTA link.

**Uso:** Páginas de servicio, página About, secciones de metodología

### Blog Grid with Featured

Grid de artículos del blog con un post destacado grande en la parte superior o izquierda, seguido de un grid de 3 columnas con posts secundarios. Incluye filtros de categoría.

**Uso:** Página principal del blog, sección de recursos en homepage

### Testimonials Carousel

Carrusel de testimonios de clientes con foto, nombre, empresa y cita. Navegación con dots y flechas. Auto-play con pausa en hover. Fondo navy o blanco según la sección.

**Uso:** Sección de casos de éxito en homepage, páginas de servicio

### Contact CTA Banner

Banner de llamada a la acción antes del footer con fondo naranja o navy, texto en blanco invitando a contactar, y botón de acción prominente. Diseño centrado y de alto contraste.

**Uso:** Final de páginas de servicios, blog posts, página About

### Newsletter Signup

Componente de suscripción al newsletter con input de email y botón naranja. Puede estar en el footer, como sección dedicada o como modal de exit-intent.

**Uso:** Footer, sección de blog, modales de captación

### Accordion FAQ

Sección de preguntas frecuentes con acordeones que se expanden al hacer clic. Ícono + en naranja que rota. Organizado por categorías con tabs o en lista única.

**Uso:** Páginas de servicio, landing pages, página de precios


---

*Generado automáticamente por Design System Extractor — 8/4/2026*