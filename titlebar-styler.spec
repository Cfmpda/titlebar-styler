Name:           titlebar-styler
Version:        1.0.0
Release:        1%{?dist}
Summary:        Personalizador de botões da barra de janelas para GNOME
Summary(en):    GNOME titlebar window controls styler

License:        GPL-3.0-or-later
URL:            https://github.com/flaviomms/titlebar-styler
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  appstream
BuildRequires:  python3-devel

Requires:       python3 >= 3.9
Requires:       python3-gobject
Requires:       gtk4
Requires:       libadwaita
Requires:       gnome-session
Requires:       hicolor-icon-theme

%description
O Titlebar Styler é uma aplicação nativa para o ambiente GNOME desenvolvida em
Python, GTK4 e Libadwaita. Permite personalizar os botões de controlo das
janelas (Minimizar, Maximizar e Fechar) de forma segura através da injeção
não-destrutiva de regras CSS em ~/.config/gtk-4.0/gtk.css e gtk-3.0/gtk.css.

%description -l en
Titlebar Styler is a native GNOME utility built with Python, GTK4, and
Libadwaita that lets users safely customize window titlebar buttons
(Minimize, Maximize, Close) using non-destructive CSS injection.

%prep
%autosetup -n %{name}-%{version}

%build
# Aplicação em Python interpretado; nada para compilar.

%install
%make_install PREFIX=%{_prefix}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/*.metainfo.xml || :

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/io.github.flaviomms.TitlebarStyler.svg
%{_datadir}/metainfo/io.github.flaviomms.TitlebarStyler.metainfo.xml

%changelog
* Mon Oct 12 2026 Flavio MMS <flaviomms@users.noreply.github.com> - 1.0.0-1
- Lançamento inicial para Fedora / COPR
- Suporte para temas macOS e Minimalista
- Injeção segura de CSS com marcadores
