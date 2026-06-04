# -*- coding: utf-8 -*-
# SSO El Paso - dataset con contenido profundo desde inicio
# 4 silos, sin canibalizacion, intenciones especificas por pagina
import json

# Datos verificables (publicos) sobre SSA
# IMPORTANTE: Para deploy final, verificar oficina exacta de El Paso en SSA locator
OFFICE_INFO = {
    "address": "11111 Gateway Blvd W, El Paso, TX 79935",
    "phone_national": "1-800-772-1213",
    "tty": "1-800-325-0778",
    "hours_general": "Monday-Friday, 9:00 AM - 4:00 PM (Wednesdays often close earlier, around noon)",
    "closed": "Federal holidays and weekends",
    "online": "ssa.gov / my Social Security account at ssa.gov/myaccount",
}

NOTE_VERIFY = ("Office addresses, phone numbers and hours can change. Always confirm the current "
               "information on the official SSA office locator at ssa.gov/locator before visiting. "
               "Last verified May 2026.")

# ---------- SILO 1: SERVICES (high-RPM money pages) ----------
services = [
{"slug":"apply-for-social-security-card-el-paso","silo":"services",
 "h1":"How to Apply for a Social Security Card in El Paso, TX",
 "title":"Apply for a Social Security Card in El Paso (2026 Guide)",
 "meta":"Step-by-step guide to applying for a Social Security card in El Paso, Texas. Required documents, where to go, and how long it takes in 2026.",
 "intro":("Getting a Social Security Number (SSN) and card is one of the first things new residents, new workers, and parents of newborns need to handle. In El Paso, the application is done in person at the local SSA office, and the process is free. This guide walks through every step: what documents you need, where to go, and what to expect."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"To apply for a Social Security card in El Paso, complete Form SS-5, gather original proof of identity, age, and U.S. citizenship or lawful immigration status, then visit the SSA office at 11111 Gateway Blvd W. The service is free, and your card arrives by mail in 7-14 business days. You cannot apply online for your first SSN — it must be done in person."},
   {"type":"section","heading":"Who needs to apply for an SSN in person",
    "body":[
      "Three groups of people typically apply for a Social Security card in El Paso: U.S. citizens applying for the first time (often new parents getting an SSN for a newborn), lawful permanent residents and work-authorized immigrants who need an SSN for employment, and individuals who have never had an SSN before. Every first-time application must be made in person at an SSA office; there is no online option for an initial SSN.",
      "If you already have an SSN and just need a replacement card, the process is different — see our guide on replacing a Social Security card in El Paso. This page covers first-time applications only."]},
   {"type":"checklist","heading":"Required documents",
    "items":[
      "Completed Form SS-5 (download from ssa.gov or pick up at the office).",
      "Proof of U.S. citizenship: original birth certificate, U.S. passport, or Certificate of Naturalization (originals only — no copies).",
      "Proof of identity: state-issued ID, driver's license, or U.S. passport.",
      "For non-citizens: current immigration documents (I-551, I-94, EAD card) and unexpired foreign passport.",
      "For children: birth certificate plus proof of parent's identity.",
      "If applying for a child age 12+: the child must be present at the interview."]},
   {"type":"troubleshoot","heading":"The step-by-step process",
    "items":[
      {"q":"Step 1 - Complete Form SS-5","a":"Download the Application for a Social Security Card (Form SS-5) from ssa.gov or pick one up at the office. Fill it out completely before your visit to save time."},
      {"q":"Step 2 - Gather original documents","a":"You must bring ORIGINAL documents, not photocopies. The SSA will photocopy them and return the originals to you on the spot. Sending originals by mail is not recommended for first-time applications."},
      {"q":"Step 3 - Visit the SSA office in El Paso","a":"Walk in or, preferably, schedule an appointment by calling 1-800-772-1213. Appointments significantly reduce wait time, which can otherwise be 1-2 hours at peak times."},
      {"q":"Step 4 - The interview","a":"An SSA representative will review your form and documents. The appointment itself typically takes 15-30 minutes if your paperwork is in order."},
      {"q":"Step 5 - Receive your card by mail","a":"Your Social Security card arrives by U.S. mail at the address you provided, typically within 7-14 business days. The SSA does not issue cards on the spot."}]},
   {"type":"section","heading":"What if you are not a U.S. citizen",
    "body":[
      "Non-citizens can apply for an SSN if they are authorized to work in the United States. This includes lawful permanent residents (green card holders), work-authorized non-immigrants (such as H-1B, L-1, OPT students), and certain other categories. You will need to show your current immigration documents along with your unexpired foreign passport.",
      "If you are not authorized to work but need an SSN for a specific federal benefit or state law requirement, the SSA has a separate process. Most people in this situation will not qualify for an SSN and should look at an Individual Taxpayer Identification Number (ITIN) from the IRS instead."]},
   {"type":"faq_extra","items":[
     {"q":"How much does it cost to apply for a Social Security card?","a":"It is completely free. The SSA never charges for issuing or replacing a Social Security card. Be wary of any third party that asks you to pay."},
     {"q":"Can I apply online for my first SSN?","a":"No. First-time applications must be done in person at an SSA office. Only replacement cards (for those who already have an SSN) can sometimes be requested online."},
     {"q":"How long does the SSN itself take to be assigned?","a":"The SSN is assigned during processing and printed on the card you receive in the mail. From application to card in hand, plan for 2-3 weeks."},
     {"q":"What if my documents are not in English?","a":"Foreign documents must be accompanied by a certified English translation. The SSA office in El Paso has Spanish-speaking staff, but written documents still need certified translations."}]},
 ]},

{"slug":"replace-social-security-card-el-paso","silo":"services",
 "h1":"How to Replace a Lost Social Security Card in El Paso",
 "title":"Replace a Lost Social Security Card in El Paso, TX (2026)",
 "meta":"Lost your Social Security card in El Paso? Learn how to replace it for free in 2026, online or in person, and the limits on how many replacements you can get.",
 "intro":("Losing your Social Security card is stressful, but replacing it is straightforward and free. Many El Paso residents can request a replacement online without ever visiting the SSA office, while others must apply in person. This guide explains both routes, the documents you need, and the lifetime limits on replacement cards that surprise some people."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"To replace a lost Social Security card in El Paso, the fastest option is the online request through your my Social Security account at ssa.gov — if you qualify, you can submit it in minutes and receive the card by mail in 7-14 days. If you do not qualify online, visit the SSA office at 11111 Gateway Blvd W with proof of identity. Replacement is free, but you are limited to 3 per year and 10 in your lifetime."},
   {"type":"section","heading":"Who can replace their card online",
    "body":[
      "The SSA expanded online replacement in recent years, and many people no longer need to visit an office. You can request a replacement card online if you are a U.S. citizen, age 18 or older, have a valid driver's license or state-issued ID from a participating state (Texas is participating), have a U.S. mailing address, and are not asking for changes to the card (name change, for example, still requires an office visit).",
      "If any of these conditions does not apply to you, you will need to go to the El Paso SSA office in person with your documents."]},
   {"type":"troubleshoot","heading":"Two routes to replace your card",
     "items":[
       {"q":"Online (fastest, if you qualify)","a":"Log in to your my Social Security account at ssa.gov/myaccount, request a replacement card, and confirm your identity using your driver's license or state ID. The card arrives by mail in 7-14 business days. No appointment, no waiting, no documents to bring in person."},
       {"q":"In person at the El Paso SSA office","a":"If you cannot use the online service, visit the office at 11111 Gateway Blvd W. Bring an original proof of identity (driver's license, state ID, or U.S. passport). Form SS-5 is required but can be completed at the office. Scheduling an appointment by calling 1-800-772-1213 is strongly recommended to avoid long waits."}]},
   {"type":"section","heading":"The replacement limits most people do not know about",
    "body":[
      "Federal regulations limit you to 3 replacement Social Security cards in a year and 10 in your lifetime. These limits exist to prevent abuse and identity theft. There are exceptions, such as legal name changes and certain immigration status changes, which do not count toward the limit. But for ordinary lost-or-stolen replacements, the cap is real.",
      "If you are approaching these limits, you should think hard about whether you actually need a physical card. For most purposes (tax filing, opening a bank account, applying for jobs), you only need to know your number — having the physical card is helpful but rarely required."]},
   {"type":"checklist","heading":"Documents you need (in-person)",
    "items":[
      "Original proof of identity: unexpired driver's license, state-issued non-driver ID, or U.S. passport.",
      "Form SS-5, completed (can be filled at the office, but pre-filling saves time).",
      "If your name has changed: legal name-change document (marriage certificate, court order, divorce decree)."]},
   {"type":"faq_extra","items":[
     {"q":"How much does a replacement card cost?","a":"It is free. The SSA never charges for replacement cards. Any service charging you a fee for this is a third party, not the SSA."},
     {"q":"Do I really need the physical card?","a":"For most purposes, no. Tax forms, employer paperwork, and bank accounts ask for the number, not the physical card. Keep your card safe at home and avoid carrying it in your wallet."},
     {"q":"What if my card was stolen and I am worried about identity theft?","a":"Replace the card normally, but also place a fraud alert with the credit bureaus and monitor your credit reports. The SSA does not change your SSN simply because the card was stolen, but you can request a new SSN in extreme cases of ongoing fraud."},
     {"q":"How long does the replacement actually take?","a":"The card itself arrives 7-14 business days after the request is approved. Online requests are processed quickly; in-person requests are typically processed the same or next day."}]},
 ]},

