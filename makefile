install:
	pip install -r reqirments.txt

format:
	black --preview  *.py

lint:
	pylint --disable=R,C main.py

