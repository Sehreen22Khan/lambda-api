from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'Hello from Khan!'

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Run the application on all available network interfaces
    app.run(host='0.0.0.0', port=5000)
