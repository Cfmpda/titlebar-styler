PREFIX ?= /usr
BINDIR ?= $(PREFIX)/bin
DATADIR ?= $(PREFIX)/share

.PHONY: all install uninstall test

all:

install:
	install -d $(DESTDIR)$(BINDIR)
	install -m 755 bin/titlebar-styler $(DESTDIR)$(BINDIR)/titlebar-styler
	install -d $(DESTDIR)$(DATADIR)/applications
	install -m 644 data/titlebar-styler.desktop $(DESTDIR)$(DATADIR)/applications/
	install -d $(DESTDIR)$(DATADIR)/icons/hicolor/scalable/apps
	install -m 644 data/icons/hicolor/scalable/apps/io.github.flaviomms.TitlebarStyler.svg $(DESTDIR)$(DATADIR)/icons/hicolor/scalable/apps/
	install -m 644 data/icons/hicolor/scalable/apps/titlebar-styler.svg $(DESTDIR)$(DATADIR)/icons/hicolor/scalable/apps/
	install -d $(DESTDIR)$(DATADIR)/metainfo
	install -m 644 data/io.github.flaviomms.TitlebarStyler.metainfo.xml $(DESTDIR)$(DATADIR)/metainfo/

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/titlebar-styler
	rm -f $(DESTDIR)$(DATADIR)/applications/titlebar-styler.desktop
	rm -f $(DESTDIR)$(DATADIR)/icons/hicolor/scalable/apps/io.github.flaviomms.TitlebarStyler.svg
	rm -f $(DESTDIR)$(DATADIR)/icons/hicolor/scalable/apps/titlebar-styler.svg
	rm -f $(DESTDIR)$(DATADIR)/metainfo/io.github.flaviomms.TitlebarStyler.metainfo.xml

test:
	desktop-file-validate data/titlebar-styler.desktop
	appstreamcli validate --no-net data/io.github.flaviomms.TitlebarStyler.metainfo.xml
	python3 -m py_compile bin/titlebar-styler
