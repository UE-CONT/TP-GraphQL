import grpc
from concurrent import futures
#import booking_pb2
#import booking_pb2_grpc
import times_pb2
import times_pb2_grpc
import json

def getShowtimes(stub):
    showtimes = stub.GetShowtimes(times_pb2.Empty())
    for showtime in showtimes:
        print("Showtime: %s %s" % (showtime.date, showtime.timesMovies))

def getShowtimesByDate(stub, date):
    showtime = stub.GetShowtimesByDate(date)
    print("Showtime: %s %s" % (showtime.date, showtime.timesMovies))

def stringToTimesDate(date):
    return times_pb2.TimesDate(date = date)
'''
class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()
'''

def run():
    with grpc.insecure_channel('localhost:3002') as channel:
        stub = times_pb2_grpc.TimesStub(channel)
        print("-------------- GetShowtimes --------------")
        getShowtimes(stub)
        print("-------------- GetShowtimesByDate --------------")
        date1 = stringToTimesDate("20151202")
        getShowtimesByDate(stub,date1)
        date2 = stringToTimesDate("20151200")
        getShowtimesByDate(stub,date2)
    channel.close()

if __name__ == '__main__':
    #serve()
    run()
