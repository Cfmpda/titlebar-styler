#!/usr/bin/python3
import sys
import os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, Gdk, GLib

MARKER_START = "/* --- TITLEBAR STYLER INICIO --- */"
MARKER_END = "/* --- TITLEBAR STYLER FIM --- */"

STYLES = {
    "macOS (Símbolos no Hover)": {
        "description": "Círculos perfeitos com as cores do macOS. Revela os ícones no hover.",
        "preview_classes": ["macos-close", "macos-min", "macos-max"],
        "css": """window headerbar windowcontrols button,
window headerbar windowcontrols button.image-button,
headerbar windowcontrols button,
headerbar windowcontrols button.image-button {
    border-radius: 9999px;
    min-width: 14px;
    min-height: 14px;
    padding: 0;
    margin: 10px 4px;
    border: 1px solid rgba(0, 0, 0, 0.15);
    box-shadow: none;
    background-clip: padding-box;
}
window headerbar windowcontrols button image,
window headerbar windowcontrols button.image-button image,
headerbar windowcontrols button image,
headerbar windowcontrols button.image-button image {
    min-width: 10px;
    min-height: 10px;
    padding: 0;
    margin: 0;
    -gtk-icon-size: 10px;
    opacity: 0;
    transition: opacity 150ms ease-in-out;
}
window headerbar windowcontrols:hover button image,
headerbar windowcontrols:hover button image,
window headerbar windowcontrols button:hover image,
headerbar windowcontrols button:hover image {
    opacity: 0.85;
}
window headerbar windowcontrols button.close,
headerbar windowcontrols button.close {
    background-color: #ff5f56;
    color: #4d0000;
}
window headerbar windowcontrols button.close:hover,
headerbar windowcontrols button.close:hover {
    background-color: #e0443e;
}
window headerbar windowcontrols button.minimize,
headerbar windowcontrols button.minimize {
    background-color: #ffbd2e;
    color: #995700;
}
window headerbar windowcontrols button.minimize:hover,
headerbar windowcontrols button.minimize:hover {
    background-color: #dea123;
}
window headerbar windowcontrols button.maximize,
headerbar windowcontrols button.maximize {
    background-color: #27c93f;
    color: #006500;
}
window headerbar windowcontrols button.maximize:hover,
headerbar windowcontrols button.maximize:hover {
    background-color: #1aab29;
}"""
    },
    "macOS (Ícones Sempre Visíveis)": {
        "description": "Círculos perfeitos com as cores do macOS e ícones sempre visíveis.",
        "preview_classes": ["macos-close", "macos-min", "macos-max"],
        "css": """window headerbar windowcontrols button,
window headerbar windowcontrols button.image-button,
headerbar windowcontrols button,
headerbar windowcontrols button.image-button {
    border-radius: 9999px;
    min-width: 14px;
    min-height: 14px;
    padding: 0;
    margin: 10px 4px;
    border: 1px solid rgba(0, 0, 0, 0.15);
    box-shadow: none;
    background-clip: padding-box;
}
window headerbar windowcontrols button image,
window headerbar windowcontrols button.image-button image,
headerbar windowcontrols button image,
headerbar windowcontrols button.image-button image {
    min-width: 10px;
    min-height: 10px;
    padding: 0;
    margin: 0;
    -gtk-icon-size: 10px;
    opacity: 0.75;
}
window headerbar windowcontrols button:hover image,
headerbar windowcontrols button:hover image {
    opacity: 1;
}
window headerbar windowcontrols button.close,
headerbar windowcontrols button.close {
    background-color: #ff5f56;
    color: #4d0000;
}
window headerbar windowcontrols button.close:hover,
headerbar windowcontrols button.close:hover {
    background-color: #e0443e;
}
window headerbar windowcontrols button.minimize,
headerbar windowcontrols button.minimize {
    background-color: #ffbd2e;
    color: #995700;
}
window headerbar windowcontrols button.minimize:hover,
headerbar windowcontrols button.minimize:hover {
    background-color: #dea123;
}
window headerbar windowcontrols button.maximize,
headerbar windowcontrols button.maximize {
    background-color: #27c93f;
    color: #006500;
}
window headerbar windowcontrols button.maximize:hover,
headerbar windowcontrols button.maximize:hover {
    background-color: #1aab29;
}"""
    },
    "Minimalista (com Ícones)": {
        "description": "Círculos translúcidos sutis com ícones nítidos e elegantes.",
        "preview_classes": ["minimal-dot", "minimal-dot", "minimal-dot"],
        "css": """window headerbar windowcontrols button,
window headerbar windowcontrols button.image-button,
headerbar windowcontrols button,
headerbar windowcontrols button.image-button {
    border-radius: 9999px;
    min-width: 16px;
    min-height: 16px;
    padding: 0;
    margin: 9px 4px;
    border: none;
    box-shadow: none;
    background-color: alpha(currentColor, 0.08);
    color: alpha(currentColor, 0.75);
}
window headerbar windowcontrols button:hover,
headerbar windowcontrols button:hover {
    background-color: alpha(currentColor, 0.20);
    color: currentColor;
}
window headerbar windowcontrols button image,
window headerbar windowcontrols button.image-button image,
headerbar windowcontrols button image,
headerbar windowcontrols button.image-button image {
    min-width: 10px;
    min-height: 10px;
    padding: 0;
    margin: 0;
    -gtk-icon-size: 10px;
    opacity: 0.85;
}"""
    },
    "Contorno / Outline (Colorido)": {
        "description": "Círculos elegantes com contornos e ícones nas cores de ação.",
        "preview_classes": ["outline-close", "outline-min", "outline-max"],
        "css": """window headerbar windowcontrols button,
window headerbar windowcontrols button.image-button,
headerbar windowcontrols button,
headerbar windowcontrols button.image-button {
    border-radius: 9999px;
    min-width: 16px;
    min-height: 16px;
    padding: 0;
    margin: 9px 4px;
    box-shadow: none;
    background-color: transparent;
}
window headerbar windowcontrols button.close,
headerbar windowcontrols button.close {
    border: 1.5px solid #ff5f56;
    color: #ff5f56;
}
window headerbar windowcontrols button.close:hover,
headerbar windowcontrols button.close:hover {
    background-color: #ff5f56;
    color: #ffffff;
}
window headerbar windowcontrols button.minimize,
headerbar windowcontrols button.minimize {
    border: 1.5px solid #ffbd2e;
    color: #ffbd2e;
}
window headerbar windowcontrols button.minimize:hover,
headerbar windowcontrols button.minimize:hover {
    background-color: #ffbd2e;
    color: #ffffff;
}
window headerbar windowcontrols button.maximize,
headerbar windowcontrols button.maximize {
    border: 1.5px solid #27c93f;
    color: #27c93f;
}
window headerbar windowcontrols button.maximize:hover,
headerbar windowcontrols button.maximize:hover {
    background-color: #27c93f;
    color: #ffffff;
}
window headerbar windowcontrols button image,
window headerbar windowcontrols button.image-button image,
headerbar windowcontrols button image,
headerbar windowcontrols button.image-button image {
    min-width: 10px;
    min-height: 10px;
    padding: 0;
    margin: 0;
    -gtk-icon-size: 10px;
    opacity: 0.9;
}"""
    },
    "Fluent / Moderno": {
        "description": "Estilo moderno retangular arredondado com fecho vermelho no hover.",
        "preview_classes": ["fluent-dot", "fluent-dot", "fluent-dot"],
        "css": """window headerbar windowcontrols button,
window headerbar windowcontrols button.image-button,
headerbar windowcontrols button,
headerbar windowcontrols button.image-button {
    border-radius: 6px;
    min-width: 24px;
    min-height: 20px;
    padding: 0;
    margin: 7px 2px;
    border: none;
    box-shadow: none;
    background-color: transparent;
    color: currentColor;
}
window headerbar windowcontrols button:hover,
headerbar windowcontrols button:hover {
    background-color: alpha(currentColor, 0.12);
}
window headerbar windowcontrols button.close:hover,
headerbar windowcontrols button.close:hover {
    background-color: #e81123;
    color: #ffffff;
}
window headerbar windowcontrols button image,
window headerbar windowcontrols button.image-button image,
headerbar windowcontrols button image,
headerbar windowcontrols button.image-button image {
    min-width: 10px;
    min-height: 10px;
    padding: 0;
    margin: 0;
    -gtk-icon-size: 10px;
    opacity: 0.9;
}"""
    },
    "Minimalista Ghost (Oculto até ao Hover)": {
        "description": "Bolinhas e ícones discretos que apenas se revelam ao passar o cursor.",
        "preview_classes": ["ghost-dot", "ghost-dot", "ghost-dot"],
        "css": """window headerbar windowcontrols button,
window headerbar windowcontrols button.image-button,
headerbar windowcontrols button,
headerbar windowcontrols button.image-button {
    border-radius: 9999px;
    min-width: 14px;
    min-height: 14px;
    padding: 0;
    margin: 10px 4px;
    border: none;
    box-shadow: none;
    background-color: alpha(currentColor, 0.15);
    color: currentColor;
    opacity: 0.25;
    transition: opacity 150ms ease-in-out;
}
window headerbar windowcontrols:hover button,
headerbar windowcontrols:hover button,
window headerbar windowcontrols button:hover,
headerbar windowcontrols button:hover {
    opacity: 1;
    background-color: alpha(currentColor, 0.3);
}
window headerbar windowcontrols button image,
window headerbar windowcontrols button.image-button image,
headerbar windowcontrols button image,
headerbar windowcontrols button.image-button image {
    min-width: 10px;
    min-height: 10px;
    padding: 0;
    margin: 0;
    -gtk-icon-size: 10px;
    opacity: 0;
    transition: opacity 150ms ease-in-out;
}
window headerbar windowcontrols:hover button image,
headerbar windowcontrols:hover button image,
window headerbar windowcontrols button:hover image,
headerbar windowcontrols button:hover image {
    opacity: 0.85;
}"""
    }
}

