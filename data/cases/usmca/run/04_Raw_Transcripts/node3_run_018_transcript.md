# node3_run_018


## ▶ Stage 0: translate_exposures (0 facts injected)


**[R1] auto_strategy** (pass 1): Who's running the underwriting discipline here? I've got RVC cost per model and labor-content wage-floor exposure, but I need to know: what are the named triggers that flip a supplier from "monitored" to "high-risk" — and what does that cost in insurance premium or credit spread?

**[R1] supplier** (pass 1): You've got the labor-content data, but here's the gap: *when* does a supplier actually blow up? Is it missed re-qual deadlines, capex spending frozen, or lead times stretching past 120 days? Because my guys are sitting on $8–12M in capex bets right now, and I need to know which signals tell me to pull the trigger and shift to a backup source. What are the three or four named failure modes you want flagged?

**[R1] compliance_lawyer** (pass 1): Auto, when you're building that RVC cost model, what's your audit timeline assumption — annual re-cert, quarterly spot-checks, post-shipment verification? Because the penalty structure changes completely depending on whether we catch a 10% non-qualifying input pre-audit versus post-CBP exam. That's the difference between a warning and tariff retroactivity.

**[R1] auto_strategy** ⚡reply: We're running quarterly spot-checks on high-volume platforms — that's the only way to catch input drift before shipment — but post-CBP exam retroactivity is a real cost we need priced into the model: assume 8–12% tariff clawback on non-qualifying inputs caught downstream. That changes our supplier re-sourcing threshold from "eventually nearshore" to "move now or accept the penalty cost as permanent production margin erosion."

**[R1] trade_credit_underwriter** (pass 1): When a supplier hits one of those failure modes — missed re-qual, frozen capex, 120+ day lead-time slip — what's your typical AR balance with that vendor? Because that's the receivables loss I'm underwriting, and it changes whether we're looking at a $500K credit insurance line or a structural supply-chain restructuring cost.

**[R1] supplier** ⚡reply: My AR with a supplier in that zone runs $1.2–$2.8M depending on platform volume, and that's *before* they miss re-qual — once they're in failure mode, I'm looking at 45–60 day payment holds while we stress-test the backup source, which burns another $300–500K in expedite costs. Here's what I need named: does a 120+ day lead-time slip *automatically* trigger your credit line drawdown, or do we wait for the re-qual miss — because that 30-day gap is where my smaller suppliers actually fold.

**[R1] auto_strategy** [speech]: Who's running the underwriting discipline here? I've got RVC cost per model and labor-content wage-floor exposure, but I need to know: what are the named triggers that flip a supplier from "monitored" to "high-risk" — and what does that cost in insurance premium or credit spread?

**[R1] supplier** [speech]: You've got the labor-content data, but here's the gap: *when* does a supplier actually blow up? Is it missed re-qual deadlines, capex spending frozen, or lead times stretching past 120 days? Because my guys are sitting on $8–12M in capex bets right now, and I need to know which signals tell me to pull the trigger and shift to a backup source. What are the three or four named failure modes you want flagged?

**[R1] compliance_lawyer** [speech]: Auto, when you're building that RVC cost model, what's your audit timeline assumption — annual re-cert, quarterly spot-checks, post-shipment verification? Because the penalty structure changes completely depending on whether we catch a 10% non-qualifying input pre-audit versus post-CBP exam. That's the difference between a warning and tariff retroactivity.

**[R1] trade_credit_underwriter** [speech]: When a supplier hits one of those failure modes — missed re-qual, frozen capex, 120+ day lead-time slip — what's your typical AR balance with that vendor? Because that's the receivables loss I'm underwriting, and it changes whether we're looking at a $500K credit insurance line or a structural supply-chain restructuring cost.

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: CBP retroactivity clawback line-item approved; 8-12% tariff hit with 60-90 day lag now quantified.  
>   side-effects: political_risk_exposure:+4.0; underwriting_discipline:+4; risk_map_completeness:+4.0; rules_of_origin_burden:+3.0; risk_map_completeness:+1

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Three-gate nearshoring trigger framework approved; gates one/two/three now define supplier failure modes.  
>   side-effects: supplier_relocation_exposure:+5.0; underwriting_discipline:+5; risk_map_completeness:+5.0; trade_credit_risk:+3.0; risk_map_completeness:+1; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: Master risk register updated with $500K reserve trigger, trade credit lock, and 2026 hard date.  
>   side-effects: underwriting_discipline:+5; risk_map_completeness:+5.0; trade_credit_risk:-4.0; supplier_relocation_exposure:+3.0; risk_map_completeness:+1


