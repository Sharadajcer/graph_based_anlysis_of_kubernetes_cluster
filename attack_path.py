import networkx as nx


class AttackPath:

    def __init__(self, graph):

        self.graph = graph


    # Check path exists
    def path_exists(self, source, target):

        try:
            return nx.has_path(
                self.graph,
                source,
                target
            )

        except nx.NodeNotFound:

            return False


    # Find shortest attack path
    def shortest_path(self, source, target):

        try:

            return nx.shortest_path(
                self.graph,
                source,
                target
            )

        except:

            return None


    # Path length
    def path_length(self, source, target):

        try:

            return nx.shortest_path_length(
                self.graph,
                source,
                target
            )

        except:

            return -1


    # Risk calculation
    def risk_level(self, hops):

        if hops <= 2:
            return "HIGH"

        elif hops <= 5:
            return "MEDIUM"

        else:
            return "LOW"


    # Print attack analysis
    def print_attack_path(self, source, target):

        print("\n===================================")
        print("        ATTACK PATH ANALYSIS")
        print("===================================\n")


        if not self.path_exists(source, target):

            print("No attack path exists")
            return


        path = self.shortest_path(
            source,
            target
        )


        hops = self.path_length(
            source,
            target
        )


        print("Attack Path:\n")

        print(
            " ---> ".join(path)
        )


        print("\nTotal Nodes :", len(path))

        print("Total Hops  :", hops)

        print(
            "Risk Level  :",
            self.risk_level(hops)
        )


        print("\n===================================\n")