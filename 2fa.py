from time import time
from hmac import new as hmac_new
from hashlib import sha1
from base64 import b32decode
from struct import pack, unpack

def generate_totp(secretKey, timeWindow=30, digitCount=6):
    secretKey = secretKey.strip().replace(" ", "").upper()
    while len(secretKey) % 8:
        secretKey += '='
    
    keyBytes = b32decode(secretKey)
    
    currentTime = int(time())
    timeCounter = currentTime // timeWindow
    timeBytes = pack(">Q", timeCounter)
    
    hmacResult = hmac_new(keyBytes, timeBytes, sha1).digest()
    
    startPosition = hmacResult[-1] & 0x0F
    codeBytes = hmacResult[startPosition:startPosition + 4]
    
    codeNumber = unpack(">I", codeBytes)[0] & 0x7FFFFFFF
    otpValue = codeNumber % (10 ** digitCount)
    
    return str(otpValue).zfill(digitCount)

if __name__ == "__main__":
    userSecret = input("Enter your secret key: ")
    totpCode = generate_totp(userSecret)
    print(f"Your TOTP code: {totpCode}")