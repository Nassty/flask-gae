import sys

yaml = """application: "%s"
version: 1
runtime: python
api_version: 1

handlers:
- url: .*
  script: main.py
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <app_key>" % sys.argv[0]
        sys.exit(1)
    handler = open("app.yaml", "w")
    handler.write(yaml % " ".join(sys.argv[1:]))
    handler.close()
    sys.exit(0)

