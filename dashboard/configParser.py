import configparser
from configparser_crypt import ConfigParserCrypt
from cryptography.fernet import Fernet
from io import StringIO

# Create an instance of ConfigParserCrypt
config_crypt = ConfigParserCrypt()

# Generate a secret key for encryption and decryption
secret_key = Fernet.generate_key()

# Create a sample configuration
config = configparser.ConfigParser()
config['client_details'] = {
    'username':'ranjith',
    'userpwd':'ranjith2022',
    'port' : '1521',
    'dsn':'192.168.161.200/RMSDEV'
}  
# Create a Fernet cipher using the secret key
cipher = Fernet(secret_key)

# Convert the configuration to a string
config_io = StringIO()
config.write(config_io)
config_string = config_io.getvalue()

# Encrypt the configuration string
encrypted_config = cipher.encrypt(config_string.encode()).decode()

# Save the encrypted configuration to a file
with open('secret.key', 'wb') as key_file:
    key_file.write(secret_key)

with open('encrypted_client_details.ini', 'w') as encrypted_file:
    encrypted_file.write(encrypted_config)

# from cryptography.fernet import Fernet

# # Generate a key to use for encryption/decryption (store this securely)
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)

# # Encrypt the credentials
# username = 'ranjith'
# password = 'ranjith2022'

# encrypted_username = cipher_suite.encrypt(username.encode())
# encrypted_password = cipher_suite.encrypt(password.encode())

# # Save the encrypted credentials to a file
# with open('encrypted_credentials.ini', 'wb') as f:
#     f.write(encrypted_username)
#     f.write(b'\n')  # Add a separator if needed
#     f.write(encrypted_password)

# # Decrypt the credentials (in your Streamlit app)
# with open('encrypted_credentials.ini', 'rb') as f:
#     encrypted_username = f.readline().strip()
#     encrypted_password = f.readline().strip()

# decrypted_username = cipher_suite.decrypt(encrypted_username).decode()
# decrypted_password = cipher_suite.decrypt(encrypted_password).decode()

# # Use decrypted credentials to establish the database connection
# # (Modify your database connection code accordingly)