{"slug":"apply-for-disability-benefits-el-paso","silo":"services",
 "h1":"How to Apply for Social Security Disability Benefits in El Paso",
 "title":"Apply for Disability Benefits (SSDI/SSI) in El Paso, TX (2026)",
 "meta":"Step-by-step guide to applying for Social Security disability benefits in El Paso, Texas. SSDI vs SSI, required medical evidence, and what to expect in 2026.",
 "intro":("Applying for Social Security disability benefits is one of the most consequential and confusing processes the SSA handles. Many El Paso residents qualify for benefits but never apply, or apply incorrectly and are denied. This guide explains how to apply, the difference between SSDI and SSI, what medical evidence you need, and realistic expectations for timing."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"To apply for Social Security disability benefits in El Paso, you can start online at ssa.gov/applyfordisability, by phone at 1-800-772-1213, or in person at the El Paso SSA office. The two main programs are SSDI (based on your work history) and SSI (based on financial need). Both require strong medical evidence proving your disability prevents substantial work. Initial decisions take 3-6 months, and the initial denial rate is around 65%."},
   {"type":"section","heading":"SSDI vs SSI: which one do you apply for?",
    "body":[
      "This is the first thing to understand and where many people get tripped up. Social Security Disability Insurance (SSDI) is funded by payroll taxes and requires that you have worked enough recent quarters (typically 5 of the last 10 years) and paid Social Security taxes. The benefit amount depends on your earnings history.",
      "Supplemental Security Income (SSI), by contrast, is needs-based. It does not require work history but does require very limited income and assets (generally under $2,000 for an individual). Some people qualify for both programs at the same time, which is called concurrent benefits.",
      "When you apply, the SSA will assess which program(s) you qualify for based on your situation. You do not need to choose in advance — apply, and the SSA evaluates eligibility for both."]},
   {"type":"troubleshoot","heading":"How to apply: three options",
    "items":[
      {"q":"Online (recommended for SSDI)","a":"The online application at ssa.gov/applyfordisability is the most convenient route and lets you save progress and come back later. It takes most people 1-2 hours to complete. SSI applications can be started online but generally require a follow-up interview."},
      {"q":"By phone","a":"Call 1-800-772-1213 to begin a phone application. A representative will help complete the forms with you over the phone. This is useful if you cannot easily complete the online application due to health or technology barriers."},
      {"q":"In person at the El Paso SSA office","a":"Visit 11111 Gateway Blvd W to apply with help from a representative. Appointments are strongly recommended — call ahead. Bring all your medical records, list of doctors, and employment history."}]},
   {"type":"checklist","heading":"What you need to apply",
    "items":[
      "Medical records: doctors, hospitals, clinics that have treated your condition (names, addresses, dates).",
      "Medications: full list with dosages and prescribing doctors.",
      "Work history for the last 15 years: jobs, dates, duties, earnings.",
      "Most recent W-2 or self-employment tax return.",
      "Birth certificate or proof of U.S. citizenship/lawful status.",
      "Bank account info for direct deposit.",
      "For SSI: detailed financial information on income, assets, and living arrangements."]},
   {"type":"section","heading":"What to expect: timing and the appeals process",
    "body":[
      "Initial disability decisions take 3-6 months in most cases, sometimes longer. Around 65% of initial applications are denied, often because of incomplete medical evidence rather than because the person is not disabled. This is the single most important fact to understand: a denial is not the end of the road, and many people who eventually receive benefits were denied at the initial stage.",
      "If denied, you have 60 days to file a reconsideration. If denied again, you can request a hearing before an Administrative Law Judge, where many cases are won. The full appeals process can take 1-2 years, which is why getting the application right from the start is so valuable. Many applicants work with a Social Security disability attorney, who typically only gets paid (a capped percentage of back-benefits) if you win."]},
   {"type":"faq_extra","items":[
     {"q":"What conditions qualify for disability?","a":"There is no fixed list. The SSA evaluates whether your condition prevents you from doing substantial work and is expected to last at least 12 months or result in death. Conditions ranging from severe physical injuries to mental health disorders, cancer, chronic illnesses, and developmental disabilities can all qualify with sufficient medical evidence."},
     {"q":"Can I work while I apply?","a":"You can earn up to a small amount (the Substantial Gainful Activity threshold, around $1,550/month in 2024) without disqualifying yourself, but earning above that level is generally treated as evidence you are not disabled."},
     {"q":"Should I hire a disability attorney?","a":"For initial applications, many people apply on their own. For appeals (especially hearings), having an attorney significantly improves your chances. Most disability attorneys work on contingency, taking a capped percentage of the back-benefits if you win, and nothing if you lose."},
     {"q":"How much will I receive?","a":"For SSDI, the amount depends on your work history (average benefit is around $1,500/month). For SSI, the federal maximum is around $943/month for an individual in 2024, with possible state supplements."}]},
 ]},

{"slug":"apply-for-ssi-el-paso","silo":"services",
 "h1":"How to Apply for Supplemental Security Income (SSI) in El Paso",
 "title":"Apply for SSI in El Paso, TX (2026 Guide)",
 "meta":"How to apply for Supplemental Security Income (SSI) in El Paso, Texas in 2026. Income limits, required documents, and how the process differs from SSDI.",
 "intro":("Supplemental Security Income (SSI) is a needs-based program that helps people with limited income who are disabled, blind, or age 65 or older. Unlike SSDI, it does not require any work history. This guide explains how SSI works in El Paso, who qualifies, and the application steps — including the income and asset limits that catch many people by surprise."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"To apply for SSI in El Paso, start at ssa.gov, call 1-800-772-1213, or visit the SSA office at 11111 Gateway Blvd W. SSI is needs-based, with strict income and asset limits (generally under $2,000 in countable assets for an individual). Eligibility requires being disabled, blind, or 65+, and meeting the financial limits. The federal maximum benefit is around $943/month for an individual."},
   {"type":"section","heading":"How SSI differs from SSDI",
    "body":[
      "SSI and SSDI are often confused because they are both administered by the SSA and both can pay benefits to disabled people. The key difference: SSDI is based on your work history and the Social Security taxes you paid, while SSI is based on financial need and does not require work history at all.",
      "This matters because SSI is often the right program for people who become disabled before they have a substantial work history (such as young adults), elderly people without enough Social Security credits, and children with serious disabilities. You can sometimes qualify for both SSI and SSDI at the same time — this is called concurrent benefits."]},
   {"type":"checklist","heading":"The income and asset limits",
    "items":[
      "Countable resources must generally be below $2,000 for an individual or $3,000 for a couple.",
      "Your home and one vehicle do not count toward the resource limit.",
      "Most income reduces the SSI benefit dollar-for-dollar after small exclusions.",
      "Some non-cash help (like food or shelter from family) is treated as 'in-kind support' and reduces SSI.",
      "Resource limits are strict, but household belongings, burial plots, and certain other assets do not count."]},
   {"type":"section","heading":"How to apply step by step",
    "body":[
      "SSI applications generally cannot be completed entirely online. You can start the application on ssa.gov, but you will typically need to follow up with a phone interview or visit to complete the financial portion. The El Paso SSA office at 11111 Gateway Blvd W can guide you through it in person.",
      "When you apply, be prepared to document not just your medical condition (if applying due to disability) but also your full financial picture: bank statements, property, vehicles, sources of income, household composition, and any in-kind support you receive. This is where SSI applications go wrong most often — incomplete financial disclosure leads to denials or later overpayment claims."]},
   {"type":"faq_extra","items":[
     {"q":"Can children get SSI?","a":"Yes. Disabled children whose family income and resources fall within the limits can qualify for SSI. The medical standard for children is different and focuses on functional limitations in age-appropriate activities."},
     {"q":"What if my income changes?","a":"You must report changes in income, assets, household, or living situation to the SSA promptly. Failing to report changes is the most common cause of SSI overpayments, which the SSA later demands back."},
     {"q":"Does SSI come with health coverage?","a":"In Texas, SSI recipients are generally automatically eligible for Medicaid, which provides health coverage. This is one of the most important practical benefits of SSI."},
     {"q":"How long until I get a decision?","a":"Like SSDI, disability-based SSI decisions take 3-6 months. Age-based SSI (for those 65+) is typically faster because it does not require medical review."}]},
 ]},

