from flask import Flask, render_template, request
import random as rd

app = Flask(__name__)

category=""
question=""
answer=""
result=""
rand_num=0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page2.html")
def page2():
    return render_template("page2.html")


@app.route("/page3.html")
def page3():

    global category,question,answer,rand_num

    rand_num=rd.randint(1,10)

    match rand_num:

        case 1:
            category="Animals"
            question="Which animal says 'Moo'?"
            answer="cow"

        case 2:
            category="Birds"
            question="Which bird is often taught to say 'Hello'?"
            answer="parrot"

        case 3:
            category="Fruits"
            question="I am yellow outside, monkeys love me. Who am I?"
            answer="banana"

        case 4:
            category="Vehicles"
            question="Which vehicle has only two wheels and no engine?"
            answer="bicycle"

        case 5:
            category="Vegetables"
            question="Which vegetable makes people cry while cutting it?"
            answer="onion"

        case 6:
            category="Flowers"
            question="Which flower has thorns but is given to express love?"
            answer="rose"

        case 7:
            category="Colors"
            question="What color do you get when you mix red and yellow?"
            answer="orange"

        case 8:
            category="Cartoon Characters"
            question="Who lives in a pineapple under the sea?"
            answer="spongebob"

        case 9:
            category="Superheroes"
            question="Which superhero is afraid of Kryptonite?"
            answer="superman"

        case 10:
            category="Movies"
            question="Which ogre says, 'Ogres are like onions'?"
            answer="shrek"

    return render_template(
        "page3.html",
        number=rand_num,
        category=category,
        question=question
    )


@app.route("/last.html",methods=["POST"])
def last():

    global answer

    inp=request.form["ans"].lower()

    if inp==answer:
        result="Woo.. It is Correct 🎉"

    else:
        result="OOPS.. It is Incorrect 😿"

    return render_template("last.html",result=result)


if __name__=="__main__":
    app.run(debug=True)