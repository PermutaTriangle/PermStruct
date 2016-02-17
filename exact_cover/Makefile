ARCHIVE=lingeling-bal-2293bef-151109
EXE=lingeling
TAR=tar
PREFIX=/usr/local/bin

all: $(ARCHIVE)/$(EXE)
.PHONY: install uninstall all

$(ARCHIVE): $(ARCHIVE).tar.gz
	$(TAR) xvzf $(ARCHIVE).tar.gz

$(ARCHIVE)/$(EXE): $(ARCHIVE)
	cd $(ARCHIVE) && ./configure.sh && $(MAKE)

install: $(ARCHIVE)/$(EXE)
	install $(ARCHIVE)/$(EXE) $(PREFIX)/$(EXE)

uninstall:
	rm -f $(PREFIX)/$(EXE)

