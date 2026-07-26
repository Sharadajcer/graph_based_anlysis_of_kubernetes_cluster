class RiskAnalyzer:

    def __init__(self, graph):

        self.graph = graph


    # -----------------------------------
    # Calculate Risk Score
    # -----------------------------------

    def calculate_score(self, path):

        score = 0

        reasons = []


        for node in path:

            node_data = self.graph.nodes[node]

            node_type = node_data.get(
                "type",
                ""
            )


            if node_type == "secret":

                score += 40

                reasons.append(
                    f"Secret exposed: {node}"
                )


            elif node_type == "role":

                score += 30

                reasons.append(
                    f"RBAC role access: {node}"
                )


            elif node_type == "serviceaccount":

                score += 20

                reasons.append(
                    f"ServiceAccount access: {node}"
                )


            elif node_type == "pod":

                score += 10

                reasons.append(
                    f"Pod compromise: {node}"
                )


            elif node_type == "service":

                score += 10

                reasons.append(
                    f"Service exposure: {node}"
                )


        return score, reasons



    # -----------------------------------
    # Risk Level
    # -----------------------------------

    def risk_level(self, score):

        if score >= 80:

            return "CRITICAL"


        elif score >= 50:

            return "HIGH"


        elif score >= 25:

            return "MEDIUM"


        else:

            return "LOW"



    # -----------------------------------
    # Generate Security Report
    # -----------------------------------

    def generate_report(self, path):

        score, reasons = self.calculate_score(path)


        return {

            "path": path,

            "score": score,

            "level": self.risk_level(score),

            "reasons": reasons

        }