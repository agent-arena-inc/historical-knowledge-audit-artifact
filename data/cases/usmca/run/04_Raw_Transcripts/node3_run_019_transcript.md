# node3_run_019


## ▶ Stage 0: translate_exposures (0 facts injected)


**[R1] auto_strategy** (pass 1): How are we actually pricing the supplier-relocation exposure? Are we anchoring on the wage-floor jump, or the RVC recount cost, or both? Right now it's just a number — I need to know what plant, what tier-1 supplier, what happens if they don't move.

**[R1] supplier** (pass 1): Fair question. Right now we're burying it — but I can tell you: Tier-2 fastener and stamping shops in Mexico are looking at 18-24 month re-qual cycles plus $2-5M capex per plant to hit 75% RVC. Half of them don't have that liquidity. So either we price in **supplier insolvency or we price in OEM capex absorption** — pick one, because both can't be zero. What's your demand signal — are the OEMs committing to absorb re-qual costs, or are we modeling supplier failures?

**[R1] auto_strategy** ⚡reply: We're not absorbing re-qual capex across the board — that's a margin kill. But I need specifics: which fastener and stamping plants are already below 75% RVC, and what's their current customer concentration? If it's single-OEM dependent, they fail and we source around them. If they're diversified, we negotiate a cost-share tied to volume commitments. Either way, trade_credit_risk goes up until we see committed capex or bankruptcy filings — don't bury it.

**[R1] compliance_lawyer** (pass 1): If we're modeling supplier failures as the default, we need audit triggers: which plants get re-qualified by when, who funds the testing, and what's the certification deadline before tariffs kick in? Right now you've got the money choice, but not the calendar — and that's where penalties live.

**[R1] supplier** ⚡reply: Look, we've got 12 plants I can name right now — three fastener shops in Monterrey, two stamping operations near Saltillo, rest scattered. Two of the fastener guys are 85% Ford-dependent, already underwater on 2023 volumes. The Saltillo pair are diversified but both flagged capex constraints to us last month. So here's the hard call: **we need a 90-day audit sprint on those five plants — capex feasibility, customer concentration, liquidity position — before we price anything.** Without that, we're guessing, and that's how we miss the insolvency signal until it's too late.

**[R1] trade_credit_underwriter** (pass 1): On those five plants — when you flag capex constraints and liquidity, are you seeing payment-term pressure from the OEMs already? Because if a Monterrey fastener shop hits insolvency mid-qual, the OEM doesn't eat the capex, they just pull supply and leave us with stranded receivables. What's the payment-collection window if they stumble?

**[R1] supply_chain_consultant** (pass 1): I'm with you on the 15% political-risk premium if enforcement uncertainty spikes — but here's the question: if that trigger hits, do we tell the OEMs "pull capex-share deals and nearshore those five plants into Texas or Ontario," or do we wait for more clarity? Because the client's decision window closes fast, and the 2026 review isn't a surprise — we should be mapping nearshoring options *before* we hit 40% uncertainty, not after.

**[R1] political_risk_insurer** ⚡reply: Those five plants fail the audit if capex feasibility comes back negative — which it will for the two Monterrey fastener shops at 85% Ford concentration. Here's what I'm pricing: **if either shop can't secure committed OEM capex-share by Q1 2025, I'm underwriting them as insolvency plays, and the political-risk premium kicks in now, not at 40% uncertainty.** Commerce enforcement velocity on RVC is already moving — the certification deadline is the real trigger, not the sunset review.

**[R1] auto_strategy** [speech]: How are we actually pricing the supplier-relocation exposure? Are we anchoring on the wage-floor jump, or the RVC recount cost, or both? Right now it's just a number — I need to know what plant, what tier-1 supplier, what happens if they don't move.

**[R1] supplier** [speech]: Fair question. Right now we're burying it — but I can tell you: Tier-2 fastener and stamping shops in Mexico are looking at 18-24 month re-qual cycles plus $2-5M capex per plant to hit 75% RVC. Half of them don't have that liquidity. So either we price in **supplier insolvency or we price in OEM capex absorption** — pick one, because both can't be zero. What's your demand signal — are the OEMs committing to absorb re-qual costs, or are we modeling supplier failures?

