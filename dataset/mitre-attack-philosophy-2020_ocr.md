Project No.: 10AOH08A-JC
The views, opinions and/or findings contained in this report are those of The MITRE Corporation and should not be construed as an official government position, policy, or decision, unless designated by other documentation.
Approved for Public Release. Distribution unlimited 19-01075-28.
©2020 The MITRE Corporation.
All rights reserved.
MITRE ATT&amp;CK and ATT&amp;CK are registered trademarks of the MITRE Corporation.
McLean, VA
Authors:
Blake E. Strom
Andy Applebaum
Doug P. Miller
Kathryn C. Nickels
Adam G. Pennington
Cody B. Thomas
Originally Published July 2018
Revised March 2020
MITRE
MP180360R1
MITRE PRODUCT

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

This page intentionally left blank.
iv
©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

4.1.2.1 Sources of Information 21
4.1.2.2 Community Contributions 22
4.1.2.3 Un(d)erreported Incidents 22
4.1.3 Abstraction 22
4.2 Tactics 24
4.2.1 Impact 24
4.3 Techniques and Sub-Techniques 25
4.3.1 What Makes a Technique or Sub-Technique 25
4.3.1.1 Naming 25
4.3.1.2 Types of Technique Abstraction 25
4.3.1.3 Technical References 26
4.3.1.4 Advisory Use 26
4.3.1.5 Technique Distinction 27
4.3.2 Creating New Techniques 27
4.3.3 Enhancing Existing Techniques 28
4.3.4 Named Advisory Groups Using Techniques 29
4.3.5 Incorporation Threat Intelligence on Groups and Software within ATT&amp;CK 29
4.3.5.1 Ungrouped Use of Techniques 30
4.3.6 Examples of Applying the Methodology for New Techniques 30
4.4 Applying the ATT&amp;CK Methodology 33
5 Summary 34
6 References 35
viii
©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.

List of Figures
Figure 1. The ATT&amp;CK for Enterprise Matrix 6
Figure 2. Persistence tactic with four expanded techniques 7
Figure 3. ATT&amp;CK Model Relationships 17
Figure 4. ATT&amp;CK Model Relationships Example 18
Figure 5. Abstraction Comparison of Models and Threat Knowledge Databases 23

ix

©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.

List of Tables
Table 1. ATT&amp;CK Technology Domains 8
Table 2. ATT&amp;CK Technique and Sub-Technique Model 10
Table 3. ATT&amp;CK Group Model 14
Table 4. ATT&amp;CK Software Model 15
Table 5. ATT&amp;CK Mitigation Model 16
x
©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.

This page intentionally left blank.
@ 2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

under 9 tactics. Since then, ATT&amp;CK has experienced tremendous growth based on contributions from the cybersecurity community. MITRE has created several additional ATT&amp;CK-based models were created based on the methodology used to create the first ATT&amp;CK. The original ATT&amp;CK was expanded in 2017 beyond Windows to include Mac and Linux and has been referred to as ATT&amp;CK for Enterprise. A complementary model called PRE-ATT&amp;CK was published in 2017 to focus on "left of exploit" behavior. ATT&amp;CK for Mobile was also published in 2017 to focus on behavior in the mobile-specific domain. ATT&amp;CK for Cloud was published in 2019 as part of Enterprise to describe behavior against cloud environments and services. ATT&amp;CK for ICS was published in 2020 to document behavior against industrial controls systems.
@ 2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.

threats against the network. Understanding the maturity of a SOC is important to determine its effectiveness. ATT&amp;CK can be used as one measurement to determine how effective a SOC is at detecting, analyzing, and responding to intrusions. Similar to the defensive gap assessment, a SOC Maturity assessment focuses on the processes a SOC uses to detect, understand, and respond to changing threats to their network over time. Cyber Threat Intelligence Enrichment – Cyber threat intelligence covers knowledge of cyber threats and threat actor groups that impact cybersecurity. It includes information about malware, tools, TTPs, tradecraft, behavior, and other indicators that are associated to threats. ATT&amp;CK is useful for understanding and documenting adversary group profiles from a behavioral perspective that is agnostic of the tools the group may use. Analysts and defenders can better understand common behaviors across many groups and more effectively map defenses to them and ask questions such as "what is my defensive posture against adversary group APT3?" Understanding how multiple groups use the same technique behavior allows analysts to focus on impactful defenses that span may types of threats. The structured format of ATT&amp;CK can add value to threat reporting by categorizing behavior beyond standard indicators. Multiple groups within ATT&amp;CK use the same techniques. For this reason, it is not recommended to attribute activity solely based on the ATT&amp;CK techniques used. Attribution to a group is a complex process involving all parts of the Diamond Model [5], not solely on an adversary's use of TTPs. 2.1 ATT&amp;CK Coverage ATT&amp;CK use cases for defense and red teaming incorporate a concept of ATT&amp;CK coverage. Whether you're a defender looking at how many ATT&amp;CK techniques can be detected in an enterprise, a red teamer tasked with testing ATT&amp;CK behaviors, or a manager looking to acquire a new tool that aligns to ATT&amp;CK, it's important to note that in general, coverage of every ATT&amp;CK technique is unrealistic. [7] At its core, ATT&amp;CK documents known adversary behavior and is not intended to provide a checklist of things that need to all be addressed. Not all adversary behaviors can or should be used as a basis for alerting or providing data to an analyst. An action as simple as running iconfig.exe to troubleshoot a network connection may happen frequently within an environment. This procedure falls under System Network Configuration Discovery in ATT&amp;CK and is in the knowledge base because adversaries have been known to use it to learn about the system and network they're in. With this example, the ability to collect telemetry on instances of iconfig.exe running in an environment may be enough "coverage" as a historical activity record that can be referenced later. If iconfig.exe is frequently and legitimately used then notifying an analyst with an alert on each instance as potential intrusion behavior would be excessive. Another example is how to address use of Valid Accounts, whether they're Local, Domain, or Cloud Accounts. Use of these accounts would normally occur in any environment, but the context of how the accounts are used may or may not indicate the use is malicious in nature. Again, it's important that data related to account use be collected, but it would be rare for simple use of the accounts to indicate an alert condition to an analyst without further context. 4 ©2020 The MITRE Corporation. All Rights Reserved Approved for Public Release. Distribution unlimited 19-01075-28.

