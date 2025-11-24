import http.server
import socketserver
import os
import sys

# Configuration
PORT = 8080
BUILD_DIR = "build"

def run_server():
    # Check if build directory exists
    if not os.path.exists(BUILD_DIR):
        print(f"Error: Build directory '{BUILD_DIR}' not found.")
        print("Please run 'python3 build.py' first to generate the build.")
        return

    # Change to build directory to serve from there
    os.chdir(BUILD_DIR)

    # Create handler
    Handler = http.server.SimpleHTTPRequestHandler

    # Allow port reuse to avoid "Address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving '{BUILD_DIR}' directory at http://localhost:{PORT}")
            print("Press Ctrl+C to stop the server.")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 48:
            print(f"Error: Port {PORT} is already in use.")
            print("Try stopping other servers or change the PORT in server.py.")
        else:
            print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    run_server()
