import os

from server import app

app.run(host=os.environ['IP'], port=int(os.environ['PORT']), debug=True)
