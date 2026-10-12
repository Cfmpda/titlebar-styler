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
- **Injeção Cirúrgica e Não-Destrutiva:** Modifica apenas o bloco delimitado por marcadores (`/* --- TITLEBAR STYLER INICIO --- */`) em `~/.config/gtk-4.0/gtk.css` e `~/.config/gtk-3.0/gtk.css`. As tuas personalizações prévias de CSS permanecem 100% intactas.
- **Zero Parser Errors no GTK4:** Não utiliza `!important`. As regras utilizam seletores de alta especificidade (`window headerbar windowcontrols button`) compatíveis com o motor do GTK4/Libadwaita.
- **Recarregamento Seguro da Sessão:** Não força o encerramento abrupto de processos (`killall`) para evitar corrupção de ficheiros ou perda de dados em aplicações abertas. Em vez disso, dialoga com o gestor de sessão via `gnome-session-quit --logout`.
- **Distribuição Nativa RPM:** Desenvolvido e empacotado nativamente para Fedora Linux (via COPR), integrando-se diretamente com o ecossistema do sistema operativo sem contornos de sandboxing.

---

## 🎨 Estilos Disponíveis

1. **macOS:** Botões redondos estilizados com as cores clássicas (Vermelho / Amarelo / Verde), com efeitos suaves de realce em `:hover` e ícones ocultados.
2. **Minimalista:** Círculos translúcidos subtis baseados na cor de texto ativa (`currentColor`), integrando-se perfeitamente com qualquer paleta Clara ou Escura do GNOME.
3. **Restaurar Padrão:** Remove de imediato as regras personalizadas e recupera o visual original do Fedora/Adwaita.

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

# Testar as especificações
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
2. Escolhe o teu estilo preferido e clica em **Aplicar**.
3. Na janela de diálogo que surgir:
   - Clica em **Terminar Sessão Agora** para aplicar as alterações de imediato a todas as janelas; ou
   - Clica em **Mais Tarde** se estiveres a meio de tarefas importantes.
4. Para voltar às definições originais de fábrica, basta aceder à secção **Repor Padrão** e clicar em **Restaurar**.

---

## 🛠️ Guia do Programador: Publicar no Fedora COPR

Para publicar uma nova versão no teu repositório COPR (`flaviomms/titlebar-styler`):

### 1. Criar o Projeto no COPR
1. Acede a [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/) e autentica-te com a tua conta FAS (Fedora Account System).
2. Clica em **New Project** e define o nome como `titlebar-styler`.
3. Escolhe as arquiteturas alvo (ex: Fedora 43, 44, Rawhide em `x86_64` e `aarch64`).

### 2. Configurar Build Automático via Git SCM
1. Na página do projeto no COPR, vai a **Builds** -> **New Build** -> aba **SCM**.
2. Preenche os campos:
   - **Clone URL:** `https://github.com/flaviomms/titlebar-styler.git`
   - **Committish:** `main` (ou a tag `v1.0.0`)
   - **Spec file path:** `titlebar-styler.spec`
   - **Source build type:** `rpkg` ou `make srpm`
3. Clica em **Build**.

O COPR irá gerar automaticamente os pacotes RPM e disponibilizá-los aos utilizadores do Fedora.

---

## 📄 Licença

Este projeto é software livre licenciado sob a [GNU General Public License v3.0](LICENSE).