{"slug":"apply-for-social-security-retirement-el-paso","silo":"services",
 "h1":"How to Apply for Social Security Retirement in El Paso",
 "title":"Apply for Social Security Retirement Benefits in El Paso (2026)",
 "meta":"Step-by-step guide to applying for Social Security retirement benefits in El Paso, TX. When to apply, how much you'll receive, and the online vs in-person options in 2026.",
 "intro":("Applying for Social Security retirement is one of the most important financial decisions you will make in your life — and the timing of when to start benefits affects how much you receive for the rest of it. This guide explains how to apply in El Paso, the trade-offs between starting early and waiting, and what documents you need."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"You can apply for Social Security retirement online at ssa.gov, by phone at 1-800-772-1213, or in person at the SSA office in El Paso. Apply 3-4 months before you want benefits to start. The earliest age is 62 (with permanently reduced benefits), Full Retirement Age is 66-67 depending on birth year, and waiting until 70 maximizes your monthly benefit by about 8% per year between FRA and 70."},
   {"type":"section","heading":"When to apply: the timing question",
    "body":[
      "The single most important retirement decision is when to start benefits, not how to apply. Starting at 62 (the earliest age) permanently reduces your monthly benefit by 25-30% compared to Full Retirement Age. Waiting from FRA to age 70 increases your benefit by about 8% per year. Over a typical retirement, these differences add up to tens of thousands of dollars.",
      "There is no universally right answer. Starting early makes sense if you have shorter-than-average life expectancy, urgent income needs, or specific tax planning reasons. Waiting makes sense if you are healthy, have other income to bridge the gap, and want the largest possible inflation-protected monthly benefit. Use our retirement age calculator to find your Full Retirement Age."]},
   {"type":"troubleshoot","heading":"How to apply in El Paso",
    "items":[
      {"q":"Online (easiest)","a":"The online application at ssa.gov/retirement takes about 15 minutes if you have a my Social Security account already set up. You can save and return, and most applications are approved without an in-person visit."},
      {"q":"By phone","a":"Call 1-800-772-1213. A representative will complete the application with you over the phone. Useful if you have questions or prefer not to use online forms."},
      {"q":"In person","a":"Visit the El Paso SSA office at 11111 Gateway Blvd W. Schedule an appointment in advance for shorter wait times. This is most useful for complex situations involving spousal benefits, divorced spouse benefits, or non-citizen status."}]},
   {"type":"checklist","heading":"Documents you need",
    "items":[
      "Birth certificate or other proof of age.",
      "Proof of U.S. citizenship or lawful immigration status.",
      "W-2 or self-employment tax return from the previous year.",
      "Military service papers if you served before 1968.",
      "Marriage and divorce documents if applying for spousal benefits.",
      "Bank account information for direct deposit (paper checks are no longer issued)."]},
   {"type":"section","heading":"What about Medicare?",
    "body":[
      "If you are 65 or older and applying for Social Security retirement, your Medicare enrollment is typically handled automatically when you apply for retirement benefits. If you want Medicare but plan to delay Social Security past 65, you need to enroll separately during your Initial Enrollment Period to avoid late-enrollment penalties.",
      "See our guide on applying for Medicare in El Paso for the full process, including Part A, Part B, and Part D enrollment details."]},
   {"type":"faq_extra","items":[
     {"q":"What is the maximum Social Security retirement benefit?","a":"In 2024 the maximum monthly benefit at Full Retirement Age was around $3,822. The maximum at age 70 was around $4,873. These figures are for high earners with 35+ years at the maximum taxable earnings, and they adjust each year with the COLA."},
     {"q":"Can I work while receiving retirement benefits?","a":"Yes, but before Full Retirement Age there is an earnings limit. Once you reach FRA, you can earn unlimited amounts with no reduction in benefits. See our guide on working while receiving Social Security."},
     {"q":"What if I am divorced — can I claim on my ex-spouse's record?","a":"Yes, if your marriage lasted at least 10 years, you are at least 62, and you are currently unmarried. You can claim up to 50% of your ex's full benefit. Your ex is not notified and your claim does not reduce their benefit."},
     {"q":"How long does retirement application take to process?","a":"Most retirement applications are processed within a few weeks. Apply 3-4 months before you want benefits to start to ensure timely first payment."}]},
 ]},

{"slug":"apply-for-medicare-el-paso","silo":"services",
 "h1":"How to Apply for Medicare in El Paso, TX",
 "title":"Apply for Medicare in El Paso (2026 Enrollment Guide)",
 "meta":"How to enroll in Medicare in El Paso, Texas. Initial enrollment period, automatic enrollment, Part A, B, and D explained, plus how to avoid late penalties in 2026.",
 "intro":("Medicare is the federal health insurance program for people 65 and older (and certain younger people with disabilities). The enrollment rules are surprisingly complex, and missing key deadlines can mean paying late-enrollment penalties for the rest of your life. This guide explains how to enroll from El Paso, what is automatic versus what requires action, and the most common mistakes to avoid."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"Most people become eligible for Medicare at age 65. If you are already receiving Social Security retirement, enrollment in Medicare Part A and Part B is automatic — your card arrives by mail. If you are not yet on Social Security, you must actively enroll during your Initial Enrollment Period (the 7-month window around your 65th birthday) at ssa.gov/medicare or by calling 1-800-772-1213. Missing this window can mean lifelong late penalties."},
   {"type":"section","heading":"Automatic enrollment vs active enrollment",
    "body":[
      "If you are already collecting Social Security retirement or SSDI when you turn 65, the SSA automatically enrolls you in Medicare Part A (hospital insurance) and Part B (medical insurance). Your Medicare card arrives in the mail about 3 months before your 65th birthday. You do not need to apply.",
      "If you are not yet collecting Social Security at 65 — common for people who plan to delay benefits to age 67 or 70 — Medicare is NOT automatic. You must actively enroll. This is where people get into trouble: they assume Medicare comes with turning 65, miss the window, and then face permanent late-enrollment penalties added to their premiums for life."]},
   {"type":"troubleshoot","heading":"The four parts of Medicare",
    "items":[
      {"q":"Part A (Hospital Insurance)","a":"Covers inpatient hospital care, skilled nursing facility care, and some home health care. Free for most people who paid Medicare taxes for at least 10 years. Enroll during your Initial Enrollment Period even if you have other coverage."},
      {"q":"Part B (Medical Insurance)","a":"Covers doctor visits, outpatient care, preventive services, and durable medical equipment. Standard premium in 2024 was around $174.70/month. Late enrollment without other qualifying coverage adds 10% to your premium for each 12-month delay — permanently."},
      {"q":"Part C (Medicare Advantage)","a":"Private plans that bundle Parts A, B, and usually D, often with extra benefits like dental or vision. Offered by private insurers approved by Medicare. You can switch between Original Medicare and a Part C plan during annual open enrollment."},
      {"q":"Part D (Prescription Drug Coverage)","a":"Optional but recommended for most people. Late enrollment without other qualifying drug coverage adds 1% to your premium for each month delayed — permanently."}]},
   {"type":"section","heading":"Your Initial Enrollment Period",
    "body":[
      "Your Initial Enrollment Period is a 7-month window: it starts 3 months before the month you turn 65, includes your birthday month, and continues for 3 months after. Enrolling during the first 3 months means your coverage starts on the first day of your birthday month. Enrolling later means coverage starts later, and missing the entire window means waiting for the General Enrollment Period (January 1 - March 31) with coverage starting July 1 — and likely paying late penalties.",
      "If you are still working at 65 and have qualifying employer health insurance, you may qualify for a Special Enrollment Period when that coverage ends, with no late penalty. Confirm with the SSA before relying on this."]},
   {"type":"faq_extra","items":[
     {"q":"Can I apply for Medicare in person at the El Paso SSA office?","a":"Yes. You can also enroll online at ssa.gov/medicare or by phone at 1-800-772-1213. Online is fastest for straightforward cases."},
     {"q":"What if I am still working at 65?","a":"If you have qualifying employer group health insurance through current employment (yours or your spouse's), you may delay Part B without penalty. Confirm this in advance and document it. When the employer coverage ends, you have an 8-month Special Enrollment Period."},
     {"q":"Does Medicare cover everything?","a":"No. Original Medicare leaves significant gaps: copays, deductibles, no dental, vision, hearing aids, or long-term custodial care. Many people buy a Medicare Supplement (Medigap) policy or join a Medicare Advantage plan to fill these gaps."},
     {"q":"How much does Medicare cost?","a":"Part A is free for most. Part B was around $174.70/month in 2024 (higher for high earners). Part D premiums vary by plan. Total monthly costs typically range from $174 to $400+ depending on coverage choices."}]},
 ]},