The techniques within ATT&amp;CK may have many procedures for how an adversary could implement them — and because adversaries are always changing, it is difficult to know what all those procedures are in advance. That makes discussing coverage of a technique tough, especially when some ways of detecting behavior rely on individual procedures and some may span multiple procedures or even an entire technique. Going back to the prior ipconfig.exe example, collecting data on ipconfig.exe running may be insufficient though for coverage of the System Network Configuration Discovery technique because the same details can be discovered by an adversary through other means, such as the Get-NetIPConfiguration cmdlet within PowerShell.

It is important to always review the threat intelligence on what techniques, sub-techniques, and procedures adversaries have used to understand the details and how variations might affect how you determine coverage. Anyone mapping to ATT&amp;CK should be able to explain the procedures they cover. Similarly to how it's unrealistic to expect coverage of 100% of ATT&amp;CK techniques, it's unrealistic to expect coverage of all procedures of a given technique, especially since we often cannot know all of them in advance.

Operationalizing ATT&amp;CK for an organization also encompasses determining what it means for you to have "ATT&amp;CK coverage". Is it that you're collecting data relevant to all techniques or just the ones that are the most important and you expect to see? Do you expect to issue alerts on all techniques or just the rarest ones? Is it important that all relevant instances of a technique being seen get tagged with an ATT&amp;CK mapping even if it may not have been performed due to a real incident? Is one, two, three, or more analytics addressing a technique sufficient to have confidence that a technique is covered? Does the definition of coverage expand beyond visibility to also cover controls and preventative measures to stop techniques from being used? Does your definition of coverage include conducting red team or adversary emulation tests to verify defenses or test for coverage gaps?

ATT&amp;CK is just as much about the mindset and process of using it as much as it is the knowledge base itself. It serves as a grounded, threat-informed baseline of activity that everyone should know about. The process of gathering intelligence, implementing defenses based on that intelligence, checking if those defenses work, and improving defenses to better cover threats over time is what should be strived for, not 100% coverage of ATT&amp;CK. When it comes to information security, the threats we face, new technologies, and the adaptability of goal-based adversaries, we cannot consider filling out a checklist as "done".

@2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
5

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

<table>\n<tr>\n<td>Supports Remote</td>\n<td>Tag</td>\n<td>technique coverage based on unique data sources. (For example, "what techniques can I detect if I have process monitoring in place?")</td>\n</tr>\n<tr>\n<td></td>\n<td></td>\n<td>If the (sub-) technique can be used to execute something on a remote system. Applies to execution (sub-) techniques only.</td>\n</tr>\n<tr>\n<td>Defense Bypassed*</td>\n<td>Tag</td>\n<td>If the (sub-) technique can be used to bypass or evade a particular defensive tool, methodology, or process. Applies to defense evasion (sub-) techniques only. *Required for defense evasion.</td>\n</tr>\n<tr>\n<td>CAPEC ID</td>\n<td>Field</td>\n<td>Hyperlink to related CAPEC entry on the CAPEC site.</td>\n</tr>\n<tr>\n<td>Version*</td>\n<td>Field</td>\n<td>Version of the (sub-) technique in the format of MAJOR.MINOR.</td>\n</tr>\n<tr>\n<td>Impact Type*</td>\n<td>Tag</td>\n<td>Denotes if the (sub-) technique can be used for integrity or availability attacks. Applies to impact (sub-) techniques only.</td>\n</tr>\n<tr>\n<td>Contributor</td>\n<td>Tag</td>\n<td>List of non-MITRE contributors (individual and/or organization) from first to most recent that contributed information on, about, or supporting the development of a (sub-) technique.</td>\n</tr>\n<tr>\n<td>Procedure Examples</td>\n<td>Relationship / Field</td>\n<td>Procedure example fields are populated on a (sub-) technique page when a group or software entity is associated to a (sub-) technique through documented use. They describe the group or software entity with a brief description of how the technique is used. The example of how a specific adversary uses a (sub-) technique is a direct reference to their procedures, or exact way of how they perform a (sub-) technique on a system.</td>\n</tr>\n<tr>\n<td>Detection*</td>\n<td>Field</td>\n<td>High level analytic process, sensors, data, and detection strategies that can be useful to identify a (sub-) technique has been used by an adversary. This section is intended to inform those responsible for detecting adversary behavior (such as network defenders) so they can take an action such as writing an analytic or deploying a sensor. There should be enough information and references to point toward useful defensive methodologies. There could be many ways of detecting a (sub-) technique but ATT&amp;CK and MITRE do not endorse any particular vendor solution. Detection recommendations should therefore remain vendor agnostic, recommending the general method and class of tools rather than a specific tool. Detection may not always be possible</td>\n</tr>\n</table>\n©2020 The MITRE Corporation. All Rights Reserved\n\nApproved for Public Release. Distribution unlimited 19-01075-28.\n\nPageNumber: 11"}

