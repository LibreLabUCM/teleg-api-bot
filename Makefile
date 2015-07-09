# makefile of teleg-api-bot proyect


install:
	@sudo python3 setup.py install

uninstall:
	@sudo pip uninstall teleg-api-bot

upload:
	@python3 setup.py sdist upload -r pypi


test_upload:
	@python3 setup.py sdist upload -r test


clean:
	rm -rf build/ dist/ teleg_api_bot.egg-info/
	rm -rf telegapi/__pycache__
