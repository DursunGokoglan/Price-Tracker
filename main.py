from bs4 import BeautifulSoup
import requests
import smtplib
import time

start_time = time.time()

link = "https://www.amazon.com.tr/Apple-iPhone-13-128-GB/dp/B09V4LQJ5C/ref=sr_1_1?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dib=eyJ2IjoiMSJ9.SqQMY1JOZqP8fY-FBuGmwsjswOyULL8E8PHa2cNCl3XXgB3uinHL9-k4PVnTolGhz5dSgo91dzwvmmPaa3HRIeUaa0-piDvfxgzHkNjfjTpRaz9E9ymCveH1UyNcxoKqxQ_zfnGG5r-m5b04gES5q9U4it3z4Bn-qKLoNyoZi6ElXJazROd9T3iNMZ24_Vp-VvIfkMnUWstln4BuHcyYTh-l1VuYEgWZ9iBPlIL61yTen7y4Mb6fi9QDC_oTPCDfQPOVqgbl2uQ533sqbWhYIi5MeUKso4-8ZYVfjHKPLO0.4SDsLeopOhyHAGGd4teTJP4L9A08MUXsvRqpiRcvLRU&dib_tag=se&keywords=iphone&qid=1710673625&refinements=p_98%3A21345978031&rnid=21345970031&rps=1&s=telephone&sr=1-1&th=1"


markup = requests.get(url=link,
                      headers={"User-Agent": "YOURUSERAGENT",
                               "Accept-Language": "YOURACCEPTLANG"}).text

soup = BeautifulSoup(markup, "html.parser")
cost = 0
product_info = ""
count = 0

while cost == 0:
    try:
        cost = soup.find(name="span", class_="a-offscreen").getText()[:6].replace(".", "")
        product_info = soup.find(name="span", id="productTitle").getText().strip()
    except AttributeError:
        count += 1
        markup = requests.get(
            url=link,
            headers={"User-Agent": "YOURUSERAGENT",
                     "Accept-Language": "YOURACCEPTLANG"}).text
        soup = BeautifulSoup(markup, "html.parser")

sender_email = "YOURSENDEREMAIL"
password = "YOURPASS"
receiver_email = "RECEIVEREMAIL"
subject = "Price Info"
body = f"Price of '{product_info}' is currently {cost}TL on Amazon. Link: {link}"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, f"Subject:{subject}\n\n{body}".encode("utf-8"))

end_time = time.time()

print(f"executed successfully in {end_time-start_time}s, {count} requests")