<table>\n<tr>\n<td>Mitigation*</td>\n<td>Relationship / Field</td>\n<td>for a given (sub-) technique and should be documented as such. Configurations, tools, or process that can prevent a (sub-) technique from working or having the desired outcome for an adversary. This section is intended to inform those responsible for mitigating against adversaries (such as network defenders or policymakers) to allow them to take an action such as changing a policy or deploying a tool. Mitigation fields are populated on a (sub-) technique page when a mitigation object is associated to a (sub-) technique. The relationship describes the details of how a specific mitigation can be applied to the (sub-) technique. Mitigation recommendations remain vendor agnostic, recommending the general method or capability class rather than a specific tool. Mitigation may not always be possible for a given (sub-) technique and is documented as such if no relationships to a given (sub-) technique are present.</td>\n</tr>\n</table>\n# 3.4.3 Sub-Technique Details\n\nThe addition of sub-techniques to ATT&amp;CK in 2020 marked a significant shift to how behavior is described within the knowledge base. The change was driven by the need to fix some of the technique abstraction level issues that occurred as ATT&amp;CK grew over the years. Some techniques were very broad and some were narrow, only describing a very specific behavior. The imbalance that this led to created unintended consequences that made it not only difficult to visualize ATT&amp;CK, but also hard to understand the purpose behind some techniques because ATT&amp;CK became so large.\n\nOur goals for how sub-technique benefits ATT&amp;CK were as follows:\n\n*   Make the abstraction level of techniques similar across the knowledge base\n\n*   Reduce the number of techniques to a manageable level\n\n*   Provide a structure to allow sub-techniques to be added easily that would decrease the need to make changes to techniques over time\n\n*   Demonstrate that techniques are not shallow and can have many ways they can be performed that should be considered\n\n*   Simplify the process for adding new technology domains to ATT&amp;CK that use overlapping techniques\n\n*   Enable more detailed data sources and descriptions for how a behavior can be observed on specific platforms\n\nThere are several points to consider about how sub-techniques are used within ATT&amp;CK.\n\n@2020 The MITRE Corporation. All Rights Reserved\nApproved for Public Release. Distribution unlimited 19-01075-28."}

Sub-techniques do not have a one-to-many relationship to techniques. Each sub technique will only have a relationship to a single parent technique and no other to avoid complicated and difficult to maintain relationships across the model. There were cases where a sub technique having multiple parents may have made sense with techniques that span multiple tactics. For example, only some sub-techniques of Scheduled Task/Job can be used for privilege escalation in addition to persistence. To address this case, sub-techniques are not required to fall under all tactics that a technique is in. As long as a sub-techniques conceptually falls under a technique (e.g. sub-techniques that are conceptually a type of process injection will be under process injection), each sub technique can contribute to which tactics a technique is a part of but are not required to fulfill every parent technique's tactic (i.e. the Process Hollowing sub technique can be used for Defense Evasion but not Privilege Escalation even though the Process Injection technique covers both tactics).
Not all techniques will have sub-techniques. Organizationally, this structural consistency makes sense. In practice, however, it was difficult to implement. Even though the purpose behind sub-techniques was to provide more detail on how techniques can be used, there remains several techniques that do not have a natural breakout into sub-techniques or do not make sense to generalize into higher level techniques. Two-Factor Authentication Interception is one example. Sub-techniques are often but not always operating system or platform specific. Having platform specific sub-techniques makes focusing the content of that technique on a particular platform much easier, but we found that sub-techniques are not always malleable enough for this purpose. It would have resulted in several of the same sub-techniques each for different platforms, such as Local, Domain, and Default Valid Accounts for each of Windows, Mac, Linux, etc. This is especially the case with techniques that apply to network communications in the Command and Control tactic since network use is often operating system and platform agnostic.
Some information within a technique will be inherited by its child sub-techniques. Both mitigation and data source information will have an upwards inheritance to the technique from sub-techniques.
Groups and software procedure examples are not inherited between techniques and sub-techniques. When reviewing threat intel to determine which level to map an example to, if the information available is specific enough to assign it to a sub technique then the information will become a procedure example only for the sub technique. If the information is ambiguous such that a sub technique cannot be identified, then the information will be mapped to the technique. The same procedure should not be mapped to both in order to reduce redundant relationships.

### 3.5 Groups

Known adversaries that are tracked by public and private organizations and reported on in threat intelligence reports are tracked within ATT&amp;CK under the Group object. Groups are defined as named intrusion sets, threat groups, actor groups, or campaigns that typically represent targeted, persistent threat activity. ATT&amp;CK primarily focuses on APT groups though it may also include other advanced groups such as financially motivated actors.
Groups can use techniques directly or employ software that implements techniques.

©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
13

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

* Tool - Commercial, open-source, built-in, or publicly available software that could be used by a defender, pen tester, red teamer, or an adversary. This category includes both software that generally is not found on an enterprise system as well as software generally available as part of an operating system that is already present in an environment. Examples include PsExec, Metasploit, Mimikatz, as well as Windows utilities such as Net, netstat, Tasklist, etc.
* Malware - Commercial, custom closed source, or open source software intended to be used for malicious purposes by adversaries. Examples include PlugX, CHOPSTICK, etc.

The software categories could be broken down further, but the idea behind the current categorization was to show how adversaries use tools and legitimate software to perform actions much like they do with traditional malware.

### 3.6.1 Software Object Structure

Items are annotated by tag if the data point is an informational reference on the software that can be used to filter and pivot on, and field if the item is a free text field used to describe software-specific information and details. Items marked with relationship indicate fields that are associated to object entity relationships with techniques or groups. Data items marked with \* denote the element is required.

