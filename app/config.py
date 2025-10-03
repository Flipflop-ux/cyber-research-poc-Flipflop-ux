# demo insecure config (benign dummy)
# Do NOT use in production

SECRET_KEY = "DUMMY_SECRET_12345"   # <-- intentionally insecure example
DATABASE_URL = "postgres://user:password@localhost:5432/demo_db"
