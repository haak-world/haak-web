.PHONY: build deploy clean preview

build:
	python3 build.py

deploy:
	python3 build.py --deploy

preview:
	python3 -m http.server 18840

clean:
	rm -f index.html .narrative-cache.json
	rm -rf people/
