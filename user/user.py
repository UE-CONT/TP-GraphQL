# REST API
from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

# CALLING gRPC requests
import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'
PORT_BOOKING = 3002
PORT_MOVIE = 3001

# CALLING GraphQL requests
@app.route("/bookings/<user>", methods=['GET'])
def get_bookings_byuser(user):
   userid = ""
   for userInfo in users:
      if str(userInfo["name"]) == str(user):
         userid = userInfo["id"]
         break
      elif str(userInfo["id"]) == str(user):
         userid = user
         break
   if not userid:
      return make_response(jsonify({"error": "User not found"}), 400)
   req = requests.get(f'http://localhost:{PORT_BOOKING}/bookings/{userid}')
   return make_response(req.json(), 200)

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

@app.route("/movies/<user>", methods=["GET"])
def get_movies_byuser(user):
   bookings = get_bookings_byuser(user).get_json()
   films = []
   for date in bookings["dates"]:
      for movieid in date["movies"]:
         query = render_template('request.txt', movie_id=movieid)
         movie = requests.post(f'http://localhost:{PORT_MOVIE}/graphql', json={'query': query})
         films.append(movie.json())
   print(films)
   return make_response(jsonify({"films": films}), 200)


with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

### --------------- Client ----------------- ###

def getBookingByUser(stub, user):
    booking = stub.GetBookingByUser(user)
    dates = booking.DateData
    print("Booking: %s" % (booking.date))
    for date in dates:
       movies=date.movieId
       print("    Date: %s" % (booking.date))
       for movie in movies:
         print("        MovieId: %s" % (movie))

def getBooking(stub):
   bookings = stub.GetBooking(booking_pb2.EmptyBooking())
   for booking in bookings:
      print("Booking: %s %s" % (booking.userid, booking.dates))

def stringToUserId(id):
    return booking_pb2.UserId(id = id)

def run():
    with grpc.insecure_channel(f'localhost:{PORT_BOOKING}') as channel:
       stub = booking_pb2_grpc.BookingStub(channel)
       print("-------------- GetBookingByUser --------------")
       userId = stringToUserId("dwight_schrute")
       getBookingByUser(stub,userId)

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
   run()