Table 4. ATT&CK Software Model
<table><tr><td>Data Item</td><td>Type</td><td>Description</td></tr><tr><td>Name*</td><td>Field</td><td>The name of the software.</td></tr><tr><td>ID*</td><td>Tag</td><td>Unique identifier for the software within the knowledge base. Format: S###.</td></tr><tr><td>Associated Software</td><td>Tag</td><td>Names that have overlapping reference to a software entry and may refer to the same or similar software in threat intelligence reporting.</td></tr><tr><td>Version*</td><td>Field</td><td>Version of the software in the format of MAJOR.MINOR.</td></tr><tr><td>Contributor</td><td>Tag</td><td>List of non-MITRE contributors (individual and/or organization) from first to most recent that contributed information on, about, or supporting the development of a software profile.</td></tr><tr><td>Type*</td><td>Tag</td><td>Type of software: malware or tool.</td></tr><tr><td>Platform*</td><td>Tag</td><td>Platform the software can be used on. E.g., Windows.</td></tr><tr><td>Description*</td><td>Field</td><td>A description of the software based on technical references or public threat reporting. It may contain ties to groups known to use the software or other technical details with appropriate references.</td></tr><tr><td>Associated Software Descriptions</td><td>Field</td><td>Section that can be used to describe the associated software names with references to the report used to</td></tr></table>

©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
15

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

Techniques
List of (sub-)techniques potentially covered by this
Addressed by
mitigation.
/ Field
Relationship
Mitigation*
3.8 ATT&amp;CK Object Model Relationships
Each high-level component of ATT&amp;CK is related to other components in some way. The
relationships described in the description fields in the previous section can be visualized in a
diagram:
Adversary Group
Mitigation
Prevents
Technique /
Sub-Technique
Accomplishes
Implements
Uses
Software
Tactic
Figure 3. ATT&amp;CK Model Relationships
An example as applied to a specific persistent threat group where APT28 uses Mimikatz for
credential dumping against Windows LSASS process memory:
©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
17

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in English.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

security from a defender's perspective with a top-down view, such as the CIA² model, focus on vulnerability scoring, such as CVSS [6], or primarily account for risk calculations, such as DREAD [7].

ATT&amp;CK's use of an adversary's perspective makes it easier to understand actions and potential countermeasures in context than it would from a purely defense perspective. For detection, oftentimes defensive analysts are presented with alerts with little to no context about the event that caused the alert. This may cause a shallow frame of reference for what caused those alerts and how that cause relates to other events that may have occurred on a system or network.

The perspective shift changes the question from what did happen based on a list of available resources to what could happen with a framework for aligning a defensive strategy to the adversary's playbook. In part, ATT&amp;CK provides a more accurate frame of reference for how to approach assessing defensive coverage. It conveys the relationships and dependencies between adversarial actions and information in a way that's agnostic of any particular defensive tool or method of collecting data. Defenders are then able to follow the adversary's motivation for individual actions and understand how the actions and dependencies relate to specific classes of defenses that may be deployed in an environment.

### 4.1.2 Empirical Use

The activity described by ATT&amp;CK is largely drawn from publicly reported incidents on suspected advanced persistent threat group behavior, which provides a grounding for the knowledge base so that it accurately portrays activity happening or likely to happen in the wild. ATT&amp;CK also draws from techniques discovered and reported through offensive research into areas that adversaries and red teams are likely to leverage against enterprise networks, such as techniques that can subvert modern and commonly used defenses. The tie to incidents keeps the model grounded to real-world threats that are likely to be encountered rather than theoretical techniques that are unlikely to be seen due to difficulty of use or low utility.

#### 4.1.2.1 Sources of Information

New information relevant to ATT&amp;CK techniques can come from many different sources. These sources are used to help meet the empirical use criteria:

*   Threat intelligence reports
*   Conference presentations
*   Webinars
*   Social media
*   Blogs
*   Open source code repositories
*   Malware samples

² Confidentiality, Integrity, and Availability
21
©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.

# 4.1.2.2 Community Contributions

ATT&amp;CK relies heavily upon input from the community into what they see happening in-the-wild in order to remain up to date with relevant information. [13] MITRE's role in the process is to collect, prioritize, and curate the information that is received to ensure it aligns with ATT&amp;CK and benefits the community's understanding of adversary behavior and improves how the community can defend against those behaviors. The information may be used in different ways depending on where the information comes from and the vantage the contributing organization or individual has.

Threat intelligence analysts typically track incidents, threat groups, and how their TTPs evolve over time. CTLI is the foundation on which ATT&amp;CK is built and provides one of the best sources of information to inform new techniques as well as groups and software.

Defenders see adversaries in action and are often in a position to see when new techniques are being used. Defenders in this context refer to threat hunters, malware analysts, and incident responders. Observations by defenders are another great source of information for ATT&amp;CK.

Red teamers may not track adversary groups or be in a position to see techniques in-the-wild, but they can provide a useful source of information on how techniques are done. Red teams also develop or use open source software that may also be used by adversaries in-the-wild.

Contributions to ATT&amp;CK expand beyond just techniques. New and updated information related to detections, data sources, mitigations, best practices and other aspects of ATT&amp;CK are used to enhance the information in the knowledge base.

## 4.1.2.3 Un(der)reported Incidents

The vast majority of incidents discovered are not reported publicly. Unreported, or underreported, incidents can contain valuable information on how adversaries behave and engage in operations. Often, the techniques used can be separated from potentially sensitive or damaging information and help provide insights into new techniques and variations, as well as statistical data to show prevalence of use.

This type of circumstantial evidence of use is valuable and is taken into consideration as empirical use related data when adding new information into ATT&amp;CK based on community contributions.

## 4.1.3 Abstraction

