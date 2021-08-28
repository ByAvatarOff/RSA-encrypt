"""
RSA decryption
If you want decrypt your txt file
locate it and private key to the folder
with this python file
Decrypted text will be placed in the file
named decyphertext.txt
"""
import pyasn1.error
import binascii
import base64
import rsa


class RSADecrypt:
    def __init__(self, name_file):
        self.name_file = name_file

    def read_encrypt_text(self):
        """
        Read encrypt text file and return it in bytes
        """
        try:
            with open(self.name_file, 'rb') as f:
                cypher = f.read()
            return cypher
        except FileNotFoundError:
            print('Encrypted file not found')
            return None

    def open_private_public_keys(self):
        """
        Open pem file with private key
        """
        try:
            with open('private.pem', 'rb') as privatefile:
                p = privatefile.read()
                privkey = rsa.PrivateKey.load_pkcs1(p)
            return privkey
        except FileNotFoundError:
            print('File with private key in pem format not found')
            return None

    def write_encrypt_message_to_file(self, encrypt_message):
        """
        Write decrypt text in txt file
        """
        with open('decyphertext.txt', 'wb') as f:
            f.write(bytes(encrypt_message))

    def main(self):
        """
        Function decodes to b64 encoding text file and decrypt it
        write decrypt text to txt file
        """
        try:
            encrypt_text = self.read_encrypt_text()
            privat_key = self.open_private_public_keys()
            if encrypt_text and privat_key:
                crypto = base64.b64decode(encrypt_text)
                message = rsa.decrypt(crypto, privat_key)
                self.write_encrypt_message_to_file(message)
        except binascii.Error:
            print('Invalid decrypt text')
        except pyasn1.error.SubstrateUnderrunError:
            print('Invalid private key')


if __name__ == '__main__':
    name_enter_file = str(input('Enter name file with it format. Example - test.txt \n'))
    print('Decryption started')
    rsa_class = RSADecrypt(name_enter_file)
    rsa_class.main()
    print('Success decrypt')