{"slug":"change-name-on-social-security-card-el-paso","silo":"services",
 "h1":"How to Change Your Name on a Social Security Card in El Paso",
 "title":"Change Your Name on Social Security Card in El Paso, TX (2026)",
 "meta":"Got married, divorced, or legally changed your name? Step-by-step guide to updating your Social Security card in El Paso in 2026.",
 "intro":("Whether you got married, divorced, or completed a legal name change in court, updating your Social Security record is one of the most important administrative steps to take. This guide walks through exactly how to change your name on your Social Security card from El Paso, what documents you need, and why doing this promptly matters for your tax return and Social Security benefits."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"To change your name on your Social Security card in El Paso, you must apply in person at the SSA office at 11111 Gateway Blvd W. Online and mail-in requests are not accepted for name changes. Bring Form SS-5, original proof of identity, and original legal name-change documents (marriage certificate, divorce decree, or court order). The new card is free and arrives by mail in 7-14 business days. The name change does not count toward your 10-lifetime replacement limit."},
   {"type":"section","heading":"Why you should change it promptly",
    "body":[
      "Your name on file with the SSA must match your name on your W-2 and your tax return, or the IRS may reject your filing or your refund. If you changed your name and have not updated the SSA, your wages may not be properly credited to your earnings record, which can affect your future Social Security benefit.",
      "There is no legal deadline to update your name, but the practical recommendation is to do it as soon as possible after the legal change, especially before tax season."]},
   {"type":"checklist","heading":"Documents you need",
    "items":[
      "Completed Form SS-5.",
      "Original or certified legal name-change document (marriage certificate, divorce decree showing name change, or court order).",
      "Original proof of identity in your NEW name (driver's license, state ID, passport) OR original proof in your old name plus the legal name change document.",
      "Proof of U.S. citizenship if not already on file.",
      "For non-citizens: current immigration documents."]},
   {"type":"section","heading":"Step by step",
    "body":[
      "Gather your original documents — not copies. The SSA will photocopy them at the office and hand the originals back to you on the spot. Complete Form SS-5 in advance, available at ssa.gov.",
      "Visit the El Paso SSA office at 11111 Gateway Blvd W. Scheduling an appointment in advance significantly reduces wait time. A representative will review your documents and process the request. Your new card with the updated name arrives by mail in 7-14 business days.",
      "Important to know: the Social Security number stays the same. Only your name on file changes. Keep your old card destroyed once the new one arrives to prevent confusion."]},
   {"type":"faq_extra","items":[
     {"q":"Does a name change count toward the 10-card lifetime limit?","a":"No. Cards issued due to a legal name change do not count toward the 10-replacement lifetime limit. Neither do certain immigration-status-related changes."},
     {"q":"What if I changed my name informally?","a":"The SSA only accepts legal name changes documented by marriage certificate, divorce decree, or court order. Simply going by a different name informally is not enough."},
     {"q":"Do I need to change my name everywhere else first?","a":"No. The SSA does not require that your driver's license or other IDs already show the new name. But practically, it's easier to do this after your name has been updated on your photo ID."},
     {"q":"How long after marriage should I update it?","a":"There is no deadline, but doing it within a month or two after the wedding is common and avoids tax-season complications the following year."}]},
 ]},

{"slug":"get-social-security-number-for-newborn-el-paso","silo":"services",
 "h1":"How to Get a Social Security Number for a Newborn in El Paso",
 "title":"Social Security Number for Newborn in El Paso, TX (2026)",
 "meta":"How to get a Social Security number and card for a newborn in El Paso. Hospital application process, what documents are needed, and how long it takes in 2026.",
 "intro":("Getting a Social Security number for your newborn is one of the first administrative tasks after birth — and it is easier than most people expect, because in most cases the hospital handles the paperwork for you. This guide explains exactly what happens at El Paso hospitals, what to do if you decline at the hospital, and why having the SSN early matters for your taxes."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"In most cases, you can apply for your newborn's Social Security number right at the hospital when you complete the birth registration paperwork. You check a box, provide your information, and the card arrives by mail in 6-12 weeks. If you decline at the hospital or need to apply later, you must visit the El Paso SSA office in person with the child's birth certificate and your own ID."},
   {"type":"section","heading":"The hospital route (the easiest path)",
    "body":[
      "When you have a baby at an El Paso hospital and complete the birth registration paperwork, one of the questions asks whether you want a Social Security number for your child. Saying yes is the simplest possible application: the hospital forwards the information to the state vital records office, which sends it to the SSA, which mails you the card. You do not need to visit the SSA office, complete additional forms, or pay anything.",
      "The card typically arrives 6-12 weeks after birth, often slower than the birth certificate itself. The SSN is assigned during processing and printed on the card."]},
   {"type":"section","heading":"If you did not apply at the hospital",
    "body":[
      "If you declined or were not asked at the hospital, you can still apply for your child's SSN later. This requires visiting the El Paso SSA office in person at 11111 Gateway Blvd W. You will need the child's certified birth certificate (not a copy), proof of the child's identity (which can be challenging for very young children — medical records, day care records, or a passport can work), and proof of your own identity as the parent.",
      "If the child is age 12 or older, the child must be present at the interview for the SSA to verify identity."]},
   {"type":"checklist","heading":"Why getting it early matters",
    "items":[
      "You need the child's SSN to claim them as a dependent on your federal tax return.",
      "Many medical insurance plans require the SSN to add the child to coverage.",
      "529 college savings plans and other financial accounts for the child require the SSN.",
      "Getting it at the hospital avoids a later in-person visit to the SSA office.",
      "There is no deadline, but doing it within the first few months simplifies tax season."]},
   {"type":"faq_extra","items":[
     {"q":"How much does it cost?","a":"It is free, like all SSN applications. Be wary of any service that charges to obtain an SSN for your child."},
     {"q":"Can I apply online for my baby's SSN?","a":"No. First-time SSN applications cannot be done online. The hospital route or in-person at an SSA office are the only options."},
     {"q":"What if my baby was born outside the U.S.?","a":"A child born abroad to U.S. citizen parents typically gets a Consular Report of Birth Abroad (CRBA) and can then apply for an SSN. The process is more involved and may need to be handled in person at an SSA office."},
     {"q":"How long does it take to receive the card?","a":"From the hospital application, typically 6-12 weeks. From an in-person SSA office application, 7-14 business days like other applications."}]},
 ]},
]

