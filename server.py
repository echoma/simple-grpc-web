import time
from concurrent import futures
import grpc
import echo_pb2 as echo
import echo_pb2_grpc as echo_grpc

SERVER_ADDRESS = '[::]:1443'  # server address

class EchoServicer(echo_grpc.EchoServicer):

    def Echo(self, req, context):
        print(str(req), str(context.invocation_metadata()))  # print metadata
        rsp = echo.EchoResponse()
        rsp.message = req.message
        return rsp


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
echo_grpc.add_EchoServicer_to_server(EchoServicer(), server)
server.add_insecure_port(SERVER_ADDRESS)
server.start()
while True:
    time.sleep(1)
