from kubernetes import client, config


class RBACAnalyzer:

    def __init__(self):

        try:
            config.load_kube_config()

        except:
            config.load_incluster_config()


        self.rbac = client.RbacAuthorizationV1Api()



    # -----------------------------------
    # Get Roles
    # -----------------------------------

    def get_roles(self):

        roles = []


        result = self.rbac.list_role_for_all_namespaces()


        for role in result.items:

            roles.append({

                "name": role.metadata.name,

                "namespace": role.metadata.namespace,

                "rules": role.rules

            })


        return roles



    # -----------------------------------
    # Get Cluster Roles
    # -----------------------------------

    def get_cluster_roles(self):

        roles = []


        result = self.rbac.list_cluster_role()


        for role in result.items:

            roles.append({

                "name": role.metadata.name,

                "rules": role.rules

            })


        return roles



    # -----------------------------------
    # Get Role Bindings
    # -----------------------------------

    def get_role_bindings(self):

        bindings = []


        result = self.rbac.list_role_binding_for_all_namespaces()


        for binding in result.items:

            bindings.append({

                "name": binding.metadata.name,

                "namespace": binding.metadata.namespace,

                "subjects": binding.subjects,

                "role": binding.role_ref.name

            })


        return bindings