# ---------- SILO 2: OFFICE (location, hours, appointments) ----------
office = [
{"slug":"social-security-office-el-paso","silo":"office",
 "h1":"Social Security Office in El Paso, TX",
 "title":"Social Security Office in El Paso, TX: Address, Hours & Services (2026)",
 "meta":"Complete guide to the Social Security office in El Paso, Texas: address, phone, hours, services, parking, and how to schedule an appointment in 2026.",
 "intro":("The Social Security Administration office in El Paso serves residents of El Paso County and nearby areas for everything from Social Security card applications to disability benefit claims, retirement applications, and Medicare enrollment. This page gathers the practical information you need before visiting: address, hours, services, and tips for making your trip efficient."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"The main Social Security Administration office serving El Paso is located at 11111 Gateway Blvd W, El Paso, TX 79935. The office is open Monday-Friday during business hours, with Wednesdays often closing earlier. Walk-ins are accepted but appointments (call 1-800-772-1213) significantly reduce wait time. The national SSA phone line at 1-800-772-1213 can handle many requests without an office visit."},
   {"type":"checklist","heading":"Office at a glance",
    "items":[
      "Address: 11111 Gateway Blvd W, El Paso, TX 79935.",
      "National phone: 1-800-772-1213.",
      "TTY: 1-800-325-0778.",
      "Hours: Monday-Friday business hours (Wednesday often closes early).",
      "Closed: weekends and federal holidays.",
      "Website: ssa.gov (most services can be handled online)."]},
   {"type":"section","heading":"What you can do at the El Paso SSA office",
    "body":[
      "Many services people associate with the SSA can actually be handled online or by phone, but several still require an in-person visit to El Paso office. First-time Social Security card applications, name changes, and certain immigration-related updates must be done in person. Submitting original documents that cannot be mailed (like birth certificates and immigration papers) is the most common reason for visiting.",
      "For disability claims, retirement applications, and Medicare enrollment, you have a choice: online at ssa.gov, phone, or in person. Online is fastest for simple cases. The office is most useful for complex situations or when you prefer face-to-face guidance."]},
   {"type":"section","heading":"Tips for visiting",
    "body":[
      "The single best tip is to schedule an appointment in advance by calling 1-800-772-1213. Walk-ins are accepted, but waits of 1-2 hours are common at peak times, especially mid-morning and around lunch. With an appointment, most visits are completed in 15-30 minutes.",
      "Bring originals of every document you might need, not photocopies. The SSA staff will copy them on the spot and hand the originals back. Mondays and the days right after a holiday are typically the busiest — try mid-week if you have flexibility."]},
   {"type":"faq_extra","items":[
     {"q":"Can I handle everything online instead of visiting?","a":"For many services, yes. Retirement applications, replacement cards (for qualifying applicants), benefit verifications, and address changes can be done online at ssa.gov. First-time SSN applications, name changes, and certain immigration matters require an in-person visit."},
     {"q":"How early should I arrive for my appointment?","a":"Arrive 15 minutes before your scheduled time. Security screening adds a few minutes, and being late can mean rescheduling."},
     {"q":"Is parking available?","a":"Yes, the office has dedicated parking on site. Arrive a few minutes earlier during busy times."},
     {"q":"What if I cannot get to the office?","a":"Many services can be handled by phone at 1-800-772-1213 or online at ssa.gov. The SSA also offers limited home visit services for people with serious mobility issues — call to inquire."}]},
 ]},

{"slug":"social-security-office-hours-el-paso","silo":"office",
 "h1":"Social Security Office Hours in El Paso, TX",
 "title":"SSA Office Hours in El Paso, TX (2026 Schedule)",
 "meta":"Current Social Security office hours in El Paso, Texas. Days open, holiday closures, and Wednesday early-close schedule for 2026.",
 "intro":("Knowing the Social Security office hours in El Paso saves a wasted trip. The SSA's schedule has a few quirks — including Wednesday early closes and a long list of federal holiday closures — that catch people out. This page explains the current hours, what days the office is closed, and how to confirm before visiting."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"The El Paso SSA office at 11111 Gateway Blvd W is generally open Monday through Friday during standard business hours, with Wednesdays often closing earlier (around noon) to allow staff to process casework. The office is closed on weekends and all federal holidays. Hours can change, so confirm by calling 1-800-772-1213 or checking the SSA office locator at ssa.gov/locator before you visit."},
   {"type":"section","heading":"The Wednesday early-close",
    "body":[
      "One quirk most people do not know: most SSA field offices nationwide, including El Paso, close earlier on Wednesdays — typically around noon. This is to give staff time to process the backlog of cases without the pressure of walk-ins. If you plan a Wednesday afternoon visit, you will likely find the office closed.",
      "If you need afternoon service, plan for Monday, Tuesday, Thursday, or Friday. Mornings are universally busier than afternoons, so if your schedule is flexible, an afternoon non-Wednesday visit usually has the shortest wait."]},
   {"type":"checklist","heading":"Federal holidays when the office is closed",
    "items":[
      "New Year's Day (January 1).",
      "Martin Luther King Jr. Day (third Monday in January).",
      "Presidents Day (third Monday in February).",
      "Memorial Day (last Monday in May).",
      "Juneteenth National Independence Day (June 19).",
      "Independence Day (July 4).",
      "Labor Day (first Monday in September).",
      "Columbus Day (second Monday in October).",
      "Veterans Day (November 11).",
      "Thanksgiving Day (fourth Thursday in November).",
      "Christmas Day (December 25)."]},
   {"type":"section","heading":"How to use the office hours efficiently",
    "body":[
      "The best practice: schedule an appointment in advance by calling 1-800-772-1213, regardless of the hours. With an appointment, you will be seen close to your scheduled time even on busy days. Walk-ins are accepted but can mean 1-2 hour waits at peak times.",
      "If you only need a quick service (like updating your address or requesting a benefit verification), check first whether you can do it online at ssa.gov — many of these no longer require an office visit at all."]},
   {"type":"faq_extra","items":[
     {"q":"Is the El Paso office open on weekends?","a":"No. All SSA field offices, including El Paso, are closed on Saturdays and Sundays. Use ssa.gov for any service available online."},
     {"q":"What if I arrive close to closing time?","a":"You may be turned away if there is not enough time to process your visit. Plan to arrive at least 30 minutes before closing — and earlier on Wednesdays, when the office closes around noon."},
     {"q":"Can I call the office directly to confirm hours?","a":"Direct local phone lines for field offices have been replaced by the national line at 1-800-772-1213. That number can confirm current hours for the El Paso office."},
     {"q":"Are the hours different around holidays?","a":"Yes. Around major holidays, the office may have modified hours in addition to the holiday closure itself. Always confirm before visiting during holiday weeks."}]},
 ]},

