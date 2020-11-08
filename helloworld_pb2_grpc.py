# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CallModel = channel.unary_unary(
                '/helloworld.Greeter/CallModel',
                request_serializer=helloworld__pb2.DoubleMatrix.SerializeToString,
                response_deserializer=helloworld__pb2.ModelResult.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def CallModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CallModel': grpc.unary_unary_rpc_method_handler(
                    servicer.CallModel,
                    request_deserializer=helloworld__pb2.DoubleMatrix.FromString,
                    response_serializer=helloworld__pb2.ModelResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def CallModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/CallModel',
            helloworld__pb2.DoubleMatrix.SerializeToString,
            helloworld__pb2.ModelResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
