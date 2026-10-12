#!/usr/bin/python3
import sys
import os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio

MARKER_START = "/* --- TITLEBAR STYLER INICIO --- */"
MARKER_END = "/* --- TITLEBAR STYLER FIM --- */"

STYLES = {
    "macOS": """window headerbar windowcontrols button,
headerbar windowcontrols button { border-radius: 9999px; min-width: 14px; min-height: 14px; padding: 0; margin: 0 4px; border: 0; box-shadow: none; color: transparent; }
window headerbar windowcontrols button image, headerbar windowcontrols button image { opacity: 0; }
window headerbar windowcontrols button.close, headerbar windowcontrols button.close { background-color: #ff5f56; }
window headerbar windowcontrols button.close:hover, headerbar windowcontrols button.close:hover { background-color: #e0443e; }
window headerbar windowcontrols button.minimize, headerbar windowcontrols button.minimize { background-color: #ffbd2e; }
window headerbar windowcontrols button.minimize:hover, headerbar windowcontrols button.minimize:hover { background-color: #dea123; }
window headerbar windowcontrols button.maximize, headerbar windowcontrols button.maximize { background-color: #27c93f; }
window headerbar windowcontrols button.maximize:hover, headerbar windowcontrols button.maximize:hover { background-color: #1aab29; }""",
    
    "Minimalista": """window headerbar windowcontrols button,
headerbar windowcontrols button { border-radius: 9999px; min-width: 12px; min-height: 12px; padding: 0; margin: 0 4px; border: 0; box-shadow: none; color: transparent; background-color: alpha(currentColor, 0.35); }
window headerbar windowcontrols button image, headerbar windowcontrols button image { opacity: 0; }
window headerbar windowcontrols button:hover, headerbar windowcontrols button:hover { background-color: alpha(currentColor, 0.7); }"""
}

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
        self.set_default_size(540, 480)
        self.set_title("Titlebar Styler")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(box)
        box.append(Adw.HeaderBar())
        page = Adw.PreferencesPage()
        box.append(page)
        group = Adw.PreferencesGroup(title="Estilos de Botões", description="Personaliza os botões das janelas (Minimizar, Maximizar, Fechar).")
        page.add(group)
        for name, css in STYLES.items():
            row = Adw.ActionRow(title=name)
            btn = Gtk.Button(label="Aplicar", valign=Gtk.Align.CENTER)
            btn.connect("clicked", self.on_apply, css, name)
            row.add_suffix(btn)
            group.add(row)
        reset_group = Adw.PreferencesGroup(title="Repor Padrão")
        page.add(reset_group)
        reset_row = Adw.ActionRow(title="Restaurar botões originais do Fedora")
        reset_btn = Gtk.Button(label="Restaurar", valign=Gtk.Align.CENTER)
        reset_btn.add_css_class("destructive-action")
        reset_btn.connect("clicked", self.on_apply, None, "Padrão")
        reset_row.add_suffix(reset_btn)
        reset_group.add(reset_row)

    def on_apply(self, button, css_code, name):
        home = os.path.expanduser("~")
        paths = [
            os.path.join(home, ".config", "gtk-4.0", "gtk.css"),
            os.path.join(home, ".config", "gtk-3.0", "gtk.css")
        ]
        try:
            for path in paths:
                apply_safe_css(path, css_code)
            dialog = Adw.AlertDialog(heading="Estilo Guardado", body=f"O estilo '{name}' foi aplicado.\n\nPara que todas as janelas assumam o novo visual em segurança, é necessário terminar a sessão.")
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