**[R1] compliance_lawyer** [speech]: If we're modeling supplier failures as the default, we need audit triggers: which plants get re-qualified by when, who funds the testing, and what's the certification deadline before tariffs kick in? Right now you've got the money choice, but not the calendar — and that's where penalties live.

**[R1] trade_credit_underwriter** [speech]: On those five plants — when you flag capex constraints and liquidity, are you seeing payment-term pressure from the OEMs already? Because if a Monterrey fastener shop hits insolvency mid-qual, the OEM doesn't eat the capex, they just pull supply and leave us with stranded receivables. What's the payment-collection window if they stumble?

**[R1] supply_chain_consultant** [speech]: I'm with you on the 15% political-risk premium if enforcement uncertainty spikes — but here's the question: if that trigger hits, do we tell the OEMs "pull capex-share deals and nearshore those five plants into Texas or Ontario," or do we wait for more clarity? Because the client's decision window closes fast, and the 2026 review isn't a surprise — we should be mapping nearshoring options *before* we hit 40% uncertainty, not after.

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Political-risk trigger framework approved: 40% enforcement uncertainty threshold activates 15% premium on capex-share deals.  
>   side-effects: political_risk_exposure:+4.0; underwriting_discipline:+5.0; risk_map_completeness:+3.0; trade_credit_risk:+2.0; stress:-2.0; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: Dec 15 capex-feasibility audit locked in for five plants; Q1 2025 cost-share window for diversified suppliers.  
>   side-effects: supplier_relocation_exposure:+5.0; trade_credit_risk:+4.0; underwriting_discipline:+5.0; risk_map_completeness:+5.0; political_risk_exposure:+3.0; stress:-3.0; risk_map_completeness:+1; risk_map_completeness:+1


_— R1 end | political_risk_exposure=33, risk_map_completeness=30, rules_of_origin_burden=32, supplier_relocation_exposure=30, trade_credit_risk=31, underwriting_discipline=40 —_


**[R2] auto_strategy** (pass 1): Dec 15 audit comes back — let's say both Monterrey shops fail ROI. Do we have a decision rule ready, or do we kick it to the OEMs to absorb capex and hope they choose nearshore over default? Because if that's a coin flip, our "approved" audit is just a data point, not a plan.

**[R2] cfo_erm** ⚡reply: We have a decision rule — if either shop fails capex ROI by Dec 15, we trigger the 15% political-risk premium *and* issue a 90-day requalification notice with funding split: OEM absorbs labor-content remediation, we cover trade-credit insurance for the relocation window. If they don't commit within 30 days, we pull the nearshoring option off the table and price in supplier insolvency. That's not a coin flip — it's a gate.

**[R2] supplier** (pass 1): Before Dec 15 drops, I need clarity: are we pre-screening those 12 plants in November for capex feasibility, or do we let them all fail the audit together and then triage? Because if the Monterrey fastener shops are already 85% Ford-dependent and liquidity-constrained, they're not committing to anything in 30 days — and I need to know that *before* we price the requalification window, not after.

**[R2] compliance_lawyer** (pass 1): CFO, I need one thing locked before we price the requalification window: if those Monterrey shops don't commit to capex by Jan 15, what's the tariff-exposure deadline? Because that's your real penalty trigger, not insolvency — are we talking CPTPP filing window, or a Commerce re-determination date? That changes what we price for the 90-day notice.

**[R2] political_risk_insurer** (pass 1): Compliance, before we quote the requalification window, I need the tariff deadline locked — CPTPP filing window, Commerce re-determination date, whatever it is. That's my enforcement-certainty anchor. Once I know when the penalty actually triggers, I can price the trade-credit gap and pull trade_credit_risk up from 31. Right now we're guessing.

**[R2] compliance_lawyer** ⚡reply: CPTPP certification window closes March 31, 2025 — that's your hard deadline for RVC compliance filing. Commerce re-determination lands 60 days after, so May 31 is when tariff exposure crystallizes. If those Monterrey shops don't commit by Jan 15, we're pricing a 75-day sprint to re-qualification, and any slip past March 15 triggers duty exposure on in-transit inventory. That's your enforcement certainty — plug it into the trade-credit premium now.

