import grpc
import example_service_pb2
import example_service_pb2_grpc
from concurrent.futures import ThreadPoolExecutor
import os
import logging
from prometheus_client import start_http_server, Counter, Histogram

# Configure the logging settings
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

POD_NAME = os.getenv("POD_NAME")

# Define custom Prometheus metrics
REQUEST_COUNTER = Counter('grpc_requests_total', 'Total number of gRPC requests')
REQUEST_LATENCY = Histogram('grpc_request_latency_seconds', 'Latency of gRPC requests')

class YourServiceServicer(example_service_pb2_grpc.YourServiceServicer):
    def SayHello(self, request, context):
        logger.info(f"Received a request from {request.client}: {request.name}")

        # Record custom metrics
        REQUEST_COUNTER.inc()
        with REQUEST_LATENCY.time():
            response = example_service_pb2.HelloResponse(message=f"Hello, {request.name}! This message is from {POD_NAME}")

        return response

def serve():
    # Start the Prometheus metrics server on port 8000
    start_http_server(9090)

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    example_service_pb2_grpc.add_YourServiceServicer_to_server(
        YourServiceServicer(), server
    )
    # Listen on port 50051
    logger.info('Starting server. Listening on port 50051.')
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
