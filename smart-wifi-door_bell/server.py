from fastapi import FastAPI
from typing import Optional
import uvicorn
import smtplib

app = FastAPI()

server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
server.login("nilendramajumder6838@gmail.com" , "lpzr nvhd rlfy ijas")
print("SMTP server started!!")

@app.get("/trigger")
def event_handler(device_accp: str):
    device_link = "http://" + device_accp

    print(device_link)

    mssg = "Subject: Someone is at your door.\n\nCheck the Camera footage by this link:- {}".format(device_link)

    email = "majumdernilendra@gmail.com"

    server.sendmail(from_addr = "nilendramajumder6838@gmail.com" , to_addrs = email , msg = mssg)
    print("Mail sent!!!")
    return {"message": "Event has been triggered!!!"}


if __name__ == "__main__":
    uvicorn.run(app , host = "0.0.0.0" , port = 8080)