**[R2] trade_credit_underwriter** (pass 1): CFO, I'm good with the 90-day gate and the nearshoring trigger — but I need one concrete number: if a Monterrey shop doesn't commit by Jan 15 and we shift to insolvency pricing, what's our receivables window? Are the OEMs still paying net-30, or do payment terms freeze while we're waiting for the tariff deadline to clarify? Because that's the trade-credit variable I'm pricing — not just supplier failure, but stranded AR.

**[R2] auto_strategy** [speech]: Dec 15 audit comes back — let's say both Monterrey shops fail ROI. Do we have a decision rule ready, or do we kick it to the OEMs to absorb capex and hope they choose nearshore over default? Because if that's a coin flip, our "approved" audit is just a data point, not a plan.

**[R2] supplier** [speech]: Before Dec 15 drops, I need clarity: are we pre-screening those 12 plants in November for capex feasibility, or do we let them all fail the audit together and then triage? Because if the Monterrey fastener shops are already 85% Ford-dependent and liquidity-constrained, they're not committing to anything in 30 days — and I need to know that *before* we price the requalification window, not after.

**[R2] compliance_lawyer** [speech]: CFO, I need one thing locked before we price the requalification window: if those Monterrey shops don't commit to capex by Jan 15, what's the tariff-exposure deadline? Because that's your real penalty trigger, not insolvency — are we talking CPTPP filing window, or a Commerce re-determination date? That changes what we price for the 90-day notice.

**[R2] political_risk_insurer** [speech]: Compliance, before we quote the requalification window, I need the tariff deadline locked — CPTPP filing window, Commerce re-determination date, whatever it is. That's my enforcement-certainty anchor. Once I know when the penalty actually triggers, I can price the trade-credit gap and pull trade_credit_risk up from 31. Right now we're guessing.

**[R2] trade_credit_underwriter** [speech]: CFO, I'm good with the 90-day gate and the nearshoring trigger — but I need one concrete number: if a Monterrey shop doesn't commit by Jan 15 and we shift to insolvency pricing, what's our receivables window? Are the OEMs still paying net-30, or do payment terms freeze while we're waiting for the tariff deadline to clarify? Because that's the trade-credit variable I'm pricing — not just supplier failure, but stranded AR.

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Pre-screening framework approved; tier assignments and viability rankings operationalize nearshoring decisions.  
>   side-effects: supplier_relocation_exposure:+5.0; risk_map_completeness:+5.0; underwriting_discipline:+4.0; trade_credit_risk:-3.0; risk_map_completeness:+1; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: Three-tier pricing model locked; concrete premium structure operationalizes underwriting and risk segmentation.  
>   side-effects: underwriting_discipline:+5.0; risk_map_completeness:+5.0; trade_credit_risk:+4.0; political_risk_exposure:+3.0; supplier_relocation_exposure:-2.0; risk_map_completeness:+1


_— R2 end | political_risk_exposure=37, risk_map_completeness=43, rules_of_origin_burden=34, supplier_relocation_exposure=33, trade_credit_risk=32, underwriting_discipline=49 —_



## ▶ Stage 1: operationalize_and_consolidate (1 facts injected)


**[R3] auto_strategy** (pass 1): You've got the viability rankings locked — now I need the RVC math. For each tier, what's the actual regional-value shortfall per model, and what's the labor-content gap versus the wage floor? That's what moves rules_of_origin_burden from a number to a cost.

**[R3] supply_chain_consultant** ⚡reply: Here's the shortfall per tier: Tier-1 fasteners are running 62% RVC against 75% required — that's a $1.2M recount cost plus 8-point labor-content gap to hit wage floor. Tier-2 stamping shops are worse — 58% RVC, $2.8M capex per plant, 12-point gap. The math says either the OEM absorbs $4M-plus across both plants by January 15, or we're pricing supplier insolvency into the requalification window — which one's your demand signal?

