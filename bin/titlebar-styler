#!/usr/bin/python3
import sys
import os
import json
import shutil
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, Gdk, GLib

MARKER_START = "/* --- TITLEBAR STYLER INICIO --- */"
MARKER_END = "/* --- TITLEBAR STYLER FIM --- */"

CONFIG_DIR = os.path.expanduser("~/.config/titlebar-styler")
PROFILES_FILE = os.path.join(CONFIG_DIR, "profiles.json")
ICONS_DIR = os.path.join(CONFIG_DIR, "custom-icons")

os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(ICONS_DIR, exist_ok=True)

ACCENT_COLORS = {
    "blue": "#3584e4",
    "teal": "#2190a4",
    "green": "#3a944a",
    "yellow": "#c88800",
    "orange": "#ed5b00",
    "red": "#e62d42",
    "pink": "#d56199",
    "purple": "#9141ac",
    "slate": "#6f8396"
}

STYLES = {
    "macOS (Símbolos no Hover)": {
        "description": "Círculos perfeitos com as cores do macOS. Revela os ícones no hover.",
        "preview_classes": ["macos-close", "macos-min", "macos-max"],
        "layout": "close,minimize,maximize:",
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
    -gtk-icon-size: 10px;
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
        "layout": "close,minimize,maximize:",
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
    -gtk-icon-size: 10px;
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
        "layout": ":minimize,maximize,close",
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
    -gtk-icon-size: 10px;
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
        "layout": ":minimize,maximize,close",
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
    -gtk-icon-size: 10px;
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
        "layout": ":minimize,maximize,close",
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
    -gtk-icon-size: 10px;
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
        "layout": ":minimize,maximize,close",
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
    -gtk-icon-size: 10px;
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

def get_accent_color_hex():
    try:
        iface = Gio.Settings(schema_id="org.gnome.desktop.interface")
        if "accent-color" in iface.keys():
            key = iface.get_string("accent-color")
            return ACCENT_COLORS.get(key, "#3584e4")
    except Exception:
        pass
    return "#3584e4"

def load_user_profiles():
    if os.path.exists(PROFILES_FILE):
        try:
            with open(PROFILES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_user_profiles(profiles):
    try:
        with open(PROFILES_FILE, "w", encoding="utf-8") as f:
            json.dump(profiles, f, indent=2)
    except Exception as e:
        print(f"Erro ao guardar perfis: {e}")

def generate_css(params, is_preview=False):
    btn_size = params["btn_size"]
    shape = params["shape"]
    tl = params["tl"]
    tr = params["tr"]
    br = params["br"]
    bl = params["bl"]
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
    shadow_enabled = params.get("shadow_enabled", False)
    shadow_type = params.get("shadow_type", "3d")
    shadow_blur = params.get("shadow_blur", 4)

    custom_icon_close = params.get("custom_icon_close")
    custom_icon_min = params.get("custom_icon_min")
    custom_icon_max = params.get("custom_icon_max")

    if hover_effect == "darken":
        close_hover = adjust_color(close_bg, 0.88)
        min_hover = adjust_color(min_bg, 0.88)
        max_hover = adjust_color(max_bg, 0.88)
    elif hover_effect == "lighten":
        close_hover = adjust_color(close_bg, 1.15)
        min_hover = adjust_color(min_bg, 1.15)
        max_hover = adjust_color(max_bg, 1.15)
    elif hover_effect == "custom":
        close_hover = params.get("close_hover_bg", close_bg)
        min_hover = params.get("min_hover_bg", min_bg)
        max_hover = params.get("max_hover_bg", max_bg)
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

    # Box-shadow
    shadow_trigger = params.get("shadow_trigger", "permanent")  # "permanent" ou "hover_only"

    if shadow_enabled:
        if shadow_type == "3d":
            shadow_css = f"box-shadow: 0 2px {shadow_blur}px rgba(0, 0, 0, 0.35);"
            shadow_close_val = shadow_css
            shadow_min_val = shadow_css
            shadow_max_val = shadow_css
        else:  # glow
            shadow_close_val = f"box-shadow: 0 0 {shadow_blur}px {close_bg};"
            shadow_min_val = f"box-shadow: 0 0 {shadow_blur}px {min_bg};"
            shadow_max_val = f"box-shadow: 0 0 {shadow_blur}px {max_bg};"

        if shadow_trigger == "hover_only":
            shadow_close_normal = "box-shadow: none;"
            shadow_min_normal = "box-shadow: none;"
            shadow_max_normal = "box-shadow: none;"
            shadow_close_hover = shadow_close_val
            shadow_min_hover = shadow_min_val
            shadow_max_hover = shadow_max_val
        else:  # permanent
            shadow_close_normal = shadow_close_val
            shadow_min_normal = shadow_min_val
            shadow_max_normal = shadow_max_val
            shadow_close_hover = shadow_close_val
            shadow_min_hover = shadow_min_val
            shadow_max_hover = shadow_max_val
    else:
        shadow_close_normal = "box-shadow: none;"
        shadow_min_normal = "box-shadow: none;"
        shadow_max_normal = "box-shadow: none;"
        shadow_close_hover = "box-shadow: none;"
        shadow_min_hover = "box-shadow: none;"
        shadow_max_hover = "box-shadow: none;"

    # Shape calculation (border-radius)
    if shape == "icon_only":
        base_shape_css = """
        border-radius: 9999px;
        background-color: transparent;
        border: none;
        box-shadow: none;
        """
        if hover_effect == "ring":
            hover_close_bg_css = "background-color: alpha(currentColor, 0.15);"
            hover_min_bg_css = "background-color: alpha(currentColor, 0.15);"
            hover_max_bg_css = "background-color: alpha(currentColor, 0.15);"
        elif hover_effect == "custom":
            hover_close_bg_css = f"background-color: {close_hover};"
            hover_min_bg_css = f"background-color: {min_hover};"
            hover_max_bg_css = f"background-color: {max_hover};"
        else:
            hover_close_bg_css = "background-color: transparent;"
            hover_min_bg_css = "background-color: transparent;"
            hover_max_bg_css = "background-color: transparent;"
        close_bg_normal = "background-color: transparent;"
        min_bg_normal = "background-color: transparent;"
        max_bg_normal = "background-color: transparent;"
    else:
        # border-radius dos 4 cantos: tl tr br bl
        base_shape_css = f"""
        border-radius: {tl}px {tr}px {br}px {bl}px;
        border: {border_css};
        background-clip: padding-box;
        """
        close_bg_normal = f"background-color: {close_bg};"
        min_bg_normal = f"background-color: {min_bg};"
        max_bg_normal = f"background-color: {max_bg};"
        hover_close_bg_css = f"background-color: {close_hover};"
        hover_min_bg_css = f"background-color: {min_hover};"
        hover_max_bg_css = f"background-color: {max_hover};"

    # Custom icons rules
    icon_source_close = f"-gtk-icon-source: url('{custom_icon_close}');" if custom_icon_close and os.path.exists(custom_icon_close) else ""
    icon_source_min = f"-gtk-icon-source: url('{custom_icon_min}');" if custom_icon_min and os.path.exists(custom_icon_min) else ""
    icon_source_max = f"-gtk-icon-source: url('{custom_icon_max}');" if custom_icon_max and os.path.exists(custom_icon_max) else ""

    if is_preview:
        return f"""
        .live-preview-box .preview-btn {{
            min-width: {btn_size}px;
            min-height: {btn_size}px;
            padding: 0;
            margin: 0 {max(1, spacing // 2)}px;
            -gtk-icon-size: {icon_size}px;
            {base_shape_css}
            transition: all 150ms ease-in-out;
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
            {close_bg_normal}
            color: {close_fg};
            {shadow_close_normal}
        }}
        .live-preview-box .preview-btn.preview-close:hover {{
            {hover_close_bg_css}
            {shadow_close_hover}
        }}
        .live-preview-box .preview-btn.preview-close image {{
            {icon_source_close}
        }}
        .live-preview-box .preview-btn.preview-min {{
            {min_bg_normal}
            color: {min_fg};
            {shadow_min_normal}
        }}
        .live-preview-box .preview-btn.preview-min:hover {{
            {hover_min_bg_css}
            {shadow_min_hover}
        }}
        .live-preview-box .preview-btn.preview-min image {{
            {icon_source_min}
        }}
        .live-preview-box .preview-btn.preview-max {{
            {max_bg_normal}
            color: {max_fg};
            {shadow_max_normal}
        }}
        .live-preview-box .preview-btn.preview-max:hover {{
            {hover_max_bg_css}
            {shadow_max_hover}
        }}
        .live-preview-box .preview-btn.preview-max image {{
            {icon_source_max}
        }}
        """
    else:
        return f"""window headerbar windowcontrols button,
window headerbar windowcontrols button.image-button,
headerbar windowcontrols button,
headerbar windowcontrols button.image-button {{
    min-width: {btn_size}px;
    min-height: {btn_size}px;
    padding: 0;
    margin: {v_margin}px {spacing}px;
    -gtk-icon-size: {icon_size}px;
    {base_shape_css}
    transition: all 150ms ease-in-out;
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
    {close_bg_normal}
    color: {close_fg};
    {shadow_close_normal}
}}
window headerbar windowcontrols button.close:hover,
headerbar windowcontrols button.close:hover {{
    {hover_close_bg_css}
    {shadow_close_hover}
}}
window headerbar windowcontrols button.close image,
headerbar windowcontrols button.close image {{
    {icon_source_close}
}}
window headerbar windowcontrols button.minimize,
headerbar windowcontrols button.minimize {{
    {min_bg_normal}
    color: {min_fg};
    {shadow_min_normal}
}}
window headerbar windowcontrols button.minimize:hover,
headerbar windowcontrols button.minimize:hover {{
    {hover_min_bg_css}
    {shadow_min_hover}
}}
window headerbar windowcontrols button.minimize image,
headerbar windowcontrols button.minimize image {{
    {icon_source_min}
}}
window headerbar windowcontrols button.maximize,
headerbar windowcontrols button.maximize {{
    {max_bg_normal}
    color: {max_fg};
    {shadow_max_normal}
}}
window headerbar windowcontrols button.maximize:hover,
headerbar windowcontrols button.maximize:hover {{
    {hover_max_bg_css}
    {shadow_max_hover}
}}
window headerbar windowcontrols button.maximize image,
headerbar windowcontrols button.maximize image {{
    {icon_source_max}
}}"""

def apply_safe_css(filepath, css_code):
    content = ""
    if os.path.exists(filepath):
        # Backup automático prévio
        bak_path = filepath + ".styler.bak"
        try:
            shutil.copyfile(filepath, bak_path)
        except Exception:
            pass
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
        self.set_default_size(680, 840)
        self.set_title("Titlebar Styler")

        self.custom_icon_close = None
        self.custom_icon_min = None
        self.custom_icon_max = None

        self.wm_settings = Gio.Settings(schema_id="org.gnome.desktop.wm.preferences")
        self.profiles = load_user_profiles()

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

        # Página 1: Modelos Prontos & Perfis
        presets_page = self.build_presets_page()
        self.view_stack.add_titled_with_icon(presets_page, "presets", "Modelos", "view-grid-symbolic")

        # Página 2: Personalizador Interativo
        custom_page = self.build_custom_page()
        self.view_stack.add_titled_with_icon(custom_page, "custom", "Personalizar", "preferences-other-symbolic")

        self.update_button_positions()

    def build_presets_page(self):
        page = Adw.PreferencesPage()

        # Perfis do Utilizador
        self.group_user_profiles = Adw.PreferencesGroup(
            title="Os Meus Perfis",
            description="Estilos personalizados criados e guardados por ti."
        )
        page.add(self.group_user_profiles)
        self.refresh_user_profiles_ui()

        # Modelos Padrão
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
            btn.connect("clicked", self.on_apply, data["css"], name, data.get("layout"))
            row.add_suffix(btn)
            group.add(row)

        reset_group = Adw.PreferencesGroup(
            title="Repor & Segurança",
            description="Restaura os botões originais ou reverte para uma cópia de segurança prévia."
        )
        page.add(reset_group)

        # Restaurar Backup
        bak_row = Adw.ActionRow(title="Restaurar Cópia de Segurança Anterior")
        bak_row.set_subtitle("Reverte o ficheiro gtk.css para o estado antes da última alteração.")
        btn_restore_bak = Gtk.Button(label="Restaurar Backup", valign=Gtk.Align.CENTER)
        btn_restore_bak.connect("clicked", self.on_restore_backup)
        bak_row.add_suffix(btn_restore_bak)
        reset_group.add(bak_row)

        # Restaurar Padrão
        reset_row = Adw.ActionRow(title="Restaurar botões originais do Fedora")
        reset_row.set_subtitle("Remove as regras personalizadas e repõe a disposição padrão de janelas.")
        reset_btn = Gtk.Button(label="Restaurar", valign=Gtk.Align.CENTER)
        reset_btn.add_css_class("destructive-action")
        reset_btn.connect("clicked", self.on_apply, None, "Padrão", ":minimize,maximize,close")
        reset_row.add_suffix(reset_btn)
        reset_group.add(reset_row)

        return page

    def refresh_user_profiles_ui(self):
        # Limpar linhas existentes
        for child in list(self.group_user_profiles.observe_children()):
            self.group_user_profiles.remove(child)

        if not self.profiles:
            empty_row = Adw.ActionRow(title="Nenhum perfil guardado ainda")
            empty_row.set_subtitle("Usa a aba 'Personalizar' e clica em 'Guardar Perfil' para guardar o teu tema.")
            self.group_user_profiles.add(empty_row)
            return

        for name, p_data in self.profiles.items():
            row = Adw.ActionRow(title=name)
            sub = f"Tamanho: {p_data.get('btn_size', 14)}px | Forma: {p_data.get('shape', 'Personalizado')}"
            row.set_subtitle(sub)

            btn_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
            btn_box.set_valign(Gtk.Align.CENTER)

            btn_del = Gtk.Button(icon_name="user-trash-symbolic")
            btn_del.add_css_class("flat")
            btn_del.set_tooltip_text("Eliminar Perfil")
            btn_del.connect("clicked", lambda b, n=name: self.on_delete_profile(n))

            btn_load = Gtk.Button(label="Aplicar")
            btn_load.add_css_class("suggested-action")
            btn_load.connect("clicked", lambda b, d=p_data, n=name: self.on_apply_profile(n, d))

            btn_box.append(btn_del)
            btn_box.append(btn_load)
            row.add_suffix(btn_box)
            self.group_user_profiles.add(row)

    def on_apply_profile(self, name, p_data):
        self.load_params_into_editor(p_data)
        sys_css = generate_css(p_data, is_preview=False)
        layout = self.get_button_layout_string()
        self.on_apply(None, sys_css, f"Perfil: {name}", layout)

    def on_delete_profile(self, name):
        if name in self.profiles:
            del self.profiles[name]
            save_user_profiles(self.profiles)
            self.refresh_user_profiles_ui()

    def build_custom_page(self):
        page = Adw.PreferencesPage()

        # Grupo: Pré-visualização ao vivo
        preview_group = Adw.PreferencesGroup(
            title="Pré-Visualização",
            description="Barra reativa em tempo real. Passa o cursor para testar cantos, posição e hover."
        )
        page.add(preview_group)

        preview_card = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        preview_card.add_css_class("preview-window-frame")
        preview_card.add_css_class("live-preview-box")

        self.box_preview_left = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        self.box_preview_right = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

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

        title_lbl = Gtk.Label(label="Exemplo de Janela GNOME")
        title_lbl.add_css_class("preview-window-title")
        title_lbl.set_hexpand(True)
        title_lbl.set_halign(Gtk.Align.CENTER)

        preview_card.append(self.box_preview_left)
        preview_card.append(title_lbl)
        preview_card.append(self.box_preview_right)

        preview_group.add(preview_card)

        # Grupo: Posição e Visibilidade dos Botões
        pos_group = Adw.PreferencesGroup(
            title="Posição e Visibilidade dos Botões",
            description="Escolhe que botões exibir e em que lado da barra colocá-los (esquerda/direita)."
        )
        page.add(pos_group)

        layout_presets = Gtk.StringList.new([
            "Personalizada",
            "Todos à Direita (Padrão GNOME)",
            "Todos à Esquerda (Estilo macOS)",
            "Separados: Minimizar à Esquerda, Fechar/Maximizar à Direita"
        ])
        self.combo_layout_preset = Adw.ComboRow(title="Predefinições de Disposição", model=layout_presets)
        self.combo_layout_preset.set_subtitle("Atalhos rápidos para alinhar os botões.")
        self.combo_layout_preset.set_selected(1)
        self.combo_layout_preset.connect("notify::selected", self.on_layout_preset_changed)
        pos_group.add(self.combo_layout_preset)

        # Fechar
        self.row_pos_close = Adw.ActionRow(title="Botão Fechar")
        self.row_pos_close.set_subtitle("Ativar/desativar e escolher posição.")
        box_close_pos = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_close_pos.set_valign(Gtk.Align.CENTER)
        lbl_c_side = Gtk.Label(label="Lado:")
        self.drop_side_close = Gtk.DropDown.new_from_strings(["Direita", "Esquerda"])
        self.drop_side_close.set_selected(0)
        self.drop_side_close.connect("notify::selected", lambda *_: self.on_individual_pos_changed())
        self.switch_close = Gtk.Switch(active=True, valign=Gtk.Align.CENTER)
        self.switch_close.connect("notify::active", lambda *_: self.on_individual_pos_changed())
        box_close_pos.append(lbl_c_side)
        box_close_pos.append(self.drop_side_close)
        box_close_pos.append(self.switch_close)
        self.row_pos_close.add_suffix(box_close_pos)
        pos_group.add(self.row_pos_close)

        # Minimizar
        self.row_pos_min = Adw.ActionRow(title="Botão Minimizar")
        self.row_pos_min.set_subtitle("Ativar/desativar e escolher posição.")
        box_min_pos = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_min_pos.set_valign(Gtk.Align.CENTER)
        lbl_m_side = Gtk.Label(label="Lado:")
        self.drop_side_min = Gtk.DropDown.new_from_strings(["Direita", "Esquerda"])
        self.drop_side_min.set_selected(0)
        self.drop_side_min.connect("notify::selected", lambda *_: self.on_individual_pos_changed())
        self.switch_min = Gtk.Switch(active=True, valign=Gtk.Align.CENTER)
        self.switch_min.connect("notify::active", lambda *_: self.on_individual_pos_changed())
        box_min_pos.append(lbl_m_side)
        box_min_pos.append(self.drop_side_min)
        box_min_pos.append(self.switch_min)
        self.row_pos_min.add_suffix(box_min_pos)
        pos_group.add(self.row_pos_min)

        # Maximizar
        self.row_pos_max = Adw.ActionRow(title="Botão Maximizar")
        self.row_pos_max.set_subtitle("Ativar/desativar e escolher posição.")
        box_max_pos = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_max_pos.set_valign(Gtk.Align.CENTER)
        lbl_mx_side = Gtk.Label(label="Lado:")
        self.drop_side_max = Gtk.DropDown.new_from_strings(["Direita", "Esquerda"])
        self.drop_side_max.set_selected(0)
        self.drop_side_max.connect("notify::selected", lambda *_: self.on_individual_pos_changed())
        self.switch_max = Gtk.Switch(active=True, valign=Gtk.Align.CENTER)
        self.switch_max.connect("notify::active", lambda *_: self.on_individual_pos_changed())
        box_max_pos.append(lbl_mx_side)
        box_max_pos.append(self.drop_side_max)
        box_max_pos.append(self.switch_max)
        self.row_pos_max.add_suffix(box_max_pos)
        pos_group.add(self.row_pos_max)

        # Grupo: Editor de Formato Estilo Nova Launcher
        geom_group = Adw.PreferencesGroup(
            title="Formato e Geometria (Estilo Nova Launcher)",
            description="Escolhe um arquétipo base ou personaliza os 4 cantos de forma independente."
        )
        page.add(geom_group)

        self.spin_btn_size = Adw.SpinRow.new_with_range(10, 26, 1)
        self.spin_btn_size.set_title("Tamanho do Botão (px)")
        self.spin_btn_size.set_subtitle("Dimensão externa da área clicável.")
        self.spin_btn_size.set_value(14)
        self.spin_btn_size.connect("notify::value", lambda *_: self.update_live_preview())
        geom_group.add(self.spin_btn_size)

        shape_model = Gtk.StringList.new([
            "Círculo Perfeito",
            "Squircle (Superelipse Apple 8px)",
            "Cantos Arredondados Suaves (6px)",
            "Quadrado (0px)",
            "Folha / Gota Diagonal",
            "Apenas Ícone (Sem Fundo / Flutuante)",
            "Personalizado (Editor dos 4 Cantos)"
        ])
        self.combo_shape = Adw.ComboRow(title="Formato Base", model=shape_model)
        self.combo_shape.set_subtitle("Arquétipo visual do botão.")
        self.combo_shape.set_selected(0)
        self.combo_shape.connect("notify::selected", self.on_shape_changed)
        geom_group.add(self.combo_shape)

        # Editor dos 4 Cantos
        self.switch_link_corners = Adw.SwitchRow(title="Vincular Todos os Cantos (Cadeado 🔗)")
        self.switch_link_corners.set_subtitle("Quando ativado, os 4 cantos partilham a mesma curvatura.")
        self.switch_link_corners.set_active(True)
        self.switch_link_corners.connect("notify::active", self.on_link_corners_changed)
        geom_group.add(self.switch_link_corners)

        self.spin_corner_all = Adw.SpinRow.new_with_range(0, 30, 1)
        self.spin_corner_all.set_title("Raio de Todos os Cantos (px)")
        self.spin_corner_all.set_value(9999)
        self.spin_corner_all.connect("notify::value", self.on_corner_all_changed)
        geom_group.add(self.spin_corner_all)

        # 4 Cantos Livres
        self.spin_corner_tl = Adw.SpinRow.new_with_range(0, 30, 1)
        self.spin_corner_tl.set_title("↖ Superior-Esquerdo (px)")
        self.spin_corner_tl.set_value(9999)
        self.spin_corner_tl.connect("notify::value", lambda *_: self.update_live_preview())
        self.spin_corner_tl.set_visible(False)
        geom_group.add(self.spin_corner_tl)

        self.spin_corner_tr = Adw.SpinRow.new_with_range(0, 30, 1)
        self.spin_corner_tr.set_title("↗ Superior-Direito (px)")
        self.spin_corner_tr.set_value(9999)
        self.spin_corner_tr.connect("notify::value", lambda *_: self.update_live_preview())
        self.spin_corner_tr.set_visible(False)
        geom_group.add(self.spin_corner_tr)

        self.spin_corner_br = Adw.SpinRow.new_with_range(0, 30, 1)
        self.spin_corner_br.set_title("↘ Inferior-Direito (px)")
        self.spin_corner_br.set_value(9999)
        self.spin_corner_br.connect("notify::value", lambda *_: self.update_live_preview())
        self.spin_corner_br.set_visible(False)
        geom_group.add(self.spin_corner_br)

        self.spin_corner_bl = Adw.SpinRow.new_with_range(0, 30, 1)
        self.spin_corner_bl.set_title("↙ Inferior-Esquerdo (px)")
        self.spin_corner_bl.set_value(9999)
        self.spin_corner_bl.connect("notify::value", lambda *_: self.update_live_preview())
        self.spin_corner_bl.set_visible(False)
        geom_group.add(self.spin_corner_bl)

        self.spin_icon_size = Adw.SpinRow.new_with_range(6, 20, 1)
        self.spin_icon_size.set_title("Tamanho dos Ícones (px)")
        self.spin_icon_size.set_subtitle("Dimensão dos símbolos (×, −, +) dentro do botão.")
        self.spin_icon_size.set_value(10)
        self.spin_icon_size.connect("notify::value", lambda *_: self.update_live_preview())
        geom_group.add(self.spin_icon_size)

        self.spin_spacing = Adw.SpinRow.new_with_range(1, 14, 1)
        self.spin_spacing.set_title("Espaçamento (px)")
        self.spin_spacing.set_subtitle("Distância horizontal entre cada botão.")
        self.spin_spacing.set_value(4)
        self.spin_spacing.connect("notify::value", lambda *_: self.update_live_preview())
        geom_group.add(self.spin_spacing)

        # Grupo: Efeitos de Profundidade e Sombra
        shadow_group = Adw.PreferencesGroup(
            title="Profundidade e Sombra (Box-Shadow & Glow)",
            description="Adiciona relevo tridimensional suave ou brilho neon aos botões."
        )
        page.add(shadow_group)

        self.switch_shadow = Adw.SwitchRow(title="Ativar Efeito de Sombra / Brilho")
        self.switch_shadow.set_subtitle("Aplica box-shadow dinâmico aos botões.")
        self.switch_shadow.set_active(False)
        self.switch_shadow.connect("notify::active", lambda *_: self.on_shadow_toggle())
        shadow_group.add(self.switch_shadow)

        shadow_types = Gtk.StringList.new([
            "Sombra 3D Suave (Relevo)",
            "Brilho Neon (Glow na Cor do Botão)"
        ])
        self.combo_shadow_type = Adw.ComboRow(title="Tipo de Efeito", model=shadow_types)
        self.combo_shadow_type.set_selected(0)
        self.combo_shadow_type.connect("notify::selected", lambda *_: self.update_live_preview())
        shadow_group.add(self.combo_shadow_type)

        shadow_triggers = Gtk.StringList.new([
            "Permanente (Sempre Visível)",
            "Apenas no Hover (Ao Passar o Rato)"
        ])
        self.combo_shadow_trigger = Adw.ComboRow(title="Comportamento da Sombra", model=shadow_triggers)
        self.combo_shadow_trigger.set_selected(0)
        self.combo_shadow_trigger.connect("notify::selected", lambda *_: self.update_live_preview())
        shadow_group.add(self.combo_shadow_trigger)

        self.spin_shadow_blur = Adw.SpinRow.new_with_range(1, 15, 1)
        self.spin_shadow_blur.set_title("Intensidade / Desfocagem (px)")
        self.spin_shadow_blur.set_value(4)
        self.spin_shadow_blur.connect("notify::value", lambda *_: self.update_live_preview())
        shadow_group.add(self.spin_shadow_blur)

        self.combo_shadow_type.set_visible(False)
        self.combo_shadow_trigger.set_visible(False)
        self.spin_shadow_blur.set_visible(False)

        # Grupo: Cores dos Botões & Sincronização de Acento
        colors_group = Adw.PreferencesGroup(
            title="Cores dos Botões",
            description="Escolhe as cores de cada ação ou sincroniza com a cor de destaque do GNOME."
        )
        page.add(colors_group)

        self.color_dialog = Gtk.ColorDialog()

        self.switch_accent = Adw.SwitchRow(title="Sincronizar com Cor de Acento do GNOME")
        self.switch_accent.set_subtitle("Usa a cor oficial de destaque do sistema Fedora nos botões.")
        self.switch_accent.set_active(False)
        self.switch_accent.connect("notify::active", self.on_accent_toggle)
        colors_group.add(self.switch_accent)

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

        # Borda
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
            "Realce de Fundo Suave (Rodela no Hover)",
            "Cor Personalizada no Hover",
            "Nenhum Efeito"
        ])
        self.combo_hover_effect = Adw.ComboRow(title="Efeito de Cor no Hover", model=effect_model)
        self.combo_hover_effect.set_subtitle("Ajuste da tonalidade da cor ao passar o cursor.")
        self.combo_hover_effect.set_selected(0)
        self.combo_hover_effect.connect("notify::selected", self.on_hover_effect_changed)
        hover_group.add(self.combo_hover_effect)

        # Cores Personalizadas no Hover
        self.row_custom_hover_colors = Adw.ActionRow(title="Cores de Fundo no Hover")
        self.row_custom_hover_colors.set_subtitle("Cores específicas exibidas durante o hover.")
        box_hover_colors = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_hover_colors.set_valign(Gtk.Align.CENTER)
        lbl_hc_c = Gtk.Label(label="Fechar:")
        self.btn_color_close_hover = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#e0443e"))
        self.btn_color_close_hover.connect("notify::rgba", lambda *_: self.update_live_preview())
        lbl_hc_m = Gtk.Label(label="Min:")
        self.btn_color_min_hover = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#dea123"))
        self.btn_color_min_hover.connect("notify::rgba", lambda *_: self.update_live_preview())
        lbl_hc_mx = Gtk.Label(label="Max:")
        self.btn_color_max_hover = Gtk.ColorDialogButton(dialog=self.color_dialog, rgba=hex_to_rgba("#1aab29"))
        self.btn_color_max_hover.connect("notify::rgba", lambda *_: self.update_live_preview())
        box_hover_colors.append(lbl_hc_c)
        box_hover_colors.append(self.btn_color_close_hover)
        box_hover_colors.append(lbl_hc_m)
        box_hover_colors.append(self.btn_color_min_hover)
        box_hover_colors.append(lbl_hc_mx)
        box_hover_colors.append(self.btn_color_max_hover)
        self.row_custom_hover_colors.add_suffix(box_hover_colors)
        self.row_custom_hover_colors.set_visible(False)
        hover_group.add(self.row_custom_hover_colors)

        # Grupo: Ícones Personalizados
        icons_group = Adw.PreferencesGroup(
            title="Importar Ícones SVG",
            description="Substitui os símbolos nativos por ficheiros SVG próprios."
        )
        page.add(icons_group)

        self.row_icon_close = Adw.ActionRow(title="Ícone Fechar")
        self.row_icon_close.set_subtitle("Padrão do sistema")
        btn_c_icon = Gtk.Button(label="Escolher SVG...", valign=Gtk.Align.CENTER)
        btn_c_icon.connect("clicked", lambda b: self.on_choose_custom_icon("close"))
        self.row_icon_close.add_suffix(btn_c_icon)
        icons_group.add(self.row_icon_close)

        self.row_icon_min = Adw.ActionRow(title="Ícone Minimizar")
        self.row_icon_min.set_subtitle("Padrão do sistema")
        btn_m_icon = Gtk.Button(label="Escolher SVG...", valign=Gtk.Align.CENTER)
        btn_m_icon.connect("clicked", lambda b: self.on_choose_custom_icon("min"))
        self.row_icon_min.add_suffix(btn_m_icon)
        icons_group.add(self.row_icon_min)

        self.row_icon_max = Adw.ActionRow(title="Ícone Maximizar")
        self.row_icon_max.set_subtitle("Padrão do sistema")
        btn_mx_icon = Gtk.Button(label="Escolher SVG...", valign=Gtk.Align.CENTER)
        btn_mx_icon.connect("clicked", lambda b: self.on_choose_custom_icon("max"))
        self.row_icon_max.add_suffix(btn_mx_icon)
        icons_group.add(self.row_icon_max)

        row_reset_icons = Adw.ActionRow(title="Repor Ícones Nativos")
        row_reset_icons.set_subtitle("Remove os ícones SVG importados e volta aos padrões.")
        btn_reset_icons = Gtk.Button(label="Repor Ícones", valign=Gtk.Align.CENTER)
        btn_reset_icons.connect("clicked", self.on_reset_icons)
        row_reset_icons.add_suffix(btn_reset_icons)
        icons_group.add(row_reset_icons)

        # Grupo: Partilha e Perfis
        share_group = Adw.PreferencesGroup(
            title="Perfis e Partilha de Temas",
            description="Guarda as tuas criações ou exporta/importa ficheiros .styler para partilhar."
        )
        page.add(share_group)

        share_row = Adw.ActionRow(title="Gerir Tema Atual")
        box_share = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box_share.set_valign(Gtk.Align.CENTER)

        btn_save_prof = Gtk.Button(label="Guardar Perfil...")
        btn_save_prof.connect("clicked", self.on_save_profile_dialog)

        btn_export = Gtk.Button(label="Exportar...")
        btn_export.connect("clicked", self.on_export_theme)

        btn_import = Gtk.Button(label="Importar...")
        btn_import.connect("clicked", self.on_import_theme)

        box_share.append(btn_save_prof)
        box_share.append(btn_export)
        box_share.append(btn_import)
        share_row.add_suffix(box_share)
        share_group.add(share_row)

        # Grupo: Ações
        apply_group = Adw.PreferencesGroup(title="Gravar Estilo")
        page.add(apply_group)

        apply_row = Adw.ActionRow(title="Aplicar Estilo Criado")
        apply_row.set_subtitle("Injeta as definições no CSS e atualiza a disposição dos botões.")

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
        # 0: Círculo (9999), 1: Squircle (8), 2: Arredondado (6), 3: Quadrado (0), 4: Folha (14 0 14 0), 5: Apenas Ícone, 6: Personalizado (4 cantos)
        is_custom = (sel == 6)
        self.switch_link_corners.set_visible(is_custom)
        self.spin_corner_all.set_visible(is_custom and self.switch_link_corners.get_active())
        self.spin_corner_tl.set_visible(is_custom and not self.switch_link_corners.get_active())
        self.spin_corner_tr.set_visible(is_custom and not self.switch_link_corners.get_active())
        self.spin_corner_br.set_visible(is_custom and not self.switch_link_corners.get_active())
        self.spin_corner_bl.set_visible(is_custom and not self.switch_link_corners.get_active())

        if sel == 0:
            self.spin_corner_all.set_value(9999)
        elif sel == 1:
            self.spin_corner_all.set_value(8)
        elif sel == 2:
            self.spin_corner_all.set_value(6)
        elif sel == 3:
            self.spin_corner_all.set_value(0)
        elif sel == 4:
            self.spin_corner_tl.set_value(14)
            self.spin_corner_tr.set_value(0)
            self.spin_corner_br.set_value(14)
            self.spin_corner_bl.set_value(0)

        self.update_live_preview()

    def on_link_corners_changed(self, row, pspec):
        linked = row.get_active()
        self.spin_corner_all.set_visible(linked)
        self.spin_corner_tl.set_visible(not linked)
        self.spin_corner_tr.set_visible(not linked)
        self.spin_corner_br.set_visible(not linked)
        self.spin_corner_bl.set_visible(not linked)
        if linked:
            val = self.spin_corner_tl.get_value()
            self.spin_corner_all.set_value(val)
        self.update_live_preview()

    def on_corner_all_changed(self, row, pspec):
        if self.switch_link_corners.get_active():
            val = row.get_value()
            self.spin_corner_tl.set_value(val)
            self.spin_corner_tr.set_value(val)
            self.spin_corner_br.set_value(val)
            self.spin_corner_bl.set_value(val)
        self.update_live_preview()

    def on_shadow_toggle(self):
        active = self.switch_shadow.get_active()
        self.combo_shadow_type.set_visible(active)
        self.combo_shadow_trigger.set_visible(active)
        self.spin_shadow_blur.set_visible(active)
        self.update_live_preview()

    def on_accent_toggle(self, row, pspec):
        if row.get_active():
            accent_hex = get_accent_color_hex()
            self.btn_color_close_bg.set_rgba(hex_to_rgba(accent_hex))
            self.btn_color_min_bg.set_rgba(hex_to_rgba(adjust_color(accent_hex, 0.85)))
            self.btn_color_max_bg.set_rgba(hex_to_rgba(adjust_color(accent_hex, 1.15)))
        self.update_live_preview()

    def on_choose_custom_icon(self, icon_type):
        dlg = Gtk.FileDialog(title=f"Escolher Ícone SVG ({icon_type})")
        filter_svg = Gtk.FileFilter()
        filter_svg.set_name("Ficheiros SVG (*.svg)")
        filter_svg.add_pattern("*.svg")
        filters = Gio.ListStore.new(Gtk.FileFilter)
        filters.append(filter_svg)
        dlg.set_filters(filters)

        def on_open_finish(d, res):
            try:
                f = d.open_finish(res)
                if f:
                    src = f.get_path()
                    dest = os.path.join(ICONS_DIR, f"{icon_type}.svg")
                    shutil.copyfile(src, dest)
                    if icon_type == "close":
                        self.custom_icon_close = dest
                        self.row_icon_close.set_subtitle(os.path.basename(src))
                    elif icon_type == "min":
                        self.custom_icon_min = dest
                        self.row_icon_min.set_subtitle(os.path.basename(src))
                    elif icon_type == "max":
                        self.custom_icon_max = dest
                        self.row_icon_max.set_subtitle(os.path.basename(src))
                    self.update_live_preview()
            except Exception as e:
                print("Cancelado ou erro:", e)

        dlg.open(self, None, on_open_finish)

    def on_reset_icons(self, button):
        self.custom_icon_close = None
        self.custom_icon_min = None
        self.custom_icon_max = None
        self.row_icon_close.set_subtitle("Padrão do sistema")
        self.row_icon_min.set_subtitle("Padrão do sistema")
        self.row_icon_max.set_subtitle("Padrão do sistema")
        self.update_live_preview()

    def on_border_switch_changed(self, row, pspec):
        active = row.get_active()
        self.row_border_opts.set_sensitive(active)
        self.update_live_preview()

    def on_hover_effect_changed(self, row, pspec):
        sel = row.get_selected()
        # idx 3 is "Cor Personalizada no Hover"
        self.row_custom_hover_colors.set_visible(sel == 3)
        self.update_live_preview()

    def on_layout_preset_changed(self, row, pspec):
        sel = row.get_selected()
        if sel == 1:  # Todos à Direita
            self.switch_close.set_active(True)
            self.drop_side_close.set_selected(0)
            self.switch_min.set_active(True)
            self.drop_side_min.set_selected(0)
            self.switch_max.set_active(True)
            self.drop_side_max.set_selected(0)
        elif sel == 2:  # Todos à Esquerda
            self.switch_close.set_active(True)
            self.drop_side_close.set_selected(1)
            self.switch_min.set_active(True)
            self.drop_side_min.set_selected(1)
            self.switch_max.set_active(True)
            self.drop_side_max.set_selected(1)
        elif sel == 3:  # Separados
            self.switch_close.set_active(True)
            self.drop_side_close.set_selected(0)  # Direita
            self.switch_min.set_active(True)
            self.drop_side_min.set_selected(1)    # Esquerda
            self.switch_max.set_active(True)
            self.drop_side_max.set_selected(0)    # Direita
        self.update_button_positions()

    def on_individual_pos_changed(self):
        self.update_button_positions()

    def update_button_positions(self):
        close_active = self.switch_close.get_active()
        close_side = "left" if self.drop_side_close.get_selected() == 1 else "right"
        self.drop_side_close.set_sensitive(close_active)

        min_active = self.switch_min.get_active()
        min_side = "left" if self.drop_side_min.get_selected() == 1 else "right"
        self.drop_side_min.set_sensitive(min_active)

        max_active = self.switch_max.get_active()
        max_side = "left" if self.drop_side_max.get_selected() == 1 else "right"
        self.drop_side_max.set_sensitive(max_active)

        for b in [self.btn_preview_close, self.btn_preview_min, self.btn_preview_max]:
            p = b.get_parent()
            if p:
                p.remove(b)

        if close_active and close_side == "left":
            self.box_preview_left.append(self.btn_preview_close)
        if min_active and min_side == "left":
            self.box_preview_left.append(self.btn_preview_min)
        if max_active and max_side == "left":
            self.box_preview_left.append(self.btn_preview_max)

        if min_active and min_side == "right":
            self.box_preview_right.append(self.btn_preview_min)
        if max_active and max_side == "right":
            self.box_preview_right.append(self.btn_preview_max)
        if close_active and close_side == "right":
            self.box_preview_right.append(self.btn_preview_close)

        self.update_live_preview()

    def get_button_layout_string(self):
        close_active = self.switch_close.get_active()
        close_side = "left" if self.drop_side_close.get_selected() == 1 else "right"

        min_active = self.switch_min.get_active()
        min_side = "left" if self.drop_side_min.get_selected() == 1 else "right"

        max_active = self.switch_max.get_active()
        max_side = "left" if self.drop_side_max.get_selected() == 1 else "right"

        left = []
        right = []

        if close_active and close_side == "left":
            left.append("close")
        if min_active and min_side == "left":
            left.append("minimize")
        if max_active and max_side == "left":
            left.append("maximize")

        if min_active and min_side == "right":
            right.append("minimize")
        if max_active and max_side == "right":
            right.append("maximize")
        if close_active and close_side == "right":
            right.append("close")

        return f"{','.join(left)}:{','.join(right)}"

    def get_custom_params(self):
        sel_shape = self.combo_shape.get_selected()
        shape_type = "circle"
        tl = 9999
        tr = 9999
        br = 9999
        bl = 9999

        if sel_shape == 0:  # Círculo
            shape_type = "circle"
            tl, tr, br, bl = 9999, 9999, 9999, 9999
        elif sel_shape == 1:  # Squircle
            shape_type = "squircle"
            tl, tr, br, bl = 8, 8, 8, 8
        elif sel_shape == 2:  # Arredondado
            shape_type = "rounded"
            tl, tr, br, bl = 6, 6, 6, 6
        elif sel_shape == 3:  # Quadrado
            shape_type = "square"
            tl, tr, br, bl = 0, 0, 0, 0
        elif sel_shape == 4:  # Folha / Gota
            shape_type = "leaf"
            tl, tr, br, bl = 14, 0, 14, 0
        elif sel_shape == 5:  # Apenas Ícone
            shape_type = "icon_only"
            tl, tr, br, bl = 9999, 9999, 9999, 9999
        else:  # Personalizado 4 cantos
            shape_type = "custom_corners"
            if self.switch_link_corners.get_active():
                val = int(self.spin_corner_all.get_value())
                tl, tr, br, bl = val, val, val, val
            else:
                tl = int(self.spin_corner_tl.get_value())
                tr = int(self.spin_corner_tr.get_value())
                br = int(self.spin_corner_br.get_value())
                bl = int(self.spin_corner_bl.get_value())

        sel_vis = self.combo_icon_vis.get_selected()
        vis_map = {0: "hover", 1: "always", 2: "hidden"}

        sel_eff = self.combo_hover_effect.get_selected()
        eff_map = {0: "darken", 1: "lighten", 2: "ring", 3: "custom", 4: "none"}

        border_active = self.switch_border.get_active()
        b_rgba = self.btn_color_border.get_rgba()
        border_color_str = f"rgba({int(b_rgba.red*255)}, {int(b_rgba.green*255)}, {int(b_rgba.blue*255)}, {b_rgba.alpha:.2f})"

        return {
            "btn_size": int(self.spin_btn_size.get_value()),
            "shape": shape_type,
            "shape_idx": sel_shape,
            "tl": tl,
            "tr": tr,
            "br": br,
            "bl": bl,
            "icon_size": int(self.spin_icon_size.get_value()),
            "spacing": int(self.spin_spacing.get_value()),
            "close_bg": rgba_to_hex(self.btn_color_close_bg.get_rgba()),
            "close_fg": rgba_to_hex(self.btn_color_close_fg.get_rgba()),
            "min_bg": rgba_to_hex(self.btn_color_min_bg.get_rgba()),
            "min_fg": rgba_to_hex(self.btn_color_min_fg.get_rgba()),
            "max_bg": rgba_to_hex(self.btn_color_max_bg.get_rgba()),
            "max_fg": rgba_to_hex(self.btn_color_max_fg.get_rgba()),
            "close_hover_bg": rgba_to_hex(self.btn_color_close_hover.get_rgba()),
            "min_hover_bg": rgba_to_hex(self.btn_color_min_hover.get_rgba()),
            "max_hover_bg": rgba_to_hex(self.btn_color_max_hover.get_rgba()),
            "border_enabled": border_active and shape_type != "icon_only",
            "border_width": int(self.spin_border_width.get_value()),
            "border_color": border_color_str,
            "icon_visibility": vis_map.get(sel_vis, "hover"),
            "hover_effect": eff_map.get(sel_eff, "darken"),
            "shadow_enabled": self.switch_shadow.get_active(),
            "shadow_type": "3d" if self.combo_shadow_type.get_selected() == 0 else "glow",
            "shadow_trigger": "permanent" if self.combo_shadow_trigger.get_selected() == 0 else "hover_only",
            "shadow_blur": int(self.spin_shadow_blur.get_value()),
            "custom_icon_close": self.custom_icon_close,
            "custom_icon_min": self.custom_icon_min,
            "custom_icon_max": self.custom_icon_max
        }

    def load_params_into_editor(self, p):
        try:
            self.spin_btn_size.set_value(p.get("btn_size", 14))
            self.spin_icon_size.set_value(p.get("icon_size", 10))
            self.spin_spacing.set_value(p.get("spacing", 4))
            self.combo_shape.set_selected(p.get("shape_idx", 0))

            tl = p.get("tl", 9999)
            tr = p.get("tr", 9999)
            br = p.get("br", 9999)
            bl = p.get("bl", 9999)

            self.spin_corner_tl.set_value(tl)
            self.spin_corner_tr.set_value(tr)
            self.spin_corner_br.set_value(br)
            self.spin_corner_bl.set_value(bl)
            self.spin_corner_all.set_value(tl)

            self.btn_color_close_bg.set_rgba(hex_to_rgba(p.get("close_bg", "#ff5f56")))
            self.btn_color_close_fg.set_rgba(hex_to_rgba(p.get("close_fg", "#4d0000")))
            self.btn_color_min_bg.set_rgba(hex_to_rgba(p.get("min_bg", "#ffbd2e")))
            self.btn_color_min_fg.set_rgba(hex_to_rgba(p.get("min_fg", "#995700")))
            self.btn_color_max_bg.set_rgba(hex_to_rgba(p.get("max_bg", "#27c93f")))
            self.btn_color_max_fg.set_rgba(hex_to_rgba(p.get("max_fg", "#006500")))

            self.switch_shadow.set_active(p.get("shadow_enabled", False))
            self.combo_shadow_type.set_selected(0 if p.get("shadow_type") == "3d" else 1)
            self.combo_shadow_trigger.set_selected(0 if p.get("shadow_trigger", "permanent") == "permanent" else 1)
            self.spin_shadow_blur.set_value(p.get("shadow_blur", 4))
            self.on_shadow_toggle()

            self.update_live_preview()
        except Exception as e:
            print(f"Erro ao carregar parâmetros: {e}")

    def update_live_preview(self):
        params = self.get_custom_params()
        preview_css = generate_css(params, is_preview=True)
        self.preview_provider.load_from_string(preview_css)

    def on_apply_custom_clicked(self, button):
        params = self.get_custom_params()
        system_css = generate_css(params, is_preview=False)
        layout = self.get_button_layout_string()
        self.on_apply(button, system_css, "Personalizado", layout)

    def on_save_profile_dialog(self, button):
        dlg = Adw.AlertDialog(heading="Guardar Perfil", body="Introduz o nome para guardar o teu tema:")
        entry = Gtk.Entry(placeholder_text="Ex: Meu Tema Cyberpunk")
        dlg.set_extra_child(entry)
        dlg.add_response("cancel", "Cancelar")
        dlg.add_response("save", "Guardar")
        dlg.set_response_appearance("save", Adw.ResponseAppearance.SUGGESTED)

        def on_response(d, response):
            if response == "save":
                name = entry.get_text().strip()
                if name:
                    p = self.get_custom_params()
                    self.profiles[name] = p
                    save_user_profiles(self.profiles)
                    self.refresh_user_profiles_ui()

        dlg.connect("response", on_response)
        dlg.present(self)

    def on_export_theme(self, button):
        dlg = Gtk.FileDialog(title="Exportar Tema")
        dlg.set_initial_name("tema.styler")
        filter_styler = Gtk.FileFilter()
        filter_styler.set_name("Temas Titlebar Styler (*.styler)")
        filter_styler.add_pattern("*.styler")
        filter_styler.add_pattern("*.json")
        filters = Gio.ListStore.new(Gtk.FileFilter)
        filters.append(filter_styler)
        dlg.set_filters(filters)

        def on_save_finish(d, res):
            try:
                f = d.save_finish(res)
                if f:
                    path = f.get_path()
                    data = self.get_custom_params()
                    with open(path, "w", encoding="utf-8") as out:
                        json.dump(data, out, indent=2)
            except Exception as e:
                print("Exportação cancelada ou erro:", e)

        dlg.save(self, None, on_save_finish)

    def on_import_theme(self, button):
        dlg = Gtk.FileDialog(title="Importar Tema")
        filter_styler = Gtk.FileFilter()
        filter_styler.set_name("Temas Titlebar Styler (*.styler, *.json)")
        filter_styler.add_pattern("*.styler")
        filter_styler.add_pattern("*.json")
        filters = Gio.ListStore.new(Gtk.FileFilter)
        filters.append(filter_styler)
        dlg.set_filters(filters)

        def on_open_finish(d, res):
            try:
                f = d.open_finish(res)
                if f:
                    path = f.get_path()
                    with open(path, "r", encoding="utf-8") as inf:
                        data = json.load(inf)
                    name = os.path.splitext(os.path.basename(path))[0]
                    self.load_params_into_editor(data)
                    self.profiles[name] = data
                    save_user_profiles(self.profiles)
                    self.refresh_user_profiles_ui()
            except Exception as e:
                print("Importação cancelada ou erro:", e)

        dlg.open(self, None, on_open_finish)

    def on_restore_backup(self, button):
        home = os.path.expanduser("~")
        p4 = os.path.join(home, ".config", "gtk-4.0", "gtk.css")
        p3 = os.path.join(home, ".config", "gtk-3.0", "gtk.css")
        bak4 = p4 + ".styler.bak"
        bak3 = p3 + ".styler.bak"

        restored = False
        if os.path.exists(bak4):
            shutil.copyfile(bak4, p4)
            restored = True
        if os.path.exists(bak3):
            shutil.copyfile(bak3, p3)
            restored = True

        if restored:
            dialog = Adw.AlertDialog(
                heading="Cópia Restaurada",
                body="A cópia de segurança do ficheiro gtk.css foi restaurada com sucesso.\n\nTermina a sessão para recarregar o visual das janelas."
            )
            dialog.add_response("cancel", "Mais Tarde")
            dialog.add_response("logout", "Terminar Sessão Agora")
            dialog.set_response_appearance("logout", Adw.ResponseAppearance.SUGGESTED)
            def on_response(dlg, response):
                if response == "logout":
                    os.system("gnome-session-quit --logout")
            dialog.connect("response", on_response)
            dialog.present(self)
        else:
            dialog = Adw.AlertDialog(heading="Sem Cópia", body="Nenhuma cópia de segurança anterior foi encontrada.")
            dialog.add_response("ok", "OK")
            dialog.present(self)

    def on_reset_editor_defaults(self, button):
        self.spin_btn_size.set_value(14)
        self.combo_shape.set_selected(0)
        self.switch_link_corners.set_active(True)
        self.spin_corner_all.set_value(9999)
        self.spin_corner_tl.set_value(9999)
        self.spin_corner_tr.set_value(9999)
        self.spin_corner_br.set_value(9999)
        self.spin_corner_bl.set_value(9999)
        self.spin_icon_size.set_value(10)
        self.spin_spacing.set_value(4)
        self.combo_layout_preset.set_selected(1)
        self.switch_shadow.set_active(False)
        self.switch_accent.set_active(False)
        self.btn_color_close_bg.set_rgba(hex_to_rgba("#ff5f56"))
        self.btn_color_close_fg.set_rgba(hex_to_rgba("#4d0000"))
        self.btn_color_min_bg.set_rgba(hex_to_rgba("#ffbd2e"))
        self.btn_color_min_fg.set_rgba(hex_to_rgba("#995700"))
        self.btn_color_max_bg.set_rgba(hex_to_rgba("#27c93f"))
        self.btn_color_max_fg.set_rgba(hex_to_rgba("#006500"))
        self.btn_color_close_hover.set_rgba(hex_to_rgba("#e0443e"))
        self.btn_color_min_hover.set_rgba(hex_to_rgba("#dea123"))
        self.btn_color_max_hover.set_rgba(hex_to_rgba("#1aab29"))
        self.switch_border.set_active(True)
        self.combo_icon_vis.set_selected(0)
        self.combo_hover_effect.set_selected(0)
        self.on_reset_icons(None)
        self.update_button_positions()

    def on_about(self, button):
        about = Adw.AboutDialog(
            application_name="Titlebar Styler",
            application_icon="io.github.flaviomms.TitlebarStyler",
            developer_name="Flavio MMS",
            version="1.0.0",
            copyright="© 2026 Flavio MMS",
            license_type=Gtk.License.GPL_3_0,
            website="https://github.com/Cfmpda/titlebar-styler",
            issue_url="https://github.com/Cfmpda/titlebar-styler/issues",
            comments="Personalizador de botões da barra de janelas para o ambiente GNOME no Fedora."
        )
        about.present(self)

    def on_apply(self, button, css_code, name, button_layout=None):
        home = os.path.expanduser("~")
        paths = [
            os.path.join(home, ".config", "gtk-4.0", "gtk.css"),
            os.path.join(home, ".config", "gtk-3.0", "gtk.css")
        ]
        try:
            for path in paths:
                apply_safe_css(path, css_code)

            if button_layout is not None:
                try:
                    self.wm_settings.set_string("button-layout", button_layout)
                except Exception as ex:
                    print(f"Aviso: não foi possível alterar button-layout: {ex}")
            elif name == "Padrão":
                try:
                    self.wm_settings.reset("button-layout")
                except Exception:
                    pass

            dialog = Adw.AlertDialog(
                heading="Estilo Guardado",
                body=f"O estilo '{name}' foi aplicado com sucesso.\n\nPara que todas as janelas assumam as alterações de tema em segurança, é necessário terminar a sessão."
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
