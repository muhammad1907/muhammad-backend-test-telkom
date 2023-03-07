import argparse
import json

parser = argparse.ArgumentParser(description='Command Line Tool untuk mengambil file log pada file system milik Linux pada folder /var/log')

parser.add_argument('file', help='Lokasi file log yang ingin diambil')
parser.add_argument('-t', '--type', choices=['text', 'json'], default='text', help='Jenis output yang diinginkan (default: text)')
parser.add_argument('-o', '--output', help='Lokasi file output yang diinginkan')
parser.add_argument('-v', '--verbose', action='store_true', help='Tampilkan pesan verbose')

args = parser.parse_args()

if args.verbose:
    print(f"Memproses file {args.file}...")

# baca file log
with open(args.file, 'r') as f:
    log_content = f.read()

# konversi ke JSON jika flag -t json digunakan
if args.type == 'json':
    log_content = [{'log': line.strip()} for line in log_content.split('\n') if line.strip()]
    log_content = json.dumps(log_content)

# menuliskan file output
if args.output:
    with open(args.output, 'w') as f:
        f.write(log_content)
else:
    print(log_content)