_— R1 end | political_risk_exposure=30, risk_map_completeness=37, rules_of_origin_burden=35, supplier_relocation_exposure=33, trade_credit_risk=24, underwriting_discipline=44 —_



## ▶ Stage 1: operationalize_and_consolidate (1 facts injected)


**[R2] auto_strategy** (pass 1): I'm running quarterly spot-checks, but here's what I need from you: what's CBP's standard audit lag on a failed RVC exam — is it 60 days post-shipment, or are we looking at longer? Because that determines whether a supplier gets flagged pre-production or eats the tariff retroactivity hit. That changes the reserve math.

**[R2] compliance_lawyer** ⚡reply: CBP's standard exam-to-notice lag runs 45–90 days post-shipment, but retroactivity exposure starts *on entry date*, not exam date — so your $500K reserve trigger needs to assume full tariff liability from day-one import, not day-45 discovery. That's the audit timeline that changes your pre-production flag threshold: you can't wait for CBP's exam results; you need RVC failures caught in your quarterly spot-checks, pre-shipment, or you're pricing a clawback you can't prevent.

**[R2] supplier** (pass 1): Auto — your quarterly spot-checks, what's the actual *fail rate* you're seeing on RVC compliance? And which platforms are blowing the labor-content floor most? Because I've got to move capex this quarter, and I'm not burning $8M on nearshoring backup plants for suppliers who are actually passing audits.

**[R2] auto_strategy** ⚡reply: Our Q3 spot-checks hit a 12% fail rate on RVC — mostly mid-size Tier 2 stamping and harness suppliers — and the labor-content floor is killing three platforms: F-Series truck frame assembly, Mustang EV battery pack integration, and our Mexico-built compact sedan platform. The Mustang EV fail is structural — we're $1.8K per unit short on qualifying labor, and nearshoring that subassembly hits us with a $3.2M capex refit, so before you burn $8M on backup plants, we need to know if you're pricing that labor-content gap into credit terms or if we're jointly re-sourcing to a qualified Mexico OEM.

**[R2] compliance_lawyer** (pass 1): Auto, your 12% fail rate—is that 12% of shipments that miss RVC on first audit, or 12% of supplier *facilities* that show non-compliant inputs? Because if it's shipments, I'm building an *individual entry* audit trigger; if it's suppliers, I'm flagging whole vendor relationships. Which one changes my penalty model—and which one tells me when to assume retroactivity clawback costs in the reserve.

**[R2] political_risk_insurer** (pass 1): Auto — is that 12% a fail rate per *shipment* or per *supplier facility*? Because if it's shipments, I'm pricing entry-level retroactivity risk for each Mustang EV or F-Series run; if it's suppliers, I'm flagging whole vendor relationships for political-risk coverage. That distinction changes my premium and reserve trigger timing.

**[R2] trade_credit_underwriter** (pass 1): Auto — of those 12% failing suppliers, how many are the mid-tier stamping/harness shops versus your big Tier 1s? Because a $2M AR hold on a $50M supplier stings but doesn't break them; same hold on a $15M shop and they're in covenant breach. Give me the top three by AR exposure, and I'll price the receivables loss into our credit insurance line right now.

**[R2] supply_chain_consultant** (pass 1): Auto, you said Mustang EV is $1.8K short per unit and a Mexico OEM refit runs $3.2M — but here's what I need: are you moving that subassembly *now*, or waiting to see what the 2026 review does to labor-content rules? Because if you're waiting, the backup supplier needs a nearshoring incentive locked in *today*, not optioned for next year. Supplier, same question — top three shops in that 12% fail zone, which ones are you actually committing capex to relocate versus which are you monitoring pending the 2026 decision?

