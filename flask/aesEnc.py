from cryptography.fernet import Fernet
key = b'm02cpfnVJXZ0VEenepvtjt4BUtF2dr67EGc9sX8qNEI='
cipher_suite = Fernet(key)

def encrypt_large_file(input_file_path, output_file_path):
    chunk_size = 64 * 1024  # 64 KB chunk size, you can adjust this according to your needs

    with open(input_file_path, 'rb') as infile:
        with open(output_file_path, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if not chunk:
                    break
                encrypted_chunk = cipher_suite.encrypt(chunk)
                #print(len(encrypted_chunk).to_bytes(4,'big'))
                outfile.write(len(encrypted_chunk).to_bytes(4,'big'))
                outfile.write(encrypted_chunk)

def decrypt_large_file(input_file_path, output_file_path, key):
    cipher_suite = Fernet(key)
    chunk_size = 64 * 1024  # 64 KB chunk size, should match with encryption
    
    with open(input_file_path, 'rb') as infile:
        with open(output_file_path, 'wb') as outfile:
            while True:
                csize = infile.read(4)
                chunk_size = int.from_bytes(csize, "big")
                #print(chunk_size)
                chunk = infile.read(chunk_size)
                if not chunk:
                    break
                decrypted_chunk = cipher_suite.decrypt(chunk)
                outfile.write(decrypted_chunk)
                


#encrypt_large_file("02.mp4","lol.enc")
#decrypt_large_file("lol.enc","dec.mp4",key)