**[R3] supplier** (pass 1): CFO, the $1.2M and $2.8M numbers — are you confident those Monterrey and Saltillo shops will still be solvent in 90 days if the OEMs don't commit by January 15? Because if they won't, we need to tell the OEMs "absorb capex or we price your supply at insolvency rates starting now" — not wait until they fail the audit.

**[R3] cfo_erm** ⚡reply: No — those shops are already Ford-dependent at 85% and liquidity-constrained; if capex doesn't land by January 15, we're pricing insolvency rates effective immediately, not waiting for the audit. Lock the OEM demand signal now: either they commit $4M by January 15 or we move the five plants into the trade-credit risk bucket at 40% enforcement-uncertainty premium. That's your decision rule.

**[R3] compliance_lawyer** (pass 1): CFO, I hear the Jan 15 gate—but here's what I need to lock rules-of-origin compliance: if those two fastener shops don't commit to capex by Jan 15, when do their RVC recounts *have* to be filed to stay ahead of the March 31 CPTPP deadline? And Supply-Chain, who's running those re-qual audits—OEM lab, third-party cert, our shop? Because that's who gets named in the compliance trigger, and that's where the penalty lives if they miss the date.

**[R3] political_risk_insurer** (pass 1): Compliance, you locked March 31 CPTPP filing and May 31 Commerce re-determination—which one triggers the tariff penalty if those two Monterrey shops miss RVC recounts? Because *that* date is what I price the 40% enforcement-uncertainty premium against. Is it filing-day exposure, or do we wait 60 days for Commerce to actually land the re-determination?

**[R3] compliance_lawyer** ⚡reply: Filing-day exposure — March 31 CPTPP deadline is hard enforcement, not conditional on Commerce re-determination. If those RVC recounts don't hit the docket by March 30, tariffs apply retroactively to shipments already in transit. That's the trigger I'm pricing: 40% premium activates March 15 if we don't see signed audit commitments from both shops by January 15.

**[R3] trade_credit_underwriter** (pass 1): CFO, the Jan 15 gate locks the OEM demand signal — but I need the payment-term picture: if those two Monterrey shops fail commitment and we move them to insolvency pricing, are the OEMs still paying net-30 on deliveries between January and March, or do payment terms freeze while you're waiting for the March 31 filing? Because that's my trade-credit variable right there.

**[R3] cfo_erm** (pass 1): Supply-Chain, on your nearshoring decision matrix — if an OEM picks Texas by Jan 15, who's actually certifying the new plant's RVC by March 31? Is that OEM's lab, a third-party cert house, or us? Because that's the execution owner I'm naming in the compliance trigger, and if they slip, that's on them, not on us waiting for Commerce.

**[R3] auto_strategy** [speech]: You've got the viability rankings locked — now I need the RVC math. For each tier, what's the actual regional-value shortfall per model, and what's the labor-content gap versus the wage floor? That's what moves rules_of_origin_burden from a number to a cost.

**[R3] supplier** [speech]: CFO, the $1.2M and $2.8M numbers — are you confident those Monterrey and Saltillo shops will still be solvent in 90 days if the OEMs don't commit by January 15? Because if they won't, we need to tell the OEMs "absorb capex or we price your supply at insolvency rates starting now" — not wait until they fail the audit.

**[R3] compliance_lawyer** [speech]: CFO, I hear the Jan 15 gate—but here's what I need to lock rules-of-origin compliance: if those two fastener shops don't commit to capex by Jan 15, when do their RVC recounts *have* to be filed to stay ahead of the March 31 CPTPP deadline? And Supply-Chain, who's running those re-qual audits—OEM lab, third-party cert, our shop? Because that's who gets named in the compliance trigger, and that's where the penalty lives if they miss the date.

**[R3] political_risk_insurer** [speech]: Compliance, you locked March 31 CPTPP filing and May 31 Commerce re-determination—which one triggers the tariff penalty if those two Monterrey shops miss RVC recounts? Because *that* date is what I price the 40% enforcement-uncertainty premium against. Is it filing-day exposure, or do we wait 60 days for Commerce to actually land the re-determination?

