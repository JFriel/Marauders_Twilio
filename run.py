from flask import Flask, request, redirect
import twilio.twiml

from redis import Redis
flask_redis = Redis()

app = Flask(__name__)

# Try adding your own number to this list!

dh_machines = flask_redis.lrange("drillhall-machines", 0, -1)
machines = {m: flask_redis.hgetall(m) for m in dh_machines}
num_rows = max([int(machines[m]['row']) for m in machines])
num_cols = max([int(machines[m]['col']) for m in machines])

rows = []
for r in xrange(0, num_rows+1):
    unsorted_cells = []
    for c in xrange(0, num_cols+1):
        default_cell = {'hostname': None, 'col': c, 'row': r}
        cell = [v for (k, v) in machines.iteritems() if int(v['row']) == r and int(v['col']) == c]
        if not cell:
            cell = default_cell
        else:
            cell = cell[0]
        unsorted_cells.append(cell)
    cells = unsorted_cells
    rows.append(cells)


callers = {
        "+447729837696": "James Friel",
        "+447578908062": "Angus Pearson",
        }

friends = {
        "Angus Pearson":["James Friel", "Andrew Smith", "William Mathewson"],
        "James Friel":["Angus Pearson", "Hugh McGrade", "Andrew Smith","Lisa Xie"],
        "Harry Reeder":["Angus Pearson","James Friel"]
        }
def friendCount(name):
    return "1738"
def space(inpt,person):
    #find active friends
    if inpt == "avoid":
        print("AVOID")
        #find computer furthest away
    if inpt == "find":
        print("FIND")
        #find a computer close by
    return "CEILING CAT"


@app.route("/respond", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    if request.method == "POST":
        from_number = request.values.get('From')
        body = request.values.get('Body')
        if from_number in callers:
            if body == "avoid":
                hostname = space("avoid",callers.get(from_number));
                message = "To Escape your friends, try " + hostname
            elif body == "find":
                hostname  = space("find", callers.get(from_number))
                friend = friendCount(callers.get(from_number))
                message = friend + " of your friends are in The Drill Hall, try " + hostname
            else:
                message = "You Nonce, use the right key words."
        else:
            message = "Mate, you're not a registered user. Do you you even go here blud?" #if the user does not have a profile
        resp = twilio.twiml.Response()
        resp.message(message)
        #print(message)
        #print(resp)
        #print(from_number)

        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
