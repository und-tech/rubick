supertools: ## isntall supertools
	python3 -m pip install --user --upgrade setuptools wheel

setup: ## python setup
	python3 setup.py sdist bdist_wheel

twine: ## install twine
	python3 -m pip install --user --upgrade twine

upload-pypi-test: ## upload the package in pypi test
	@python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	@make clear

upload-pypi-production: ## upload the package in pypi production
	@python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
	@make clear

install-from-prod:
	@sudo python3 -m pip install --no-cache-dir ant

install-from-test: ## install package from pypi test
	@sudo python3 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ ant

install-from-source: ## install command for developer mode
	@sudo python3 setup.py install
	@make clear

remove: ## remove library
	@sudo pip3 uninstall ant-cli
	@make clear

clear: ## clear workspace
	@sudo rm -rf build dist ant_cli.egg-info


# Docker Commands #
build-docker:
	@docker build -f docker/Dockerfile --no-cache -t devlusaja/ant .

push-image:
	@docker push devlusaja/ant