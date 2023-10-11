import grpc
from concurrent import futures
import times_pb2
import times_pb2_grpc
import json

#python -m grpc_tools.protoc -I=./protos --python_out=. --grpc_python_out=. times.proto

class TimesServicer(times_pb2_grpc.TimesServicer):

    def __init__(self):
        with open('{}/data/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]
    
    def GetShowtimes(self, request, context):
        for showtime in self.db:
            yield times_pb2.TimesData(date=showtime['date'], timesMovies=showtime['movies'])

    def GetShowtimesByDate(self, request, context):
        for showtime in self.db:
            if showtime['date'] == request.date:
                print("Showtime found!")
                return times_pb2.TimesData(date=showtime['date'], timesMovies=showtime['movies'])
        return times_pb2.TimesData(date="", timesMovies=[])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    times_pb2_grpc.add_TimesServicer_to_server(TimesServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