APP_INTERNAL_CSS = """
.preview-badge {
    padding: 6px 10px;
    background-color: alpha(currentColor, 0.05);
    border-radius: 8px;
    margin-right: 6px;
}
.preview-dot {
    min-width: 12px;
    min-height: 12px;
    border-radius: 9999px;
    margin: 0 2px;
}
.preview-dot.macos-close { background-color: #ff5f56; }
.preview-dot.macos-min { background-color: #ffbd2e; }
.preview-dot.macos-max { background-color: #27c93f; }

.preview-dot.outline-close { border: 1.5px solid #ff5f56; background-color: transparent; }
.preview-dot.outline-min { border: 1.5px solid #ffbd2e; background-color: transparent; }
.preview-dot.outline-max { border: 1.5px solid #27c93f; background-color: transparent; }

.preview-dot.minimal-dot { background-color: alpha(currentColor, 0.4); }
.preview-dot.ghost-dot { background-color: alpha(currentColor, 0.2); }
.preview-dot.fluent-dot { border-radius: 3px; min-width: 14px; min-height: 10px; background-color: alpha(currentColor, 0.3); }
.preview-dot.default-dot { background-color: alpha(currentColor, 0.35); }

/* Live Preview Mock Window */
.preview-window-frame {
    border-radius: 12px;
    background-color: @headerbar_bg_color;
    border: 1px solid alpha(currentColor, 0.15);
    padding: 10px 14px;
    margin-bottom: 6px;
}
.preview-window-title {
    font-weight: bold;
    font-size: 0.9em;
    opacity: 0.85;
}
"""

