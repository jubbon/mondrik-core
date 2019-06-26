all:
	docker-compose --file source/docker-compose.yml run mondrik pyinstaller /usr/src/pyinstaller/mondrik.spec

install:
	install ./dist/mondrik /usr/local/bin

uninstall:
	rm -rf /usr/local/bin/mondrik