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

O **Titlebar Styler** é uma aplicação nativa rápida e elegante projetada para permitir que os utilizadores do GNOME (incluindo GNOME 51 / Fedora 44+) personalizem o aspeto e comportamento dos controlos de janelas (**Fechar**, **Minimizar**, **Maximizar**), sem quebrar a integridade do sistema ou causar conflitos de temas.

A aplicação inclui dois modos de utilização através de abas no topo da janela (`Adw.ViewSwitcher`):
1. **Modelos Prontos:** Estilos pré-configurados prontos a aplicar com um clique.
2. **Personalizar:** Editor interativo com pré-visualização ao vivo (*Live Preview*) para desenhar botões sob medida com geometrias avançadas, formas vetoriais e suporte a ficheiros SVG próprios.

### 🛡️ Princípios Técnicos & Segurança
- **Disposição Segura via GSettings Mutter:** O posicionamento dos botões (esquerda, direita ou divididos) e a sua ativação/desativação utilizam a API oficial `org.gnome.desktop.wm.preferences button-layout`, aplicando-se instantaneamente no sistema com 100% de estabilidade.
- **Geometria Perfeita 1:1:** Cálculo dinâmico das margens de compensação para evitar que o GTK4 deforme os botões. Garante simetria exata em qualquer dimensão (de 10px a 26px).
- **Formas Vetoriais e Importação de SVGs:** Suporte para polígonos vetoriais dinâmicos (hexágonos, estrelas, diamantes, escudos) e importação de ficheiros SVG personalizados tanto para as formas como para os ícones.
- **Injeção Cirúrgica e Não-Destrutiva:** Modifica apenas o bloco delimitado por marcadores (`/* --- TITLEBAR STYLER INICIO --- */`) em `~/.config/gtk-4.0/gtk.css` e `~/.config/gtk-3.0/gtk.css`. As tuas personalizações prévias de CSS permanecem 100% intactas.
- **Zero Parser Errors no GTK4:** Não utiliza `!important`. As regras utilizam seletores de alta especificidade (`window headerbar windowcontrols button`).
- **Recarregamento Seguro da Sessão:** Sugestão de logout seguro via `gnome-session-quit --logout`.

---

## 🎨 Funcionalidades

### 1. Modelos Prontos (Presets)
- **macOS (Símbolos no Hover):** Círculos com as cores clássicas da Apple no lado esquerdo que revelam os símbolos (`×`, `−`, `+`) em contraste escuro ao passar o cursor.
- **macOS (Ícones Sempre Visíveis):** Círculos com as cores do macOS e ícones simbólicos permanentemente visíveis.
- **Minimalista (com Ícones):** Círculos translúcidos elegantes com ícones que se adaptam aos temas claro e escuro.
- **Contorno / Outline (Colorido):** Círculos com borda fina e ícones nas cores de ação (vermelho, amarelo, verde).
- **Fluent / Moderno:** Cantos arredondados suaves (6px), ícones nítidos e destaque a vermelho no botão de fechar durante o hover.
- **Minimalista Ghost (Oculto até ao Hover):** Botões ultradiscretos que apenas se revelam ao aproximar o rato.
- **Repor Padrão:** Restaura os botões originais do Fedora/Adwaita e a sua posição nativa.

### 2. Personalizador Interativo (Live Editor)
- **Pré-Visualização em Tempo Real:** Uma barra de janelas reativa que mostra os botões a moverem-se entre a esquerda e a direita, desaparecerem quando desativados e reagirem ao passar o rato (*hover*).
- **Editor de Formato Estilo Nova Launcher (4 Cantos Independentes):**
  - **Arquetipos Rápidos:** Círculo (`9999px`), Squircle (`8px`), Arredondado (`6px`), Quadrado (`0px`), Folha/Gota (`14px 0px 14px 0px`) e Apenas Ícone.
  - **Bloqueio / Ligação de Cantos (Link Switch):** Altere todos os 4 cantos em uníssono ou desbloqueie para definir independentemente:
    - *Canto Superior Esquerdo (TL)*
    - *Canto Superior Direito (TR)*
    - *Canto Inferior Direito (BR)*
    - *Canto Inferior Esquerdo (BL)*
  - Permite criar facilmente qualquer geometria híbrida: gotas, escudos, cantos cortados ou formas personalizadas.
