from waitress import serve
import app as app
serve(app.app, host='0.0.0.0', port=8080)
