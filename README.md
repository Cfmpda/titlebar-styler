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

A aplicação inclui agora dois modos de utilização através de abas no topo da janela (`Adw.ViewSwitcher`):
1. **Modelos Prontos:** Estilos pré-configurados prontos a aplicar com um clique.
2. **Personalizador:** Editor interativo com pré-visualização ao vivo (*Live Preview*) para criar estilos personalizados sob medida.

### 🛡️ Princípios Técnicos & Segurança
- **Geometria Perfeita 1:1:** Cálculo dinâmico das margens de compensação para evitar que o GTK4 deforme ou estique os botões verticalmente. Garante círculos e quadrados matematicamente simétricos em qualquer dimensão (de 10px a 26px).
- **Injeção Cirúrgica e Não-Destrutiva:** Modifica apenas o bloco delimitado por marcadores (`/* --- TITLEBAR STYLER INICIO --- */`) em `~/.config/gtk-4.0/gtk.css` e `~/.config/gtk-3.0/gtk.css`. As tuas personalizações prévias de CSS permanecem 100% intactas.
- **Zero Parser Errors no GTK4:** Não utiliza `!important`. As regras utilizam seletores de alta especificidade (`window headerbar windowcontrols button`) compatíveis com o motor do GTK4/Libadwaita.
- **Recarregamento Seguro da Sessão:** Não força o encerramento abrupto de processos (`killall`) para evitar perda de dados em aplicações abertas. Em vez disso, dialoga com o gestor de sessão via `gnome-session-quit --logout`.
- **Distribuição Nativa RPM:** Desenvolvido e empacotado nativamente para Fedora Linux (via COPR).

---

## 🎨 Funcionalidades

### 1. Modelos Prontos (Presets)
- **macOS (Símbolos no Hover):** Círculos com as cores clássicas da Apple que revelam os símbolos (`×`, `−`, `+`) em contraste escuro ao passar o cursor.
- **macOS (Ícones Sempre Visíveis):** Círculos perfeitos com as cores do macOS e ícones simbólicos permanentemente visíveis.
- **Minimalista (com Ícones):** Círculos translúcidos elegantes com ícones que se adaptam aos temas claro e escuro.
- **Contorno / Outline (Colorido):** Círculos com borda fina e ícones nas cores de ação (vermelho, amarelo, verde).
- **Fluent / Moderno:** Cantos arredondados suaves (6px), ícones nítidos e destaque a vermelho no botão de fechar durante o hover.
- **Minimalista Ghost (Oculto até ao Hover):** Botões ultradiscretos que apenas se revelam ao aproximar o rato.
- **Repor Padrão:** Restaura os botões originais do Fedora/Adwaita.

### 2. Personalizador Interativo (Live Editor)
- **Pré-Visualização em Tempo Real:** Uma barra de janelas de teste no topo que reage instantaneamente aos ajustes e permite testar o *hover*.
- **Dimensões e Formato:**
  - Tamanho dos Botões (10px a 26px).
  - Formato: *Círculo Perfeito*, *Cantos Arredondados (6px)*, *Quadrado (0px)* ou *Curvatura Personalizada*.
  - Tamanho dos Ícones internos (6px a 20px).
  - Espaçamento horizontal entre botões (1px a 14px).
- **Paleta de Cores:**
  - Cores de fundo e cores do ícone para cada botão (Fechar, Minimizar, Maximizar) usando o `Gtk.ColorDialogButton` nativo.
  - Opção de borda/contorno com cor e espessura ajustáveis.
- **Comportamentos no Hover:**
  - Visibilidade dos Ícones: *Símbolos no Hover*, *Sempre Visíveis* ou *Ocultar Ícones*.
  - Efeitos de Cor no Hover: *Escurecer suavemente*, *Iluminar / Clarear* ou *Sem efeito*.

---

## 📦 Instalação

### Opção 1: Via Fedora COPR (Recomendado)

```bash
# 1. Ativar o repositório COPR
sudo dnf copr enable flaviomms/titlebar-styler

# 2. Instalar a aplicação
sudo dnf install titlebar-styler
```

### Opção 2: Instalação Local no Sistema (A partir do Código-Fonte)

```bash
git clone https://github.com/flaviomms/titlebar-styler.git
cd titlebar-styler

# Testar as validações
make test

# Instalar no sistema
sudo make install
```

Para atualizar após alterações no código:
```bash
sudo make install
```

Para desinstalar:
```bash
sudo make uninstall
```

---

## 🚀 Como Utilizar

1. Abre o **Titlebar Styler** a partir da gaveta de aplicações do GNOME (ou executa `titlebar-styler` no terminal).
2. Na aba **Modelos**, podes escolher um dos estilos predefinidos e clicar em **Aplicar**.
3. Na aba **Personalizar**, podes ajustar cada detalhe visual ao teu gosto, testar o hover na pré-visualização e clicar em **Aplicar no Sistema**.
4. Quando surgir a janela de diálogo:
   - Clica em **Terminar Sessão Agora** para que todas as aplicações assumam o visual em segurança; ou
   - Clica em **Mais Tarde** se estiveres a trabalhar.
5. Para restaurar o visual de fábrica a qualquer momento, basta aceder a **Repor Padrão** e clicar em **Restaurar**.

---

## 📄 Licença

Este projeto é software livre licenciado sob a [GNU General Public License v3.0](LICENSE).