**[R3] trade_credit_underwriter** [speech]: CFO, the Jan 15 gate locks the OEM demand signal — but I need the payment-term picture: if those two Monterrey shops fail commitment and we move them to insolvency pricing, are the OEMs still paying net-30 on deliveries between January and March, or do payment terms freeze while you're waiting for the March 31 filing? Because that's my trade-credit variable right there.

**[R3] cfo_erm** [speech]: Supply-Chain, on your nearshoring decision matrix — if an OEM picks Texas by Jan 15, who's actually certifying the new plant's RVC by March 31? Is that OEM's lab, a third-party cert house, or us? Because that's the execution owner I'm naming in the compliance trigger, and if they slip, that's on them, not on us waiting for Commerce.

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: The Jan 15 decision matrix with concrete wage floors and re-qual timelines operationalizes supplier relocation exposure into actionable triggers. The consensus demand for RVC math, payment-term clarity, and certification ownership transforms vague nearshoring risk into priced underwriting factors.  
>   side-effects: supplier_relocation_exposure:-4.0; underwriting_discipline:+5.0; risk_map_completeness:+4.0; trade_credit_risk:+3.0; rules_of_origin_burden:+2.0; risk_map_completeness:-1; risk_map_completeness:+1


_— R3 end | political_risk_exposure=38, risk_map_completeness=47, rules_of_origin_burden=38, supplier_relocation_exposure=29, trade_credit_risk=35, underwriting_discipline=54 —_


**[R4] auto_strategy** (pass 1): Supply-Chain, I've got the shortfall numbers by tier — but I need to map it to actual models. Which platforms hit tariff exposure by March 31 if those Monterrey and Saltillo shops miss the RVC recount? That's what tells me whether we're investing $1.2M or $6M to stay compliant.

**[R4] supply_chain_consultant** ⚡reply: The fastener tier—Ford F-Series platform—is the hard exposure: that's $1.2M Monterrey, $2.8M Saltillo combined. If either shop misses recount by March 31, we lose RVC certification on roughly 40% of F-Series sub-assemblies, which triggers tariff on parts-in-transit *and* inventory sitting in OEM staging. The other two tiers—Bosch electrical, Lear seating—have looser supplier depth, so we can pivot those to Canada or Texas without full-chain failure. Bottom line: Monterrey fasteners are the gate; if they don't commit by Jan 15, we're looking at the full $1.2M exposure plus business interruption on the fastest-moving platform.

**[R4] supplier** (pass 1): CFO, the $1.2M Monterrey and $2.8M Saltillo numbers are solid, but here's the gap: if Ford commits to nearshoring capex by Jan 15, who's actually running the RVC recount audit — your OEM lab, a third-party cert house, or the supplier's in-house team? Because that's the name I put in the compliance trigger, and their audit schedule is what determines whether we hit March 31 or blow past it. Without that owner locked, the Jan 15 commitment is just a signal, not an execution plan.

**[R4] cfo_erm** ⚡reply: Ford runs their own lab for fastener RVC — they've got the capacity and they want audit control on safety-critical parts. That's locked. But here's what matters: if Monterrey doesn't commit capex by Jan 15, Ford delays the audit queue, and we slip past March 31. So the real trigger isn't who audits — it's whether Ford's capex commitment *pulls* the audit onto their calendar or leaves it floating. I'm pricing trade-credit exposure assuming a 60-day audit slip if capex stalls; you need to tell me if that's conservative or I'm underwriting the wrong date.

**[R4] compliance_lawyer** (pass 1): CFO, here's the question that moves us from signal to execution: if Ford commits capex by Jan 15 and pulls Monterrey into their audit queue, what's the actual RVC recount window — is that 30 days, 45 days, can they guarantee March 15 completion so we hit the filing deadline with buffer? Because that timeline is what I name in the compliance trigger, and if Ford can't commit to the schedule, we're pricing the 60-day slip assumption as the baseline, not the upside.