{"slug":"social-security-office-appointment-el-paso","silo":"office",
 "h1":"How to Book an Appointment at the El Paso SSA Office",
 "title":"Book a Social Security Appointment in El Paso, TX (2026)",
 "meta":"How to schedule an appointment at the El Paso Social Security office. Why appointments save hours of waiting, and what to bring with you in 2026.",
 "intro":("Walking into the El Paso SSA office without an appointment can mean waiting 1-2 hours during busy periods. With an appointment, the same visit typically takes 15-30 minutes total. This page explains exactly how to schedule one, why it makes such a difference, and the questions you should be ready to answer when you call."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"To book an appointment at the El Paso SSA office, call the national SSA line at 1-800-772-1213 (TTY: 1-800-325-0778) Monday through Friday during business hours. Tell the representative you want an appointment at the El Paso office and the service you need. Appointments are usually available within 2-4 weeks. There is no online appointment booking for general services at the time of writing."},
   {"type":"section","heading":"Why an appointment is worth the wait",
    "body":[
      "The El Paso SSA office, like most field offices, sees significantly more walk-ins than scheduled appointments. Walk-ins are taken in order of arrival, behind scheduled appointments, which means a Monday morning visit without an appointment can easily mean 1-2 hours of waiting in the lobby. With an appointment, you typically wait 5-15 minutes past your scheduled time, and the actual visit takes 15-30 minutes.",
      "Time savings aside, an appointment also lets you know exactly what documents to bring, because the representative who books you will tell you what is needed for the specific service."]},
   {"type":"troubleshoot","heading":"How to book step by step",
    "items":[
      {"q":"Step 1 - Call 1-800-772-1213","a":"This is the national SSA line and the only way to book an appointment at any field office, including El Paso. Have a pen ready to write down your appointment time and the documents you need to bring."},
      {"q":"Step 2 - Tell them which office and which service","a":"Specify El Paso and what you need (apply for SSN card, name change, retirement, disability, etc.). The representative will look up available slots."},
      {"q":"Step 3 - Confirm and note what to bring","a":"Once your appointment is confirmed, the representative will tell you exactly which documents are required. Write everything down."},
      {"q":"Step 4 - Arrive 15 minutes early","a":"On the day, arrive at 11111 Gateway Blvd W at least 15 minutes before your slot to allow for security screening and check-in."}]},
   {"type":"section","heading":"What to do if you cannot get an appointment soon enough",
    "body":[
      "If the wait for an appointment is too long for your situation, consider whether your need can be handled online or by phone. Many SSA services do not require an in-person visit at all: online retirement applications, replacement card requests, benefit verifications, address changes, and direct deposit updates can all be done at ssa.gov.",
      "If you genuinely need an in-person visit and cannot wait, the office accepts walk-ins. Try to arrive at opening, on a non-Monday, non-Wednesday morning for the shortest typical wait."]},
   {"type":"faq_extra","items":[
     {"q":"Can I book an appointment online?","a":"At the time of writing, the SSA does not offer online appointment booking for most services. Appointments are scheduled by calling 1-800-772-1213. Some specific services may have separate online intake processes."},
     {"q":"How far in advance should I call?","a":"2-4 weeks is typical, but availability varies. Call as soon as you know you need an appointment, especially around tax season or year-end when demand is high."},
     {"q":"What if I miss my appointment?","a":"Call 1-800-772-1213 to reschedule. Missing without rescheduling can mean a longer wait for the next available slot."},
     {"q":"Is there an extra cost for an appointment?","a":"No. All SSA services are free, with no fee for scheduling or for the appointment itself."}]},
 ]},

{"slug":"social-security-office-near-me-el-paso","silo":"office",
 "h1":"Social Security Office Near Me in El Paso, TX",
 "title":"Social Security Office Near Me in El Paso, TX (2026)",
 "meta":"Find the Social Security office serving your area of El Paso, TX. Address, distance from major neighborhoods, and how to confirm which office to visit in 2026.",
 "intro":("'Social Security office near me' is one of the most common searches in El Paso, and the answer is simple: the El Paso SSA field office at 11111 Gateway Blvd W serves the entire El Paso area. Whether you live in West El Paso, the Northeast, the East side, or downtown, this is the office for you. This page explains which office to use, how to find it, and what to do if you live in a neighboring county."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"The Social Security office serving El Paso is located at 11111 Gateway Blvd W, El Paso, TX 79935. This single office covers all El Paso city neighborhoods including West Side, Northeast, East Side, Lower Valley, Mission Valley, and Downtown. If you are unsure which SSA office serves your address, use the official locator at ssa.gov/locator and enter your ZIP code."},
   {"type":"section","heading":"Which neighborhoods are served by this office",
    "body":[
      "Every neighborhood within the city of El Paso is served by the same field office at 11111 Gateway Blvd W. Whether you are in Cielo Vista on the east side, Westside near UTEP, Northeast near Fort Bliss, Downtown, or further out in the Lower Valley, this is your office.",
      "The Gateway Blvd location is on the east side of El Paso, near the Cielo Vista Mall area. From most parts of the city, it is a 15-30 minute drive depending on traffic and starting point."]},
   {"type":"section","heading":"What if you live near El Paso but not in the city",
    "body":[
      "Residents of nearby communities like Sunland Park, Anthony, Horizon City, and Socorro generally also use the El Paso SSA office at 11111 Gateway Blvd W, as it is the closest field office. If you live further away (in Hudspeth County, for example, or in New Mexico beyond Sunland Park), use the SSA office locator at ssa.gov/locator with your ZIP code to confirm which office serves you.",
      "There is no choice involved — the SSA assigns each ZIP code to a specific field office. You go to whichever office covers your address."]},
   {"type":"checklist","heading":"Tips for finding the office",
    "items":[
      "Use a navigation app (Google Maps, Apple Maps) with the address 11111 Gateway Blvd W, El Paso, TX 79935.",
      "Plan extra time during rush hour, especially on I-10 and Loop 375.",
      "Free parking is available on site.",
      "The office is wheelchair accessible.",
      "Security screening is required at the entrance — allow a few extra minutes."]},
   {"type":"faq_extra","items":[
     {"q":"Is there more than one SSA office in El Paso?","a":"There is one main field office serving the city of El Paso. The SSA periodically updates its office locations, so confirm by checking ssa.gov/locator with your ZIP code."},
     {"q":"Can I visit any SSA office or do I have to go to mine?","a":"For most services, you can visit any SSA office in the country. However, for complex local matters, your assigned office may need to handle it. Confirm with 1-800-772-1213 if in doubt."},
     {"q":"What about residents of Las Cruces, NM?","a":"Las Cruces has its own SSA office and is not served by El Paso. Residents of southern New Mexico should confirm their assigned office using ssa.gov/locator."},
     {"q":"How do I get to the office without a car?","a":"Sun Metro buses serve the Gateway Blvd area. Check Sun Metro schedules for the best route from your neighborhood. Rideshare (Uber, Lyft) is also a common option."}]},
 ]},