The level of abstraction for adversary tactics and techniques within ATT&amp;CK is an important distinction between it and other types of threat models. High level models such as the various adversary lifecycles, including the Lockheed Martin Cyber Kill Chain®, Microsoft STRIDE, etc., are useful at understanding high level processes and adversary goals. However, these models are not effective at conveying what individual actions adversaries make, how one action relates to another, how sequences of actions relate to tactical adversary objectives, and how the actions correlate with data sources, defenses, configurations, and other countermeasures used for the security of a platform and domain.

By contrast, exploit databases and models describe specific instances of exploitable software – which are often available for use with code examples – but are very far removed from the

©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
22

circumstances in which they could or should be used as well as from the difficulty of using them. Similarly, malware databases also exist but typically lack context around how the malware is used and by whom. They also do not take into account how legitimate software can be used for malicious purposes. A mid-level adversary model like ATT&CK is necessary to tie these various components together. The tactics and techniques in ATT&CK define adversarial behaviors within a lifecycle to a degree where they can be more effectively mapped to defenses. The high-level concepts like Control, Execute, and Maintain are further broken down into more descriptive categories where individual actions on a system can be defined and categorized. A mid-level model is also useful to put lower level concepts into context. Behavior-based techniques are the focus as opposed to exploits and malware because they are numerous but are difficult to reason about them with a holistic defensive program other than regular vulnerability scans, rapid patching, and IOCs. Exploits and malicious software are useful to an adversary toolkit, but to fully understand their utility, it's necessary to understand the context in which they can be used to achieve a goal. The mid-level model is also a useful construct to tie in threat intelligence and incident data to show who is doing what as well as the prevalence of use for particular techniques. Figure 4 shows a comparison of the level of abstraction between high, mid, and low level models and threat knowledge databases:

High Level Models
(Lockheed Martin Kill Chain®,
Microsoft STRIDE)

Mid-level Model (MITRE ATT&CK)

Low Level Concepts
(Exploit &amp; Vulnerability
databases &amp; models)

Figure 5. Abstraction Comparison of Models and Threat Knowledge Databases

What the ATT&CK technique abstraction provides:

*   A common taxonomy of individual adversary actions and goals understood by both offense and defense.
*   An appropriate level of categorization to relate adversary's action and specific ways of defending against it.

23
©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

stored in a data base, activity which falls under Data Manipulation: Stored Data Manipulation, damages the integrity of the balance information. Each technique and sub technique in the Impact tactic includes a mandatory "Impact Type" tag with a value of "Availability" or "Integrity" indicating which one the (sub-) technique impacts. Similar to other tactics in ATT&CK, it's important to take into account adversary goals when leveraging Impact techniques. An adversary deleting files in order to decrease their likelihood of detection on an end system would fall under Indicator Removal on Host: File Deletion in Defense Evasion, rather than Data Destruction in Impact despite both techniques involving the deletion of files. 4.3 Techniques and Sub-Techniques Techniques and sub-techniques are the foundation of ATT&CK and represent the individual actions adversaries make or pieces of information the adversary learns by performing an action. 4.3.1 What Makes a Technique or Sub-Technique There are several factors to techniques and sub-techniques within ATT&CK. All factors are weighed in the decision process to create a technique or sub technique and contribute to the information that populates their respective details within the knowledge base. 4.3.1.1 Naming Technique names focus on the aspect of the technique that makes it unique—what the adversary achieves at an intermediate level of abstraction from using the tactic. Sub-techniques often signify how a technique is used at a lower level of abstraction. One example of the former is Credential Dumping [10] for Credential Access where dumping credentials is one method of gaining access to new credentials—and credentials can be dumped in several different ways. A sub technique example of the latter is Rundll32 [11] for Defense Evasion. It sits at a lower level of abstraction where Rundll32 represents a specific way the technique Signed Binary Proxy Execution can used. Industry-accepted terminology tends to be used if it is already established and documented through conference presentations, blog posts, other articles, etc. 4.3.1.2 Types of Technique Abstraction Techniques generally fall into two levels of abstraction: 1. General techniques that apply to multiple platforms in general ways (e.g. Exploit Public- Facing Application [12] which depends on vulnerable software) 2. General techniques that apply to multiple platforms in specific ways (e.g. Process Injection [13] which has several platform specific ways it can be done) Sub-techniques generally fall into one level of abstraction: 1. Specific ways a technique can be performed that may apply to one or more platforms (e.g. Rundll32 [11] as a specific way to perform Signed Binary Proxy Execution [14]) For the first, breaking out how that technique applies to multiple platforms with specific sections for each platform in the technical description likely does not make sense because the technique 25 ©2020 The MITRE Corporation. All Rights Reserved Approved for Public Release. Distribution unlimited 19-01075-28.

describes a general platform agnostic behavior, such as much of the Command and Control
tactic. The description is kept general and details are provided with references to the examples
from the different platforms as needed.

Techniques that can be performed a few different ways to achieve the same or similar results are
grouped under a general category of techniques, such as Credential Dumping. These techniques
can apply to multiple platforms in specific ways. Those different ways would then be defined as
sub-techniques that describe how those behaviors can apply individually based on platform.

Sub-techniques generally are specific ways an adversary acts against either against a particular
platform or by using a similar concept that works similarly across platforms. Rundll32 is one
example of the former that only applies to Windows systems. These sub-techniques tend to
describe how individual components of the platform are abused by adversaries. Hidden Files and
Directories is one example of the latter since it takes advantage of a similar concept that spans
Windows, Linux, and Mac but is a specific example of how an adversary would hide artifacts on
a system that is designated by the technique Hide Artifacts.

