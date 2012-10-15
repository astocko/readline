.PHONY: test test-coverage

test:
	@nosetests

test-coverage:
	@nosetests --with-coverage --cover-erase --cover-package=readline
