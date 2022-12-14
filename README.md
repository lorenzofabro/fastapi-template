# FastAPI Template

### About this template:
- ๐ณ Dockerized project.
- ๐ฎ Integrated with redis.
- ๐พ Logging configured.
- ๐งน Ready to be used with pre-commit, flake8 and isort.
- ๐๏ธ Requirements divided under three different categories: base, dev and test. This way allows you to only build what you need (e.g. only installing the base dependencies on a production environment).
- ๐ฅค To work with asynchronous requests, use the `BaseClient` class.
- ๐ To wrap an API call under the SSL protocols, use the `SSLAdapter` class.

---

### How to use it:
- โป๏ธ Clone the repo and run it with `docker compose up`.
- ๐จ Create all your APIs under the `apps` folder and then import your routes on the `config/main.py` file.
- โ๏ธ Create all your tests importing the test `client` that you can find on the `core/tests.py` file.