{"slug":"ssa-required-documents-el-paso","silo":"office",
 "h1":"What Documents to Bring to the SSA Office in El Paso",
 "title":"SSA Required Documents Checklist: El Paso Office (2026)",
 "meta":"Complete checklist of what to bring to your Social Security office visit in El Paso, TX. Originals only, common mistakes, and what each service requires in 2026.",
 "intro":("The single most common reason a trip to the El Paso SSA office is wasted is bringing the wrong documents — or photocopies instead of originals. This guide breaks down exactly what to bring for each common service, the cardinal rules (originals, not copies), and the gotchas that catch people out."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"The SSA requires ORIGINAL documents, not photocopies, for almost every service. They will photocopy them on the spot and hand the originals back. The exact documents depend on the service: SSN applications need proof of citizenship/status and identity; name changes need legal name-change documents; disability needs medical records; retirement needs birth certificate and proof of citizenship. When in doubt, bring more than you think you need."},
   {"type":"section","heading":"The cardinal rules",
    "body":[
      "Rule 1: ORIGINALS ONLY. The SSA does not accept photocopies for almost any document. They will take the originals, photocopy them while you wait, and hand the originals back to you in the same visit. Do not mail originals unless instructed.",
      "Rule 2: UNEXPIRED. IDs and passports must be current, not expired. Birth certificates are an exception — they do not expire and originals are fine.",
      "Rule 3: CERTIFIED, NOT NOTARIZED. For birth certificates, divorce decrees, and similar documents, you need a CERTIFIED copy (with the official seal of the issuing agency), not a notarized photocopy."]},
   {"type":"troubleshoot","heading":"What to bring by service",
     "items":[
       {"q":"First-time Social Security card","a":"Form SS-5, original birth certificate (for U.S. citizens) or immigration documents (for non-citizens), and original photo ID. For minors, parent's ID."},
       {"q":"Replacement card","a":"Form SS-5 and original unexpired photo ID (driver's license, state ID, or U.S. passport). If your name has changed since the last card, bring the legal name-change document."},
       {"q":"Name change","a":"Form SS-5, original legal name-change document (marriage certificate, divorce decree showing name change, court order), and original photo ID — ideally already in your new name."},
       {"q":"Apply for retirement","a":"Birth certificate, proof of U.S. citizenship/lawful status, last year's W-2 or tax return, military discharge papers if pre-1968 service, and bank info for direct deposit."},
       {"q":"Apply for disability","a":"Medical records and provider list, medications list, work history (15 years), recent W-2, birth certificate, and bank info for direct deposit. SSI applications need detailed financial records in addition."},
       {"q":"Apply for Medicare (without already on Social Security)","a":"Birth certificate, proof of U.S. citizenship, and proof of any prior creditable coverage if delaying parts."}]},
   {"type":"section","heading":"Common mistakes",
    "body":[
      "Bringing photocopies instead of originals. This is the number-one wasted trip. Even high-quality photocopies are not accepted for primary documents.",
      "Expired IDs. A driver's license that expired last month will be rejected. Renew first, then come in.",
      "Notarized copies instead of certified copies. A notary's stamp on a photocopy of your birth certificate is not the same as a certified birth certificate from the vital records office.",
      "Forgetting Form SS-5 for SSN-related services. You can complete it at the office, but pre-filling at home saves time. Download from ssa.gov.",
      "Not bringing supporting documents 'just in case.' If a service has any chance of needing extra documentation, bring it. Going home to get something is far worse than carrying an extra envelope."]},
   {"type":"faq_extra","items":[
     {"q":"Will the SSA accept a digital copy on my phone?","a":"Generally no. Original physical documents are required. Some limited exceptions exist for specific situations — ask when you book your appointment."},
     {"q":"What if my documents are in another language?","a":"Foreign documents must be accompanied by a certified English translation. The translator can be the document holder, but the translation must be certified as accurate."},
     {"q":"How do I get a certified copy of a document?","a":"For birth certificates, contact the vital records office of the state where the birth occurred. For court documents, the issuing court. Certified copies usually cost a small fee and arrive by mail in a few days to weeks."},
     {"q":"Can someone else bring my documents for me?","a":"For most services, no. You must appear in person with your own documents. The SSA does not generally accept third-party representatives without specific legal authority (such as a Power of Attorney for certain situations)."}]},
 ]},
]

# ---------- SILO 3: LEARN (informational, supporting authority) ----------
learn = [
{"slug":"what-is-social-security","silo":"learn",
 "h1":"What Is Social Security? A Plain-English Guide",
 "title":"What Is Social Security? Complete Guide (2026)",
 "meta":"What is Social Security and how does it work? A plain-English guide to the program, who qualifies, how benefits are calculated, and what it covers in 2026.",
 "intro":("Social Security is the largest government program in the United States, paying benefits to over 70 million people every month. Despite that, most workers do not really understand how it works until they need it. This guide explains the program in plain English: what it is, what it pays for, who qualifies, and the basic mechanics of how your benefit is calculated."),
 "sections":[
   {"type":"quick_answer","heading":"In one sentence",
    "body":"Social Security is a federal program funded by payroll taxes that pays monthly benefits to retired workers, disabled workers, and the families of deceased workers, with eligibility and benefit amounts based on your earnings history."},
   {"type":"section","heading":"The four major programs Social Security runs",
    "body":[
      "Retirement Insurance is the largest and best-known program: monthly benefits to retired workers who paid into the system through payroll taxes. You can start as early as 62 (with reduced benefits) or wait until 70 (for maximum benefits).",
      "Disability Insurance (SSDI) pays workers who cannot work due to a medically-determinable disability expected to last at least 12 months or result in death. It is funded by the same payroll taxes as retirement.",
      "Survivors Insurance pays the spouse, ex-spouse, children, and sometimes parents of a deceased worker. This is the least-known major program but pays significant benefits to millions of families.",
      "Supplemental Security Income (SSI) is technically administered by the SSA but is a separate, needs-based program funded by general tax revenue, not payroll taxes. It pays disabled, blind, or elderly people with very limited income and resources."]},
   {"type":"section","heading":"How your benefit is calculated",
    "body":[
      "Social Security calculates your benefit using your highest 35 years of earnings, indexed for inflation. The formula is progressive: lower earners replace a higher percentage of their working income than higher earners. This is why Social Security is sometimes called insurance against poverty in old age, rather than a pure investment return.",
      "Your benefit is fixed at Full Retirement Age (between 66 and 67 depending on birth year). Starting earlier (as young as 62) permanently reduces your benefit by up to 30%. Delaying past FRA increases your benefit by about 8% per year until age 70. After 70 there is no additional gain from delaying."]},
   {"type":"section","heading":"How the program is funded",
    "body":[
      "Social Security is funded primarily by FICA payroll taxes: 6.2% from the employee and 6.2% from the employer (12.4% total), up to a wage base limit that adjusts each year. Self-employed people pay the full 12.4% themselves through SECA tax. There is also a small Medicare portion on top.",
      "The taxes go into the Social Security Trust Funds, which currently hold enough reserves to keep paying full benefits for many years. Long-term funding challenges have been debated for decades; current projections show the trust funds depleting in the 2030s, after which incoming taxes would fund roughly 80% of scheduled benefits unless Congress acts. The program has been adjusted many times in its history and is widely expected to continue, though future benefits could change."]},
   {"type":"faq_extra","items":[
     {"q":"How do I see my future Social Security benefits?","a":"Create an account at ssa.gov/myaccount. The SSA provides personalized estimates based on your actual earnings history and various claiming ages."},
     {"q":"Will Social Security run out before I retire?","a":"The trust funds are projected to deplete in the 2030s unless Congress acts. Even in that scenario, incoming payroll taxes would still fund roughly 80% of scheduled benefits. Social Security itself does not 'go bankrupt' — but benefit levels could be adjusted."},
     {"q":"Do I have to be a U.S. citizen?","a":"No. Lawful permanent residents and certain other legal residents can qualify based on their work history paying into Social Security. Citizenship is not required."},
     {"q":"Can my Social Security benefit be taxed?","a":"Possibly. If your combined income (Social Security + other income) exceeds certain thresholds, up to 85% of your benefit may be subject to federal income tax. Texas has no state income tax, so Texas residents pay no state tax on Social Security."}]},
 ]},

{"slug":"ssi-vs-ssdi-difference","silo":"learn",
 "h1":"SSI vs SSDI: What Is the Difference?",
 "title":"SSI vs SSDI: Differences, Eligibility, and Which You Qualify For (2026)",
 "meta":"Confused about SSI vs SSDI? Plain-English guide to the two main Social Security disability programs, eligibility rules, and how to know which one applies to you in 2026.",
 "intro":("SSI and SSDI both pay disability benefits, and both are run by the SSA, but they work very differently and have totally different eligibility rules. Mixing them up is one of the most common mistakes people make when applying. This guide explains the differences clearly and helps you understand which program (or both) might apply to you."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"SSDI (Social Security Disability Insurance) is for people who became disabled and have a sufficient work history paying Social Security taxes. SSI (Supplemental Security Income) is for people who are disabled, blind, or 65+ and have very limited income and assets, regardless of work history. SSDI is based on what you paid in; SSI is needs-based. Some people qualify for both at the same time, which is called concurrent benefits."},
   {"type":"troubleshoot","heading":"Side by side comparison",
    "items":[
      {"q":"Funding","a":"SSDI is funded by Social Security payroll taxes (FICA). SSI is funded by general U.S. tax revenue, not payroll taxes."},
      {"q":"Eligibility","a":"SSDI requires a substantial work history (generally 5 of the last 10 years for adults). SSI requires no work history but has strict income and asset limits."},
      {"q":"Disability standard","a":"Both use the same medical standard for adults — a disability preventing substantial work, expected to last 12+ months or result in death. SSI for children uses a slightly different standard based on functional limitations."},
      {"q":"Benefit amount","a":"SSDI is based on your past earnings (average around $1,500/month). SSI federal maximum is about $943/month for an individual, often with state supplements."},
      {"q":"Health coverage","a":"SSDI recipients become eligible for Medicare after a 24-month waiting period. SSI recipients in Texas are generally automatically eligible for Medicaid."},
      {"q":"Asset limits","a":"SSDI has no asset limit. SSI has strict limits (generally under $2,000 for individuals, $3,000 for couples)."}]},
   {"type":"section","heading":"Who typically applies for SSDI",
    "body":[
      "SSDI is the right program for adults who became disabled after building a meaningful work history. The classic case: someone who worked for 10-20 years, then developed a serious illness or had an accident that prevents them from continuing to work. Because they paid into Social Security through their job, they qualify for SSDI regardless of how much money they have in the bank or whether they own their home.",
      "SSDI benefits are also generally higher than SSI because they are based on past earnings rather than a fixed federal amount."]},
   {"type":"section","heading":"Who typically applies for SSI",
    "body":[
      "SSI is the right program for people without enough work history to qualify for SSDI, but who meet the financial limits. The classic cases: young adults who became disabled before working much, elderly people without enough Social Security credits, and children with disabilities in low-income families.",
      "Because SSI is needs-based, it can be lost or reduced if your financial situation changes — receiving an inheritance, marrying someone with assets, or earning above the limits can all affect SSI."]},
   {"type":"section","heading":"Can you get both? (Concurrent benefits)",
    "body":[
      "Yes, you can sometimes qualify for both SSDI and SSI at the same time, which is called concurrent benefits. This typically happens when your SSDI benefit is low (because you had limited earnings before becoming disabled) and you also meet the SSI financial limits.",
      "When you apply for disability, the SSA automatically evaluates you for both programs. You do not need to choose in advance. If you qualify for both, you receive the SSDI amount plus enough SSI to bring you up to the SSI maximum, and you get both Medicare (after the SSDI waiting period) and Medicaid coverage."]},
   {"type":"faq_extra","items":[
     {"q":"Which program is faster to qualify for?","a":"Decisions on both programs take roughly the same time (3-6 months for the initial decision). SSI sometimes pays first because the 5-month waiting period that applies to SSDI does not apply to SSI."},
     {"q":"Can I work while on SSDI or SSI?","a":"You can work small amounts under both programs without losing benefits. There are different rules — SSDI uses the Substantial Gainful Activity threshold (~$1,550/month in 2024), while SSI reduces your benefit gradually as you earn more."},
     {"q":"Do SSI recipients automatically get Medicaid?","a":"In Texas, generally yes. In some other states, SSI recipients must separately apply for Medicaid. Texas is a 1634 state, which means SSI eligibility automatically conveys Medicaid eligibility."},
     {"q":"Can my children get benefits if I qualify?","a":"Under SSDI, your minor children may qualify for dependent benefits on your record. SSI does not have a dependent benefit, but disabled children can qualify for SSI on their own based on the family's income and resources."}]},
 ]},