**[R2] cfo_erm** (pass 1): Auto, before we price this — of your 12% fail rate, are those *individual shipments* hitting RVC issues or *whole supplier facilities* non-compliant? And more important: top three suppliers in that zone by AR balance. I need names and dollar exposure so I can lock trade-credit terms and reserve sizing *this round*, not next quarter.

**[R2] auto_strategy** [speech]: I'm running quarterly spot-checks, but here's what I need from you: what's CBP's standard audit lag on a failed RVC exam — is it 60 days post-shipment, or are we looking at longer? Because that determines whether a supplier gets flagged pre-production or eats the tariff retroactivity hit. That changes the reserve math.

**[R2] supplier** [speech]: Auto — your quarterly spot-checks, what's the actual *fail rate* you're seeing on RVC compliance? And which platforms are blowing the labor-content floor most? Because I've got to move capex this quarter, and I'm not burning $8M on nearshoring backup plants for suppliers who are actually passing audits.

**[R2] compliance_lawyer** [speech]: Auto, your 12% fail rate—is that 12% of shipments that miss RVC on first audit, or 12% of supplier *facilities* that show non-compliant inputs? Because if it's shipments, I'm building an *individual entry* audit trigger; if it's suppliers, I'm flagging whole vendor relationships. Which one changes my penalty model—and which one tells me when to assume retroactivity clawback costs in the reserve.

**[R2] political_risk_insurer** [speech]: Auto — is that 12% a fail rate per *shipment* or per *supplier facility*? Because if it's shipments, I'm pricing entry-level retroactivity risk for each Mustang EV or F-Series run; if it's suppliers, I'm flagging whole vendor relationships for political-risk coverage. That distinction changes my premium and reserve trigger timing.

**[R2] trade_credit_underwriter** [speech]: Auto — of those 12% failing suppliers, how many are the mid-tier stamping/harness shops versus your big Tier 1s? Because a $2M AR hold on a $50M supplier stings but doesn't break them; same hold on a $15M shop and they're in covenant breach. Give me the top three by AR exposure, and I'll price the receivables loss into our credit insurance line right now.

**[R2] supply_chain_consultant** [speech]: Auto, you said Mustang EV is $1.8K short per unit and a Mexico OEM refit runs $3.2M — but here's what I need: are you moving that subassembly *now*, or waiting to see what the 2026 review does to labor-content rules? Because if you're waiting, the backup supplier needs a nearshoring incentive locked in *today*, not optioned for next year. Supplier, same question — top three shops in that 12% fail zone, which ones are you actually committing capex to relocate versus which are you monitoring pending the 2026 decision?

**[R2] cfo_erm** [speech]: Auto, before we price this — of your 12% fail rate, are those *individual shipments* hitting RVC issues or *whole supplier facilities* non-compliant? And more important: top three suppliers in that zone by AR balance. I need names and dollar exposure so I can lock trade-credit terms and reserve sizing *this round*, not next quarter.


_— R2 end | political_risk_exposure=31, risk_map_completeness=37, rules_of_origin_burden=37, supplier_relocation_exposure=33, trade_credit_risk=24, underwriting_discipline=44 —_


**[R3] auto_strategy** (pass 1): The 12% is *facility-level* — we've got seven mid-tier stamping shops running non-compliant inputs consistently, not random shipment misses. Mustang EV: we're moving that Mexico OEM refit *now*, locking the $3.2M capex this quarter — the 2026 labor review doesn't move our timeline, we're past that risk. Top three AR exposures in that zone: TierCo stamping ($2.1M), Midwest harness ($1.8M), Precision frames ($1.4M). Trade-credit team, those are your reserve anchors.

**[R3] supplier** (pass 1): The $2.1M TierCo, $1.8M Midwest, $1.4M Precision — when they hit gate one or two, what's the hold trigger? Are we freezing 45 days of AR automatically, or waiting for audit confirmation? And are those AR freezes priced into our credit insurance line, or is that still loose?

