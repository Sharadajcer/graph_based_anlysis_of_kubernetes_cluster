from kubernetes import client, config


class SecurityScanner:

    def __init__(self):

        try:
            config.load_kube_config()

        except:
            config.load_incluster_config()


        self.v1 = client.CoreV1Api()



    # -----------------------------------
    # Scan Pod Security
    # -----------------------------------

    def scan_pods(self):

        findings = []


        pods = self.v1.list_pod_for_all_namespaces()



        for pod in pods.items:


            pod_name = pod.metadata.name



            # -----------------------------
            # Pod Level Checks
            # -----------------------------


            if pod.spec.host_network:


                findings.append({

                    "resource": pod_name,

                    "type": "Pod",

                    "issue": "Host Network Enabled",

                    "severity": "HIGH",

                    "score": 20

                })



            if pod.spec.host_pid:


                findings.append({

                    "resource": pod_name,

                    "type": "Pod",

                    "issue": "Host PID Enabled",

                    "severity": "HIGH",

                    "score": 20

                })



            if pod.spec.host_ipc:


                findings.append({

                    "resource": pod_name,

                    "type": "Pod",

                    "issue": "Host IPC Enabled",

                    "severity": "HIGH",

                    "score": 20

                })



            # -----------------------------
            # Volume Checks
            # -----------------------------


            if pod.spec.volumes:


                for volume in pod.spec.volumes:


                    if volume.host_path:


                        findings.append({

                            "resource": pod_name,

                            "type": "Volume",

                            "issue": "HostPath Volume Mounted",

                            "severity": "CRITICAL",

                            "score": 40

                        })



                    if volume.secret:


                        findings.append({

                            "resource": pod_name,

                            "type": "Volume",

                            "issue": "Secret Volume Mounted",

                            "severity": "MEDIUM",

                            "score": 15

                        })



            # -----------------------------
            # Container Checks
            # -----------------------------


            for container in pod.spec.containers:


                security = container.security_context



                if security:


                    if security.privileged:


                        findings.append({

                            "resource": pod_name,

                            "container": container.name,

                            "issue": "Privileged Container",

                            "severity": "CRITICAL",

                            "score": 50

                        })



                    if security.run_as_user == 0:


                        findings.append({

                            "resource": pod_name,

                            "container": container.name,

                            "issue": "Running Container As Root",

                            "severity": "HIGH",

                            "score": 30

                        })



                    if security.allow_privilege_escalation:


                        findings.append({

                            "resource": pod_name,

                            "container": container.name,

                            "issue": "Privilege Escalation Allowed",

                            "severity": "HIGH",

                            "score": 30

                        })



                    if security.read_only_root_filesystem is False:


                        findings.append({

                            "resource": pod_name,

                            "container": container.name,

                            "issue": "Writable Root Filesystem",

                            "severity": "MEDIUM",

                            "score": 15

                        })



                    if security.capabilities:


                        dangerous = [

                            "SYS_ADMIN",

                            "NET_ADMIN",

                            "SYS_PTRACE"

                        ]


                        caps = security.capabilities.add or []


                        for cap in caps:


                            if cap in dangerous:


                                findings.append({

                                    "resource": pod_name,

                                    "container": container.name,

                                    "issue": f"Dangerous Capability Added: {cap}",

                                    "severity": "CRITICAL",

                                    "score": 40

                                })



        return findings