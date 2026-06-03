#!/usr/bin/env python3
import json
import os
import sys
import requests

WP_USERNAME = os.environ.get("WP_USERNAME", "")
WP_APP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")
WP_API_URL = "https://couplesrehab.com/wp-json/wp/v2/pages"

if not WP_USERNAME or not WP_APP_PASSWORD:
    print("ERROR: WP_USERNAME or WP_APP_PASSWORD not set")
    sys.exit(1)

# ── ARTICLE CONTENT ──────────────────────────────────────────────────────────
CONTENT = """<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Couples Rehab Admissions Guide: A Step-by-Step Roadmap to Getting Help Together</h1>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="background:#12244a;color:#ffffff;border-radius:14px;padding:32px;margin:35px 0;font-family:Arial,sans-serif;box-shadow:0 10px 28px rgba(18,36,74,.18);">
  <p style="margin:0 0 10px;color:#8bbbc6;font-size:14px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;">Couples Rehab Admissions</p>
  <h2 style="margin:0 0 15px;font-size:30px;line-height:1.2;color:#ffffff;">Ready to Start Recovery Together? We Can Help You Navigate Every Step.</h2>
  <p style="font-size:18px;line-height:1.6;margin:0 0 24px;color:#f4f7fb;">Couples Rehab is a national placement and referral network that helps partners find coordinated addiction treatment. Our care navigators can walk you through every step of the admissions process — from insurance verification to joint placement — confidentially and at no obligation.</p>
  <a href="tel:8885002110" style="display:inline-block;background:#ffffff;color:#12244a;padding:15px 26px;border-radius:8px;font-size:18px;font-weight:800;text-decoration:none;">Call Now: (888) 500-2110</a>
</div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><em>Medically Reviewed by Dr. James R. Whitfield, MD, FASAM &mdash; Updated 2025</em></p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><strong>If you or your partner is in immediate danger, call 911.</strong> For mental health crisis support, call or text <strong>988</strong> (Suicide &amp; Crisis Lifeline). For confidential couples rehab placement assistance, call <strong>(888) 500-2110</strong> &mdash; available 24/7.</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Deciding to get help together is one of the most important choices a couple in addiction can make &mdash; and the admissions process does not have to be overwhelming. <strong>Couples Rehab is a national addiction treatment placement and referral network, not a treatment facility itself.</strong> Our placement team coordinates access to licensed detox centers, inpatient programs, and outpatient services that admit couples, handling the logistics so you can focus on getting well. This guide walks you through every stage of the admissions process, from the first phone call through placement and beyond.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">What Does a Couples Rehab Admission Actually Mean?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>A couples rehab admission is the process through which two partners &mdash; whether in a romantic relationship, a marriage, or a committed partnership &mdash; enter treatment for substance use disorder at the same time. This may mean joint placement in the same facility when clinically appropriate, simultaneous placement at separate programs in the same geographic area, or coordinated care with shared clinical goals across different levels of the <a href="/care-paths/">treatment continuum</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Not every couple entering treatment will be placed in the same room or even the same building, and that is not a failure. Coordinated admission means both partners receive structured, clinically appropriate care at the same time, with shared therapy components where the treatment plan supports it. What makes it couples rehab is the coordination, the joint therapy elements, and the shared recovery trajectory &mdash; not necessarily shared physical space.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Step 1: Making the First Call &mdash; What Happens in the First 15 Minutes</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The single most important thing you can do right now is <a href="tel:8885002110">call (888) 500-2110</a>. When you reach a care navigator, expect a calm, confidential conversation &mdash; not an intake form or a sales pitch. In the first call, the navigator will:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Ask briefly about both partners&rsquo; substance use history and current situation</li>
<li>Screen for any immediate safety concerns, including withdrawal severity and overdose risk</li>
<li>Ask about insurance coverage for both partners</li>
<li>Explain what joint versus coordinated placement typically looks like</li>
<li>Begin identifying programs in your area or region that admit couples</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>You do not need to have everything figured out before you call. The navigator&rsquo;s job is to help you organize information and begin the placement process &mdash; not to push you toward a specific program. If either partner is currently in active withdrawal or showing signs of medical distress, mention that immediately so the navigator can prioritize <a href="/couples-detox-programs/">medical detox placement</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Step 2: Insurance Verification for Both Partners</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Most commercial insurance plans &mdash; including PPO plans, HMO plans, and many employer-sponsored plans &mdash; include some level of substance use disorder treatment coverage under the Mental Health Parity and Addiction Equity Act (MHPAEA). Coverage is always verified before any program commitment is made, so you know what to expect before any decision is finalized.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For couples, the insurance verification process runs separately for each partner, since each person has their own plan, deductible history, and prior-authorization requirements. Common coverage variables include:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>In-network vs. out-of-network benefits</strong> &mdash; some couples-focused programs may be out-of-network for one partner but not the other</li>
<li><strong>Level of care authorization</strong> &mdash; insurance medical directors determine whether detox, residential, or outpatient level is covered based on clinical criteria</li>
<li><strong>Prior authorization timelines</strong> &mdash; urgent admissions may qualify for expedited review</li>
<li><strong>Deductible and out-of-pocket status</strong> &mdash; important to review before placement, since timing in the benefit year affects cost-sharing</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Coverage outcomes are always verified, never guaranteed in advance. For a free benefits review for both partners, call <a href="tel:8885002110">(888) 500-2110</a> or visit our <a href="/resources/insurance-coverage/">insurance coverage resource page</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Step 3: Clinical Assessment &mdash; ASAM Criteria, CIWA-Ar, and COWS</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Before any placement decision is made, both partners undergo a clinical assessment. This is the most important step in the admissions process &mdash; not just a formality. The assessment determines:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Withdrawal risk and medical detox need</strong> &mdash; scored using the CIWA-Ar (Clinical Institute Withdrawal Assessment for Alcohol) for alcohol dependence and the COWS (Clinical Opiate Withdrawal Scale) for opioid dependence. High scores on either scale indicate that unsupervised withdrawal carries significant medical risk and that 24-hour monitoring is required.</li>
<li><strong>ASAM level of care placement</strong> &mdash; the <a href="https://www.asam.org/asam-criteria" target="_blank" rel="noopener noreferrer">American Society of Addiction Medicine (ASAM) criteria</a> map each person&rsquo;s clinical picture to the appropriate level of care: detox, residential, partial hospitalization (PHP), intensive outpatient (IOP), or standard outpatient.</li>
<li><strong>Co-occurring mental health conditions</strong> &mdash; anxiety, depression, PTSD, bipolar disorder, and trauma histories are assessed because they affect both placement and treatment planning. <a href="/dual-diagnosis-programs/">Dual diagnosis treatment</a> is often the clinically appropriate level of care for couples where mental health conditions have driven or been worsened by substance use.</li>
<li><strong>Relationship safety screening</strong> &mdash; every couples intake includes an intimate partner violence (IPV) screening. Joint placement is appropriate only when both partners are assessed as safe in a shared therapeutic environment. This evaluation is non-negotiable and in both partners&rsquo; clinical interest.</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The assessment is conducted by a licensed clinician &mdash; typically an LCSW, LADC, or MD depending on the program &mdash; and typically takes 60 to 90 minutes per person. Some programs complete a detailed phone-based pre-assessment before admission, followed by a full in-person assessment on day one.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Step 4: Joint Placement &mdash; When Can Couples Be Admitted Together?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Joint placement &mdash; where both partners enter the same residential or detox program simultaneously &mdash; is regularly possible and often clinically beneficial, but it is never guaranteed ahead of time. The following clinical factors determine whether joint placement is appropriate:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Compatible treatment needs</strong> &mdash; both partners placed at a similar level of care, no clinical contraindication to joint therapy</li>
<li><strong>Clear IPV screening for both partners</strong> &mdash; no active domestic violence history that would create safety risk in a shared clinical setting</li>
<li><strong>Relationship dynamics that support recovery</strong> &mdash; the couple&rsquo;s interaction patterns can be addressed therapeutically rather than enabling or undermining treatment progress</li>
<li><strong>Facility capacity and admissions timing</strong> &mdash; programs that admit couples often have limited shared-room or co-treatment capacity; waitlists are possible</li>
<li><strong>Matching levels of care</strong> &mdash; if one partner requires medical detox and the other does not, or if ASAM placements differ significantly, coordinated but separate admissions may be the appropriate approach</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Learn more about what couples-specific programs offer at our <a href="/couples-addiction-treatment/">couples addiction treatment page</a> and our <a href="/couples-detox-programs/">couples detox programs page</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div style="background:#ffffff;border:1px solid #d7dee8;border-left:7px solid #8bbbc6;border-radius:14px;padding:30px;margin:35px 0;font-family:Arial,sans-serif;box-shadow:0 8px 22px rgba(18,36,74,.10);">
  <h2 style="margin:0 0 12px;font-size:28px;color:#2b3345;">The Right Level of Care Depends on Clinical Assessment, Not Assumptions</h2>
  <p style="font-size:17px;line-height:1.6;color:#34415a;margin:0 0 22px;">Each partner&rsquo;s withdrawal risk, substance history, and mental health picture determine the safest treatment level. A clinical assessment &mdash; not a phone call or a search engine &mdash; determines the appropriate placement. Call now or take the Couples Assessment to begin.</p>
  <div style="display:flex;flex-wrap:wrap;gap:12px;">
    <a href="/couples-residential-rehab/" style="background:#12244a;color:#ffffff;padding:14px 22px;border-radius:8px;font-weight:800;text-decoration:none;">Learn About Couples Residential Rehab</a>
    <a href="/resources/insurance-coverage/" style="background:#ffffff;color:#12244a;border:1px solid #12244a;padding:13px 22px;border-radius:8px;font-weight:800;text-decoration:none;">Check Insurance Options</a>
  </div>
</div>
<!-- /wp:html -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Step 5: Choosing the Right Level of Care</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>One of the most important admissions decisions is selecting the appropriate level of care. The ASAM continuum moves from most to least intensive, and most couples in active addiction &mdash; especially those with significant substance dependence histories &mdash; begin at the detox or residential level and step down progressively.</p>
<!-- /wp:paragraph -->

<!-- wp:table -->
<figure class="wp-block-table"><table><thead><tr><th>Level of Care</th><th>Setting</th><th>Typical Duration</th><th>Appropriate For</th></tr></thead><tbody><tr><td><strong>Medical Detox (ASAM 3.7 / 4.0)</strong></td><td>Inpatient / hospital-based</td><td>3&ndash;10 days</td><td>Alcohol, benzo, or opioid dependence with high CIWA-Ar / COWS scores; medically complex withdrawal</td></tr><tr><td><strong>Residential Rehab (ASAM 3.5 / 3.7)</strong></td><td>24-hour residential</td><td>28&ndash;90 days</td><td>Severe SUD, polysubstance use, limited sober support at home, high relapse risk</td></tr><tr><td><strong>Partial Hospitalization (PHP)</strong></td><td>Day program, 6&ndash;8 hrs/day</td><td>2&ndash;6 weeks</td><td>Step-down from residential; stable housing, some daily structure needed</td></tr><tr><td><strong>Intensive Outpatient (IOP)</strong></td><td>3&ndash;5 days/week, 3 hrs/session</td><td>6&ndash;12 weeks</td><td>Early recovery, step-down from PHP, managing work or family obligations</td></tr><tr><td><strong>Standard Outpatient / MAT</strong></td><td>Weekly sessions</td><td>Ongoing</td><td>Maintenance, medication management (buprenorphine / methadone / naltrexone), relapse prevention</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Step 6: Medical Detox &mdash; When It Is Required and What to Expect</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Certain substances require supervised medical detox before residential or outpatient treatment can begin safely. <strong>Medical detox is not optional for alcohol, benzodiazepines, or high-dose opioid dependence</strong> &mdash; attempting withdrawal from these substances without medical supervision carries the risk of seizure, delirium tremens (DTs), or, in high-risk opioid cases, dangerous dehydration and cardiovascular stress.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Alcohol withdrawal:</strong> CIWA-Ar assessed on admission. Early symptoms appear 6&ndash;24 hours after the last drink and include tremors, anxiety, elevated blood pressure, and nausea. Seizure risk peaks 12&ndash;48 hours post-drink. Delirium tremens &mdash; characterized by severe autonomic instability, fever, and confusion &mdash; can occur 48&ndash;96 hours after cessation. Medical management uses a benzodiazepine taper (diazepam, lorazepam, or chlordiazepoxide) combined with thiamine and folate supplementation.</li>
<li><strong>Opioid withdrawal (including fentanyl):</strong> COWS scored at intake. Intensely uncomfortable but not directly life-threatening for most otherwise healthy adults. Buprenorphine or methadone induction, supplemented with clonidine for autonomic symptoms, ondansetron for nausea, and loperamide for gastrointestinal distress, significantly reduces suffering. The fentanyl-contaminated illicit supply makes relapse after detox especially dangerous, as tolerance resets rapidly and the risk of fatal overdose on return to use is elevated.</li>
<li><strong>Benzodiazepine withdrawal:</strong> Can be as medically serious as alcohol withdrawal. A gradual taper &mdash; typically substituting a longer-acting benzodiazepine (diazepam) for a shorter-acting one &mdash; is the standard of care. Seizure risk may persist for several days.</li>
<li><strong>Stimulant withdrawal (methamphetamine, cocaine):</strong> No significant pharmacological danger, but psychiatric risk is real &mdash; crash depression, dysphoria, anhedonia, and, in heavy methamphetamine users, stimulant-induced psychosis requiring clinical monitoring and sometimes short-term antipsychotic support.</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>For more on substance-specific withdrawal management, see our <a href="/couples-detox-programs/">couples detox programs page</a> and the <a href="https://www.samhsa.gov/find-help/national-helpline" target="_blank" rel="noopener noreferrer">SAMHSA National Helpline</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Step 7: Dual Diagnosis Treatment for Couples</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The majority of individuals entering addiction treatment have a co-occurring mental health condition &mdash; anxiety, depression, PTSD, bipolar disorder, or unresolved trauma. When both partners carry dual diagnoses, integrated treatment that addresses both conditions simultaneously is strongly preferred over treating each in isolation, as <a href="https://nida.nih.gov/research-topics/treatment" target="_blank" rel="noopener noreferrer">NIDA&rsquo;s research on treatment approaches</a> consistently demonstrates.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Dual diagnosis programs for couples typically include individual psychiatry or medication management, evidence-based individual therapy (CBT, DBT, or EMDR for trauma), joint couples sessions addressing enabling and communication patterns, and group therapy with peers navigating similar recovery challenges. Learn more at our <a href="/dual-diagnosis-programs/">dual diagnosis programs page</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Step 8: Navigating Special Circumstances in the Admissions Process</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">When One Partner Is Reluctant to Enter Treatment</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>It is common for one partner to be more treatment-ready than the other. If you are the one reaching out, know that calling on behalf of a reluctant partner is appropriate and supported. Our care navigators can explain motivational approaches, discuss whether a professional intervention may be helpful, and help you understand your own options &mdash; including whether it makes clinical sense to begin treatment as an individual while your partner decides. You can also visit our <a href="/how-it-works/">how it works page</a> to understand what the process looks like end-to-end.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Children at Home</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Many couples entering treatment have children at home. Planning for childcare coverage is a critical pre-admission logistics step, and our placement team can help connect families with community resources where available. Some residential programs also include family therapy components that allow children to participate in structured sessions during treatment, beginning to address the family system&rsquo;s broader healing.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Work and Professional Obligations</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The Family and Medical Leave Act (FMLA) may protect your job if you require medical or mental health treatment, including substance use disorder treatment. Speak with HR or a benefits coordinator before admission to understand your protections. Many PHP and IOP programs are designed to accommodate working schedules, and telehealth-based options may bridge care during transitions &mdash; explore our <a href="/telehealth/">telehealth services</a> for more information.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div style="background:#f6f8fb;border-radius:14px;padding:30px;margin:35px 0;font-family:Arial,sans-serif;border:1px solid #d7dee8;">
  <h2 style="margin:0 0 12px;font-size:28px;color:#2b3345;">Admissions Is the Beginning &mdash; Recovery Is the Long Game</h2>
  <p style="font-size:17px;line-height:1.6;color:#34415a;margin:0 0 22px;">Getting through the admissions door is a critical first step. What follows &mdash; detox, residential care, outpatient transition, couples therapy, and relapse prevention &mdash; is what builds lasting recovery for both partners. Our care navigators can outline the full continuum for your specific situation.</p>
  <a href="/couples-residential-rehab/" style="display:inline-block;background:#12244a;color:#ffffff;padding:15px 24px;border-radius:8px;font-size:17px;font-weight:800;text-decoration:none;">View Couples Residential Rehab Options</a>
</div>
<!-- /wp:html -->

<!-- wp:heading -->
<h2 class="wp-block-heading">What to Pack and Prepare Before Admission</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Most residential programs provide a detailed packing list upon admission confirmation. General guidelines that apply across most programs include:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Insurance cards and a valid photo ID for each partner</li>
<li>Prescription medications in their original pharmacy bottles (the admitting medical team will review all medications on intake)</li>
<li>Comfortable clothing for approximately two to four weeks; most programs offer laundry facilities</li>
<li>Personal hygiene items (check with the specific program regarding aerosol restrictions or alcohol-containing products)</li>
<li>A modest amount of cash for personal items; avoid bringing large sums, unnecessary electronics, or valuables</li>
<li>Written emergency contacts for both partners, including family members and any prescribing physicians</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">How to Begin: The First Call Is the First Step</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Couples Rehab exists to take the logistical weight of finding treatment off your shoulders at the hardest moment. Our care navigators work 24 hours a day to verify benefits, identify appropriate programs, and coordinate simultaneous or joint admission for both partners. You do not need to have every answer before you call. You need to make the call.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can also begin with our <a href="/couples-assessment/">Couples Assessment</a> for a preliminary self-evaluation, or visit our <a href="/crisis-support/">crisis support page</a> if you or your partner needs immediate help.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><strong>Ready to start?</strong> Call <a href="tel:8885002110"><strong>(888) 500-2110</strong></a> for confidential, 24/7 couples rehab placement assistance. If either partner is in medical distress, call <strong>911</strong> immediately. For mental health crisis support, call or text <strong>988</strong>.</p></blockquote>
<!-- /wp:quote -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Frequently Asked Questions About Couples Rehab Admissions</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Can both partners be admitted to the same program at the same time?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Joint admission to the same facility is regularly possible when both partners are clinically appropriate for the same level of care, the relationship safety screening is clear, and the facility has capacity. It is not guaranteed in advance, as placement depends on clinical fit and program availability. Our team works to coordinate timing so both partners enter treatment as close together as possible.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What happens if one partner needs medical detox and the other does not?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Each partner&rsquo;s level of care is determined by their own clinical picture. If one partner requires supervised medical detox and the other does not, our placement team coordinates simultaneous admission to appropriate programs &mdash; often at the same or nearby facilities &mdash; with a shared transition plan so both partners move toward residential care together once detox is complete.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">How long does the admissions process take?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>For urgent medical situations, same-day or next-day admission to detox may be possible. For planned residential admissions, the process &mdash; initial call, benefits verification, clinical pre-assessment, program identification, and insurance authorization &mdash; typically takes one to five business days. Our team works to accelerate every step wherever clinically safe to do so.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Does insurance cover couples rehab?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Most major commercial insurance plans include substance use disorder treatment benefits under federal parity law. Coverage levels &mdash; including which level of care is authorized, what network tier applies, and what cost-sharing applies &mdash; vary significantly by plan. Both partners&rsquo; benefits are verified separately before any placement commitment. Coverage is always verified, never assumed.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What is an ASAM assessment and why does it matter for couples?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>The ASAM criteria are a standardized, evidence-based framework used by clinicians to determine the most appropriate level of care for a person with substance use disorder. The assessment evaluates six dimensions: withdrawal risk, biomedical conditions, emotional and behavioral conditions, readiness to change, relapse potential, and recovery environment. For couples, both partners are assessed independently; the results guide individual placement as well as whether joint or coordinated admission is clinically appropriate.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What is the CIWA-Ar and when is it used?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>The CIWA-Ar (Clinical Institute Withdrawal Assessment for Alcohol, Revised) is a 10-item scale used at intake to assess alcohol withdrawal severity. Scores guide medication dosing &mdash; typically a benzodiazepine taper protocol &mdash; and determine whether inpatient medical monitoring is required. Scores above 15 indicate significant withdrawal risk requiring 24-hour medical supervision.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Is medical detox required for opioid withdrawal?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Medical detox is strongly recommended for opioid withdrawal, particularly for fentanyl dependence. While opioid withdrawal is rarely life-threatening for otherwise healthy adults, the intensity of symptoms and the elevated overdose risk during a compromised state make medically supervised withdrawal management significantly safer. Buprenorphine-assisted detox, timed using the COWS scale, is the current standard of care.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What does the IPV screening involve and why is it required?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>An intimate partner violence (IPV) screening is a structured clinical assessment conducted separately with each partner during intake. It evaluates whether the relationship has a history of physical, emotional, or sexual abuse and whether joint treatment would create safety risks in a shared clinical environment. Joint placement is appropriate only when both partners&rsquo; screenings indicate a safe therapeutic setting. This process protects both partners and is a clinical standard in reputable couples programs.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Can couples participate in virtual or telehealth rehab together?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Yes. Telehealth-based IOP and couples counseling options have expanded significantly. Virtual rehab may be appropriate for couples in early recovery who need structured support but cannot access residential care, or as a step-down from in-person treatment. Learn more at our <a href="/telehealth/">telehealth page</a>. Note that virtual treatment is generally not appropriate as the primary modality for partners with high withdrawal risk or severe psychiatric instability.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What if my partner refuses to get help?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>You can begin the process even if your partner is not yet ready. Care navigators can discuss motivational approaches, professional intervention options, and whether individual treatment makes clinical sense while your partner considers their options. It is also worth knowing that one partner entering treatment often creates positive modeling that increases the other partner&rsquo;s willingness to engage over time.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What happens after rehab for couples?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Recovery does not end at discharge. Most couples transition from residential care through a step-down continuum: PHP, then IOP, then outpatient therapy, couples counseling, and relapse prevention planning. Aftercare planning typically begins before discharge. Long-term couples in recovery benefit from continued therapeutic support for communication, accountability, and trust-rebuilding through specialized couples counseling.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What is dual diagnosis and how does it affect the admissions process?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Dual diagnosis refers to the co-occurrence of a substance use disorder with one or more mental health conditions, most commonly anxiety, depression, PTSD, or bipolar disorder. Many couples entering treatment carry dual diagnoses, and it is important that the admissions assessment captures this accurately. Placement at a program that treats only substance use without the mental health component often results in poorer outcomes; integrated dual diagnosis treatment is the evidence-supported approach.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Is there typically a wait to be admitted?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Wait times depend on the program, level of care, and geographic area. Medical detox beds for urgent situations are often available same-day or next-day. Residential programs may have wait times ranging from a few days to a couple of weeks depending on capacity. Our placement team identifies available openings across a network of providers to minimize wait time, and can often locate immediate admissions for urgent cases.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">How do I know which treatment level is right for us?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>The clinical assessment conducted during intake &mdash; using ASAM criteria, CIWA-Ar or COWS scoring, mental health screening, and the IPV evaluation &mdash; determines the appropriate level of care for each partner. You do not need to know the answer before you call. Take our <a href="/couples-assessment/">Couples Assessment</a> for a preliminary self-evaluation, or call <a href="tel:8885002110">(888) 500-2110</a> to speak with a care navigator now.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What should I do if we need help today?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Call <a href="tel:8885002110">(888) 500-2110</a> immediately. Our care navigators are available 24 hours a day, seven days a week, including holidays. If either partner is in medical distress &mdash; showing signs of severe withdrawal, overdose, or psychiatric emergency &mdash; call <strong>911</strong> first. For crisis mental health support, call or text <strong>988</strong>. For placement coordination, call us.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Trusted Sources</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><a href="https://www.samhsa.gov/find-help/national-helpline" target="_blank" rel="noopener noreferrer">SAMHSA National Helpline &mdash; 1-800-662-4357</a></li>
<li><a href="https://nida.nih.gov/research-topics/treatment" target="_blank" rel="noopener noreferrer">NIDA &mdash; Treatment Approaches for Drug Addiction</a></li>
<li><a href="https://www.asam.org/asam-criteria" target="_blank" rel="noopener noreferrer">ASAM &mdash; ASAM Criteria for Substance Use Disorder Treatment</a></li>
<li><a href="https://988lifeline.org/" target="_blank" rel="noopener noreferrer">988 Suicide &amp; Crisis Lifeline</a></li>
<li><a href="https://www.cdc.gov/overdose-prevention/" target="_blank" rel="noopener noreferrer">CDC &mdash; Drug Overdose Prevention</a></li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><em><strong>Editorial Disclaimer:</strong> Couples Rehab is a placement and referral service, not a treatment facility. This article is for informational purposes only and does not constitute medical advice. All treatment decisions should be made in consultation with licensed clinical professionals. Admission to any program is contingent on clinical assessment, bed availability, and insurance authorization. If you or your partner are experiencing a medical emergency, call 911. For crisis mental health support, call or text 988. For confidential placement assistance, call (888) 500-2110.</em></p>
<!-- /wp:paragraph -->"""

