# test server side
import time
from concurrent import futures
import grpc
import echo_pb2 as echo
import echo_pb2_grpc as echo_grpc

with grpc.insecure_channel('127.0.0.1:1443') as channel:
    stub = echo_grpc.EchoStub(channel)
    req = echo.EchoRequest()
    req.message = 'Fuck U'
    rsp = stub.Echo(req)
    print(rsp)