Sometimes techniques or sub-techniques can have multiple required steps within them, some of
these steps may be relatable to other existing techniques or steps that could be individual
techniques. When this occurs, it is important to focus on the distinguishing attribute of the
behavior or what makes it different than the others.

### 4.3.1.3 Technical References

Technical references are provided to point users to further research or more detail on techniques.
Areas where technical references are useful include: background on the technique, expected use
in benign cases, general use examples, variations of a technique, relevant tools and open source
code repositories, detection examples and best practices, and mitigation categories and best
practices.

### 4.3.1.4 Adversary Use

ATT&amp;CK also includes information on if (and by whom) a technique or sub-technique is used in
the wild and its reported impacts. As mentioned in the empirical use section, there are many
sources of this information. ATT&amp;CK remains strongly tied to threat intelligence sources on
persistent threat groups. As the scope of ATT&amp;CK has expanded and been refined, so too have
the criteria necessary to add information. ATT&amp;CK also includes public offensive research used
by red teams against enterprise networks since adversaries have been known to adopt such
published techniques. There are also fewer persistent threat incidents reported against Linux and
Mac systems than there are against Windows, causing available threat data to be substantially
less available. General in-the-wild sources of data that are not necessarily tied to persistent threat
group use may be used in lieu when the techniques align well with how persistent threats
typically behave.

There are several general categories of empirical use information that can be used:

*   Reported - Behavior is reported with in the wild use through public sources.
*   Reported, non-public - Behavior use is reported in non-public sources but knowledge of
    the technique or sub-technique existing is present in public sources.

Approved for Public Release. Distribution unlimited 19-01075-28.
©2020 The MITRE Corporation. All Rights Reserved
26

*   **Underreported** – Behaviors that are likely being used but are not being reported for some reason. There may also be cases where circumstantial information that a technique is in use exists but it's generally difficult for information to be collected or disseminated stating the technique is in use due to sensitivities related to the source of information or method of collection. Discretion is used based on the credibility of the source.
*   **Unreported** – There is no public or non-public source of intel saying a behavior is in use. This category may contain new offensive research used by red teams that has been published, but in the wild use by adversary groups is unknown. Discretion is used based on the utility of the technique or sub-technique and likelihood of use by adversaries.

### 4.3.1.5 Technique Distinction

Several factors are considered when including new information to determine where and how it fits into the model:

*   **Objective**- What the technique or sub-technique is accomplishing. Similar techniques may be performed the same way to accomplish different tactics. Likewise, different techniques may accomplish the same tactic in different ways.
*   **Actions**- How a technique or sub-technique is performed. Is the "trigger" different between techniques that distinguishes them even though the result may be the same or similar?
*   **Use**- Who is using it? Are there multiple groups? If so, how is the use different or the same?
*   **Requirements**- The components that are needed to use a technique or sub-technique, or are affected by use of a technique. For example, files, locations, registry changes, API calls, permissions, etc. What is the overlap of components between the techniques? Are they distinct or similar?
*   **Detection**- What needs to be instrumented to detect use of the technique or sub-technique? This is related to requirements and actions but could differ across techniques that are related.
*   **Mitigations**- What mitigation options available for the technique? Are they similar to or different from other techniques that are either performed in the same way or have the same result?

### 4.3.2 Creating New Techniques

When a potential new behavior is identified, there are several possible approaches to including it in ATT&CK:

*   Adding an entirely new technique,
*   Adding a new sub-technique under an existing technique, or
*   Enhancing or abstracting an existing technique or sub-technique to make it inclusive of the newly-identified or otherwise previously un categorized behavior.

©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
27

This choice is not always clear - the following questions help guide the decision:
* What tactic does the behavior fall under? Do multiple tactics apply?
    * Within a tactic, are other techniques similar to this one?
        * If so, how are they similar?
        * Is the similarity enough to categorize them together?
        * Is it a specific way to perform an existing technique?
    * Does the empirical use reference support the tactic use?
        * Is it plausible that the behavior can be used for that tactic objective even if data is unavailable due to related techniques?
* For behaviors similar to existing techniques or sub-techniques:
    * Does the new behavior naturally fit under the similar technique as a new sub- technique?
    * How is the new behavior performed? Is it similar in execution to other techniques? How many different ways can it be performed with existing adversary malware and other tools?
        * Would a red or adversary emulation team conceptually group this technique with others or treat it separately?
    * Does the new behavior have a different detection method or set of methods than the existing technique?
        * Are there similar data sources or methods for creating analytics that are similar or different than existing techniques?
    * Does the new behavior have a different mitigation method or set of methods than the existing technique?
        * Is the implementation or deployment methods of the mitigation fundamentally different than existing techniques that can be inhibited by a similar mitigation?
    * Would creating a new technique be useful for an end user of the model?
        * Would defenders conceptually group this technique with others or treat it separately?

### 4.3.3 Enhancing Existing Techniques

If a new behavior is not conceptually different in how it is implemented or defended against, then it likely should be included in an existing technique or sub-technique. Further questions to consider when adding new information to an existing technique:
* What distinguishes this variation from existing methods of using the technique or sub- technique?
    * How is it performed?

©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
28

o What analytic differences, if any, may be necessary to effectively detect use of or system and network side artifacts resulting from the technique being used?
o Are there different considerations for mitigation?
### 4.3.4 Named Advisory Groups Using Techniques

It is also important to consider advisory group usage of and variations to techniques and sub- technique to determine how they should be properly documented. These factors may also contribute to whether or not a new technique is created or an existing one enhanced.

*   Are there different advisory groups that use this technique or sub- technique?
    o If so, how is it different?
    o Are the differences distinguishing characteristics of that group?
    o Should the differences be documented in the advisory group's profile for how they have been known to implement the technique?
