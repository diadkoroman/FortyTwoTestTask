#/bin/sh
source django272/bin/activate
uwsgi --http :8000 --module fortytwo_test_task.wsgi 
#uwsgi --socket ../run/42test.sock --module ../fortytwo_test_task.wsgi --chmod-socket=664
