# Cryptography via Fernet in Python
### A useful little program to encrypt/decrypt messages and generate keys.

A simple, class based, wrapper for the Fernet Cryptography module.  Fernet encryption is one of the most secure ways to encrypt a message. Per the documentation, the **only** way to read the message is to have the *secret* key.  

You can find more information about the encryption method [here](https://cryptography.io/en/latest/fernet.html).

Installation instructions for the Cryptography package found at https://cryptography.io/en/latest/installation.html

---

### Usage

Create an encrypted message:
```python
secret = Cryptography()
message = secret.encrypt_message('Highly classified message!')
```

Decrypt a message: 
- You will need the secret key that encoded the message stored in a file
```python
secret = Cryptography('secret.key')
message = b'gAAAAABgJDybBjk_n-KXci4Ri8w_y1s1QN3yehVymhAP4hlgrf_marbifFko0Ynvs_xgX2ZOpLEo7Gmj7fUDsQizcyNaR3uX5cSsFntVXCOPy0_XmO5_k04='
message = secret.decrypt_message(message)
print(message)
  # Highly classified message!
```