# ── SCHEMA ───────────────────────────────────────────────────────────────────
PAGE_URL = "https://couplesrehab.com/couples-rehab-admissions-guide/"

SCHEMA = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Organization",
            "@id": "https://couplesrehab.com/#organization",
            "name": "Couples Rehab",
            "url": "https://couplesrehab.com/",
            "telephone": "+1-888-500-2110",
            "logo": {
                "@type": "ImageObject",
                "url": "https://couplesrehab.com/wp-content/uploads/couples-rehab-logo.png",
                "width": 300,
                "height": 60
            },
            "contactPoint": {"@id": "https://couplesrehab.com/#contact"}
        },
        {
            "@type": "MedicalOrganization",
            "@id": "https://couplesrehab.com/#medicalorganization",
            "name": "Couples Rehab",
            "url": "https://couplesrehab.com/",
            "telephone": "+1-888-500-2110",
            "medicalSpecialty": ["Psychiatric"],
            "knowsAbout": [
                "Couples addiction treatment",
                "Medical detox for couples",
                "Substance use disorder treatment",
                "Opioid withdrawal management",
                "Alcohol withdrawal management",
                "Dual diagnosis treatment",
                "Couples therapy in recovery",
                "Behavioral health placement",
                "Insurance verification for addiction treatment",
                "ASAM criteria placement"
            ],
            "areaServed": {"@type": "Country", "name": "United States"},
            "description": "A national addiction treatment placement and referral network specializing in coordinated admissions for couples seeking detox, residential rehab, and outpatient services together."
        },
        {
            "@type": "ContactPoint",
            "@id": "https://couplesrehab.com/#contact",
            "telephone": "+1-888-500-2110",
            "contactType": "customer service",
            "areaServed": "US",
            "availableLanguage": "English"
        },
        {
            "@type": "Place",
            "@id": "https://couplesrehab.com/#place",
            "address": {"@type": "PostalAddress", "addressCountry": "US"}
        },
        {
            "@type": "WebSite",
            "@id": "https://couplesrehab.com/#website",
            "name": "Couples Rehab",
            "url": "https://couplesrehab.com/",
            "publisher": {"@id": "https://couplesrehab.com/#organization"},
            "inLanguage": "en-US",
            "potentialAction": {
                "@type": "SearchAction",
                "target": "https://couplesrehab.com/?s={search_term_string}",
                "query-input": "required name=search_term_string"
            }
        },
        {
            "@type": "WebPage",
            "@id": PAGE_URL + "#webpage",
            "url": PAGE_URL,
            "name": "Couples Rehab Admissions Guide | Step-by-Step Help Together",
            "description": "Complete guide to the couples rehab admissions process — from first call to joint placement. Insurance verification, clinical assessment, and levels of care explained. Call (888) 500-2110.",
            "isPartOf": {"@id": "https://couplesrehab.com/#website"},
            "publisher": {"@id": "https://couplesrehab.com/#organization"},
            "about": {"@id": PAGE_URL + "#primary-topic"},
            "mainEntity": {"@id": PAGE_URL + "#article"},
            "inLanguage": "en-US",
            "significantLink": [
                "https://couplesrehab.com/couples-detox-programs/",
                "https://couplesrehab.com/couples-residential-rehab/",
                "https://couplesrehab.com/couples-addiction-treatment/",
                "https://couplesrehab.com/dual-diagnosis-programs/",
                "https://couplesrehab.com/resources/insurance-coverage/",
                "https://couplesrehab.com/couples-assessment/",
                "https://couplesrehab.com/crisis-support/",
                "https://couplesrehab.com/telehealth/"
            ]
        },
        {
            "@type": "Article",
            "@id": PAGE_URL + "#article",
            "headline": "Couples Rehab Admissions Guide: A Step-by-Step Roadmap to Getting Help Together",
            "description": "Complete guide to the couples rehab admissions process — from first call to joint placement. Insurance verification, clinical assessment, and levels of care explained.",
            "author": {"@id": "https://couplesrehab.com/#organization"},
            "publisher": {"@id": "https://couplesrehab.com/#organization"},
            "mainEntityOfPage": {"@id": PAGE_URL + "#webpage"},
            "datePublished": "2025-06-03",
            "dateModified": "2025-06-03",
            "articleSection": "Admissions & Treatment Process",
            "keywords": "couples rehab admissions, couples rehab admissions guide, how to get into couples rehab, joint admission couples treatment, ASAM assessment couples, couples detox admissions",
            "wordCount": 2800,
            "inLanguage": "en-US"
        },
        {
            "@type": "Service",
            "@id": PAGE_URL + "#service",
            "name": "Couples Addiction Treatment Navigation & Admissions Coordination",
            "provider": {"@id": "https://couplesrehab.com/#medicalorganization"},
            "areaServed": {"@type": "Country", "name": "United States"},
            "audience": {
                "@type": "Audience",
                "audienceType": "Couples seeking joint addiction treatment admissions"
            },
            "serviceOutput": [
                "Benefits verification for both partners",
                "Clinical pre-assessment coordination",
                "Joint or coordinated placement in licensed treatment programs",
                "Aftercare planning and continuum guidance"
            ],
            "description": "A national placement and referral service that coordinates simultaneous or joint admissions for couples into licensed detox, residential, and outpatient addiction treatment programs."
        },
        {
            "@type": "BreadcrumbList",
            "@id": PAGE_URL + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://couplesrehab.com/"},
                {"@type": "ListItem", "position": 2, "name": "Care Paths", "item": "https://couplesrehab.com/care-paths/"},
                {"@type": "ListItem", "position": 3, "name": "Couples Rehab Admissions Guide", "item": PAGE_URL}
            ]
        },
        {
            "@type": "FAQPage",
            "@id": PAGE_URL + "#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Can both partners be admitted to the same program at the same time?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Joint admission to the same facility is regularly possible when both partners are clinically appropriate for the same level of care, the relationship safety screening is clear, and the facility has capacity. It is not guaranteed in advance, as placement depends on clinical fit and program availability."}
                },
                {
                    "@type": "Question",
                    "name": "What happens if one partner needs medical detox and the other does not?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Each partner's level of care is determined by their own clinical picture. If one partner requires supervised medical detox and the other does not, the placement team coordinates simultaneous admission to appropriate programs, often at the same or nearby facilities, with a shared transition plan."}
                },
                {
                    "@type": "Question",
                    "name": "Does insurance cover couples rehab?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Most major commercial insurance plans include substance use disorder treatment benefits under federal parity law. Coverage levels vary significantly by plan. Both partners' benefits are verified separately before any placement commitment. Coverage is always verified, never assumed."}
                },
                {
                    "@type": "Question",
                    "name": "What is an ASAM assessment and why does it matter?",
                    "acceptedAnswer": {"@type": "Answer", "text": "The ASAM criteria are a standardized, evidence-based framework used by clinicians to determine the most appropriate level of care for a person with substance use disorder. It evaluates six dimensions including withdrawal risk, co-occurring conditions, and relapse potential to guide placement decisions."}
                },
                {
                    "@type": "Question",
                    "name": "Is medical detox required for opioid withdrawal?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Medical detox is strongly recommended for opioid withdrawal, particularly for fentanyl dependence. While opioid withdrawal is rarely life-threatening for otherwise healthy adults, medically supervised withdrawal management using buprenorphine-assisted protocols is significantly safer and reduces the risk of relapse and overdose."}
                },
                {
                    "@type": "Question",
                    "name": "What if my partner refuses to get help?",
                    "acceptedAnswer": {"@type": "Answer", "text": "You can begin the placement process even if your partner is not yet ready. Care navigators can discuss motivational approaches, professional intervention options, and whether individual treatment makes sense while your partner considers their options."}
                },
                {
                    "@type": "Question",
                    "name": "What happens after rehab for couples?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Most couples transition from residential care through a step-down continuum: PHP, IOP, outpatient therapy, couples counseling, and relapse prevention planning. Aftercare planning typically begins before discharge and includes ongoing couples therapy and relapse prevention strategies."}
                },
                {
                    "@type": "Question",
                    "name": "What should I do if we need help today?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Call (888) 500-2110 immediately. Care navigators are available 24 hours a day, seven days a week. If either partner is in medical distress, call 911 first. For mental health crisis support, call or text 988."}
                }
            ]
        },
        {
            "@type": "DefinedTermSet",
            "@id": PAGE_URL + "#terms",
            "name": "Couples Rehab Admissions Clinical Glossary",
            "hasDefinedTerm": [
                {
                    "@type": "DefinedTerm",
                    "name": "ASAM Criteria",
                    "description": "A standardized, six-dimensional framework developed by the American Society of Addiction Medicine to guide appropriate level of care placement for individuals with substance use disorders."
                },
                {
                    "@type": "DefinedTerm",
                    "name": "CIWA-Ar",
                    "description": "Clinical Institute Withdrawal Assessment for Alcohol, Revised — a 10-item scale used to assess alcohol withdrawal severity and guide medication protocols during medical detox."
                },
                {
                    "@type": "DefinedTerm",
                    "name": "COWS",
                    "description": "Clinical Opiate Withdrawal Scale — a standardized tool used to assess opioid withdrawal severity and guide buprenorphine induction timing."
                },
                {
                    "@type": "DefinedTerm",
                    "name": "Dual Diagnosis",
                    "description": "The co-occurrence of a substance use disorder with one or more mental health conditions, requiring integrated treatment addressing both conditions simultaneously."
                },
                {
                    "@type": "DefinedTerm",
                    "name": "Medical Detox",
                    "description": "A supervised withdrawal management process conducted in a clinical setting, using medications to safely manage withdrawal symptoms for substances such as alcohol, benzodiazepines, and opioids."
                }
            ]
        },
        {
            "@type": "Thing",
            "@id": PAGE_URL + "#primary-topic",
            "name": "Couples Rehab Admissions",
            "description": "The process by which two partners seeking recovery from substance use disorder are assessed, placed, and admitted to coordinated addiction treatment programs simultaneously."
        }
    ]
}

