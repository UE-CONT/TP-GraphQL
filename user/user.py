# REST API
from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

# CALLING gRPC requests
import grpc
from concurrent import futures
# import booking_pb2
# import booking_pb2_grpc
# import movie_pb2
# import movie_pb2_grpc

app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'
PORT_BOOKING = 3201
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
         query = render_template('template/request/txt', movie_id=movieid)
         movie = requests.post(f'http://172.16.134.175:{PORT_MOVIE}/graphql', json={'query': query})
         films.append(movie.json())
   print(films)
   return make_response(jsonify({"films": films}), 200)


with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
