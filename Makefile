load:
	python src/etl/loader.py

ratios:
	python src/etl/ratios.py

test:
	pytest tests/etl -v

report:
	python src/etl/report.py

dashboard:
	python src/etl/dashboard.py

api:
	python API_Assignment/convert_json_to_csv.py

clean:
	python -c "import shutil; shutil.rmtree('output', ignore_errors=True)"