#!/usr/bin/python3
import sys
import os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, Gdk

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
"""

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
        self.set_default_size(600, 680)
        self.set_title("Titlebar Styler")
        
        # Injetar CSS de preview da própria app
        css_provider = Gtk.CssProvider()
        css_provider.load_from_string(APP_INTERNAL_CSS)
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(box)
        
        # HeaderBar com botão Sobre
        header_bar = Adw.HeaderBar()
        box.append(header_bar)
        
        about_btn = Gtk.Button(icon_name="help-about-symbolic")
        about_btn.set_tooltip_text("Sobre o Titlebar Styler")
        about_btn.connect("clicked", self.on_about)
        header_bar.pack_end(about_btn)
        
        page = Adw.PreferencesPage()
        box.append(page)
        
        # Grupo de Estilos
        group = Adw.PreferencesGroup(
            title="Estilos de Botões",
            description="Personaliza os botões das janelas (Fechar, Minimizar, Maximizar) no GNOME 51."
        )
        page.add(group)
        
        for name, data in STYLES.items():
            row = Adw.ActionRow(title=name)
            row.set_subtitle(data["description"])
            
            # Adicionar badge com pré-visualização de ícones/bolinhas
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
            
        # Grupo de Restauração
        reset_group = Adw.PreferencesGroup(
            title="Repor Padrão",
            description="Remove todas as regras injetadas e volta ao aspeto nativo do Fedora/Adwaita."
        )
        page.add(reset_group)
        
        reset_row = Adw.ActionRow(title="Restaurar botões originais do Fedora")
        reset_row.set_subtitle("Repõe a barra de janelas original sem alterações de CSS.")
        
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
