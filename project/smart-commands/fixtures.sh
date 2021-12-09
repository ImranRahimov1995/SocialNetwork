mkdir media


cp fixtures/media/* media

python3 manage.py loaddata fixtures/all-test-dumps.json