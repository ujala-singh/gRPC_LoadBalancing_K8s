import grpc
import example_service_pb2
import example_service_pb2_grpc
import time
import logging
import os

# Configure the logging settings (optional, can be customized as needed)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

POD_NAME           = os.getenv("POD_NAME")
GRPC_SERVER_DOMAIN = os.getenv("GRPC_SERVER_DOMAIN")
GRPC_SERVER_PORT   = os.getenv("GRPC_SERVER_PORT")

def run():
    while True:
        try:
            channel = grpc.insecure_channel(f"{GRPC_SERVER_DOMAIN}:{GRPC_SERVER_PORT}")
            stub = example_service_pb2_grpc.YourServiceStub(channel)
            response = stub.SayHello(example_service_pb2.HelloRequest(name="Ujala",client=f"{POD_NAME}"))
            logger.info(f"Received: {response.message}")
        except grpc.RpcError as e:
            # Capture and print the gRPC error details
            logger.error(f"gRPC Error: {e}")
        
        # Sleep for 5 seconds before the next invocation
        time.sleep(5)

if __name__ == "__main__":
    run()