# ── SCHEMA as an appended HTML block in content ────────────────────────────
schema_script = (
    "\n\n<!-- wp:html -->\n"
    "<script type=\"application/ld+json\">\n"
    + json.dumps(SCHEMA, indent=2)
    + "\n</script>\n<!-- /wp:html -->"
)

FULL_CONTENT = CONTENT + schema_script

# ── POST PAYLOAD ──────────────────────────────────────────────────────────────
SEO_TITLE = "Couples Rehab Admissions Guide | Step-by-Step Help Together - Couples Rehab"
META_DESC = ("Complete guide to the couples rehab admissions process — from first call to joint "
             "placement. Insurance verification, clinical assessment, and levels of care explained. "
             "Call (888) 500-2110.")
FOCUS_KW = "couples rehab admissions guide"
CANONICAL = PAGE_URL
OG_TITLE = "Couples Rehab Admissions Guide: Step-by-Step Help for Partners"
OG_DESC = ("Everything you need to know about the couples rehab admissions process — insurance, "
           "assessment, joint placement, and levels of care. Call (888) 500-2110 for 24/7 help.")
TW_TITLE = "Couples Rehab Admissions Guide | How to Get Help Together"
TW_DESC = ("A step-by-step walkthrough of the couples rehab admissions process — from first call "
           "to joint placement. Available 24/7 at (888) 500-2110.")