- **Sincronização com a Cor de Destaque do GNOME (Accent Color):**
  - Com um clique, sincroniza os botões com a cor de destaque atual do sistema (`org.gnome.desktop.interface accent-color`), integrando perfeitamente com o tema Adwaita do utilizador.
- **Profundidade, Sombras e Efeito Neon (Box-Shadow):**
  - **Elevação 3D Suave:** Adiciona profundidade e relevo com sombra sutil aos botões.
  - **Brilho Neon (Glow):** Projeção luminosa suave calculada com a própria cor de cada botão.
  - Controlo do raio de desfoque (Blur Radius) de 1px a 16px.
- **Biblioteca de Perfis de Utilizador:**
  - Guarde as suas criações como perfis personalizados com nome próprio (`~/.config/titlebar-styler/profiles.json`).
  - Carregue ou apague perfis guardados diretamente na aba "Modelos".
- **Exportar e Importar Temas (.styler / JSON):**
  - Partilhe e faça cópia dos seus temas através de ficheiros JSON portáteis com diálogo nativo de ficheiros (`Gtk.FileDialog`).
- **Segurança com Cópia de Segurança Automática (Backup):**
  - Antes de qualquer alteração, o `Titlebar Styler` cria automaticamente uma cópia em `~/.config/gtk-4.0/gtk.css.styler.bak`.
  - Botão de restauro com 1 clique para reverter imediatamente para o estado anterior.
- **Importação de Ícones Próprios (SVG):**
  - Seleção de ficheiros SVG personalizados para **Fechar**, **Minimizar** e **Maximizar**.
  - Reposição dos ícones padrão do sistema a qualquer momento.
- **Posição e Visibilidade dos Botões:**
  - Ativar ou desativar individualmente qualquer botão (**Fechar**, **Minimizar**, **Maximizar**).
  - Escolher o lado de cada botão: **Esquerda** ou **Direita** (permitindo separar botões livremente).
  - Atalhos pré-definidos (Todos à Direita, Todos à Esquerda, Separados).
- **Dimensões e Formato:**
  - Tamanho dos Botões (10px a 26px).
  - Tamanho dos Ícones internos (6px a 20px).
  - Espaçamento horizontal entre botões (1px a 14px).
- **Paleta de Cores:**
  - Cores de fundo e cores do ícone para cada botão usando o `Gtk.ColorDialogButton` nativo.
  - Opção de borda/contorno com cor e espessura ajustáveis.
- **Comportamentos no Hover:**
  - Visibilidade dos Ícones: *Símbolos no Hover*, *Sempre Visíveis* ou *Ocultar Ícones*.
  - Efeitos no Hover:
    - *Escurecer suavemente*
    - *Iluminar / Clarear*
    - *Realce de Fundo Suave (Rodela no Hover)* (ideal para o modo "Apenas Ícone")
    - *Cor Personalizada no Hover* (com seletores de cor individuais)
    - *Sem efeito*

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

# Instalar ou atualizar no sistema
sudo make install
```

Para desinstalar:
```bash
sudo make uninstall
```

---

## 🚀 Como Utilizar

1. Abre o **Titlebar Styler** a partir da gaveta de aplicações do GNOME (ou executa `titlebar-styler` no terminal).
2. Na aba **Modelos**, podes aplicar um dos estilos prontos com 1 clique.
3. Na aba **Personalizar**:
   - Escolhe uma forma da lista (ou importa o teu próprio SVG).
   - Opcionalmente, importa os teus próprios ícones SVG para Fechar, Minimizar e Maximizar.
   - Ativa/desativa os botões que desejas exibir e escolhe se ficam à esquerda ou à direita.
   - Ajusta as dimensões do botão e dos ícones.
   - Escolhe as cores normais e o comportamento/cores durante o hover.
   - Testa tudo na **Pré-Visualização** no topo.
   - Clica em **Aplicar no Sistema**.
4. Quando surgir a janela de confirmação de sessão, podes terminar sessão de imediato ou mais tarde.
5. Para restaurar o visual original do sistema a qualquer altura, basta clicar em **Restaurar** na secção **Repor Padrão**.

---

## 📄 Licença

Este projeto é software livre licenciado sob a [GNU General Public License v3.0](LICENSE).
