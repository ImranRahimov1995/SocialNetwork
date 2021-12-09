export DJANGO_SETTINGS_MODULE=config.settings.local


cd ..
python3 -m venv venv
source venv/bin/activate
cd project/

pip3 install -r requirements.txt
python3 manage.py migrate --settings=config.settings.local
. ./smart-commands/fixtures.sh
python3 manage.py collectstatic --noinput