**[R4] compliance_lawyer** ⚡reply: March 31 filing is your execution date—Commerce re-determination lands May 31, and *that's* when tariff penalties actually trigger, not filing day. If the Hill moves on RVC mid-cycle, it won't hit enforcement until after May 31, so your 25% shock premium is priced against a post-determination rule change, not pre-filing churn. Lock the 45-day Monterrey audit window with Ford by end of this week, or I'm pulling it to 60 days and pricing the trade-credit slip upfront.

**[R4] supplier** ⚡reply: Ford stays net-30 through March 31—that's contractual lock. But if Monterrey fails the audit or misses the recount window, we shift that plant to insolvency pricing *starting January 16*, and Ford's payment obligation freezes at invoice date pending tariff clarity on May 31. So your stranded AR window is 75 days minimum if the shop stumbles; I'm holding $340K reserve against that slip right now.

**[R4] supply_chain_consultant** (pass 1): CFO, here's what I need: if Monterrey doesn't get Ford's capex commitment by Jan 15, we're flipping to insolvency pricing—but I need to name the Texas nearshoring option *right now* so we can tell Ford "commit or we're moving Monterrey's line to our Dallas supplier by Q2, and you're absorbing the transition cost." Which Texas plant are we actually offering, and what's the lead time? Because *that's* what moves relocation from a threat to a plan.

**[R4] auto_strategy** [speech]: Supply-Chain, I've got the shortfall numbers by tier — but I need to map it to actual models. Which platforms hit tariff exposure by March 31 if those Monterrey and Saltillo shops miss the RVC recount? That's what tells me whether we're investing $1.2M or $6M to stay compliant.

**[R4] supplier** [speech]: CFO, the $1.2M Monterrey and $2.8M Saltillo numbers are solid, but here's the gap: if Ford commits to nearshoring capex by Jan 15, who's actually running the RVC recount audit — your OEM lab, a third-party cert house, or the supplier's in-house team? Because that's the name I put in the compliance trigger, and their audit schedule is what determines whether we hit March 31 or blow past it. Without that owner locked, the Jan 15 commitment is just a signal, not an execution plan.

**[R4] compliance_lawyer** [speech]: CFO, here's the question that moves us from signal to execution: if Ford commits capex by Jan 15 and pulls Monterrey into their audit queue, what's the actual RVC recount window — is that 30 days, 45 days, can they guarantee March 15 completion so we hit the filing deadline with buffer? Because that timeline is what I name in the compliance trigger, and if Ford can't commit to the schedule, we're pricing the 60-day slip assumption as the baseline, not the upside.

**[R4] supply_chain_consultant** [speech]: CFO, here's what I need: if Monterrey doesn't get Ford's capex commitment by Jan 15, we're flipping to insolvency pricing—but I need to name the Texas nearshoring option *right now* so we can tell Ford "commit or we're moving Monterrey's line to our Dallas supplier by Q2, and you're absorbing the transition cost." Which Texas plant are we actually offering, and what's the lead time? Because *that's* what moves relocation from a threat to a plan.

> _GM ⟶ cfo_erm (ACTION, approved)_: The CFO locks a comprehensive risk calendar with named triggers, dollar reserves, and audit cycles—transforming fragmented exposures into a priceable timeline. The map is now operationalized with concrete decision gates.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+5; trade_credit_risk:-3.0; political_risk_exposure:-2.0; risk_map_completeness:+1

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Political-risk insurer layers conditional shock premium on 2026 USMCA review uncertainty into pricing model.  
>   side-effects: political_risk_exposure:+4.0; underwriting_discipline:+4; risk_map_completeness:+3.0; trade_credit_risk:+2.0; risk_map_completeness:+1

> _GM ⟶ trade_credit_underwriter (PROPOSAL, approved)_: Trade-credit underwriter defines payment-freeze trigger tied to Jan 15 gate and May 31 re-determination.  
>   side-effects: trade_credit_risk:+5.0; underwriting_discipline:+5; risk_map_completeness:+4.0; supplier_relocation_exposure:+2.0; risk_map_completeness:+1; risk_map_completeness:+1


_— R4 end [TERMINATED] | political_risk_exposure=41, risk_map_completeness=66, rules_of_origin_burden=40, supplier_relocation_exposure=31, trade_credit_risk=39, underwriting_discipline=68 —_

