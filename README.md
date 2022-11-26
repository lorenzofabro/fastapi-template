# FastAPI Template

### About this template:
- 🐳 Dockerized project.
- 🏮 Integrated with redis.
- 💾 Logging configured.
- 🧹 Ready to be used with pre-commit, flake8 and isort.
- 🗃️ Requirements divided under three different categories: base, dev and test. This way allows you to only build what you need (e.g. only installing the base dependencies on a production environment).
- 🥤 To work with asynchronous requests, use the `BaseClient` class.
- 🎈 To wrap an API call under the SSL protocols, use the `SSLAdapter` class.

---

### How to use it:
- ♻️ Clone the repo and run it with `docker compose up`.
- 🎨 Create all your APIs under the `apps` folder and then import your routes on the `config/main.py` file.
- ⚙️ Create all your tests importing the test `client` that you can find on the `core/tests.py` file.