**[R3] cfo_erm** ⚡reply: Those three are hitting my reserve trigger *now* — $500K across all three, locked this quarter. TierCo and Midwest freeze at gate one (missed re-qual or CBP audit flag); Precision at gate two if lead times blow past 120 days. Credit insurance line covers the AR hold, but supplier gets 15 days to cure before we escalate to nearshoring backup — that's priced into the $8–12M capex commitment we're making today.

**[R3] compliance_lawyer** (pass 1): Auto, when TierCo or Midwest "miss re-qual" — is that a failed CBP exam on a live shipment, or a self-audit failure you catch before CBP sees it? Because those are two different retroactivity triggers for me, and the CFO's $500K reserve assumption hinges on which one we're actually defending against.

**[R3] auto_strategy** ⚡reply: Both — TierCo's last two runs failed our pre-audit spot-checks, so we caught it internal; Midwest hasn't been re-certified since Q3, which means CBP could flag them cold on the next shipment. That's the $500K split: TierCo's defensible as a warning-level fix, Midwest is live retroactivity exposure if they ship before re-qual clears.

**[R3] auto_strategy** [speech]: The 12% is *facility-level* — we've got seven mid-tier stamping shops running non-compliant inputs consistently, not random shipment misses. Mustang EV: we're moving that Mexico OEM refit *now*, locking the $3.2M capex this quarter — the 2026 labor review doesn't move our timeline, we're past that risk. Top three AR exposures in that zone: TierCo stamping ($2.1M), Midwest harness ($1.8M), Precision frames ($1.4M). Trade-credit team, those are your reserve anchors.

**[R3] supplier** [speech]: The $2.1M TierCo, $1.8M Midwest, $1.4M Precision — when they hit gate one or two, what's the hold trigger? Are we freezing 45 days of AR automatically, or waiting for audit confirmation? And are those AR freezes priced into our credit insurance line, or is that still loose?

**[R3] compliance_lawyer** [speech]: Auto, when TierCo or Midwest "miss re-qual" — is that a failed CBP exam on a live shipment, or a self-audit failure you catch before CBP sees it? Because those are two different retroactivity triggers for me, and the CFO's $500K reserve assumption hinges on which one we're actually defending against.

> _GM ⟶ political_risk_insurer (PROPOSAL, denied)_: Question deferred — board must first resolve Mexico vs US vendor location before premium structure can be priced.  
>   side-effects: —

> _GM ⟶ trade_credit_underwriter (PROPOSAL, approved)_: AR freeze triggers locked: TierCo/Midwest 45d gate-one, Precision 60d confirmed-slip only; 2.5% default spreads priced.  
>   side-effects: underwriting_discipline:+5.0; trade_credit_risk:-4.0; risk_map_completeness:+5.0; risk_map_completeness:+1

> _GM ⟶ supply_chain_consultant (PROPOSAL, denied)_: Question deferred — CFO must resolve Mexico vs US vendor location before capex exposure can be quantified.  
>   side-effects: —

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: CFO forces decision: backup vendor location and reserve structure must be resolved NOW to unlock consolidated map.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+5.0; supplier_relocation_exposure:+3.0; political_risk_exposure:+2.0; risk_map_completeness:+1


_— R3 end | political_risk_exposure=34, risk_map_completeness=48, rules_of_origin_burden=39, supplier_relocation_exposure=36, trade_credit_risk=20, underwriting_discipline=54 —_


**[R4] auto_strategy** (pass 1): Look, I can't price the RVC burden — that's my core variable — until you call Mexico or US on those three backup vendors. Here's the trade: Mexico keeps capex at $3.2M but eats the 2026 wage-floor hit twice; US is $5–6M upfront but locks us out of that review risk. Which one unblocks the reserve and the map? Pick one, and I'll model the compliance cost by end of day.

