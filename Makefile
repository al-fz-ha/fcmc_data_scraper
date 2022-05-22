# this is the makefile

run:
	python3 scraper/scraper1.py

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

