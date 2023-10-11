# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBooking = channel.unary_stream(
                '/Booking/GetBooking',
                request_serializer=booking__pb2.EmptyBooking.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.GetBookingByUser = channel.unary_unary(
                '/Booking/GetBookingByUser',
                request_serializer=booking__pb2.UserId.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.SetBookingByUser = channel.unary_unary(
                '/Booking/SetBookingByUser',
                request_serializer=booking__pb2.SetBookingId.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBookingByUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetBookingByUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBooking': grpc.unary_stream_rpc_method_handler(
                    servicer.GetBooking,
                    request_deserializer=booking__pb2.EmptyBooking.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'GetBookingByUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBookingByUser,
                    request_deserializer=booking__pb2.UserId.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'SetBookingByUser': grpc.unary_unary_rpc_method_handler(
                    servicer.SetBookingByUser,
                    request_deserializer=booking__pb2.SetBookingId.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetBooking',
            booking__pb2.EmptyBooking.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBookingByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetBookingByUser',
            booking__pb2.UserId.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetBookingByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/SetBookingByUser',
            booking__pb2.SetBookingId.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