**[R4] cfo_erm** ⚡reply: Mexico. Lock it now — $3.2M capex this quarter, and I'm pricing the 2026 wage-floor retroactivity into political risk at 8–12% tariff hit. That unblocks your RVC model, my reserve sizing, and the consolidated map. Trade credit team gets the TierCo/Midwest/Precision AR anchors today; you get your compliance baseline by EOD.

**[R4] supplier** (pass 1): Auto, you said seven shops are running non-compliant inputs — of those, how many have already signaled they can re-tool for Mexico, and how many are we writing off? Because once TierCo and Midwest freeze, the other five are going to panic-spend on re-qual or pack it in. I need names and viability scores so I can start qualifying replacement vendors now, not after gate one triggers.

**[R4] auto_strategy** ⚡reply: Of the seven shops, TierCo and Midwest are Mexico-capable—they're already talking to our OEM partner there, so they move fast once we lock the capex. The other five are smaller stamping and harness ops; three can re-tool domestically in 90 days if we fund it, but two are basically done—tooling's too old and their labor math doesn't work either geography. I'm naming the three viable ones for your replacement vendor screen right now: Precision Frames, Midwest Harness, and Allied Stamping; the other two we treat as sunset and start qualifying alternatives this week.

**[R4] compliance_lawyer** (pass 1): Auto, TierCo failed your internal spot-check — that's self-audit, so you catch it before CBP sees it. Midwest hasn't been re-cert'd since Q3, so CBP could hit them cold on the next shipment. For TierCo, the freeze and disclosure stop retroactivity; for Midwest, we assume 60-90 day lag *plus* duty recalculation on prior entries. Are those two vendors on the same AR freeze schedule, or does Midwest's timeline hit differently?

**[R4] political_risk_insurer** (pass 1): Midwest hasn't been re-cert'd since Q3 — when CBP flags them cold on the next run, does retroactivity clock back to their *last valid cert date*, or just forward from the audit notice? Because if it's back-dated, we're eating duty recalculation on every entry since Q3. That changes my reserve trigger and whether the $500K holds.

**[R4] trade_credit_underwriter** (pass 1): Compliance, on Midwest — if CBP claws back to their last valid cert date in Q3, are we talking duty recalc on *all* entries since then, or just the flagged shipment? Because if it's all entries, my AR freeze and credit insurance line don't cover the tariff hit, and I'm flagging that $1.8M receivable as a retroactivity loss, not a payment hold. Which one are we defending against?

**[R4] compliance_lawyer** ⚡reply: CBP retroactivity on Midwest claws back to the last *valid cert date* — Q3 — so you're defending against duty recalculation on *all* entries from Q3 forward, not just the flagged shipment. That $1.8M receivable flips from payment hold to retroactivity loss the moment CBP issues the exam notice; your credit insurance line doesn't absorb tariff recalculation, so flag it now as a reserve trigger, not a spread adjustment.

**[R4] auto_strategy** [speech]: Look, I can't price the RVC burden — that's my core variable — until you call Mexico or US on those three backup vendors. Here's the trade: Mexico keeps capex at $3.2M but eats the 2026 wage-floor hit twice; US is $5–6M upfront but locks us out of that review risk. Which one unblocks the reserve and the map? Pick one, and I'll model the compliance cost by end of day.

**[R4] supplier** [speech]: Auto, you said seven shops are running non-compliant inputs — of those, how many have already signaled they can re-tool for Mexico, and how many are we writing off? Because once TierCo and Midwest freeze, the other five are going to panic-spend on re-qual or pack it in. I need names and viability scores so I can start qualifying replacement vendors now, not after gate one triggers.

**[R4] compliance_lawyer** [speech]: Auto, TierCo failed your internal spot-check — that's self-audit, so you catch it before CBP sees it. Midwest hasn't been re-cert'd since Q3, so CBP could hit them cold on the next shipment. For TierCo, the freeze and disclosure stop retroactivity; for Midwest, we assume 60-90 day lag *plus* duty recalculation on prior entries. Are those two vendors on the same AR freeze schedule, or does Midwest's timeline hit differently?

