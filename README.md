# Opentracing

This tutorial runs a python application, which is calling http://wwww.google.com, http://www.bing.com, and http://fr.yahoo.com.

The application sends traces of requests to a jaeger application.

## Getting Starting


1. Clone repository :

```bash
$ git clone https://github.com/ferreolgodebarge/opentracing.git

$ cd opentracing
```

2. Run jaeger

```bash
$ ./jaeger/jaeger-all-in-one
```

3. Run application

```bash
$ virtualenv venv

$ source venv/bin/activate

(venv) $ pip install -r requirements.txt

(venv) $ python app.py 8080
```

4. Go to http://localhost:8080/

5. Execute the endpoint /search_site

6. Go to http://localhost:16686/

7. Choose `Service` > `fake provider` and click on `Find Traces`
