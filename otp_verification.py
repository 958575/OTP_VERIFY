import random
#random package for generating the different otp value or number.

def generate_otp():
    return random.randint(1000,9999)
def send_otp(phone_number,otp):
    print(f"OTP sent to {phone_number}:  {otp}")
#implement the code to send otp by SMS or EMAIL.    
    
def verify_otp(entered_otp,generated_otp):
    return entered_otp==generated_otp


phone_number=int(input("enter the mobile number : "))
generated_otp=generate_otp()
send_otp(phone_number,generated_otp)

#simulate the user enter otp to verifiy.

entered_otp=int(input("enter the otp you received : "))
if verify_otp(entered_otp,generated_otp):
    print("OTP VERIFIED ,PLEASE LOGIN")
else:
     print("OTP INVALID ,PLEASE TRY AGAIN")
    