**[R4] political_risk_insurer** [speech]: Midwest hasn't been re-cert'd since Q3 — when CBP flags them cold on the next run, does retroactivity clock back to their *last valid cert date*, or just forward from the audit notice? Because if it's back-dated, we're eating duty recalculation on every entry since Q3. That changes my reserve trigger and whether the $500K holds.

**[R4] trade_credit_underwriter** [speech]: Compliance, on Midwest — if CBP claws back to their last valid cert date in Q3, are we talking duty recalc on *all* entries since then, or just the flagged shipment? Because if it's all entries, my AR freeze and credit insurance line don't cover the tariff hit, and I'm flagging that $1.8M receivable as a retroactivity loss, not a payment hold. Which one are we defending against?

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Vendor roadmap initiated; gate-one trigger locked to first responder.  
>   side-effects: supplier_relocation_exposure:+3.0; risk_map_completeness:+4.0; underwriting_discipline:+3.0; agent_stress:+2.0

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: Reserve split locked: $200K AR freeze, $300K retroactivity lag.  
>   side-effects: trade_credit_risk:-4.0; political_risk_exposure:-3.0; risk_map_completeness:+5.0; underwriting_discipline:+4.0; agent_stress:+2.0; risk_map_completeness:+1


_— R4 end | political_risk_exposure=32, risk_map_completeness=56, rules_of_origin_burden=41, supplier_relocation_exposure=39, trade_credit_risk=16, underwriting_discipline=61 —_


**[R5] auto_strategy** (pass 1): CFO — the $300K retroactivity reserve: does that cover *both* Midwest's cold CBP clawback (all Q3+ entries) *and* any retroactivity exposure on TierCo if we disclose their internal failures to CBP, or are those two separate buckets? Because if TierCo's disclosure caps retroactivity at current shipment only, my RVC burden calculation drops, but if CBP still claws back on TierCo's prior entries, I need to flag that cost now.

**[R5] cfo_erm** ⚡reply: The $300K covers *Midwest's cold clawback* on Q3+ entries—that's our baseline. TierCo's disclosure stops retroactivity at the current shipment, so no prior-entry recalc there. If CBP pushes back on TierCo's disclosure adequacy, we burn through that reserve fast—so I'm pricing TierCo as capped, Midwest as open-ended, and flagging a $150K contingency if either one bleeds.

**[R5] supplier** (pass 1): Auto — when TierCo or Midwest hits gate one, who's calling the AR freeze and how fast? Is it your internal spot-check flagging it same-day, or waiting for CBP audit notice? And real talk: of those five smaller shops you're not moving to Mexico, which ones are you actually keeping on life support versus writing off? Because I need to know which ones I'm re-qualifying now versus which ones I'm already replacing.

**[R5] auto_strategy** ⚡reply: TierCo we catch same-day on our spot-check—AR freeze triggers within 24 hours of our audit flag, no waiting for CBP. Midwest is different: cold CBP hit means we're reactive, probably 48–72 hours lag once they notify us. On the five smaller shops: three are committing capex for re-tooling (stamping retrofit at two midwest facilities, one harness refit in Tennessee), two I'm writing off—they can't absorb the labor-content cost without pricing themselves out, so we're moving those inputs to the Mexico OEM line now.

**[R5] compliance_lawyer** (pass 1): CFO—the reserve brackets Midwest and TierCo, but here's what I need for the map: when TierCo and those five re-tooling shops hit re-certification, what's our audit assumption—Q2 2025 gate-two or do we stagger them? Because that timing locks whether the re-qual cost lands in this reserve or next quarter's compliance budget. And I need one sentence on what a failed re-cert actually costs us in penalty exposure so I can price it into the RVC burden.

**[R5] political_risk_insurer** (pass 1): Compliance—when TierCo and those five re-tooling shops go through re-cert, are we staggering Q2 2025 or hitting them all at once? And what's the actual penalty hit if one of them fails—tariff recalc, hold on shipments, or both? I need that cost quantified so I can price whether the $300K retroactivity bucket holds or we need to flag a separate re-cert penalty reserve.

