"""
RSA encryption
If you want encrypt your txt file
locate it to the folder
with this python file
Encrypted text will be placed in the file
named cyphertext.txt
"""
import rsa
import base64


class RSAEncrypt:
    def __init__(self, name_file):
        self._public_key, self._privat_key = rsa.newkeys(4096)
        self.name_file = name_file
        self.text_string = ''

    def read_encrypted_text(self):
        """
        Read text file and return it in bytes
        """
        try:
            with open(self.name_file, 'r') as f:
                for line in f:
                    self.text_string += line
            return self.text_string.encode('utf-8')
        except FileNotFoundError:
            print('File with enters name not found in folder\n')
            return None

    def write_encrypt_message_to_file(self, encrypt_message):
        """
        Write encrypted text to cyphertext.txt file
        """
        with open('cyphertext.txt', 'wb') as f:
            f.write(bytes(encrypt_message))

    def write_public_private_keys(self):
        """
        Write write public and private_keys to files
        with format pem
        """
        public = self._public_key.save_pkcs1()
        private = self._privat_key.save_pkcs1()
        with open('public.pem', 'wb') as pubfile:
            pubfile.write(public)
        with open('private.pem', 'wb') as prifile:
            prifile.write(private)

    def main(self):
        """
        Function encrypt bytes text, encodes it to b64 encoding
        write it to file and write public and private keys to file
        """
        try:
            text = self.read_encrypted_text()
            if text:
                encrypt_message = rsa.encrypt(text, self._public_key)
                crypto_message = base64.b64encode(encrypt_message)
                self.write_encrypt_message_to_file(crypto_message)
                self.write_public_private_keys()
        except OverflowError:
            print('Your text is too large. Try reduce text or '
                  'change size of keys.\nIn constructor you '
                  'can change number on `rsa.newkeys(2048)` string '
                  'for a larger one')
            return None


if __name__ == '__main__':
    name_enter_file = str(input('Enter name file with it format. Example - test.txt \n'))
    print('Encryption started')
    rsa_class = RSAEncrypt(name_enter_file)
    rsa_class.main()
    print('Success encrypt')