{"slug":"when-to-apply-for-social-security-retirement","silo":"learn",
 "h1":"When Should You Apply for Social Security Retirement?",
 "title":"When to Apply for Social Security Retirement: 62, 67, or 70? (2026)",
 "meta":"Should you claim Social Security at 62, Full Retirement Age, or 70? Plain-English guide to the tradeoffs and how to decide in 2026.",
 "intro":("The most consequential financial decision of most retirements is also the most misunderstood: when to start claiming Social Security. Start at 62 and your monthly benefit is permanently reduced by up to 30%. Wait until 70 and you get the largest possible monthly benefit for life. This guide explains the real tradeoffs, the math behind 'break-even' ages, and how to think about the decision."),
 "sections":[
   {"type":"quick_answer","heading":"The quick answer",
    "body":"You can start Social Security retirement anywhere from age 62 to age 70. Starting at 62 permanently cuts your benefit by 25-30%. Your 'Full Retirement Age' (FRA) is between 66 and 67 depending on the year you were born — that is when you get 100% of your earned benefit. Each year you wait past FRA up to 70 adds about 8% to your benefit. After 70, there is no additional gain from waiting. There is no single right answer — the best age depends on your health, finances, and life expectancy."},
   {"type":"section","heading":"What 'Full Retirement Age' means",
    "body":[
      "Full Retirement Age (FRA) is the age at which you receive 100% of your earned Social Security benefit. For people born 1943-1954, FRA is 66. It gradually increases for those born 1955-1959, reaching FRA of 67 for everyone born 1960 or later.",
      "FRA is not a deadline — you can claim before or after — but it is the reference point. Your benefit is permanently reduced if you start before FRA, and permanently increased if you start after FRA, up to age 70. After 70, there is no further increase, so there is no reason to wait beyond 70."]},
   {"type":"troubleshoot","heading":"The three main claiming choices",
     "items":[
       {"q":"Age 62 (earliest)","a":"Permanent reduction of 25-30% from your full benefit. Best for: shorter-than-average life expectancy, immediate income need, or specific tax-planning reasons. Worst for: healthy people with other income who plan to live into their 80s+."},
       {"q":"Full Retirement Age (66-67)","a":"Full earned benefit. Best for: those who need the income at FRA, want a middle-ground option, or want to avoid the earnings test (which only applies before FRA)."},
       {"q":"Age 70 (latest)","a":"Maximum possible benefit, roughly 124-132% of your FRA amount. Best for: healthy people with other income to bridge the gap, those expecting longer-than-average life expectancy, married couples optimizing combined benefits."}]},
   {"type":"section","heading":"The break-even age",
    "body":[
      "A common framework is the 'break-even age' — the age at which the total benefits received under different claiming strategies become equal. For most people, claiming at 70 versus 62 breaks even around age 80-82. If you live past that, claiming later wins; if you do not, claiming earlier wins.",
      "But break-even analysis misses an important point: Social Security is insurance against living a long time. If you have any chance of living into your late 80s or 90s, the larger monthly benefit from delaying is enormously valuable, regardless of break-even math. It is the only inflation-adjusted, guaranteed-for-life income most people will ever have."]},
   {"type":"section","heading":"How marital status changes the calculation",
    "body":[
      "For married couples, the higher earner's claiming age affects not just their own benefit but also the survivor benefit the lower earner will receive after the higher earner dies. Delaying the higher earner's claim to 70 maximizes the surviving spouse's benefit, which often makes delaying the more valuable strategy for the household.",
      "For divorced people who were married 10+ years, you may be able to claim on your ex-spouse's record without their knowledge or affecting their benefit. This can be valuable if your ex earned much more than you."]},
   {"type":"faq_extra","items":[
     {"q":"What if I claim early and regret it?","a":"You have 12 months from your start date to withdraw your application, repay any benefits received, and effectively restart the clock. After 12 months, the only option is to suspend benefits at FRA, which lets you earn delayed retirement credits until 70 but does not erase the early reduction."},
     {"q":"Does it ever make sense to claim at 62?","a":"Yes — for people with serious health issues affecting life expectancy, immediate financial need, or specific situations where bird-in-hand outweighs the future upside. It is not the wrong choice for everyone."},
     {"q":"What is the earnings test?","a":"If you claim before FRA and keep working, the SSA reduces your benefit if you earn above an annual limit. After FRA, you can earn unlimited amounts with no reduction. This is why some people work to FRA before claiming."},
     {"q":"How do I decide what is right for me?","a":"Use the SSA's retirement estimator at ssa.gov/myaccount, consider your health and family longevity, your other income sources, your spouse's situation, and your tax situation. For larger amounts, talking to a fee-only financial planner often pays for itself."}]},
 ]},
]

# Construir el dataset completo
dataset = {
    "site": {"name":"SSO El Paso","domain":"ssoelpasotx.com",
             "tagline":"Your simple guide to Social Security services in El Paso, Texas.",
             "office": OFFICE_INFO, "note_verify": NOTE_VERIFY},
    "services": services, "office": office, "learn": learn,
}
json.dump(dataset, open('data/sso.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
total = len(services)+len(office)+len(learn)
print(f"OK dataset construido: {total} paginas de contenido profundo")
print(f"  SERVICES (high RPM): {len(services)}")
print(f"  OFFICE (location):   {len(office)}")
print(f"  LEARN (informativo): {len(learn)}")
