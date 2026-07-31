def main():
    file = input('File: ').strip().lower()
    print(files_media(file))

def files_media(f):
    if f.endswith('.gif'):
        return 'image/gif'
    elif f.endswith('.png'):
        return 'image/png'
    elif f.endswith('.jpeg') or f.endswith('.jpg'):
        return 'image/jpeg'
    elif f.endswith('.pdf'):
        return 'application/pdf'
    elif f.endswith('.txt'):
        return 'text/plain'
    elif f.endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'

main()