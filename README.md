

# KubeGoat

KubeGoat is a deliberately vulnerable Kubernetes-based CTF (Capture The Flag) project inspired by Kubernetes Goat challenges. It is designed to teach Kubernetes security, container exploitation, and ethical hacking techniques through hands-on labs.

##  Features

- 10 Kubernetes challenges mapped to real-world attack scenarios  
- Hands-on exploitation in containers & clusters  
- Web-based **dashboard** for flag submission and validation  
- Resilient design: reset & rebuild labs any time with Docker Compose  


### Prerequisites
- **Docker** (20.10+)  
- **Docker Compose** (v2+)  
- Recommended OS: Parrot Security OS / Kali Linux / Ubuntu

### Installation

git clone https://github.com/yourusername/KubeGoat.git
cd KubeGoat

# Build and start all services
docker-compose up -d

# Access the Dashboard

Open your browser at:

http://localhost:10000/


# Challenges

Challenge	Name	Port	Category	Goal
01	Sensitive Keys in Codebase	10001	Secrets Management	Find leaked credentials/keys in the container and extract the flag.
02	Docker-in-Docker Exploitation	10002	Container Security	Exploit a DinD setup to escape into the host-like environment.
03	SSRF in Kubernetes	10003	Web Exploitation	Abuse SSRF to query internal Kubernetes services and steal the flag.
04	Container Escape	10004	Privilege Escalation	Break out of the container and access restricted files.
05	Misconfigured Secrets Mount	10005	Kubernetes Secrets	Retrieve sensitive data mounted as volumes/secrets.
06	Insecure Service Account	10006	RBAC Misconfigurations	Use over-permissioned service accounts to escalate privileges.
07	NodePort Exposure	10007	Networking	Abuse exposed NodePort to pivot into restricted services.
08	Privileged Pod Abuse	10008	Kubernetes Runtime	Exploit a privileged pod spec to gain host access.
09	Hidden Layers	10009	Image Security	Analyze container image layers to recover hidden flag files.
10	RBAC Misconfiguration	10010	Access Control	Exploit weak RBAC rules to read secrets and capture the flag.


# How to Play
	1.	Start the lab with docker-compose up -d.
	2.	Go to the dashboard (port 10000).
	3.	Each challenge has its own container and port.
	4.	Use tools like curl, kubectl, or exploitation scripts to solve.
	5.	Submit your flag in the dashboard for validation.




# Credits
	•	Inspired by Kubernetes Goat
	•	Created by Prabhu Perumal

