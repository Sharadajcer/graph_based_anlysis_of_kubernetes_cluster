from kubernetes import client, config


class KubernetesReader:

    def __init__(self):
        # Load kubeconfig
        config.load_kube_config()

        self.core = client.CoreV1Api()
        self.apps = client.AppsV1Api()
        self.rbac = client.RbacAuthorizationV1Api()

    # ---------------- PODS ----------------
    def get_pods(self):
        return self.core.list_pod_for_all_namespaces().items

    # ---------------- SERVICES ----------------
    def get_services(self):
        return self.core.list_service_for_all_namespaces().items

    # ---------------- DEPLOYMENTS ----------------
    def get_deployments(self):
        return self.apps.list_deployment_for_all_namespaces().items

    # ---------------- SECRETS ----------------
    def get_secrets(self):
        return self.core.list_secret_for_all_namespaces().items

    # ---------------- SERVICE ACCOUNTS ----------------
    def get_service_accounts(self):
        return self.core.list_service_account_for_all_namespaces().items

    # ---------------- ROLES ----------------
    def get_roles(self):
        return self.rbac.list_role_for_all_namespaces().items

    # ---------------- ROLE BINDINGS ----------------
    def get_role_bindings(self):
        return self.rbac.list_role_binding_for_all_namespaces().items

    # ---------------- CLUSTER ROLES ----------------
    def get_cluster_roles(self):
        return self.rbac.list_cluster_role().items

    # ---------------- CLUSTER ROLE BINDINGS ----------------
    def get_cluster_role_bindings(self):
        return self.rbac.list_cluster_role_binding().items

    # ---------------- PRINT SUMMARY ----------------
    def print_summary(self):

        pods = self.get_pods()
        services = self.get_services()
        deployments = self.get_deployments()
        secrets = self.get_secrets()
        service_accounts = self.get_service_accounts()
        roles = self.get_roles()
        role_bindings = self.get_role_bindings()

        print("\n========== Kubernetes Cluster Summary ==========\n")

        print(f"Pods                : {len(pods)}")
        print(f"Services            : {len(services)}")
        print(f"Deployments         : {len(deployments)}")
        print(f"Secrets             : {len(secrets)}")
        print(f"Service Accounts    : {len(service_accounts)}")
        print(f"Roles               : {len(roles)}")
        print(f"Role Bindings       : {len(role_bindings)}")

        print("\n================= PODS =================")

        for pod in pods:
            print(f"{pod.metadata.namespace} --> {pod.metadata.name}")

        print("\n================ SERVICES ===============")

        for service in services:
            print(f"{service.metadata.namespace} --> {service.metadata.name}")