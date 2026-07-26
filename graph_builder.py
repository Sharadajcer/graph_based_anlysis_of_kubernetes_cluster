import networkx as nx


class GraphBuilder:

    def __init__(self):
        self.graph = nx.DiGraph()


    # Add Pod
    def add_pod(self, pod):
        self.graph.add_node(
            pod,
            type="pod"
        )


    # Add Service
    def add_service(self, service):
        self.graph.add_node(
            service,
            type="service"
        )


    # Add Namespace
    def add_namespace(self, namespace):
        self.graph.add_node(
            namespace,
            type="namespace"
        )


    # Add Secret
    def add_secret(self, secret):
        self.graph.add_node(
            secret,
            type="secret"
        )


    # Add Attacker
    def add_attacker(self, attacker):
        self.graph.add_node(
            attacker,
            type="attacker"
        )


    # Add connection between resources
    def add_connection(self, source, target):

        self.graph.add_edge(
            source,
            target
        )


    # Get graph
    def get_graph(self):

        return self.graph


    # Display graph
    def show_graph(self):

        print("\n========== KUBERNETES ATTACK GRAPH ==========\n")


        for node, data in self.graph.nodes(data=True):

            print(
                f"{node} --> {data['type']}"
            )


        print("\nConnections:\n")


        for source, target in self.graph.edges():

            print(
                f"{source} ---> {target}"
            )

        print()