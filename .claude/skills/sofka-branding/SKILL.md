---
name: sofka-branding
description: >
  Sofka Technologies brand identity and design system reference. Use this skill ALWAYS when creating
  any visual asset, presentation (pptx), document (docx), landing page, React component, HTML page,
  SVG diagram, or any other deliverable that must carry Sofka's branding. Trigger whenever the user
  mentions "Sofka" together with design, presentation, slide deck, branding, brand, landing page,
  website, UI component, mockup, poster, banner, social media post, or any visual output. Also
  trigger when the user says "presentación para Sofka", "deck de Sofka", "landing Sofka",
  "componente Sofka", "documento con marca Sofka", or similar. This skill does NOT create
  presentations by itself — it provides the branding rules that other skills (pptx, frontend-design,
  docx) must follow when the output is for Sofka.
---

# Sofka Branding Skill

This skill contains Sofka Technologies' official brand guidelines and web design system.
Read this file first, then consult the appropriate reference file for detailed specs.

## When to Read References

| Context | Reference to read |
|---|---|
| Presentations (pptx), Word docs, print, corporate materials | `references/brand-manual.md` |
| Web components, React, HTML, landing pages, dashboards | `references/web-design-system.md` |
| Both (e.g., a pptx that will also be shown as a web embed) | Read both, prioritize brand-manual for colors/fonts |

## Brand Essence

Sofka is a Colombian technology company (founded 2000) specializing in digital transformation,
agile development, QA, DevOps, cloud architecture, and AI. Present across Latin America and the US.

**Tagline:** "Your technology companion"
**Claim:** "Better happens every day." (variants: "Better digital experiences. Every day.",
"Better human experiences. Every day.", "Better work experiences. Every day.")
**Personality:** innovative, agile, reliable, human, tech-forward, Latin American, expert, collaborative
**Philosophy:** Kaizen — continuous improvement through small, constant daily steps.

## Logo Rules

The logo is the word "sofka" in lowercase bold sans-serif followed by an orange underscore: **sofka_**

1. Use the color version on light or white backgrounds. Use the inverted (white) version on dark backgrounds.
2. Place the logo in a corner with clearspace equal to the height of the underscore symbol on all sides.
3. Minimum size: 72px wide (digital) or 1 inch (print); 20px tall (digital) or 5.5mm (print).
4. When co-branding, separate logos by 2x the underscore height. Partner logo must not exceed Sofka logo height.
5. NEVER: compress/stretch, add shadows/gradients, alter the underscore, place on busy or low-contrast backgrounds.

## Color Systems

There are TWO color contexts. The official brand manual palette is the canonical source of truth.
The web design system adapts some values for screen rendering and accessibility on web.

### Official Brand Palette (presentations, documents, print, corporate)

| Token | Hex | Role |
|---|---|---|
| Sofka.Orange | `#FF7E08` | Primary brand color, accents, CTAs |
| Sofka.Light | `#EFEAE4` | Light backgrounds |
| Sofka.Dark | `#B8A894` | Muted accents, secondary backgrounds |
| Sofka.Blk | `#000000` | Text on light backgrounds |
| Sofka.Wht | `#FFFFFF` | Text on dark backgrounds |

Secondary: Green `#42D36F`, Teal `#06C8C8`, Violet `#9747FF`, Pink `#FE9CAB`

### Web Design System Palette (React, HTML, landing pages, dashboards)

| Token | Hex | Role |
|---|---|---|
| Sofka Orange | `#FF6B2B` | Primary CTA, buttons, accents |
| Sofka Orange Dark | `#E55A1C` | Hover/pressed states |
| Sofka Navy | `#1C1C3C` | Dark backgrounds, navbar, footer |
| Sofka Navy Mid | `#2A2A5A` | Dark cards, hover states |
| White | `#FFFFFF` | Light sections, text on dark |
| Light Gray | `#F5F5F7` | Alternate section backgrounds |
| Dark Gray | `#3D3D4E` | Body text on light |

See `references/web-design-system.md` for full palette including semantic colors and gradients.

## Typography

### For Presentations & Print (Official Brand Manual)

| Role | Family | Weights |
|---|---|---|
| Headlines | **Clash Grotesk** | Regular, Medium, SemiBold |
| Body text | **Inter** | Regular, Bold |

Rules: max 3 font sizes/weights per layout, sentence case for headlines, flush left alignment,
4.5:1 contrast ratio minimum (3:1 for large text).

### For Web (Design System)

| Role | Family | Weights |
|---|---|---|
| Headings, buttons, nav | **Poppins** | 400–800 |
| Body text | **Poppins** | 400, 500 |
| Code snippets | System monospace | 400 |

See `references/web-design-system.md` for the full type scale (Display XL through Caption).

## Grid & Layout

**Brand manual:** Square grid based on logo height. Symbol height = 1.5% of (layout width + height).
Divide internal area into equal-width columns as needed. Clean lines, balance, structure.

**Web:** 12-column grid, 24px gutter desktop, 16px tablet/mobile. Container max-width 1280px.
Breakpoints: xs 375px, sm 640px, md 768px, lg 1024px, xl 1280px, 2xl 1536px.

## Illustrations & Imagery

Illustration style uses simple geometric shapes on a strong grid with mathematically derived
proportions. The Kaizen philosophy inspires abstract illustration and visual metaphors.
The brand's radial "sun" motif (orange dashes radiating from a center) is a signature decorative element.

Photography: professional shots of people in modern tech environments, team collaboration,
warm tones, diversity. Overlay navy semi-transparent on background images for text legibility.
Logos of clients/partners in grayscale on light backgrounds or white on dark.

## Applying This Skill

When creating any Sofka-branded deliverable:

1. **Read this file** to understand the brand rules.
2. **Read the appropriate reference** (`brand-manual.md` for presentations/docs, `web-design-system.md` for web).
3. **If also using another skill** (pptx, docx, frontend-design), read that skill too, but override its default styling with Sofka's brand tokens.
4. **For presentations:** use dark backgrounds (black/navy) with white text and orange accents. Place the sofka_ logo in a corner. Use Clash Grotesk for headlines, Inter for body. Apply the orange underscore motif and the radial sun pattern as decorative elements.
5. **For web:** use the navy-to-light section alternation pattern. Orange for CTAs, navy for hero/footer, white/light-gray for content sections. Poppins throughout. Follow component specs in the design system.
6. **Always:** respect logo clearspace, minimum sizes, and color contrast ratios.