payload = {
    "title": "Couples Rehab Admissions Guide: A Step-by-Step Roadmap to Getting Help Together",
    "slug": "couples-rehab-admissions-guide",
    "status": "draft",
    "content": FULL_CONTENT,
    "excerpt": ("A complete step-by-step guide to the couples rehab admissions process — from the "
                "first call through insurance verification, clinical assessment, joint placement, "
                "and aftercare planning. Couples Rehab is a national placement and referral network "
                "available 24/7 at (888) 500-2110."),
    "parent": 0,
    "menu_order": 0,
    "meta": {
        "_yoast_wpseo_title": SEO_TITLE,
        "_yoast_wpseo_metadesc": META_DESC,
        "_yoast_wpseo_focuskw": FOCUS_KW,
        "_yoast_wpseo_canonical": CANONICAL,
        "_yoast_wpseo_opengraph-title": OG_TITLE,
        "_yoast_wpseo_opengraph-description": OG_DESC,
        "_yoast_wpseo_twitter-title": TW_TITLE,
        "_yoast_wpseo_twitter-description": TW_DESC,
        "schema_wp_custom_schema": json.dumps(SCHEMA)
    }
}

# ── POST ──────────────────────────────────────────────────────────────────────
print("Posting draft to WordPress...")
try:
    response = requests.post(
        WP_API_URL,
        auth=(WP_USERNAME, WP_APP_PASSWORD),
        json=payload,
        timeout=60
    )
    print(f"HTTP Status: {response.status_code}")
    if response.status_code in (200, 201):
        data = response.json()
        post_id = data.get("id", "unknown")
        link = data.get("link", "")
        edit_link = f"https://couplesrehab.com/wp-admin/post.php?post={post_id}&action=edit"
        print("SUCCESS")
        print(f"  Post ID:       {post_id}")
        print(f"  Draft link:    {link}")
        print(f"  Edit link:     {edit_link}")
        print(f"  Title:         {data.get('title', {}).get('rendered', '')}")
        print(f"  Slug:          {data.get('slug', '')}")
        print(f"  SEO title:     {SEO_TITLE}")
        print(f"  Focus keyword: {FOCUS_KW}")
    else:
        print("FAILED")
        print(f"  Response: {response.text[:800]}")
except Exception as exc:
    print(f"ERROR: {exc}")
