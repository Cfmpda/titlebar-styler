# Titlebar Styler

<p align="center">
  <img src="data/icons/hicolor/scalable/apps/io.github.flaviomms.TitlebarStyler.svg" width="96" height="96" alt="Titlebar Styler Logo" />
</p>

<p align="center">
  <b>Personalizador nativo dos botões da barra de janelas para o ambiente GNOME no Fedora.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Fedora-COPR-294172?style=flat&logo=fedora&logoColor=white" alt="Fedora COPR" />
  <img src="https://img.shields.io/badge/GTK-4-4a90d9?style=flat&logo=gtk&logoColor=white" alt="GTK4" />
  <img src="https://img.shields.io/badge/Libadwaita-1-4a90d9?style=flat" alt="Libadwaita" />
  <img src="https://img.shields.io/badge/Python-3-3776ab?style=flat&logo=python&logoColor=white" alt="Python 3" />
  <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License GPLv3" />
</p>

---

## 📖 Visão Geral

O **Titlebar Styler** é uma aplicação nativa rápida e elegante projetada para permitir que os utilizadores do GNOME (incluindo GNOME 51 / Fedora 44+) personalizem o aspeto dos controlos de janelas (**Fechar**, **Minimizar**, **Maximizar**), sem quebrar a integridade do sistema ou causar conflitos de temas.

### 🛡️ Princípios Técnicos & Segurança
- **Geometria Perfeita 1:1:** Resolve a deformação vertical das janelas GTK4/Libadwaita, garantindo círculos matematicamente exatos (14px × 14px / 16px × 16px) e ícones nítidos e centrados.
- **Injeção Cirúrgica e Não-Destrutiva:** Modifica apenas o bloco delimitado por marcadores (`/* --- TITLEBAR STYLER INICIO --- */`) em `~/.config/gtk-4.0/gtk.css` e `~/.config/gtk-3.0/gtk.css`. As tuas personalizações prévias de CSS permanecem 100% intactas.
- **Zero Parser Errors no GTK4:** Não utiliza `!important`. As regras utilizam seletores de alta especificidade (`window headerbar windowcontrols button`) compatíveis com o motor do GTK4/Libadwaita.
- **Recarregamento Seguro da Sessão:** Não força o encerramento abrupto de processos (`killall`) para evitar perda de dados em aplicações abertas. Em vez disso, dialoga com o gestor de sessão via `gnome-session-quit --logout`.
- **Distribuição Nativa RPM:** Desenvolvido e empacotado nativamente para Fedora Linux (via COPR).

---

## 🎨 Estilos e Ícones Disponíveis

1. **macOS (Símbolos no Hover):** Bolinhas perfeitamente circulares com as cores clássicas (Vermelho / Amarelo / Verde), revelando os símbolos de controlo (`×`, `−`, `+`) em contraste escuro ao passar o rato (estilo autêntico do macOS).
2. **macOS (Ícones Sempre Visíveis):** Círculos perfeitos com as cores clássicas e os ícones simbólicos permanentemente visíveis e legíveis.
3. **Minimalista (com Ícones):** Círculos translúcidos modernos que mantêm a visibilidade e clareza dos ícones (sem ocultar a identidade do botão).
4. **Contorno / Outline (Colorido):** Círculos com contorno fino e ícones simbólicos nas cores de ação (vermelho para fechar, amarelo para minimizar, verde para maximizar).
5. **Fluent / Moderno:** Estilo retangular suave com cantos arredondados (6px), ícones nítidos e destaque a vermelho no botão de fecho durante o hover.
6. **Minimalista Ghost (Oculto até ao Hover):** Botões discretos e translúcidos que apenas revelam os seus detalhes ao passar o cursor pela barra.
7. **Repor Padrão:** Remove todas as injeções e recupera de imediato os botões originais do Fedora/Adwaita.

---

## 📦 Instalação

### Opção 1: Via Fedora COPR (Recomendado)

O Titlebar Styler está disponível no Fedora COPR para instalação simples via gestor de pacotes `dnf`:

```bash
# 1. Ativar o repositório COPR
sudo dnf copr enable flaviomms/titlebar-styler

# 2. Instalar a aplicação
sudo dnf install titlebar-styler
```

### Opção 2: Instalação Manual (A partir do Código-Fonte)

Se preferires instalar diretamente a partir deste repositório Git:

#### Requisitos
```bash
sudo dnf install python3 python3-gobject gtk4 libadwaita gnome-session make
```

#### Compilação e Instalação
```bash
git clone https://github.com/flaviomms/titlebar-styler.git
cd titlebar-styler

# Testar as especificações e validações
make test

# Instalar no sistema
sudo make install
```

Para desinstalar:
```bash
sudo make uninstall
```

---

## 🚀 Como Utilizar

1. Abre a gaveta de aplicações do GNOME e pesquisa por **Titlebar Styler** (ou executa `titlebar-styler` no terminal).
2. Cada linha apresenta um indicador visual do aspeto dos botões e a sua descrição.
3. Escolhe o teu estilo preferido e clica em **Aplicar**.
4. Na janela de diálogo que surgir:
   - Clica em **Terminar Sessão Agora** para aplicar as alterações com segurança no gestor de sessão; ou
   - Clica em **Mais Tarde** se estiveres a trabalhar.
5. Para voltar às definições originais do sistema, basta aceder à secção **Repor Padrão** e clicar em **Restaurar**.

---

## 🛠️ Publicação no Fedora COPR

Para publicar no repositório COPR (`flaviomms/titlebar-styler`):

1. **Configurar o Repositório:** Acede a [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/) e cria o projeto `titlebar-styler`.
2. **Build via SCM:**
   - **Clone URL:** `https://github.com/flaviomms/titlebar-styler.git`
   - **Committish:** `main` (ou a tag `v1.0.0`)
   - **Spec file path:** `titlebar-styler.spec`
   - **Method:** `make_srpm` ou `rpkg`

---

## 📄 Licença

Este projeto é software livre licenciado sob a [GNU General Public License v3.0](LICENSE).
