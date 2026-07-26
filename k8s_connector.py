from kubernetes import client, config


class KubernetesConnector:

    def __init__(self):

        try:
            config.load_kube_config()

        except:
            config.load_incluster_config()


        self.v1 = client.CoreV1Api()


    # -----------------------------------
    # Get Pods
    # -----------------------------------

    def get_pods(self):

        pods = []

        result = self.v1.list_pod_for_all_namespaces()


        for pod in result.items:

            pods.append({
                "name": pod.metadata.name,
                "namespace": pod.metadata.namespace,
                "labels": pod.metadata.labels
            })


        return pods



    # -----------------------------------
    # Get Services
    # -----------------------------------

    def get_services(self):

        services = []

        result = self.v1.list_service_for_all_namespaces()


        for service in result.items:

            services.append({

                "name": service.metadata.name,

                "namespace": service.metadata.namespace,

                "selector": service.spec.selector

            })


        return services



    # -----------------------------------
    # Get Secrets
    # -----------------------------------

    def get_secrets(self):

        secrets = []

        result = self.v1.list_secret_for_all_namespaces()


        for secret in result.items:

            secrets.append({

                "name": secret.metadata.name,

                "namespace": secret.metadata.namespace

            })


        return secrets