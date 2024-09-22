import requests
import argparse
import sys
import os

from concurrent.futures import ThreadPoolExecutor

API_URL = "http://path/to/api/service"

def authenticate(credentials: dict):
    response = requests.post(f'{API_URL}/auth', data=credentials)
    if response.get('error'):
        print(f'authentication failed: {response.get('error')}')
        return
    
    token = response.json().get('token', '')
    if token == '':
        print(f'token is empty. check response: {response}')
        return
    return token

def upload_file(token: str, file_path: str):
    headers = {'Authorization': f'Bearer: {token}'}
    with open(file_path, 'rb') as file:
        response = requests.post(f'{API_URL}/upload', headers=headers, files=file)
        if response.get('error'):
            print(f'failed to upload a file: {response.get('errir')}')
            return
        doc_id = response.json().get('doc_id')
        if doc_id == '':
            print(f'doc_id is empty. check response: {response}')
            return
        return doc_id

def upload_files(token: str, file_paths: list):
    doc_ids = []

    def upload(file_path: str):
        doc_id = upload_file(token, file_path)
        doc_ids.append(doc_id)

    with ThreadPoolExecutor(max_worker=5) as executor:
        executor.map(upload, file_paths)

    return doc_ids

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to file operation to an API")

    parser.add_argument('-u', '--username', type=str, required=True, help='API username')
    parser.add_argument('-p', '--password', type=str, required=True, help='API password')
    parser.add_argument('-f', '--file', type=str, help='File to upload')
    parser.add_argument('-d', '--directory', type=str, help='Directory that containing the list of files to upload')
    args = parser.parse_args()

    if args.file == "" | args.directory == "":
        print("\nenter a file or dictionary")
        sys.exit(0)

    token = authenticate(credentials=dict(user="username", secret="secret"))
    if args.file != "":
        doc_id = upload_file(token, args.file)
        print(f'uploaded document ID {doc_id}')

    if args.dictionary != "":
        file_paths = [f for f in os.listdir(args.directory) if os.path.isfile(os.path.join(args.directory, f))]
        doc_ids = upload_files(token, file_paths)
        print(f'uploaded document IDs {doc_ids}')