def rgba_to_hex(rgba):
    r = int(rgba.red * 255)
    g = int(rgba.green * 255)
    b = int(rgba.blue * 255)
    return f"#{r:02x}{g:02x}{b:02x}"

def hex_to_rgba(hex_str):
    rgba = Gdk.RGBA()
    rgba.parse(hex_str)
    return rgba

def adjust_color(hex_str, factor):
    try:
        h = hex_str.lstrip('#')
        if len(h) != 6:
            return hex_str
        r = int(h[0:2], 16)
        g = int(h[2:4], 16)
        b = int(h[4:6], 16)
        r = max(0, min(255, int(r * factor)))
        g = max(0, min(255, int(g * factor)))
        b = max(0, min(255, int(b * factor)))
        return f"#{r:02x}{g:02x}{b:02x}"
    except Exception:
        return hex_str

def generate_css(params, is_preview=False):
    btn_size = params["btn_size"]
    radius = params["radius"]
    icon_size = params["icon_size"]
    spacing = params["spacing"]
    close_bg = params["close_bg"]
    close_fg = params["close_fg"]
    min_bg = params["min_bg"]
    min_fg = params["min_fg"]
    max_bg = params["max_bg"]
    max_fg = params["max_fg"]
    border_enabled = params["border_enabled"]
    border_width = params["border_width"]
    border_color = params["border_color"]
    icon_visibility = params["icon_visibility"]
    hover_effect = params["hover_effect"]

    if hover_effect == "darken":
        close_hover = adjust_color(close_bg, 0.88)
        min_hover = adjust_color(min_bg, 0.88)
        max_hover = adjust_color(max_bg, 0.88)
    elif hover_effect == "lighten":
        close_hover = adjust_color(close_bg, 1.15)
        min_hover = adjust_color(min_bg, 1.15)
        max_hover = adjust_color(max_bg, 1.15)
    else:
        close_hover = close_bg
        min_hover = min_bg
        max_hover = max_bg

    border_css = f"{border_width}px solid {border_color}" if border_enabled else "none"

    if icon_visibility == "hover":
        icon_opacity = "0"
        icon_hover_opacity = "0.85"
    elif icon_visibility == "hidden":
        icon_opacity = "0"
        icon_hover_opacity = "0"
    else:  # always
        icon_opacity = "0.75"
        icon_hover_opacity = "1"

    v_margin = max(0, (34 - btn_size) // 2)

    if is_preview:
        return f"""
        .live-preview-box .preview-btn {{
            border-radius: {radius}px;
            min-width: {btn_size}px;
            min-height: {btn_size}px;
            padding: 0;
            margin: 0 {max(1, spacing // 2)}px;
            border: {border_css};
            box-shadow: none;
            background-clip: padding-box;
        }}
        .live-preview-box .preview-btn image {{
            min-width: {icon_size}px;
            min-height: {icon_size}px;
            padding: 0;
            margin: 0;
            -gtk-icon-size: {icon_size}px;
            opacity: {icon_opacity};
            transition: opacity 150ms ease-in-out;
        }}
        .live-preview-box:hover .preview-btn image,
        .live-preview-box .preview-btn:hover image {{
            opacity: {icon_hover_opacity};
        }}
        .live-preview-box .preview-btn.preview-close {{
            background-color: {close_bg};
            color: {close_fg};
        }}
        .live-preview-box .preview-btn.preview-close:hover {{
            background-color: {close_hover};
        }}
        .live-preview-box .preview-btn.preview-min {{
            background-color: {min_bg};
            color: {min_fg};
        }}
        .live-preview-box .preview-btn.preview-min:hover {{
            background-color: {min_hover};
        }}
        .live-preview-box .preview-btn.preview-max {{
            background-color: {max_bg};
            color: {max_fg};
        }}
        .live-preview-box .preview-btn.preview-max:hover {{
            background-color: {max_hover};
        }}
        """
    else:
        return f"""window headerbar windowcontrols button,
window headerbar windowcontrols button.image-button,
headerbar windowcontrols button,
headerbar windowcontrols button.image-button {{
    border-radius: {radius}px;
    min-width: {btn_size}px;
    min-height: {btn_size}px;
    padding: 0;
    margin: {v_margin}px {spacing}px;
    border: {border_css};
    box-shadow: none;
    background-clip: padding-box;
}}
window headerbar windowcontrols button image,
window headerbar windowcontrols button.image-button image,
headerbar windowcontrols button image,
headerbar windowcontrols button.image-button image {{
    min-width: {icon_size}px;
    min-height: {icon_size}px;
    padding: 0;
    margin: 0;
    -gtk-icon-size: {icon_size}px;
    opacity: {icon_opacity};
    transition: opacity 150ms ease-in-out;
}}
window headerbar windowcontrols:hover button image,
headerbar windowcontrols:hover button image,
window headerbar windowcontrols button:hover image,
headerbar windowcontrols button:hover image {{
    opacity: {icon_hover_opacity};
}}
window headerbar windowcontrols button.close,
headerbar windowcontrols button.close {{
    background-color: {close_bg};
    color: {close_fg};
}}
window headerbar windowcontrols button.close:hover,
headerbar windowcontrols button.close:hover {{
    background-color: {close_hover};
}}
window headerbar windowcontrols button.minimize,
headerbar windowcontrols button.minimize {{
    background-color: {min_bg};
    color: {min_fg};
}}
window headerbar windowcontrols button.minimize:hover,
headerbar windowcontrols button.minimize:hover {{
    background-color: {min_hover};
}}
window headerbar windowcontrols button.maximize,
headerbar windowcontrols button.maximize {{
    background-color: {max_bg};
    color: {max_fg};
}}
window headerbar windowcontrols button.maximize:hover,
headerbar windowcontrols button.maximize:hover {{
    background-color: {max_hover};
}}"""

def apply_safe_css(filepath, css_code):
    content = ""
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    if MARKER_START in content and MARKER_END in content:
        start_idx = content.find(MARKER_START)
        end_idx = content.find(MARKER_END) + len(MARKER_END)
        content = content[:start_idx] + content[end_idx:]
    if css_code:
        if content and not content.endswith('\n'):
            content += '\n'
        content += f"{MARKER_START}\n{css_code}\n{MARKER_END}\n"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

class MainWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(620, 750)
        self.set_title("Titlebar Styler")

        # Injetar CSS base e de Live Preview
        base_provider = Gtk.CssProvider()
        base_provider.load_from_string(APP_INTERNAL_CSS)
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            base_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.preview_provider = Gtk.CssProvider()
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            self.preview_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION + 2000
        )

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(main_box)

        # HeaderBar com ViewSwitcher e Botão Sobre
        header_bar = Adw.HeaderBar()
        main_box.append(header_bar)

        self.view_stack = Adw.ViewStack()
        view_switcher = Adw.ViewSwitcher(stack=self.view_stack, policy=Adw.ViewSwitcherPolicy.WIDE)
        header_bar.set_title_widget(view_switcher)

        about_btn = Gtk.Button(icon_name="help-about-symbolic")
        about_btn.set_tooltip_text("Sobre o Titlebar Styler")
        about_btn.connect("clicked", self.on_about)
        header_bar.pack_end(about_btn)

        main_box.append(self.view_stack)

        # Página 1: Modelos Prontos
        presets_page = self.build_presets_page()
        self.view_stack.add_titled_with_icon(presets_page, "presets", "Modelos", "view-grid-symbolic")

        # Página 2: Personalizador Interativo
        custom_page = self.build_custom_page()
        self.view_stack.add_titled_with_icon(custom_page, "custom", "Personalizar", "preferences-other-symbolic")

        # Inicializar pré-visualização ao vivo com valores padrão
        self.update_live_preview()

    def build_presets_page(self):
        page = Adw.PreferencesPage()

        group = Adw.PreferencesGroup(
            title="Modelos Prontos",
            description="Escolhe um estilo de botões pré-configurado para o GNOME 51."
        )
        page.add(group)

        for name, data in STYLES.items():
            row = Adw.ActionRow(title=name)
            row.set_subtitle(data["description"])

            badge = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
            badge.add_css_class("preview-badge")
            badge.set_valign(Gtk.Align.CENTER)
            for c in data["preview_classes"]:
                dot = Gtk.Box()
                dot.add_css_class("preview-dot")
                dot.add_css_class(c)
                badge.append(dot)
            row.add_prefix(badge)

            btn = Gtk.Button(label="Aplicar", valign=Gtk.Align.CENTER)
            btn.add_css_class("suggested-action")
            btn.connect("clicked", self.on_apply, data["css"], name)
            row.add_suffix(btn)
            group.add(row)

        reset_group = Adw.PreferencesGroup(
            title="Repor Padrão",
            description="Restaura os botões originais do Fedora/Adwaita sem alterações de CSS."
        )
        page.add(reset_group)

        reset_row = Adw.ActionRow(title="Restaurar botões originais do Fedora")
        reset_row.set_subtitle("Remove as regras personalizadas de ~/.config/gtk-4.0/gtk.css.")

        reset_badge = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        reset_badge.add_css_class("preview-badge")
        reset_badge.set_valign(Gtk.Align.CENTER)
        for _ in range(3):
            dot = Gtk.Box()
            dot.add_css_class("preview-dot")
            dot.add_css_class("default-dot")
            reset_badge.append(dot)
        reset_row.add_prefix(reset_badge)

        reset_btn = Gtk.Button(label="Restaurar", valign=Gtk.Align.CENTER)
        reset_btn.add_css_class("destructive-action")
        reset_btn.connect("clicked", self.on_apply, None, "Padrão")
        reset_row.add_suffix(reset_btn)
        reset_group.add(reset_row)

        return page

    def build_custom_page(self):
        page = Adw.PreferencesPage()

        # Grupo: Pré-visualização ao vivo
        preview_group = Adw.PreferencesGroup(
            title="Pré-Visualização",
            description="Passa o rato pelos botões abaixo para testar os efeitos de hover."
        )
        page.add(preview_group)

        preview_card = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        preview_card.add_css_class("preview-window-frame")
        preview_card.add_css_class("live-preview-box")

        self.btn_preview_close = Gtk.Button()
        self.btn_preview_close.set_icon_name("window-close-symbolic")
        self.btn_preview_close.add_css_class("preview-btn")
        self.btn_preview_close.add_css_class("preview-close")
        self.btn_preview_close.set_valign(Gtk.Align.CENTER)

        self.btn_preview_min = Gtk.Button()
        self.btn_preview_min.set_icon_name("window-minimize-symbolic")
        self.btn_preview_min.add_css_class("preview-btn")
        self.btn_preview_min.add_css_class("preview-min")
        self.btn_preview_min.set_valign(Gtk.Align.CENTER)

        self.btn_preview_max = Gtk.Button()
        self.btn_preview_max.set_icon_name("window-maximize-symbolic")
        self.btn_preview_max.add_css_class("preview-btn")
        self.btn_preview_max.add_css_class("preview-max")
        self.btn_preview_max.set_valign(Gtk.Align.CENTER)

        buttons_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        buttons_container.append(self.btn_preview_close)
        buttons_container.append(self.btn_preview_min)
        buttons_container.append(self.btn_preview_max)

        preview_card.append(buttons_container)

        title_lbl = Gtk.Label(label="Exemplo de Janela GNOME")
        title_lbl.add_css_class("preview-window-title")
        title_lbl.set_hexpand(True)
        title_lbl.set_halign(Gtk.Align.CENTER)
        preview_card.append(title_lbl)

        preview_group.add(preview_card)

        # Grupo: Dimensões e Formato
        geom_group = Adw.PreferencesGroup(
            title="Dimensões e Formato",
            description="Configura o tamanho exato dos botões e a curvatura geométrica."
        )
        page.add(geom_group)

        self.spin_btn_size = Adw.SpinRow.new_with_range(10, 26, 1)
        self.spin_btn_size.set_title("Tamanho do Botão (px)")
        self.spin_btn_size.set_subtitle("Largura e altura dos botões de janela.")
        self.spin_btn_size.set_value(14)
        self.spin_btn_size.connect("notify::value", lambda *_: self.update_live_preview())
        geom_group.add(self.spin_btn_size)

        shape_model = Gtk.StringList.new([
            "Círculo Perfeito",
            "Cantos Arredondados Suaves (6px)",
            "Quadrado (0px)",
            "Curvatura Personalizada"
        ])
        self.combo_shape = Adw.ComboRow(title="Formato do Botão", model=shape_model)
        self.combo_shape.set_subtitle("Forma geométrica do botão.")
        self.combo_shape.set_selected(0)
        self.combo_shape.connect("notify::selected", self.on_shape_changed)
        geom_group.add(self.combo_shape)

        self.spin_radius = Adw.SpinRow.new_with_range(0, 30, 1)
        self.spin_radius.set_title("Raio da Curvatura (px)")
        self.spin_radius.set_subtitle("Raio manual dos cantos.")
        self.spin_radius.set_value(9999)
        self.spin_radius.set_sensitive(False)
        self.spin_radius.connect("notify::value", lambda *_: self.update_live_preview())
        geom_group.add(self.spin_radius)

        self.spin_icon_size = Adw.SpinRow.new_with_range(6, 20, 1)
        self.spin_icon_size.set_title("Tamanho dos Ícones (px)")
        self.spin_icon_size.set_subtitle("Dimensão do glifo simbólico interno.")
        self.spin_icon_size.set_value(10)
        self.spin_icon_size.connect("notify::value", lambda *_: self.update_live_preview())
        geom_group.add(self.spin_icon_size)

        self.spin_spacing = Adw.SpinRow.new_with_range(1, 14, 1)
        self.spin_spacing.set_title("Espaçamento (px)")
        self.spin_spacing.set_subtitle("Distância horizontal entre cada botão.")
        self.spin_spacing.set_value(4)
        self.spin_spacing.connect("notify::value", lambda *_: self.update_live_preview())
        geom_group.add(self.spin_spacing)

        # Grupo: Cores
        colors_group = Adw.PreferencesGroup(
            title="Cores dos Botões",
            description="Escolhe as cores de fundo e dos ícones para cada ação."
        )
        page.add(colors_group)

        self.color_dialog = Gtk.ColorDialog()

        # Fechar
        row_close = Adw.ActionRow(title="Botão Fechar")
        row_close.set_subtitle("Cor do botão e do símbolo '×'.")
        box_close = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_close.set_valign(Gtk.Align.CENTER)

        lbl_c_bg = Gtk.Label(label="Fundo:")
        self.btn_color_close_bg = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#ff5f56"))
        self.btn_color_close_bg.connect("notify::rgba", lambda *_: self.update_live_preview())

        lbl_c_fg = Gtk.Label(label="Ícone:")
        self.btn_color_close_fg = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#4d0000"))
        self.btn_color_close_fg.connect("notify::rgba", lambda *_: self.update_live_preview())

        box_close.append(lbl_c_bg)
        box_close.append(self.btn_color_close_bg)
        box_close.append(lbl_c_fg)
        box_close.append(self.btn_color_close_fg)
        row_close.add_suffix(box_close)
        colors_group.add(row_close)

        # Minimizar
        row_min = Adw.ActionRow(title="Botão Minimizar")
        row_min.set_subtitle("Cor do botão e do símbolo '−'.")
        box_min = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_min.set_valign(Gtk.Align.CENTER)

        lbl_m_bg = Gtk.Label(label="Fundo:")
        self.btn_color_min_bg = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#ffbd2e"))
        self.btn_color_min_bg.connect("notify::rgba", lambda *_: self.update_live_preview())

        lbl_m_fg = Gtk.Label(label="Ícone:")
        self.btn_color_min_fg = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#995700"))
        self.btn_color_min_fg.connect("notify::rgba", lambda *_: self.update_live_preview())

        box_min.append(lbl_m_bg)
        box_min.append(self.btn_color_min_bg)
        box_min.append(lbl_m_fg)
        box_min.append(self.btn_color_min_fg)
        row_min.add_suffix(box_min)
        colors_group.add(row_min)

        # Maximizar
        row_max = Adw.ActionRow(title="Botão Maximizar")
        row_max.set_subtitle("Cor do botão e do símbolo '+'.")
        box_max = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_max.set_valign(Gtk.Align.CENTER)

        lbl_mx_bg = Gtk.Label(label="Fundo:")
        self.btn_color_max_bg = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#27c93f"))
        self.btn_color_max_bg.connect("notify::rgba", lambda *_: self.update_live_preview())

        lbl_mx_fg = Gtk.Label(label="Ícone:")
        self.btn_color_max_fg = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#006500"))
        self.btn_color_max_fg.connect("notify::rgba", lambda *_: self.update_live_preview())

        box_max.append(lbl_mx_bg)
        box_max.append(self.btn_color_max_bg)
        box_max.append(lbl_mx_fg)
        box_max.append(self.btn_color_max_fg)
        row_max.add_suffix(box_max)
        colors_group.add(row_max)

        # Borda / Contorno
        self.switch_border = Adw.SwitchRow(title="Adicionar Contorno / Borda")
        self.switch_border.set_subtitle("Desenha uma borda fina em redor de cada botão.")
        self.switch_border.set_active(True)
        self.switch_border.connect("notify::active", self.on_border_switch_changed)
        colors_group.add(self.switch_border)

        self.row_border_opts = Adw.ActionRow(title="Opções da Borda")
        box_border = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_border.set_valign(Gtk.Align.CENTER)

        lbl_b_c = Gtk.Label(label="Cor:")
        rgba_border = Gdk.RGBA()
        rgba_border.parse("rgba(0,0,0,0.2)")
        self.btn_color_border = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=rgba_border)
        self.btn_color_border.connect("notify::rgba", lambda *_: self.update_live_preview())

        lbl_b_w = Gtk.Label(label="Espessura (px):")
        self.spin_border_width = Gtk.SpinButton.new_with_range(1, 3, 1)
        self.spin_border_width.set_value(1)
        self.spin_border_width.connect("value-changed", lambda *_: self.update_live_preview())

        box_border.append(lbl_b_c)
        box_border.append(self.btn_color_border)
        box_border.append(lbl_b_w)
        box_border.append(self.spin_border_width)
        self.row_border_opts.add_suffix(box_border)
        colors_group.add(self.row_border_opts)

        # Grupo: Comportamento no Hover
        hover_group = Adw.PreferencesGroup(
            title="Comportamento no Hover",
            description="Define a reação dos botões quando o cursor do rato passa por cima."
        )
        page.add(hover_group)

        vis_model = Gtk.StringList.new([
            "Símbolos Apenas no Hover (macOS)",
            "Ícones Sempre Visíveis",
            "Ocultar Ícones (Apenas Cores)"
        ])
        self.combo_icon_vis = Adw.ComboRow(title="Visibilidade dos Ícones", model=vis_model)
        self.combo_icon_vis.set_subtitle("Como e quando os ícones devem ser exibidos.")
        self.combo_icon_vis.set_selected(0)
        self.combo_icon_vis.connect("notify::selected", lambda *_: self.update_live_preview())
        hover_group.add(self.combo_icon_vis)

        effect_model = Gtk.StringList.new([
            "Escurecer Suavemente",
            "Iluminar / Clarear",
            "Nenhum Efeito de Cor"
        ])
        self.combo_hover_effect = Adw.ComboRow(title="Efeito de Cor no Hover", model=effect_model)
        self.combo_hover_effect.set_subtitle("Ajuste da tonalidade da cor ao passar o cursor.")
        self.combo_hover_effect.set_selected(0)
        self.combo_hover_effect.connect("notify::selected", lambda *_: self.update_live_preview())
        hover_group.add(self.combo_hover_effect)

        # Grupo: Ações
        apply_group = Adw.PreferencesGroup(title="Gravar Estilo")
        page.add(apply_group)

        apply_row = Adw.ActionRow(title="Aplicar Estilo Criado")
        apply_row.set_subtitle("Injeta as tuas definições personalizadas no sistema.")

        btn_reset_editor = Gtk.Button(label="Repor Predefinições", valign=Gtk.Align.CENTER)
        btn_reset_editor.connect("clicked", self.on_reset_editor_defaults)
        apply_row.add_suffix(btn_reset_editor)

        btn_apply_custom = Gtk.Button(label="Aplicar no Sistema", valign=Gtk.Align.CENTER)
        btn_apply_custom.add_css_class("suggested-action")
        btn_apply_custom.connect("clicked", self.on_apply_custom_clicked)
        apply_row.add_suffix(btn_apply_custom)

        apply_group.add(apply_row)

        return page

    def on_shape_changed(self, row, pspec):
        sel = row.get_selected()
        if sel == 0:  # Círculo
            self.spin_radius.set_value(9999)
            self.spin_radius.set_sensitive(False)
        elif sel == 1:  # 6px
            self.spin_radius.set_value(6)
            self.spin_radius.set_sensitive(False)
        elif sel == 2:  # Quadrado
            self.spin_radius.set_value(0)
            self.spin_radius.set_sensitive(False)
        else:  # Manual
            self.spin_radius.set_sensitive(True)
        self.update_live_preview()

    def on_border_switch_changed(self, row, pspec):
        active = row.get_active()
        self.row_border_opts.set_sensitive(active)
        self.update_live_preview()

    def get_custom_params(self):
        sel_vis = self.combo_icon_vis.get_selected()
        vis_map = {0: "hover", 1: "always", 2: "hidden"}

        sel_eff = self.combo_hover_effect.get_selected()
        eff_map = {0: "darken", 1: "lighten", 2: "none"}

        border_active = self.switch_border.get_active()
        b_rgba = self.btn_color_border.get_rgba()
        border_color_str = f"rgba({int(b_rgba.red*255)}, {int(b_rgba.green*255)}, {int(b_rgba.blue*255)}, {b_rgba.alpha:.2f})"

        sel_shape = self.combo_shape.get_selected()
        if sel_shape == 0:
            calc_radius = 9999
        elif sel_shape == 1:
            calc_radius = 6
        elif sel_shape == 2:
            calc_radius = 0
        else:
            calc_radius = int(self.spin_radius.get_value())

        return {
            "btn_size": int(self.spin_btn_size.get_value()),
            "radius": calc_radius,
            "icon_size": int(self.spin_icon_size.get_value()),
            "spacing": int(self.spin_spacing.get_value()),
            "close_bg": rgba_to_hex(self.btn_color_close_bg.get_rgba()),
            "close_fg": rgba_to_hex(self.btn_color_close_fg.get_rgba()),
            "min_bg": rgba_to_hex(self.btn_color_min_bg.get_rgba()),
            "min_fg": rgba_to_hex(self.btn_color_min_fg.get_rgba()),
            "max_bg": rgba_to_hex(self.btn_color_max_bg.get_rgba()),
            "max_fg": rgba_to_hex(self.btn_color_max_fg.get_rgba()),
            "border_enabled": border_active,
            "border_width": int(self.spin_border_width.get_value()),
            "border_color": border_color_str,
            "icon_visibility": vis_map.get(sel_vis, "hover"),
            "hover_effect": eff_map.get(sel_eff, "darken")
        }

    def update_live_preview(self):
        params = self.get_custom_params()
        preview_css = generate_css(params, is_preview=True)
        self.preview_provider.load_from_string(preview_css)

    def on_apply_custom_clicked(self, button):
        params = self.get_custom_params()
        system_css = generate_css(params, is_preview=False)
        self.on_apply(button, system_css, "Personalizado")

    def on_reset_editor_defaults(self, button):
        self.spin_btn_size.set_value(14)
        self.combo_shape.set_selected(0)
        self.spin_radius.set_value(9999)
        self.spin_icon_size.set_value(10)
        self.spin_spacing.set_value(4)
        self.btn_color_close_bg.set_rgba(hex_to_rgba("#ff5f56"))
        self.btn_color_close_fg.set_rgba(hex_to_rgba("#4d0000"))
        self.btn_color_min_bg.set_rgba(hex_to_rgba("#ffbd2e"))
        self.btn_color_min_fg.set_rgba(hex_to_rgba("#995700"))
        self.btn_color_max_bg.set_rgba(hex_to_rgba("#27c93f"))
        self.btn_color_max_fg.set_rgba(hex_to_rgba("#006500"))
        self.switch_border.set_active(True)
        self.combo_icon_vis.set_selected(0)
        self.combo_hover_effect.set_selected(0)
        self.update_live_preview()

    def on_about(self, button):
        about = Adw.AboutDialog(
            application_name="Titlebar Styler",
            application_icon="io.github.flaviomms.TitlebarStyler",
            developer_name="Flavio MMS",
            version="1.0.0",
            copyright="© 2026 Flavio MMS",
            license_type=Gtk.License.GPL_3_0,
            website="https://github.com/flaviomms/titlebar-styler",
            issue_url="https://github.com/flaviomms/titlebar-styler/issues",
            comments="Personalizador de botões da barra de janelas para o ambiente GNOME no Fedora."
        )
        about.present(self)

    def on_apply(self, button, css_code, name):
        home = os.path.expanduser("~")
        paths = [
            os.path.join(home, ".config", "gtk-4.0", "gtk.css"),
            os.path.join(home, ".config", "gtk-3.0", "gtk.css")
        ]
        try:
            for path in paths:
                apply_safe_css(path, css_code)
            dialog = Adw.AlertDialog(
                heading="Estilo Guardado",
                body=f"O estilo '{name}' foi aplicado com sucesso.\n\nPara que todas as janelas assumam o novo visual em segurança, é necessário terminar a sessão."
            )
            dialog.add_response("cancel", "Mais Tarde")
            dialog.add_response("logout", "Terminar Sessão Agora")
            dialog.set_response_appearance("logout", Adw.ResponseAppearance.SUGGESTED)
            def on_response(dlg, response):
                if response == "logout":
                    os.system("gnome-session-quit --logout")
            dialog.connect("response", on_response)
            dialog.present(self)
        except Exception as e:
            dialog = Adw.AlertDialog(heading="Erro Crítico", body=f"Erro: {str(e)}")
            dialog.add_response("ok", "OK")
            dialog.present(self)

class StylerApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="io.github.flaviomms.TitlebarStyler", flags=Gio.ApplicationFlags.FLAGS_NONE)
    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

def main():
    app = StylerApp()
    return app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main())
