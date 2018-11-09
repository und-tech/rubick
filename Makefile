supertools: ## isntall supertools
	python3 -m pip install --user --upgrade setuptools wheel

setup: ## python setup
	python3 setup.py sdist bdist_wheel

twine: ## install twine
	python3 -m pip install --user --upgrade twine

upload-pypi-test: ## upload the package in pypi test
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install-test: ## install package from pypi test
	sudo python3 -m pip install --index-url https://test.pypi.org/simple/ rubick

install-developer: ## install command for developer mode
	sudo python3 setup.py install
	@make clear

remove: ## remove library
	sudo pip3 uninstall rubick
	@make clear

clear: ## clear workspace
	sudo rm -rf build dist rubick.egg-info


# Docker Commands #
build-docker:
	docker build -f docker/Dockerfile --no-cache -t devlusaja/rubick .