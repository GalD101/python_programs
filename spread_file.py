from time import sleep

CHUNK_SIZE = 1_100_000_000
file_number = 1
offset = 0
with open('YOUR_FILE_NAME', 'rb') as f:
    f.seek(offset)
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        print("file_iteration: " + str(file_number))
        sleep(5)
        with open('part_' + str(file_number), 'wb') as chunk_file:
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)
    offset += CHUNK_SIZE

