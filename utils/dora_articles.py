PILLARS = [
    {
        "id": "ict_risk",
        "title": "ICT Risk Management",
        "chapter": "II",
        "articles_range": "5–16",
        "color": "#1565C0",
        "icon": "🛡️",
        "articles": [
            {
                "id": "5",
                "title": "Governance and organisation",
                "controls": [
                    {"id": "5_1", "text": "Management body defines, approves, oversees and is accountable for the ICT risk management framework"},
                    {"id": "5_2", "text": "ICT risk tolerance level is defined and approved by the management body"},
                    {"id": "5_3", "text": "Management body members maintain sufficiently up-to-date knowledge and skills to understand and assess ICT risk"},
                    {"id": "5_4", "text": "ICT risk management framework is reviewed by the management body at least annually"},
                    {"id": "5_5", "text": "Adequate ICT budget is allocated for digital operational resilience needs"},
                    {"id": "5_6", "text": "Dedicated internal control structure for ICT risk management is established"},
                ],
            },
            {
                "id": "6",
                "title": "ICT risk management framework",
                "controls": [
                    {"id": "6_1", "text": "A comprehensive, documented ICT risk management framework is maintained"},
                    {"id": "6_2", "text": "Framework is reviewed and updated at least annually and after major ICT incidents"},
                    {"id": "6_3", "text": "ICT risk strategies, policies, procedures and protocols are documented"},
                    {"id": "6_4", "text": "Framework covers identify, protect, detect, respond and recover capabilities"},
                    {"id": "6_5", "text": "Internal audit of the ICT risk management framework is performed at least annually"},
                    {"id": "6_6", "text": "Lessons from testing exercises and real incidents are incorporated into the framework"},
                ],
            },
            {
                "id": "7",
                "title": "ICT systems, protocols and tools",
                "controls": [
                    {"id": "7_1", "text": "ICT systems, protocols and tools are fit for purpose and support business continuity"},
                    {"id": "7_2", "text": "ICT systems can handle peak transaction volumes and adverse conditions without degradation"},
                    {"id": "7_3", "text": "Technologies are kept up-to-date to address security risks and ensure reliability"},
                    {"id": "7_4", "text": "Redundancy measures are implemented for critical ICT systems and components"},
                ],
            },
            {
                "id": "8",
                "title": "Identification",
                "controls": [
                    {"id": "8_1", "text": "An up-to-date ICT asset inventory (hardware, software, data, services) is maintained"},
                    {"id": "8_2", "text": "ICT assets are classified by criticality, including those supporting critical/important functions"},
                    {"id": "8_3", "text": "Dependencies and interconnections between ICT assets are documented"},
                    {"id": "8_4", "text": "ICT third-party service provider dependencies are identified and mapped"},
                    {"id": "8_5", "text": "Single points of failure in ICT assets and services are identified"},
                ],
            },
            {
                "id": "9",
                "title": "Protection and prevention",
                "controls": [
                    {"id": "9_1", "text": "ICT security policies, procedures and controls are documented and implemented"},
                    {"id": "9_2", "text": "Identity and access management controls (including privileged access) are in place"},
                    {"id": "9_3", "text": "Patch management and vulnerability management processes are operational"},
                    {"id": "9_4", "text": "Data security controls including encryption and data integrity checks are implemented"},
                    {"id": "9_5", "text": "Network security, segmentation and perimeter controls are in place"},
                    {"id": "9_6", "text": "Physical and environmental security measures protect ICT assets"},
                ],
            },
            {
                "id": "10",
                "title": "Detection",
                "controls": [
                    {"id": "10_1", "text": "Mechanisms to detect and report anomalous activities are implemented"},
                    {"id": "10_2", "text": "Multiple layers of detection controls are deployed across the ICT environment"},
                    {"id": "10_3", "text": "Automated alerts are configured for anomalous activities and potential ICT incidents"},
                    {"id": "10_4", "text": "Indicators of compromise (IOCs) are actively monitored and reviewed"},
                    {"id": "10_5", "text": "Detection mechanisms are tested regularly to verify effectiveness"},
                ],
            },
            {
                "id": "11",
                "title": "Response and recovery",
                "controls": [
                    {"id": "11_1", "text": "An ICT business continuity policy is documented and approved by the management body"},
                    {"id": "11_2", "text": "Business continuity and disaster recovery plans are documented for all critical functions"},
                    {"id": "11_3", "text": "Recovery time objectives (RTO) and recovery point objectives (RPO) are defined for each critical function"},
                    {"id": "11_4", "text": "Business continuity and recovery plans are tested at least annually"},
                    {"id": "11_5", "text": "Post-incident review process is established and applied after every major ICT incident"},
                    {"id": "11_6", "text": "Crisis communication plans are in place and cover internal and external stakeholders"},
                ],
            },
            {
                "id": "12",
                "title": "Backup policies and procedures",
                "controls": [
                    {"id": "12_1", "text": "Backup policies and procedures for critical data are documented and approved"},
                    {"id": "12_2", "text": "Critical data is backed up at minimum daily; frequency is aligned with business requirements"},
                    {"id": "12_3", "text": "Backup systems are logically and physically separated from source production systems"},
                    {"id": "12_4", "text": "Backup restoration procedures are tested at least annually"},
                    {"id": "12_5", "text": "Backup storage locations are geographically separated from the primary production environment"},
                    {"id": "12_6", "text": "Backup restoration capabilities are verified to meet defined RPO and RTO targets"},
                ],
            },
            {
                "id": "13",
                "title": "Learning and evolving",
                "controls": [
                    {"id": "13_1", "text": "A post-incident lessons-learned process captures, documents and distributes findings"},
                    {"id": "13_2", "text": "The ICT risk management framework is updated based on lessons learned and incident outcomes"},
                    {"id": "13_3", "text": "A threat intelligence gathering and analysis programme is operational"},
                    {"id": "13_4", "text": "ICT security awareness and training is delivered to all relevant staff at least annually"},
                    {"id": "13_5", "text": "Training content is regularly updated to reflect emerging threats and regulatory changes"},
                ],
            },
            {
                "id": "14",
                "title": "Communication",
                "controls": [
                    {"id": "14_1", "text": "Crisis communication plans for ICT-related incidents are documented and tested"},
                    {"id": "14_2", "text": "Internal escalation and communication procedures for incidents are defined and assigned"},
                    {"id": "14_3", "text": "External communication procedures covering clients, counterparties and regulators are in place"},
                    {"id": "14_4", "text": "A responsible disclosure policy for ICT vulnerabilities is documented and published"},
                ],
            },
            {
                "id": "15",
                "title": "Further harmonisation of ICT risk management tools",
                "controls": [
                    {"id": "15_1", "text": "ICT risk management practices are aligned with applicable Regulatory Technical Standards (RTS)"},
                    {"id": "15_2", "text": "Compliance with EBA/EIOPA/ESMA ICT risk management guidelines has been assessed and verified"},
                ],
            },
            {
                "id": "16",
                "title": "Simplified ICT risk management framework",
                "controls": [
                    {"id": "16_1", "text": "Entity applicability for the simplified framework has been assessed and documented"},
                    {"id": "16_2", "text": "Simplified framework covers all required ICT risk management elements per RTS"},
                    {"id": "16_3", "text": "Annual review of the simplified ICT risk management framework is performed"},
                ],
            },
        ],
    },
    {
        "id": "incident",
        "title": "ICT Incident Management",
        "chapter": "III",
        "articles_range": "17–23",
        "color": "#B71C1C",
        "icon": "🚨",
        "articles": [
            {
                "id": "17",
                "title": "ICT-related incident management process",
                "controls": [
                    {"id": "17_1", "text": "A documented ICT incident management process covering the full lifecycle is in place"},
                    {"id": "17_2", "text": "Incident detection, classification, escalation and closure procedures are defined"},
                    {"id": "17_3", "text": "Roles and responsibilities for incident response are clearly assigned"},
                    {"id": "17_4", "text": "An ICT incident log/register is maintained with required data fields"},
                    {"id": "17_5", "text": "Post-incident analysis is performed for all significant ICT incidents"},
                ],
            },
            {
                "id": "18",
                "title": "Classification of ICT-related incidents and cyber threats",
                "controls": [
                    {"id": "18_1", "text": "ICT incident classification criteria are documented and consistently applied"},
                    {"id": "18_2", "text": "Criteria for identifying 'major' ICT incidents are aligned with DORA RTS criteria"},
                    {"id": "18_3", "text": "Incident criticality and impact assessment process is in place"},
                    {"id": "18_4", "text": "Classification thresholds are reviewed and updated when regulatory guidance changes"},
                ],
            },
            {
                "id": "19",
                "title": "Reporting of major ICT-related incidents to competent authorities",
                "controls": [
                    {"id": "19_1", "text": "A major incident regulatory reporting process and procedure is documented"},
                    {"id": "19_2", "text": "Initial notification to competent authority can be submitted within 4 hours of major incident classification"},
                    {"id": "19_3", "text": "Intermediate report can be submitted within 72 hours of initial classification"},
                    {"id": "19_4", "text": "Final report can be submitted within one month of incident resolution"},
                    {"id": "19_5", "text": "Voluntary notification process for significant cyber threats is established"},
                    {"id": "19_6", "text": "Client notification process for incidents affecting clients' financial interests is defined"},
                ],
            },
            {
                "id": "20",
                "title": "Harmonisation of reporting content and timelines",
                "controls": [
                    {"id": "20_1", "text": "Incident reporting templates and content align with applicable RTS/ITS requirements"},
                    {"id": "20_2", "text": "Reporting process is mapped to regulatory timelines (4h / 72h / 1 month)"},
                    {"id": "20_3", "text": "Single reporting point of entry to the competent authority is established and tested"},
                ],
            },
            {
                "id": "21",
                "title": "Delegating outsourcing of reporting",
                "controls": [
                    {"id": "21_1", "text": "Where reporting is outsourced, contractual requirements with the ICT provider are in place"},
                    {"id": "21_2", "text": "Oversight and quality control of the outsourced reporting process is maintained"},
                    {"id": "21_3", "text": "Ultimate legal responsibility for regulatory reporting is retained internally"},
                ],
            },
            {
                "id": "22",
                "title": "Supervisory feedback",
                "controls": [
                    {"id": "22_1", "text": "A process to receive, acknowledge and act on supervisory feedback is established"},
                    {"id": "22_2", "text": "Remediation actions arising from supervisory feedback are tracked to completion"},
                ],
            },
            {
                "id": "23",
                "title": "Operational or security payment-related incidents",
                "controls": [
                    {"id": "23_1", "text": "(PSPs) Payment incident reporting is aligned with DORA and PSD2 requirements without duplication"},
                    {"id": "23_2", "text": "Reporting interface between DORA and PSD2 obligations is documented and operationalised"},
                ],
            },
        ],
    },
    {
        "id": "testing",
        "title": "Digital Operational Resilience Testing",
        "chapter": "IV",
        "articles_range": "24–27",
        "color": "#1B5E20",
        "icon": "🧪",
        "articles": [
            {
                "id": "24",
                "title": "General requirements for digital operational resilience testing",
                "controls": [
                    {"id": "24_1", "text": "A digital operational resilience testing programme is documented and approved by management"},
                    {"id": "24_2", "text": "Testing programme covers all ICT systems and applications supporting critical/important functions"},
                    {"id": "24_3", "text": "Testing programme is reviewed and updated at least annually"},
                    {"id": "24_4", "text": "A risk-based approach to test prioritisation is documented and applied"},
                    {"id": "24_5", "text": "Testing results and remediation status are reviewed by the management body"},
                ],
            },
            {
                "id": "25",
                "title": "Testing of ICT tools and systems",
                "controls": [
                    {"id": "25_1", "text": "Vulnerability assessments and scans are performed on a regular, risk-based schedule"},
                    {"id": "25_2", "text": "Network and application security testing (including penetration testing) is conducted"},
                    {"id": "25_3", "text": "Gap analyses of ICT security posture are performed and findings tracked"},
                    {"id": "25_4", "text": "Open-source component analysis is conducted for critical ICT systems where applicable"},
                    {"id": "25_5", "text": "Source code reviews are conducted for applications supporting critical/important functions"},
                    {"id": "25_6", "text": "Scenario-based resilience tests (including cyber attack simulations) are performed"},
                ],
            },
            {
                "id": "26",
                "title": "Advanced testing based on Threat-Led Penetration Testing (TLPT)",
                "controls": [
                    {"id": "26_1", "text": "TLPT applicability assessment has been completed and documented"},
                    {"id": "26_2", "text": "TLPT is conducted at least every 3 years (for entities where TLPT is required)"},
                    {"id": "26_3", "text": "TLPT scope covers all critical and important functions and underlying ICT systems"},
                    {"id": "26_4", "text": "Qualified TLPT testers meeting DORA RTS qualification criteria are engaged"},
                    {"id": "26_5", "text": "TLPT results and residual risk are reviewed and formally accepted by the management body"},
                    {"id": "26_6", "text": "A remediation plan for TLPT findings is documented and tracked to completion"},
                ],
            },
            {
                "id": "27",
                "title": "Requirements for testers carrying out TLPT",
                "controls": [
                    {"id": "27_1", "text": "TLPT tester qualification and independence requirements per RTS are verified before engagement"},
                    {"id": "27_2", "text": "Internal tester independence requirements are assessed and met (if using internal testers)"},
                    {"id": "27_3", "text": "External testers are assessed for compliance with DORA TLPT qualification criteria"},
                ],
            },
        ],
    },
    {
        "id": "third_party",
        "title": "ICT Third-Party Risk Management",
        "chapter": "V",
        "articles_range": "28–44",
        "color": "#E65100",
        "icon": "🔗",
        "articles": [
            {
                "id": "28",
                "title": "General principles for ICT third-party risk management",
                "controls": [
                    {"id": "28_1", "text": "An ICT third-party risk management policy is documented and approved by the management body"},
                    {"id": "28_2", "text": "Pre-contract due diligence process for ICT third-party service providers is in place"},
                    {"id": "28_3", "text": "An ICT third-party provider risk classification framework is defined and applied"},
                    {"id": "28_4", "text": "Management body oversight of ICT third-party risk is established and evidenced"},
                    {"id": "28_5", "text": "Exit strategies are documented for all critical ICT third-party service providers"},
                ],
            },
            {
                "id": "29",
                "title": "Preliminary assessment of ICT concentration risk",
                "controls": [
                    {"id": "29_1", "text": "An ICT concentration risk assessment at entity level has been performed"},
                    {"id": "29_2", "text": "Single points of failure in the ICT third-party ecosystem have been identified"},
                    {"id": "29_3", "text": "Sub-outsourcing chains are mapped and assessed for concentration risk"},
                    {"id": "29_4", "text": "Concentration risk findings are reported to senior management and reflected in risk appetite"},
                ],
            },
            {
                "id": "30",
                "title": "Key contractual provisions",
                "controls": [
                    {"id": "30_1", "text": "All ICT third-party contracts contain the required DORA mandatory provisions"},
                    {"id": "30_2", "text": "SLAs define availability, performance, security and data processing requirements"},
                    {"id": "30_3", "text": "Audit, inspection and access rights are included in all ICT third-party contracts"},
                    {"id": "30_4", "text": "Termination rights and exit assistance provisions are included and practically enforceable"},
                    {"id": "30_5", "text": "Sub-outsourcing notification and consent requirements are contractually covered"},
                    {"id": "30_6", "text": "Data location, processing, portability and deletion requirements are contractually specified"},
                    {"id": "30_7", "text": "Business continuity requirements and incident notification obligations are contractually included"},
                ],
            },
            {
                "id": "31",
                "title": "Designation of critical ICT third-party service providers",
                "controls": [
                    {"id": "31_1", "text": "A complete and up-to-date register of all ICT third-party service providers is maintained"},
                    {"id": "31_2", "text": "Critical ICT third-party service providers (as designated by ESAs) have been identified"},
                    {"id": "31_3", "text": "Obligations arising from ESA oversight of critical providers are understood and being met"},
                ],
            },
            {
                "id": "32",
                "title": "Structure of the Oversight Framework",
                "controls": [
                    {"id": "32_1", "text": "Cooperation processes with ESA oversight authorities and Lead Overseer are established"},
                    {"id": "32_2", "text": "Requirements from Lead Overseer recommendations are tracked and formally remediated"},
                ],
            },
            {
                "id": "33",
                "title": "Tasks of the Lead Overseer",
                "controls": [
                    {"id": "33_1", "text": "Process to respond to information requests from the Lead Overseer is defined and tested"},
                    {"id": "33_2", "text": "On-site inspection facilitation and cooperation process is documented"},
                ],
            },
            {
                "id": "34",
                "title": "Powers of the Lead Overseer",
                "controls": [
                    {"id": "34_1", "text": "Compliance with Lead Overseer corrective measures and recommendations is formally tracked"},
                ],
            },
            {
                "id": "35",
                "title": "Exercise of powers by the Lead Overseer",
                "controls": [
                    {"id": "35_1", "text": "Engagement processes for inspections and information requests from Lead Overseer are documented"},
                ],
            },
            {
                "id": "36",
                "title": "Follow-up by competent authorities",
                "controls": [
                    {"id": "36_1", "text": "Process to act on competent authority follow-up from Lead Overseer recommendations is in place"},
                ],
            },
            {
                "id": "37",
                "title": "Designation and structure of oversight fees",
                "controls": [
                    {"id": "37_1", "text": "Understanding of the oversight fee structure for critical ICT providers is documented and budgeted"},
                ],
            },
            {
                "id": "38",
                "title": "Cooperation between Lead Overseer and competent authorities",
                "controls": [
                    {"id": "38_1", "text": "Internal understanding of the ESA cooperation framework and its implications is maintained"},
                ],
            },
            {
                "id": "39",
                "title": "Oversight of ICT third-party service providers",
                "controls": [
                    {"id": "39_1", "text": "Ongoing monitoring and performance review of critical ICT third-party providers is in place"},
                    {"id": "39_2", "text": "Annual review of critical ICT provider performance against contractual SLAs is conducted"},
                ],
            },
            {
                "id": "40",
                "title": "Harmonisation enabling supervisory convergence",
                "controls": [
                    {"id": "40_1", "text": "ICT third-party risk management practices are aligned with applicable RTS/ITS requirements"},
                ],
            },
            {
                "id": "41",
                "title": "Further harmonisation of ICT third-party risk tools",
                "controls": [
                    {"id": "41_1", "text": "Sub-outsourcing risk management framework covers full chains of service providers"},
                ],
            },
            {
                "id": "42",
                "title": "Delegated acts for ICT third-party risk",
                "controls": [
                    {"id": "42_1", "text": "Awareness of delegated acts and their implementation timeline is maintained and tracked"},
                ],
            },
            {
                "id": "43",
                "title": "Transitional period for critical ICT third-party service providers",
                "controls": [
                    {"id": "43_1", "text": "Transition planning for critical ICT providers entering ESA oversight is documented"},
                ],
            },
            {
                "id": "44",
                "title": "Peer reviews of competent authorities",
                "controls": [
                    {"id": "44_1", "text": "Peer review outcomes affecting ICT third-party risk supervisory expectations are monitored"},
                ],
            },
        ],
    },
    {
        "id": "info_sharing",
        "title": "Information Sharing Arrangements",
        "chapter": "VI",
        "articles_range": "45–46",
        "color": "#4A148C",
        "icon": "🔄",
        "articles": [
            {
                "id": "45",
                "title": "Information-sharing arrangements on cyber threat intelligence",
                "controls": [
                    {"id": "45_1", "text": "An assessment of cyber threat intelligence sharing arrangement participation has been conducted"},
                    {"id": "45_2", "text": "Participation in relevant ISACs or equivalent threat sharing arrangements is in place or formally assessed"},
                    {"id": "45_3", "text": "A threat intelligence sharing policy covering scope, confidentiality and classification is documented"},
                    {"id": "45_4", "text": "Confidentiality and data protection requirements for shared threat intelligence are satisfied"},
                    {"id": "45_5", "text": "The competent authority has been notified of participation in any sharing arrangements"},
                ],
            },
            {
                "id": "46",
                "title": "Further provisions on information sharing",
                "controls": [
                    {"id": "46_1", "text": "Information sharing practices follow applicable DORA regulatory guidelines and conditions"},
                    {"id": "46_2", "text": "Compliance with GDPR and data protection requirements in sharing arrangements is verified"},
                ],
            },
        ],
    },
]