### 4.3.5 Incorporation Threat Intelligence on Groups and Software within ATT&amp;CK

Information about groups is derived from open source reporting, and each of the techniques and sub- techniques used should have a reference to the source that explains how the group uses it. ATT&amp;CK is based upon open source references to ensure the traceability of information and allow users to evaluate information sources.

Sources should be known to be reputable within the cybersecurity community and demonstrate intelligence analysis best practices. Common sources include security vendor blogs, but other sources such as personal blogs or Twitter may be used provided the information is deemed to be reliable. Original sources should be used whenever possible as opposed to secondary reporting about sources. We do not accept leaked or classified information from any corporation or government as the basis for threat intelligence within ATT&amp;CK.

Examples from publicly-available threat reporting sources are deemed to be reliable based on widely accepted criteria for evaluating information, including:

1.  Is the source internally and externally consistent?
2.  Is the source known to have reported reliably in the past?
3.  Is the source widely used, respected, and referenced by cybersecurity analysts in the community?
4.  Does the source contain spelling or grammatical errors?
5.  Does the source demonstrate sound analysis methodology (including stating supporting evidence, confidence levels, and gaps)? Does it include analytic "leaps"?
6.  Do other sources corroborate information provided?

When documenting techniques and sub- techniques used, multiple techniques may simultaneously apply to the same behavior. For example, HTTP-based Command and Control traffic over port 8088 would fall under both the Non-Standard Port technique and the Web Protocols sub- technique of Application Layer Protocol. This is to capture the various technical

@2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
29

aspects of a technique and relate them to specific reasons they are used and what data sources and countermeasures can be used by defenders. Analysts should also use caution and not assume a technique was used if it is not explicitly stated or could not have happened in any other way during the reported incident. In the same example, if Command and Control traffic is over HTTP, unless explicitly stated or known, an analyst should not assume the traffic is over port 80 because adversaries may use non-standard ports, as in the example.
Some groups in ATT&CK have multiple names associated with related sets of activity due to various organizations tracking the same (or similar) set(s) of activities by different names. Organizations' group definitions may be only partially overlapping and may disagree on specific activity. There could be several nuances that lead an analyst and organization to categorize adversary activity separately, such as differences in visibility into a group's suspected activity. [12] Despite this challenge, tracking associated groups for similar activity is useful to many users of ATT&CK, so the group pages make a best effort to track related naming based on public reporting. Similar to how techniques used must be cited, each associated group also must be cited. There could be additional information, or analysis based on incomplete or unavailable data, that may lead to changes in how adversary groups are categorized.
Techniques used by a group should focus on those techniques and sub-techniques believed to have been directly performed by adversaries, not those performed without adversary interaction by a specific software sample. Techniques performed by software should be listed under the appropriate software page, and that software then linked back to the group having used it using the relationship/field noted above.

## 4.3.5.1 Ungrouped Use of Techniques

Reports often include adversarial behavior and technique use for ungrouped or unnamed activity. This is still a very useful source of information. Just because activity is not correlated to a named group does not mean it should not be included as justification for a technique or enhancing information. Typically, this information is included as a reference within the technical section of a technique describing instances of how the technique may be used.

## 4.3.6 Examples of Applying the Methodology for New Techniques

This section considers two separate techniques - Process Injection and SQL Injection - and steps through the methodology described above to illustrate when and how to add new techniques to the ATT&CK knowledge base.

**Process Injection** - Analysis of a technique that exists within ATT&CK by applying the above methodology. Process Injection, sometimes referred to as DLL injection, is a class of behavior that describes how an adversary can use an existing benign, running process as a way to hide the presence of their code executing.

Considerations:
*   This technique is used to hide from some common defenses, like process tree analysis. It also could be used to execute within a certain context of another process that has certain user rights or permissions.

©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
30

*   It applies to Windows and Linux systems and represents benign functionality used by legitimate software that can be used by adversaries for malicious purposes.
*   It requires real-time telemetry from the system on running processes and interactions with processes through the API to effectively detect effective use. Some forensic detection of process injection is possible, depending on the variation used, from loaded libraries and other data sources but requires proper timing.
*   Mitigation is difficult due to its benign usefulness in software. Some security features may mitigate aspects of this technique, such as application whitelisting that includes analysis of loaded modules, or code integrity that prevents processes from a lower integrity level from interfacing with processes running in at a higher integrity level.
*   Many adversary groups use this technique, which is a component of tools, scripts, and malware.
*   There are several variations of process injection, but most follow a common sequence of an initial adversary controlled process requesting access to a non-malicious process, loading code within it, and forcing that process to execute the new code.
*   Some variations load DLLs from disk, while others perform reflective loading that do not require a file on disk.
*   Related methods of execution require a binary to be put on disk and/or some configuration change that will load and execute the code in a new process representing different opportunities to detect and mitigate.
*   Other related methods use different functionality provided by Windows to load and execute code, such as application shims.
*   Similar concepts exist in Linux based systems for dynamically loading libraries into processes.

Conclusions:

*   The core feature of this technique is loading malicious code within an existing live process.
*   The technique is used widely across many groups of adversaries.
*   There are several variations of this technique and the core behavior is distinct enough from other related methods of defense evasion and privilege escalation to warrant an individual entry.
*   There are several variations within this core concept to include in the process injection entry which should be defined as sub-techniques under a process injection parent technique.
*   Process injection should be included as a technique under defense evasion and privilege escalation. [13]

**SQL Injection (SQLi)** – an example analysis of a technique that is not explicitly in ATT&amp;CK by applying the above methodology.

©2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
31

