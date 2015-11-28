from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+447729837696": "James Friel",
    "+447578908062": "Angus Pearson",
}

friends = {
   # "Angus Pearson":["James Friel", "Andrew Smith", "William Mathewson"]
    #"James Friel":["Angus Pearson", "Hugh McGrade", "Andrew Smith","Lisa Xie"]
    #"Harry Reader":["Angus Pearson","James Friel"]
}
#machine_list = [

#if(from_number in callers):
#    Available_friends = []#to be pulled from somewhere

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = "There are 420 of your friends in the Drill Hall" #if the user has a profile
    else:
        message = "Mate, you're not a registered user. Do you you even go here blud?" #if the user does not have a profile
    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
