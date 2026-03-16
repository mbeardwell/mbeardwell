.PHONY: automation
automation:
	make dev
	make clean

.PHONY: dev
dev:
	sudo apt install -y python3 python3-venv python3-pip
	make venv
	src/venv/bin/python3 -m pip install -r requirements.txt && \
	src/venv/bin/python3 src/readme.py

.PHONY: venv
venv:
	if [ ! -d ./src/venv ]; then \
		python3 -m venv src/venv; \
	fi

.PHONY: clean
clean:
	rm -rf src/__pycache__ src/components/__pycache__ src/venv
