.PHONY: test coverage

test:
	@nosetests

coverage:
	@nosetests --with-coverage --cover-erase
