1)http://127.0.0.1:8000/api/metrics/?col=channel,country,impressions,clicks&date_to=2017-06-01&group_by=channel,country&order_by=clicks&sort=desc;
2)http://127.0.0.1:8000/api/metrics/?col=installs,date&date_of=2017-05-01&date_to=2017-05-31&os=ios&group_by=date&order_by=date&sort=asc;
3)http://127.0.0.1:8000/api/metrics/?col=revenue,os&date_of=2017-06-01&date_to=2017-06-01&country=US&group_by=os&order_by=revenue&sort=desc;
4)http://127.0.0.1:8000/api/metrics/?col=cpi,channel&country=CA&group_by=channel&order_by=cpi&sort=desc;

To fill the database, you need to specify the address
of the csv-file in the tsk/parser.py file and then start the application and go to http://127.0.0.1:8000/
