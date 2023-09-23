from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class t5model:
    def __init__(self,paper_text):
        self.tokenizer = AutoTokenizer.from_pretrained("pszemraj/long-t5-tglobal-base-sci-simplify")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("pszemraj/long-t5-tglobal-base-sci-simplify")
        self.paper_text = paper_text
    def output(self):
        # Tokenize the input paper
        input_ids = self.tokenizer.encode("summarize: " + self.paper_text, return_tensors="pt", max_length=1024, truncation=True)

        # Generate the summary
        summary_ids = self.model.generate(input_ids, max_length=2000, min_length=500, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode and print the generated summary
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    
input = '''There are innumerous types of network attacks, that feeds on the vulnerabilities present inside a network. In this article we will take a look at few of those and how we might prevent it and how to monitor the network.

Most Common Types of Attacks:
Active Attack:
In active attack, the attacker infiltrates the network and causes harm to the network. These kind of attacks are generally detected by the security system present in the network.

A few common types of Active attacks are:

Masquerade: It basically means, pretending to be someone else. The attacker masks itself and pretends to be a trusted user to enter and infiltrate the network.

The Masquerade attack explained
2. Modification of Messages: In this type of attack, the attacker modifies the data before sending it from the sender to the receiver.


Message Modification Explained
3. Reply Attack: In this type attack, the attacker masquerades the communication and then captures the messages and then sends it to the victim.


Reply Attack Explained
4. DOS(Denial of Service attack): The attacker overloads the service with innumerous false requests. They increase the traffic in the network denying communication through the network. It is a type of breach of availability.


DOS attack explained
Passive Attack:
In passive attack, the attacker doesn't harm the communication but analyzes and tracks the network. These attacks are generally more dangerous than the active attacks as they are hard to detect.

Few common types of passive attacks are:

Traffic Analysis: The attacker analyses the incoming and outgoing traffic and monitors the communication channel. It is a type of information gathering techniques.
Release of Message Contents: In this type of attack, the attacker can extract the packets and decrypt the data and read it, while traffic analysis, without the victims knowing anything about it.
Now that we have seen the most common types of network attacks, we will now check the different phases of network attack.

Several Phases to Network Attacks:
Reconnaissance:
The act of gathering information by the attacker is known as reconnaissance. The attacker plants itself inside the network and gather information present inside the network, generally looking for vulnerabilities.

There are two types of Reconnaissance:

Active Reconnaissance:

Packet Scanning and sniffing.
Port Scanning.
Ping Sweep.
Passive Reconnaissance:

DNS Recon

One of the common tool for performing reconnaissance attack is Pentmenu. It consists of different recon methods to attack a network.

Access Attack:
In these types of attack, the attacker access the network without permission and through illegal means. The attacker then get access to everything present inside the network and cause a breach in confidentiality. Few examples of access attacks are: MITM, Port Redirection, Social Engineering, etc.

Ettercap is a very common tool that can be used to perform access attack, mainly MITM attack.

Service Attack:
In this type of attack the attacker hampers the services of the network by overloading the network with innumerous false traffic thus denying service to the users in the network. Example of this type of attack is: DOS or DDOS.

Service attacks like DOS and DDOS can be done using pentmenu tool and the hping3 tool.

Malware Attack:
It is a type of attack where the attacker infects the victim’s network or system through different scrips and malicious applications to gain access to the system. Some very common types of malware are: Worms, Trojans, Zero Day, Ransomware, etc.

Zirikatu is a tool that can be used to generate payload scrips that is a kind of trojan that attacks to victim’s system and gives the attacker full command on the system.

Advanced Persistent Threat:
It is one of the most talked threat in the current world. Is is a stealthy threat actor that gains unauthorized access to out computer network and stays hidden for an extended period of time. It is known as Advanced Persistent Threat because it used advanced intelligence methods and stays in the system for a very long time undetected.

Life cycle or Progression of APT:

Step 1: Initial Compromise.

Step 2: Establish Foothold.

Step 3: Escalate Privileges.

Step 4: Internal Reconnaissance.

Step 5: Move Laterally.

Step 6: Maintain Presence.

To prevent APT from progressing into the network, the traffic should be analyzed regularly to detect uncommon signatures and flush them out of the network.

Countermeasures of Network Attacks:
Secure Physical Environment:
The physical environment of the organization should be kept secure through different security measures like CCTV cameras or ID card Authentication, etc. The organization should make sure that no external threat actors gain access to the network administration inside the organization.

Patch Management:
Whenever a vulnerability is detected, it should be patched at the earliest. Patch management is the implementation of multiple patches into an application or system to make it secure.

Automated Patch management is the process of updating the patches automatically. The patch management software checks the application for missing patches and then updates the applications with those missing patches after downloading them from the application server.

Patch Management Life Cycle:

Step 1: Update Vulnerability details from software vendors.

Step 2: Scan the enterprise network for vulnerabilities.

Step 3: Examine the vulnerability and identify the missing patches.

Step 4: Deploy patches and validate patch installation.

Step 5: Generate status report on the latest patch updates.

Active Scanning:
Actively scanning the network for unusual traffics.

Use of Firewalls, IDS and IPS.
Hardening Techniques.
All these techniques doesn't guarantee prevention of network attacks but reduces the probability of attacks by a certain amount.

Network Monitoring
Monitoring the various packets inside the network is a key component of network security and attack prevention. An attack can be detected by monitoring the traffic and looking for unusual behaviors.

Based on monitoring techniques, they are roughly divided into two types, Active and Passive Monitoring.

Active Monitoring:
Wireshark: It is a free and open source packet scanner/ sniffing tool. Its main features include, Cross platform support, Fancy GUI and extreme detailed capturing.

Here are some reasons people use Wireshark:

Network administrators use it to troubleshoot network problems
Network security engineers use it to examine security problems
QA engineers use it to verify network applications
Developers use it to debug protocol implementations
People use it to learn network protocol internals
Wireshark can also be helpful in many other situations.

A complete guide about Wireshark could be found in their official website.


The Wireshark application capturing packets.
Nmap: Nmap is a free and open source network scanner. Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses.

Nmap provides a number of features for probing computer networks, including hosts discovery and service and operating system detection.


An example of the information shown by nmap command
Few basic commands are:

nmap ip address//Shows all the open ports of the mentioned ip address.

nmap -p port number ip address//Shows the status of the specified port numbers.

nmap -F ip address//Fast Scan.

nmap -A ip address//Aggressive Scan.

There are a lot of commands, each of them can be found in the nmap — help command.

Passive Monitoring:
Log Maintenance and Monitoring: Anything that happens in a network is recorded, and these records are known as Logs.

There are innumerous types of logs, as logs depends on the application and the creator of those applications. Few important types of logs are access log, activity log, etc.

Checking the logs regularly and analyzing them is known as log monitoring.

Log Auditing is another very important term. It basically means maintaining a sequential record of data that are relevant or crucial to the maintenance of security of the system.

Log analyzer are used to analyze the logs. A very famous log analyzer is Kibana.'''
t5 = t5model(input)
out = t5.output()
print(out)