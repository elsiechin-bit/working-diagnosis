---
title: Notes on health data, after MMH and MediMap
dek: Two breaches in two months, one regulatory regime, and a hard look at the trust we extend to private platforms.
description: Reflections on the Manage My Health and MediMap breaches of 2025–26, what they reveal about NZ's privacy regime, and what they mean for working GPs.
category: NZ Health System & Policy
date: 2026-05-02
---

Two cyber incidents in NZ general practice infrastructure between late December 2025 and February 2026 made it impossible to keep treating health data privacy as somebody else's problem. They are also genuinely instructive about what we trust when we hand patient information to a private technology company, and what happens when that trust fails.

A brief note on names. In what follows I'll refer to **Manage My Health (MMH)** — the patient portal at the centre of the December breach, originally spun out of Medtech Global in 2008 — and **MediMap**, an unrelated medication-charting platform used in aged care, hospices, disability services and community health [1,2]. The two companies are separate. What links them is the gap between sector reliance on private digital infrastructure and the regulatory teeth that should attend it.

## What happened

**Manage My Health.** On 30 December 2025, MMH was notified by a partner organisation that its systems had been accessed by an unauthorised actor [1,3]. Investigation identified that one module — "My Health Documents" — had been compromised, exposing files uploaded by users along with hospital discharge summaries and referral letters from GPs to specialists between 2017 and 2019 [1,4]. Approximately 6–7% of MMH's roughly 1.8 million registered users were affected, equating to around 125,000 individuals [1,5]. A hacker (or group) using the name "Kazu" claimed responsibility, demanded a ransom of approximately US$60,000, and posted a small sample of data to substantiate the claim [3].

The data exposed included sensitive material — clinical correspondence, discharge summaries, mental health records, and documents uploaded directly by users [5]. MMH applied to the High Court on 5 January 2026 and obtained interim injunctive relief restraining unknown defendants from publishing or distributing the stolen information [4]. The Privacy Commissioner, Michael Webster, announced an inquiry [3]. Health Minister Simeon Brown commissioned a Ministry of Health review of the breach and the response [3,4]. As of mid-April 2026, MMH reported that all patient notifications were complete [1].

**MediMap.** On Sunday 22 February 2026 at around 1:30pm, MediMap was breached by an unauthorised actor who *altered* patient records, rather than only exfiltrating them [2,6,7]. Demographic fields were modified — names, dates of birth, assigned prescribers, locations of care, and resident status. Some living patients were marked as "deceased" [2,6]. Some patient names in altered records were replaced with the names of public political figures, including a US figure and a serving NZ minister [7,8]. Cybersecurity specialists suggested the incident had hallmarks of a hacktivist-style campaign rather than a conventional financially-driven ransomware attack [8].

MediMap took the platform offline. The company sought, and obtained, court injunctions to limit further access to or use of any data that may have been exfiltrated [6]. The Office of the Privacy Commissioner and NZ Police were notified [2]. MediMap reported no evidence that medication charts or administration records had been altered [6]. The platform was brought back online in phases through early March 2026 after a forensic review and authentication strengthening [9]. The Health Minister's office indicated that the systemic issues raised by the MediMap breach would likely be considered as part of the existing MMH review, even though MediMap was not explicitly named in its terms of reference [9].

These are the bare facts. They are not, in themselves, the most interesting part of the story.

## The regulatory architecture, and its limits

NZ's Privacy Act 2020 — replacing the original 1993 Act — established mandatory notification of "notifiable privacy breaches" to the Office of the Privacy Commissioner (OPC) [10]. The Health Information Privacy Code 2020 (HIPC) gives more specific obligations to agencies handling health information [11]. The architecture is principles-based and was well-regarded internationally when it was passed. It is also, as the OPC itself has acknowledged, under-resourced for proactive assurance, and unlike the GDPR regime in Europe — which carries financial penalties of up to 4% of global annual turnover for serious breaches — the NZ Privacy Commissioner has limited direct enforcement powers [5,10].

Following the MMH breach, an extended commentary published by the International Association of Privacy Professionals — co-authored by NZ-based privacy practitioners — argued that the events have exposed structural under-enforcement, and called for the introduction of substantive financial penalties for serious privacy breaches [5]. An opposition member of Parliament agreed to present a petition to the same effect [5]. The Cyber Security Strategy 2026–2030, published on 27 February 2026 — five days after the MediMap breach — provided the first concrete signal that the government may be willing to revisit Privacy Act enforcement settings [5,12]. As of writing, no specific legislative amendments have passed.

The MMH breach also raised a quieter but consequential question about responsibility allocation under the Privacy Act and HIPC. Where health documents originate from multiple sources — a referral letter, for example, originates with a GP and is delivered through MMH to a specialist — the Privacy Act places notification obligations on the agency that *holds* the information [10,11]. MMH took this to mean it bore primary notification obligations, which is correct as a matter of law; however, the practical effect was that GPs received aggregated lists of affected patients later than the public news cycle, and were left fielding patient enquiries without clear information [3]. The president of the Royal NZ College of General Practitioners reported learning of the breach through the media, calling it "terribly disappointing" [3]. That is a serviceable summary of the operational failure.

## What it means for working GPs

The most uncomfortable fact about both breaches is that GPs and patients had no realistic alternative to the platforms involved.

A GP working with a Medtech-family practice management system and an MMH-integrated patient portal cannot, in any practical sense, opt out of the chain of custody. The systems are how referrals get made, how labs come back, how discharge summaries land. A patient signing up to receive their own results through the patient portal isn't choosing MMH over a competitor; they're choosing whether to use the portal their clinic has integrated with. Trust in the system is functionally a sector-level decision, not an individual one.

