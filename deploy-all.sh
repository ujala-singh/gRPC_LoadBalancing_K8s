#!/bin/bash

# Deploy resources from envoy_proxy_k8s
kubectl apply -f envoy_proxy_k8s/ns.yaml
kubectl apply -f envoy_proxy_k8s/envoy-configmap.yaml
kubectl apply -f envoy_proxy_k8s/envoy-deployment.yaml
kubectl apply -f envoy_proxy_k8s/envoy-service.yaml

# Deploy resources from grafana_k8s
kubectl apply -f grafana_k8s/ns.yaml
kubectl apply -f grafana_k8s/grafana-datastore.yaml
kubectl apply -f grafana_k8s/grafana-dashboard.yaml
kubectl apply -f grafana_k8s/grafana-deployment.yaml
kubectl apply -f grafana_k8s/grafana-service.yaml

# Deploy resources from grpc_server_k8s
kubectl apply -f grpc_server_k8s/ns.yaml
kubectl apply -f grpc_server_k8s/grpc-server-deployment.yaml
kubectl apply -f grpc_server_k8s/grpc-server-service.yaml

# Deploy resources from prometheus_k8s
kubectl apply -f prometheus_k8s/ns.yaml
kubectl apply -f prometheus_k8s/prometheus-cm.yaml
kubectl apply -f prometheus_k8s/prometheus-rbac.yaml
kubectl apply -f prometheus_k8s/prometheus-service.yaml
kubectl apply -f prometheus_k8s/prometheus.yaml

# Deploy resources from grpc_client_k8s
kubectl apply -f grpc_client_k8s/ns.yaml
kubectl apply -f grpc_client_k8s/grpc-client-deployment.yaml
