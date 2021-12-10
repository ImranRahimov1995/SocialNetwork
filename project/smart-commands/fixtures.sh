mkdir media


cp -r fixtures/media/* media

python3 manage.py loaddata fixtures/all-data.json