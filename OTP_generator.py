import secrets

def generate_otp(length=6): 
    return ''.join(str(secrets.randbelow(10)) for _ in range(6))

print("Generated OTP:", generate_otp())