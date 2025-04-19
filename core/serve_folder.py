import os
import http.server
import socketserver
import argparse


def serve(directory):
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8000), handler) as httpd:
        print(f"Serving {directory} at http://localhost:8000")
        httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description="Serve a webpage from a folder.")
    parser.add_argument(
        "path",
        nargs="?",
        help="The path to the folder to serve. If not provided, you will be prompted.",
    )
    args = parser.parse_args()

    if args.path:
        folder_path = args.path
    else:
        folder_path = input("Please provide the path to the folder you want to serve: ")

    if not os.path.isdir(folder_path):
        print(f"The path '{folder_path}' is not valid or is not a directory.")
        return

    serve(folder_path)


if __name__ == "__main__":
    main()
