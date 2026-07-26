from pyvis.network import Network
import os


class GraphVisualizer:

    def __init__(self, graph):

        self.graph = graph


    # -----------------------------------
    # Generate Interactive Attack Graph
    # -----------------------------------

    def generate(self, output_path=None):

        net = Network(

            height="750px",

            width="100%",

            directed=True,

            bgcolor="#ffffff",

            font_color="black"

        )


        # -------------------------------
        # Add Nodes
        # -------------------------------

        for node, data in self.graph.nodes(data=True):

            node_type = data.get("type", "unknown")


            color = "#97C2FC"


            if node_type == "attacker":

                color = "#ff4d4d"

            elif node_type == "service":

                color = "#4da6ff"

            elif node_type == "pod":

                color = "#4CAF50"

            elif node_type == "secret":

                color = "#FF9800"

            elif node_type == "role":

                color = "#9C27B0"

            elif node_type == "serviceaccount":

                color = "#00BCD4"


            net.add_node(

                node,

                label=node,

                title=node_type,

                color=color

            )


        # -------------------------------
        # Add Connections
        # -------------------------------

        for source, target in self.graph.edges():

            net.add_edge(

                source,

                target,

                arrows="to"

            )


        # Physics Settings

        net.set_options("""

        var options = {

          "physics": {

            "enabled": true,

            "barnesHut": {

              "gravitationalConstant": -3000,

              "springLength": 150

            }

          }

        }

        """)


        # -------------------------------
        # Save Graph
        # -------------------------------

        if output_path is None:

            root = os.path.dirname(

                os.path.dirname(

                    os.path.abspath(__file__)

                )

            )


            output_path = os.path.join(

                root,

                "frontend",

                "static",

                "attack_graph.html"

            )


        net.save_graph(output_path)


        return output_path