**[R5] compliance_lawyer** ⚡reply: TierCo and the five re-tooling shops hit re-cert staggered—TierCo Q2 gate-two, the five mid-tier facilities Q2–Q3 rolling—so compliance costs spread across two quarters, not one lump. Failed re-cert triggers 19 CFR 162.8 penalty assessment *plus* entry-level duty recalculation on all shipments under that cert—so if Midwest fails cold, we're looking at base tariff plus 20% compliance penalty on every Q3+ entry, not just the flag shipment. That's a separate bucket from the $300K retroactivity reserve—I'm flagging $150–200K re-cert penalty exposure and need CFO to split that out now so the map holds.

**[R5] trade_credit_underwriter** (pass 1): CFO—Compliance flagged 19 CFR 162.8 re-cert penalties on top of duty recalculation. Is the $300K retroactivity bucket covering *both* Midwest's clawback *and* the re-cert penalty, or do we need to carve out $150–200K separately so I can price the actual receivables loss on Midwest and lock insurance coverage terms?

**[R5] auto_strategy** [speech]: CFO — the $300K retroactivity reserve: does that cover *both* Midwest's cold CBP clawback (all Q3+ entries) *and* any retroactivity exposure on TierCo if we disclose their internal failures to CBP, or are those two separate buckets? Because if TierCo's disclosure caps retroactivity at current shipment only, my RVC burden calculation drops, but if CBP still claws back on TierCo's prior entries, I need to flag that cost now.

**[R5] supplier** [speech]: Auto — when TierCo or Midwest hits gate one, who's calling the AR freeze and how fast? Is it your internal spot-check flagging it same-day, or waiting for CBP audit notice? And real talk: of those five smaller shops you're not moving to Mexico, which ones are you actually keeping on life support versus writing off? Because I need to know which ones I'm re-qualifying now versus which ones I'm already replacing.

**[R5] compliance_lawyer** [speech]: CFO—the reserve brackets Midwest and TierCo, but here's what I need for the map: when TierCo and those five re-tooling shops hit re-certification, what's our audit assumption—Q2 2025 gate-two or do we stagger them? Because that timing locks whether the re-qual cost lands in this reserve or next quarter's compliance budget. And I need one sentence on what a failed re-cert actually costs us in penalty exposure so I can price it into the RVC burden.

**[R5] political_risk_insurer** [speech]: Compliance—when TierCo and those five re-tooling shops go through re-cert, are we staggering Q2 2025 or hitting them all at once? And what's the actual penalty hit if one of them fails—tariff recalc, hold on shipments, or both? I need that cost quantified so I can price whether the $300K retroactivity bucket holds or we need to flag a separate re-cert penalty reserve.

**[R5] trade_credit_underwriter** [speech]: CFO—Compliance flagged 19 CFR 162.8 re-cert penalties on top of duty recalculation. Is the $300K retroactivity bucket covering *both* Midwest's clawback *and* the re-cert penalty, or do we need to carve out $150–200K separately so I can price the actual receivables loss on Midwest and lock insurance coverage terms?

> _GM ⟶ cfo_erm (ACTION, approved)_: The CFO locks the final $500K penalty architecture into three distinct loss buckets with named triggers and staggered timelines—the map now has operational teeth. Risk translation complete.  
>   side-effects: underwriting_discipline:+5.0; risk_map_completeness:+5.0; rules_of_origin_burden:+3.0; risk_map_completeness:+1

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: The CFO's three-bucket reserve structure ($200K AR freeze, $150K retroactivity clawback, $150K re-cert penalty) operationalizes the compliance cost model with named triggers and staggered timelines, closing the final gap in the Policy-to-Supply-Chain Risk Map.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+5.0; rules_of_origin_burden:+3.0; trade_credit_risk:-2.0; risk_map_completeness:+1


_— R5 end [TERMINATED] | political_risk_exposure=33, risk_map_completeness=73, rules_of_origin_burden=49, supplier_relocation_exposure=39, trade_credit_risk=14, underwriting_discipline=71 —_

