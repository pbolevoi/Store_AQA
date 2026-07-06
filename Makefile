test-api:
	pytest tests/test_api.py -v --alluredir=allure-results

test-ui:
	pytest tests/test_ui.py -v --alluredir=allure-results

test-all:
	pytest -v --alluredir=allure-results

report:
	allure generate \
	allure-results \
	--clean \
	-o allure-report

open:
	allure open allure-report

clean:
	rm -rf allure-results
	rm -rf allure-report
	rm -rf screenshots

lint:
	ruff check .


format:
	black .