Three implications for ordinary practice follow.

First, **trust in digital infrastructure is something the profession holds collectively, not individually.** The College, GPNZ, the Medical Council, and Health New Zealand all have legitimate interests in how private health technology vendors are selected, audited, and held accountable. The breaches are not just an OPC problem; they are a profession-level governance question.

Second, **the doctor–patient relationship absorbs the trust damage from breaches it didn't cause.** When a patient learns through the news that their referral letter from 2018 might be on a dark-web index, the immediate sense of betrayal lands on the relationship that owned the original disclosure — the GP–patient one — even when the technical fault lies elsewhere. Acknowledging this directly with affected patients, rather than deflecting to the vendor, is part of what restoring trust requires.

Third, **what we put in the notes matters.** A discharge summary that was clinically necessary in 2018 and is now sitting in a forensic log as a privacy breach in 2026 was always going to be necessary; nothing about the breaches makes accurate clinical documentation a bad idea. But the older principle — write what's needed, be precise, don't put in writing what isn't required — has acquired some additional teeth.

## What we owe patients

If a patient asks at the desk whether their information is safe, the honest answer is something like this: it is safer than it would be on paper sitting in an unlocked cabinet, less safe than it would be under an enforced standard with proper external assurance, and the recent breaches have shown that the assurances we have been operating under are not adequate. We should be telling patients what we know, when we know it, in language they can actually act on. We should be supporting calls for stronger regulatory settings. And we should resist any temptation to treat these incidents as isolated technology failures rather than what they are: a structural problem in how a small country has built its digital health spine.

Both breaches share a common shape. Critical NZ health infrastructure is provided by privately-owned vendors, on commercial terms, with limited public visibility into security posture and limited external assurance. This isn't unique to NZ. It does interact with two distinctive features of the local system: a high reliance on a small number of dominant vendors with substantial market share, and a regulator with thin enforcement powers. There's a defensible argument that the appropriate response is consolidation under public health infrastructure. There's a defensible argument that the appropriate response is regulation: stronger Privacy Act powers, mandatory security standards for health vendors, civil monetary penalties for serious organisational failures. There's a defensible argument that both are needed.

What is not defensible is leaving things as they are. Without meaningful change to enforcement settings, neither these vendors nor the next one have strong reasons to do better. The breaches were not the failure of any one company. They were the foreseeable consequence of an architecture without adequate enforcement.

The profession's job — beyond the obvious clinical one of caring for patients in the meantime — is to refuse to let that fact get buried.

---

### References

1. ManageMyHealth data breach. Wikipedia [Internet]. [cited 2026 May 2]. Available from: https://en.wikipedia.org/wiki/ManageMyHealth_data_breach
2. Patient data changed as major NZ health app MediMap hacked. Radio New Zealand [Internet]. 2026 Feb 24 [cited 2026 May 2]. Available from: https://www.rnz.co.nz/news/national/587773/patient-data-changed-as-major-nz-health-app-medimap-hacked
3. Manage My Health data breach: a timeline of what happened, and everything we know so far. Radio New Zealand [Internet]. 2026 Jan 14 [cited 2026 May 2]. Available from: https://www.rnz.co.nz/news/national/584053/manage-my-health-data-breach-a-timeline-of-what-happened-and-everything-we-know-so-far
4. Manage My Health. MMH cyber breach updates [Internet]. Auckland: Manage My Health [cited 2026 May 2]. Available from: https://managemyhealth.co.nz/mmh-cyber-breach-update-january-2026/
5. Akhavan-Moosavi N, Warner D. Calls to strengthen New Zealand's Privacy Act grow amid an increasing number of major breaches. International Association of Privacy Professionals [Internet]. 2026 Mar [cited 2026 May 2]. Available from: https://iapp.org/news/a/calls-to-strengthen-new-zealand-s-privacy-act-grow-amid-an-increasing-number-of-major-breaches
6. MediMap urgently seeks court injunction to protect stolen data after cyber hack. Radio New Zealand [Internet]. 2026 Feb 25 [cited 2026 May 2]. Available from: https://www.rnz.co.nz/news/national/587890/medimap-urgently-seeks-court-injunction-to-protect-stolen-data-after-cyber-hack
7. Patient details changed to 'deceased' in major NZ health app hack. Otago Daily Times [Internet]. 2026 Feb 24 [cited 2026 May 2]. Available from: https://www.odt.co.nz/news/national/patient-names-changed-charlie-kirk-major-nz-health-app-hack-rnz
8. MediMap seeks urgent court orders after cyber patient data incident. Insurance Business NZ [Internet]. 2026 Feb 25 [cited 2026 May 2]. Available from: https://www.insurancebusinessmag.com/nz/news/cyber/medimap-seeks-urgent-court-orders-after-cyber-patient-data-incident-566556.aspx
9. MediMap failings likely to be canvassed as part of Manage My Health review. Radio New Zealand [Internet]. 2026 Mar 4 [cited 2026 May 2]. Available from: https://www.rnz.co.nz/news/national/588547/medimap-failings-likely-to-be-canvassed-as-part-of-manage-my-health-review
10. Privacy Act 2020 (NZ) [Internet]. Wellington: New Zealand Government [cited 2026 May 2]. Available from: https://www.legislation.govt.nz/act/public/2020/0031/latest/
11. Office of the Privacy Commissioner. Health Information Privacy Code 2020 [Internet]. Wellington: OPC [cited 2026 May 2]. Available from: https://www.privacy.org.nz/privacy-act-2020/codes-of-practice/hipc2020/
12. Department of the Prime Minister and Cabinet. Cyber Security Strategy 2026–2030. Wellington: DPMC; 2026 Feb 27.