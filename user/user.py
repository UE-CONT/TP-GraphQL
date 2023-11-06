# REST API
import asyncio
import time
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

# CALLING gRPC requests
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
   with grpc.insecure_channel(f'localhost:{PORT_BOOKING}') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)
      req = getBookingByUser(stub, stringToUserId(userid))
      return make_response(req, 200)

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
   return make_response(jsonify({"movies": films}), 200)

@app.route("/bookings/<user>", methods=['POST'])
def set_booking_user(user):
   req = request.get_json()
   title = req["title"]
   date = req["date"]
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
   query = render_template('request_movie_title.txt', title=title)
   movie = requests.post(f'http://localhost:{PORT_MOVIE}/graphql', json={'query': query})
   if (movie.json()["data"]["movie_with_title"]["id"]):
      movieid = movie.json()["data"]["movie_with_title"]["id"]
   else:
      return make_response(jsonify({"error": "Movie not found"}), 401)
   with grpc.insecure_channel(f'localhost:{PORT_BOOKING}') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)
      valid, errormsg = setBookingByUser(stub, stringToSetBookingId(userid, date, movieid))
      if valid:
         return make_response(req, 200)
      else:
         return make_response(jsonify({"error": f"Booking could not be made: {errormsg}"}), 402)

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

### --------------- Client ----------------- ###

def setBookingByUser(stub, booking):
   valid = stub.SetBookingByUser(booking)
   return valid.status, valid.message


def getBookingByUser(stub, user):
    future = stub.GetBookingByUser.future(user)
    future.add_done_callback(process_response)

def process_response(future_response):
    print('------------After 5 seconds-------------')
    response = {}
    booking = future_response.result()
    dates = booking.dates
    print("User: %s" % (booking.userid))
    response['userid'] = booking.userid
    Dates = []
    for date in dates:
       date_response = {}
       movies=date.movieid
       print("    Date: %s" % (date.date))
       date_response['date'] = date.date
       Movies = []
       for movie in movies:
         print("        MovieId: %s" % (movie))
         Movies.append(movie)
       date_response['movies'] = Movies
       Dates.append(date_response)
    response['dates'] = Dates
    return response

def getBooking(stub):
   bookings = stub.GetBooking(booking_pb2.EmptyBooking())
   for booking in bookings:
      dates = booking.dates
      print("User: %s" % (booking.userid))
      for date in dates:
         movies=date.movieid
         print("    Date: %s" % (date.date))
         for movie in movies:
            print("        MovieId: %s" % (movie))

def stringToUserId(id):
    return booking_pb2.UserId(id = id)

def stringToSetBookingId(userid, date, movieid):
    return booking_pb2.SetBookingId(userid = userid, movieid = movieid, date = date)

def run():
    with grpc.insecure_channel(f'localhost:{PORT_BOOKING}') as channel:
       stub = booking_pb2_grpc.BookingStub(channel)
       print("-------------- GetBookingByUser in 5 seconds--------------")
       userId = stringToUserId("dwight_schrute")
       getBookingByUser(stub,userId)
       print("-------------- GetBooking --------------")
       getBooking(stub)
       while(True):
            time.sleep(1000000)

if __name__ == "__main__":
   # print("Server running in port %s"%(PORT))
   # app.run(host=HOST, port=PORT)
   run()
   while(True):
      time.sleep(1000000)