SQLi is a method of injecting code through an improperly secured web interface that is interpreted and executed by a database process. The resulting code execution can be used for a number of purposes, including adding or modifying information, gaining access to a system, causing the server to download and execute other code which may result in persistence, credential access, privilege escalation, collection, and exfiltration.

Considerations:

*   SQLi may be performed to gain access to an externally facing web server in a DMZ or improperly positioned web server that would result in network compromise. It may also be performed to achieve lateral movement within an enterprise, but in-the-wild reported incidents have been scarce on this use case.
*   Fundamentally, SQLi is exploiting a vulnerability in web application software due to poor code design and is not a benign behavior that an adversary could use for some purpose.
*   SQLi is a predominant vulnerability that occurs frequently across many different types of web applications, regardless of language or platform they are written in.
*   Software has been developed to automate SQLi; it is unlikely that this would be performed manually.
*   For the external variation, data sources collecting traffic on the boundary would likely see this behavior. Application logs from the web and database server may be used as well. True positive detection may be difficult due to certain variance that can be used in frequency and timing of attempts and methods to hide indicators.
*   For the internal variation, tools that may not normally be present within an enterprise network would likely need to be downloaded and used by an adversary. Depending on the tool and how it is used, it may create an enormous amount of traffic against an internally accessible web server. Internal netflow, packet capture, web logs, and endpoint monitoring may be used to detect aspects of the download and usage of the tool.
*   There are many methods on how SQLi may reach a database through various malformed data inputs and parameters. How they are detected or mitigated are not fundamentally different from each other. Database input or web logs can be used to look for common SQLi inputs that result in code execution. Likewise, using secure web development and existing secure programming constructs mitigates a large number of SQLi instances.
*   Adversaries have been known to use SQLi as a means of gaining access to externally available web servers. There is not good data available on use within internal networks for other purposes.

Conclusions:

*   The context in which SQLi fits within an adversary's tactical goals puts it within attempts to gain access to a system through an existing software vulnerability. An example is for initial access in a network compromise by compromising an externally facing application.
*   SQLi is a variation of an exploitation technique against a specific software technology and is an appropriate abstraction within how an adversary performs initial compromise. It
*   @2020 The MITRE Corporation. All Rights Reserved
*   Approved for Public Release. Distribution unlimited 19-01075-28.
*   32

would not need to be described in various ways at this technique level due to the limited variations in how it is performed by an adversary, detected by defenders, or mitigated through proper software design. Additional resources can be cited as needed, such as CAPEC, CWE, OWASP that detail specifics.
*   Include SQLi in ATT&amp;CK as a technical detail enhancement of Exploit Public-Facing Application for gaining access to exposed web servers or databases. [15]
4.4 Applying the ATT&amp;CK Methodology
ATT&amp;CK succinctly organizes adversary tactics and techniques along with providing a common language used across security disciplines. These attributes make it a useful concept for those who need to defend against adversaries by better understanding their behavior. Even though ATT&amp;CK focuses on how adversaries compromise and operate within computer information networks and related technologies, the methodology behind how it was built can be applied to other areas.
Since ATT&amp;CK was published, MITRE has expanded it into several additional technology domains including mobile, cloud, and ICS. Still more domains could be researched, but given our criteria of basing the information in ATT&amp;CK on in-the-wild use of techniques, oftentimes an application of the ATT&amp;CK methodology does not mean that the result is an ATT&amp;CK model. There are two cases where this could apply. The first case is where there exists little to no available threat intelligence on adversaries operating, either because there is no data collected and reported or there are no adversaries operating in that space. Building automation control systems could be one example. In this case, the process of identifying the model's structure and content may include significant amounts of theoretical or red team-derived behaviors. The second is when the model does not relate to adversary use of computer information technology networks, deviating from the core space that ATT&amp;CK is designed to address. In this case, the model may be built around a completely different adversarial domain, such as misinformation, using the same criteria that ATT&amp;CK was built upon with available in-the-wild use of techniques. The AMITT project by the Credibility Coalition is one such example where the ATT&amp;CK methodology was applied to build a model describing misinformation and influence campaigns. [16] Both cases are a valid and potentially useful application of the methodology MITRE used to create and maintain ATT&amp;CK even though they are not MITRE ATT&amp;CK models.

@2020 The MITRE Corporation. All Rights Reserved
Approved for Public Release. Distribution unlimited 19-01075-28.
33

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

Describe the image's main elements (people, objects, text), note any contextual clues (place, event, culture), mention visible text and its meaning, provide deeper analysis when relevant (especially for financial charts, graphs, or documents), comment on style or architecture if relevant, then give a concise overall summary. Describe in Thai.

[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October 2019. [Online]. Available: https://attack.mitre.org/techniques/T1190/. [Accessed 16 March 2020].
[17] The MITRE Corporation, "Process Injection," 18 July 2019. [Online]. Available: https://attack.mitre.org/techniques/T1055/. [Accessed 16 March 2020].
[18] The MITRE Corporation, March 2020. [Online]. Available: http://attack.mitre.org/techniques/T1218/. [Accessed 16 March 2020].
[19] F. Roth, "The Newcomer's Guide to Cyber Threat Actor Naming," 25 March 2018. [Online]. Available: https://medium.com/@cyb3rops/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263. [Accessed 4 April 2018].
[20] The Credibility Coalition, "AMITT," 15 October 2019. [Online]. Available: https://github.com/misinforecproject/amitt_framework. [Accessed 16 March 2020].
[15] The MITRE Corporation, "Rundll32," 24 June 2019. [Online]. Available: https://attack.mitre.org/techniques/T1085/. [Accessed 16 March 2020].
[16] The MITRE Corporation, "Exploit Public-Facing Application," 22 October