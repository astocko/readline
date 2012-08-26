.PHONY: test tests

tests test:
	@./tests.py

coverage:
	@nosetests tests.py --with-coverage --cover-erase --cover-package readline
