from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def shoppingcart():
    cart=[]
    testitem=["Bell Automotive 22-1-53183-A Universal Cheetah Plush Steering Wheel Cover","$23.94","https://www.amazon.com/dp/B0013GSQXS?psc=1&ref=ppx_yo2ov_dt_b_product_details"]
    testitem2=["Paper Mate Inkjoy Gel Pens, Medium Point, 2-Pack, Black (1951634)","$5.68","https://www.amazon.com/dp/B019QBNZ9Q?psc=1&ref=ppx_yo2ov_dt_b_product_details"]
    cart.append(testitem)
    cart.append(testitem2)
    return render_template("base.html", cart=cart)