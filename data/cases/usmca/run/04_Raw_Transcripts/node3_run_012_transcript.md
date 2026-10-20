# node3_run_012


## ▶ Stage 0: translate_exposures (0 facts injected)


**[R1] auto_strategy** (pass 1): Who's owning the supplier-relocation-to-insolvency bridge? If we're nearshoring to Mexico and a Tier-2 shop goes under mid-transition, what's the actual cash impact and timeline hit — because that's the pricing variable we're missing.

**[R1] supplier** (pass 1): Auto_strategy's right — if a Tier-2 shop goes dark while we're halfway through re-qualifying them for Mexico, we're looking at line-restart delays *and* capex sunk on their tooling. Who's pricing the cash impact of that failure window? Because right now "trade credit risk" is 25, but that doesn't account for a 6-month qualification gap while we scramble to a backup supplier.

**[R1] compliance_lawyer** (pass 1): During that qualification window, are you still certifying product origin under USMCA, or does the gap void your certification? Because if you're shipping unqualified goods to avoid line stoppage, that's a penalty exposure we need to price—not just a cash-flow delay.

**[R1] supplier** ⚡reply: Look, if a Tier-2 supplier collapses mid-transition to Mexico, we're talking 8–12 weeks to qualify a replacement *plus* whatever capex we've already burned on their line—that's $2–5M per supplier depending on tooling complexity, and we're bleeding lead time the whole way. Trade credit at 25 doesn't touch this; we need a separate "supplier-failure cash impact" variable priced at 40+ to account for the qualification gap *and* the certification void the compliance lawyer just flagged—because shipping unqualified goods to keep the line hot turns a cash problem into a legal one.

**[R1] auto_strategy** [speech]: Who's owning the supplier-relocation-to-insolvency bridge? If we're nearshoring to Mexico and a Tier-2 shop goes under mid-transition, what's the actual cash impact and timeline hit — because that's the pricing variable we're missing.

**[R1] supplier** [speech]: Auto_strategy's right — if a Tier-2 shop goes dark while we're halfway through re-qualifying them for Mexico, we're looking at line-restart delays *and* capex sunk on their tooling. Who's pricing the cash impact of that failure window? Because right now "trade credit risk" is 25, but that doesn't account for a 6-month qualification gap while we scramble to a backup supplier.

**[R1] compliance_lawyer** [speech]: During that qualification window, are you still certifying product origin under USMCA, or does the gap void your certification? Because if you're shipping unqualified goods to avoid line stoppage, that's a penalty exposure we need to price—not just a cash-flow delay.

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Political-risk layer priced: enforcement exposure at 45-55 bps for supplier-failure + certification gap.  
>   side-effects: political_risk_exposure:+4.0; underwriting_discipline:+3; risk_map_completeness:+2; trade_credit_risk:+2.0; stress:-2.0

> _GM ⟶ trade_credit_underwriter (PROPOSAL, approved)_: Supplier-Failure-in-Transit Trigger locked: $2-5M cash + 45-55 bps enforcement, now discrete variable.  
>   side-effects: trade_credit_risk:+5.0; underwriting_discipline:+4; risk_map_completeness:+3; supplier_relocation_exposure:+3.0; stress:-3.0; risk_map_completeness:+1; risk_map_completeness:+1

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Supplier-relocation matrix initiated: Tier-2 shop allocation (Mexico vs domestic) to close qualification gap.  
>   side-effects: supplier_relocation_exposure:+4.0; risk_map_completeness:+3; underwriting_discipline:+3; rules_of_origin_burden:+2.0; stress:+2.0; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: Policy-to-Supply-Chain Risk Map consolidation ordered: four variables ranked by materiality with priced scenarios.  
>   side-effects: risk_map_completeness:+5; underwriting_discipline:+3; supplier_relocation_exposure:+3.0; rules_of_origin_burden:-2.0; stress:+3.0; stress:+2.0; stress:+0.0


_— R1 end | political_risk_exposure=30, risk_map_completeness=35, rules_of_origin_burden=32, supplier_relocation_exposure=35, trade_credit_risk=32, underwriting_discipline=43 —_



## ▶ Stage 1: operationalize_and_consolidate (1 facts injected)


**[R2] auto_strategy** (pass 1): Supply chain—where are you on the relocation matrix output? I need the supplier-by-supplier RVC gap and labor-cost bridge to Mexico for each model platform. Without that, we can't price the nearshoring scenario or tell finance which capex bets actually close the USMCA compliance gap.

**[R2] supply_chain_consultant** ⚡reply: Matrix is locked at Tier-2 shop level—RVC gaps by platform ready, labor-cost bridge to Mexico modeled at $80–120K per shop per quarter, but I'm holding final allocation pending the trade-credit underwriter's failure-in-transit trigger. If a shop goes dark mid-qualification, that resets capex timing; need that cash-impact window before I sign off on the relocation sequence.

**[R2] supplier** (pass 1): Trade-credit—the matrix is ready to lock, but supply chain needs your failure-in-transit window nailed down: if a Tier-2 shop goes dark during month 4 of a 12-week re-qual to Mexico, what's the actual cash hit *and* the line-restart timeline? That's the decision rule we're missing to operationalize this thing.

**[R2] trade_credit_underwriter** ⚡reply: Month 4 failure during 12-week re-qual costs $2–5M in sunk tooling plus 6–8 weeks line restart; I'm pricing that as a discrete trade-credit trigger at 45–55 bps on the relocation capex pool. Supply chain, lock your matrix to that window—once you do, I can price the receivables hit if the backup supplier's cash position deteriorates mid-transition.

**[R2] compliance_lawyer** (pass 1): Supply chain, when that Tier-2 shop is mid-transition to Mexico — weeks 4 through 12 of re-qual — what's your certification posture? Are you claiming USMCA origin on shipments, or are you pulling them off the line until re-qual clears? Because if you're shipping qualified goods from an *unqualified* supplier location, that's a separate penalty exposure we haven't priced yet.

**[R2] political_risk_insurer** (pass 1): Compliance, supply chain — I need to know the shipment plan during weeks 4–12 of the re-qual window. Are you pulling product off the line until certification clears, or are you shipping it and *not* claiming USMCA origin to avoid the penalty? Because those are two completely different enforcement exposures and I'm pricing the wrong one if you haven't decided yet.

**[R2] trade_credit_underwriter** (pass 1): Supply chain — during weeks 4–12 when a Tier-2 shop is mid-transition to Mexico, are you *pulling product off the line* until certification clears, or *shipping it domestically* to keep cash flowing? Because that choice determines whether the supplier survives the qualification window or goes dark. I need that decision rule locked before I can price which shops in your matrix actually hit the failure trigger.

**[R2] supply_chain_consultant** (pass 1): [supply_chain_consultant attempted to propose a new action, but their team is executing: supplier_relocation_matrix_build. Action blocked — monitoring continues.]

**[R2] compliance_lawyer** ⚡reply: That domestic-only shipment rule kills the certification-gap penalty, but it locks you into a 6–8 week cash drain while the shop re-quals to Mexico—and if your backup supplier's insolvency risk is priced at 45–55 bps, you're now betting the entire relocation capex pool on that shop staying solvent through weeks 4–12. I need the CFO to name the cash-reserve floor that triggers a pivot to a third-tier supplier before the backup goes dark—otherwise we're pricing trade-credit risk without a failure abort clause.

**[R2] supply_chain_consultant** [speech]: [supply_chain_consultant attempted to propose a new action, but their team is executing: supplier_relocation_matrix_build. Action blocked — monitoring continues.]

**[R2] auto_strategy** [speech]: Supply chain—where are you on the relocation matrix output? I need the supplier-by-supplier RVC gap and labor-cost bridge to Mexico for each model platform. Without that, we can't price the nearshoring scenario or tell finance which capex bets actually close the USMCA compliance gap.

**[R2] supplier** [speech]: Trade-credit—the matrix is ready to lock, but supply chain needs your failure-in-transit window nailed down: if a Tier-2 shop goes dark during month 4 of a 12-week re-qual to Mexico, what's the actual cash hit *and* the line-restart timeline? That's the decision rule we're missing to operationalize this thing.

**[R2] compliance_lawyer** [speech]: Supply chain, when that Tier-2 shop is mid-transition to Mexico — weeks 4 through 12 of re-qual — what's your certification posture? Are you claiming USMCA origin on shipments, or are you pulling them off the line until re-qual clears? Because if you're shipping qualified goods from an *unqualified* supplier location, that's a separate penalty exposure we haven't priced yet.

**[R2] political_risk_insurer** [speech]: Compliance, supply chain — I need to know the shipment plan during weeks 4–12 of the re-qual window. Are you pulling product off the line until certification clears, or are you shipping it and *not* claiming USMCA origin to avoid the penalty? Because those are two completely different enforcement exposures and I'm pricing the wrong one if you haven't decided yet.

**[R2] trade_credit_underwriter** [speech]: Supply chain — during weeks 4–12 when a Tier-2 shop is mid-transition to Mexico, are you *pulling product off the line* until certification clears, or *shipping it domestically* to keep cash flowing? Because that choice determines whether the supplier survives the qualification window or goes dark. I need that decision rule locked before I can price which shops in your matrix actually hit the failure trigger.

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: CFO locks a critical decision rule: Tier-2 shops mid-transition ship domestically only, eliminating USMCA penalty exposure during weeks 4-12. This operationalizes the compliance posture and gives supply chain/trade-credit a concrete constraint for pricing failure scenarios.  
>   side-effects: underwriting_discipline:+5.0; rules_of_origin_burden:-3.0; trade_credit_risk:+3.0; risk_map_completeness:+4.0; risk_map_completeness:+1


_— R2 end | political_risk_exposure=30, risk_map_completeness=41, rules_of_origin_burden=31, supplier_relocation_exposure=35, trade_credit_risk=35, underwriting_discipline=48 —_


**[R3] auto_strategy** (pass 1): Supply chain—matrix is ready, but I need the output: which model platforms hit the RVC floor under current sourcing, and which ones need Tier-2 shops in Mexico to close the gap? Give me the dollar compliance cost per platform, because that's what operationalizes the CFO's shipment rule against the actual production impact.

**[R3] supply_chain_consultant** ⚡reply: The matrix shows three platforms short: F-Series sits 2.1 points below RVC floor—costs $840K to nearshore Tier-2 ops to Mexico; Ranger and Transit each need $620K capex to hit compliance. Those are your hard numbers against the CFO's weeks-4-through-12 rule—if we're shipping domestically during re-qual, we're eating penalties on F-Series unless we move that supplier now, not in month two.

**[R3] supplier** (pass 1): CFO—before we call this map complete, I need clarity: are we bankrolling the $840K F-Series nearshoring capex *now*, or is that on the supplier to fund? Because if we're not putting cash on the table in month one, that supplier's not moving in time, and we're right back to shipping unqualified goods and eating penalties anyway. That's the decision that operationalizes the whole rule.

**[R3] cfo_erm** ⚡reply: We fund the F-Series capex upfront—$840K deployed in month one, non-recoverable against supplier performance guarantees. That's the condition that makes the domestic-shipment rule executable; without it, we're pricing phantom compliance. Lock it now or we're back to penalty exposure and I'm re-pricing the political-risk layer.

**[R3] compliance_lawyer** (pass 1): CFO, your domestic-shipment rule solves the penalty gap, but it creates an audit exposure we haven't priced: CBP will scrutinize *why* you're not claiming USMCA on goods that *could* qualify if the supplier weren't mid-transition. That's a discrete origin-falsification audit trigger—different from the certification-gap penalty. Political-risk layer needs to price that separately, or we're leaving enforcement exposure on the table. What's the audit frequency assumption for non-claimed shipments in your model?

**[R3] supplier** ⚡reply: We're running 15–20 CBP container audits per quarter on non-USMCA claims from mid-transition suppliers—that's our baseline from the last three years. If we're shipping F-Series domestically for 12 weeks straight without origin claims, you're looking at 3–5 targeted audits in that window alone, and each one costs $50–75K in legal and documentation pull. Price that as a discrete $200–300K enforcement bucket separate from the penalty layer, or we're understating the total compliance cost by 25 percent.

**[R3] compliance_lawyer** ⚡reply: The audit frequency holds—15–20 per quarter is CBP's historical pattern on mid-transition suppliers, and shipping F-Series domestically for 12 weeks without origin claims puts you *squarely* in that targeting window. Lock the $200–300K enforcement bucket as a separate line item in the political-risk layer, because if we don't price it discretely, you're underwriting blind when the first audit hits in week 5.

**[R3] trade_credit_underwriter** (pass 1): CFO—you're funding $840K month-one for F-Series tooling, but if that supplier goes dark in week 8, is that capex a sunk loss or do we have lien rights on the equipment? Because that changes whether my receivables exposure is $2–5M or $5–8M, and whether we price this as trade-credit risk or straight business interruption.

**[R3] supply_chain_consultant** (pass 1): CFO—you're funding F-Series month-one, domestic-only weeks 4–12. But I need the allocation trigger: are we deciding *now* which Tier-2 shops move to Mexico to close the RVC gap, or are we deferring that call until post-audit in month 3? Because if we're waiting, the 2026 USMCA review becomes a *prospective risk*—we could fund tooling today and face re-qualification all over again in 18 months. What's the decision gate?

**[R3] compliance_lawyer** [speech]: CFO, your domestic-shipment rule solves the penalty gap, but it creates an audit exposure we haven't priced: CBP will scrutinize *why* you're not claiming USMCA on goods that *could* qualify if the supplier weren't mid-transition. That's a discrete origin-falsification audit trigger—different from the certification-gap penalty. Political-risk layer needs to price that separately, or we're leaving enforcement exposure on the table. What's the audit frequency assumption for non-claimed shipments in your model?

**[R3] auto_strategy** [speech]: Supply chain—matrix is ready, but I need the output: which model platforms hit the RVC floor under current sourcing, and which ones need Tier-2 shops in Mexico to close the gap? Give me the dollar compliance cost per platform, because that's what operationalizes the CFO's shipment rule against the actual production impact.

**[R3] supplier** [speech]: CFO—before we call this map complete, I need clarity: are we bankrolling the $840K F-Series nearshoring capex *now*, or is that on the supplier to fund? Because if we're not putting cash on the table in month one, that supplier's not moving in time, and we're right back to shipping unqualified goods and eating penalties anyway. That's the decision that operationalizes the whole rule.

**[R3] trade_credit_underwriter** [speech]: CFO—you're funding $840K month-one for F-Series tooling, but if that supplier goes dark in week 8, is that capex a sunk loss or do we have lien rights on the equipment? Because that changes whether my receivables exposure is $2–5M or $5–8M, and whether we price this as trade-credit risk or straight business interruption.

**[R3] supply_chain_consultant** [speech]: CFO—you're funding F-Series month-one, domestic-only weeks 4–12. But I need the allocation trigger: are we deciding *now* which Tier-2 shops move to Mexico to close the RVC gap, or are we deferring that call until post-audit in month 3? Because if we're waiting, the 2026 USMCA review becomes a *prospective risk*—we could fund tooling today and face re-qualification all over again in 18 months. What's the decision gate?

> _GM ⟶ political_risk_insurer (ACTION, approved)_: The insurer operationalizes a second political-risk bucket with concrete enforcement triggers and cost bands, directly advancing underwriting discipline. The audit-frequency question to compliance_lawyer surfaces cross-variable dependencies that strengthen the risk map's internal logic.  
>   side-effects: underwriting_discipline:+5.0; political_risk_exposure:+3.0; risk_map_completeness:+4.0; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: The CFO's month-one allocation decision operationalizes the risk map with concrete triggers and timelines, advancing both completeness and discipline. However, the proposal surfaces new risk layers (audit exposure, lien rights, 2026 re-qualification) that increase assessed burden across multiple dimensions.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+5.0; rules_of_origin_burden:+3.0; political_risk_exposure:+4.0; trade_credit_risk:+3.0; supplier_relocation_exposure:+5.0; risk_map_completeness:+1; risk_map_completeness:+1


_— R3 end | political_risk_exposure=37, risk_map_completeness=54, rules_of_origin_burden=35, supplier_relocation_exposure=40, trade_credit_risk=38, underwriting_discipline=58 —_


**[R4] auto_strategy** (pass 1): Supply chain—you've got the RVC gaps locked, but I need one more output before we call this map done: what's the total compliance *cost* to keep F-Series, Ranger, and Transit in the current sourcing mix through 2026, including tariff clawback risk and re-qualification penalties if CBP challenges us? Because right now we're pricing the nearshoring scenario, but we're not pricing the *cost of inaction*—and that's what closes the risk map.

**[R4] supply_chain_consultant** ⚡reply: F-Series and Ranger hit 78–82% RVC under current sourcing; Transit clears 89% but bleeds $340K annually on labor content alone. Full compliance cost through 2026: $2.1–2.4M in penalties, tariff clawback, and re-qual audits if CBP challenges the certification gaps—versus $840K upfront to move two Tier-2 shops to Mexico and lock RVC at 95%+. The inaction scenario costs you twice what nearshoring does, but only if you fund the capex *this month* before qualification windows lock.

**[R4] supplier** (pass 1): CFO—F-Series is locked. But Ranger and Transit: are we funding both relocations in month one, or are we staggering them? Because if Ranger goes domestic-only while we're still deciding on Transit, we're eating two different audit exposures instead of one clean transition. What's the month-one allocation call?

**[R4] cfo_erm** ⚡reply: F-Series month-one is locked—$840K committed. Ranger and Transit both fund now, $1.2M total, single qualification window, one audit posture. Staggering kills the compliance narrative and doubles our enforcement exposure; we're not doing that.

**[R4] compliance_lawyer** (pass 1): Supply chain—when F-Series Tier-2 hits Mexico in weeks 4–12, who's *certifying* the re-qual to CBP? Are we filing a certification amendment upfront, or documenting the transition retrospectively and hoping CBP accepts "domestic-only during transition" as the audit defense? Because that changes whether the audit trigger fires on *intent-to-defraud* or just *procedural gap*.

**[R4] political_risk_insurer** (pass 1): Compliance—when F-Series files the certification amendment for the Mexico transition in weeks 4–12, does CBP's approval letter lock the origin status of goods shipped *before* the amendment, or does a 2026 USMCA rule change let them retroactively challenge shipments we certified as compliant today? That's the difference between a $200K audit cost and a $2–5M clawback exposure—and it's the piece that operationalizes the prospective political risk.

**[R4] compliance_lawyer** ⚡reply: CBP's approval of a certification amendment locks origin status *prospectively*—goods shipped before amendment filing remain defensible under the certification that was current when shipped, *but only if* you document the transition contemporaneously and don't amend retroactively. A 2026 rule change can't claw back shipments certified under rules valid at shipment date, *unless* the rule change includes retroactive enforcement language—which USMCA precedent suggests is low-probability but non-zero. 

The audit trigger fires on *procedural gap*, not intent, so file that amendment in week 4 when the first Mexico-sourced Tier-2 unit ships, not retrospectively in month 3—that's the difference between a $200K procedural penalty and a $2–5M clawback exposure. What's the filing timeline in your transition plan?

**[R4] trade_credit_underwriter** (pass 1): CFO—before we lock the map: if F-Series Tier-2 supplier goes insolvent in week 6 while we're mid-qual to Mexico, do we have lien security on the $840K tooling we just funded, or is that capex a straight loss? Because that determines whether my receivables exposure stays at $2–5M or balloons to $3–8M—and whether we need a separate tooling-recovery reserve in the month-one budget.

**[R4] cfo_erm** (pass 1): Before we lock this map: on the $2M month-one tooling spend—do we have first lien on the equipment, or is that capex unsecured? Because if a supplier goes insolvent in week 6, I need to know if we're recovering $1–1.5M of that spend or eating the full loss. That changes whether we need a separate reserve or whether the trade-credit trigger holds.

**[R4] auto_strategy** [speech]: Supply chain—you've got the RVC gaps locked, but I need one more output before we call this map done: what's the total compliance *cost* to keep F-Series, Ranger, and Transit in the current sourcing mix through 2026, including tariff clawback risk and re-qualification penalties if CBP challenges us? Because right now we're pricing the nearshoring scenario, but we're not pricing the *cost of inaction*—and that's what closes the risk map.

**[R4] supplier** [speech]: CFO—F-Series is locked. But Ranger and Transit: are we funding both relocations in month one, or are we staggering them? Because if Ranger goes domestic-only while we're still deciding on Transit, we're eating two different audit exposures instead of one clean transition. What's the month-one allocation call?

**[R4] compliance_lawyer** [speech]: Supply chain—when F-Series Tier-2 hits Mexico in weeks 4–12, who's *certifying* the re-qual to CBP? Are we filing a certification amendment upfront, or documenting the transition retrospectively and hoping CBP accepts "domestic-only during transition" as the audit defense? Because that changes whether the audit trigger fires on *intent-to-defraud* or just *procedural gap*.

**[R4] political_risk_insurer** [speech]: Compliance—when F-Series files the certification amendment for the Mexico transition in weeks 4–12, does CBP's approval letter lock the origin status of goods shipped *before* the amendment, or does a 2026 USMCA rule change let them retroactively challenge shipments we certified as compliant today? That's the difference between a $200K audit cost and a $2–5M clawback exposure—and it's the piece that operationalizes the prospective political risk.

**[R4] trade_credit_underwriter** [speech]: CFO—before we lock the map: if F-Series Tier-2 supplier goes insolvent in week 6 while we're mid-qual to Mexico, do we have lien security on the $840K tooling we just funded, or is that capex a straight loss? Because that determines whether my receivables exposure stays at $2–5M or balloons to $3–8M—and whether we need a separate tooling-recovery reserve in the month-one budget.

**[R4] cfo_erm** [speech]: Before we lock this map: on the $2M month-one tooling spend—do we have first lien on the equipment, or is that capex unsecured? Because if a supplier goes insolvent in week 6, I need to know if we're recovering $1–1.5M of that spend or eating the full loss. That changes whether we need a separate reserve or whether the trade-credit trigger holds.

> _GM ⟶ supply_chain_consultant (PROPOSAL, denied)_: Denied—this contingency reserve is already embedded in the political_risk_exposure variable the team has been operationalizing. The CFO and insurer need the *lien security answer* and *certification timing* from compliance before allocating reserves, not another reserve line item that duplicates existing risk buckets.  
>   side-effects: —


_— R4 end | political_risk_exposure=37, risk_map_completeness=53, rules_of_origin_burden=36, supplier_relocation_exposure=40, trade_credit_risk=38, underwriting_discipline=58 —_


**[R5] auto_strategy** (pass 1): Compliance—F-Series is funded and moving in month one, but I need the timeline locked: when do we *file* the certification amendment with CBP, and does that lock the origin status retroactively for goods we shipped weeks 1–3 before the amendment cleared? Because if CBP can challenge those early shipments in 2026, that's a separate $1–2M clawback exposure we haven't priced into the map yet.

**[R5] compliance_lawyer** ⚡reply: File the amendment *prospectively*—weeks 2–3, before Mexico transition starts week 4. CBP approval locks origin status *forward* from filing date; shipments weeks 1–3 stay under current sourcing rules, no retroactive challenge exposure. That's the defensible posture and kills the $1–2M clawback risk.

**[R5] supplier** (pass 1): Before we lock the map: do we have first-lien security on all three suppliers' tooling—F-Series $840K, Ranger and Transit $620K combined—or are we walking in unsecured? Because if one supplier goes dark in week 8, I need to know if we're recovering $400–600K or eating the full hit.

**[R5] cfo_erm** ⚡reply: We're taking first lien on all three—$840K F-Series, $620K Ranger/Transit combined. Counsel is filing the security agreements this week, so we're protected if anyone goes dark during qualification. That caps receivables exposure at $2–5M and lets us price trade-credit triggers cleanly.

**[R5] compliance_lawyer** (pass 1): CFO—we're filing the amendment weeks 2–3, but what's the actual *compliance labor and legal cost* to execute that filing? I'm not seeing that line item in the month-one spend. Because if CBP scrutinizes the amendment during audit, we need to show defensible documentation and timeline—and that costs money we haven't budgeted yet.

**[R5] trade_credit_underwriter** (pass 1): CFO—first lien is solid, but here's what I need locked: if F-Series goes dark in week 8, who's actually *enforcing* that lien on the $840K tooling—us, the supplier's lender, or CBP holds it in limbo during the audit? Because that determines whether we recover $600K in 6 weeks or eat a 90-day delay and 20% haircut. What's the enforcement timeline assumption?

**[R5] supply_chain_consultant** (pass 1): Supply chain—you've got F-Series at $840K to Mexico. But what's the *annual* tariff and penalty hit if Ranger and Transit stay domestic through 2026? Because if keeping them here costs $600–800K per year in clawback risk plus labor-content bleed, then funding them both now at $620K total becomes a one-year payback, not a capex gamble. That's the number that closes the map.

**[R5] cfo_erm** (pass 1): Supply chain—give me the annual compliance *bleed* if Ranger and Transit stay domestic through 2026. Tariff clawback, penalty exposure, labor-content gap—total annual cost, not capex. That's what tells me if $620K nearshoring is a one-year payback or a gamble.

**[R5] supply_chain_consultant** ⚡reply: Ranger and Transit staying domestic through 2026 runs $520–680K annually in tariff exposure plus $180–220K in penalty clawback risk if CBP challenges labor content—that's $700–900K annual bleed. Against $620K capex month-one, you're looking at a 9–13 month payback, and that's *before* the 2026 retroactive rule-change risk hits. Fund both relocations now.

**[R5] auto_strategy** [speech]: Compliance—F-Series is funded and moving in month one, but I need the timeline locked: when do we *file* the certification amendment with CBP, and does that lock the origin status retroactively for goods we shipped weeks 1–3 before the amendment cleared? Because if CBP can challenge those early shipments in 2026, that's a separate $1–2M clawback exposure we haven't priced into the map yet.

**[R5] supplier** [speech]: Before we lock the map: do we have first-lien security on all three suppliers' tooling—F-Series $840K, Ranger and Transit $620K combined—or are we walking in unsecured? Because if one supplier goes dark in week 8, I need to know if we're recovering $400–600K or eating the full hit.

**[R5] compliance_lawyer** [speech]: CFO—we're filing the amendment weeks 2–3, but what's the actual *compliance labor and legal cost* to execute that filing? I'm not seeing that line item in the month-one spend. Because if CBP scrutinizes the amendment during audit, we need to show defensible documentation and timeline—and that costs money we haven't budgeted yet.

**[R5] trade_credit_underwriter** [speech]: CFO—first lien is solid, but here's what I need locked: if F-Series goes dark in week 8, who's actually *enforcing* that lien on the $840K tooling—us, the supplier's lender, or CBP holds it in limbo during the audit? Because that determines whether we recover $600K in 6 weeks or eat a 90-day delay and 20% haircut. What's the enforcement timeline assumption?

**[R5] supply_chain_consultant** [speech]: Supply chain—you've got F-Series at $840K to Mexico. But what's the *annual* tariff and penalty hit if Ranger and Transit stay domestic through 2026? Because if keeping them here costs $600–800K per year in clawback risk plus labor-content bleed, then funding them both now at $620K total becomes a one-year payback, not a capex gamble. That's the number that closes the map.

**[R5] cfo_erm** [speech]: Supply chain—give me the annual compliance *bleed* if Ranger and Transit stay domestic through 2026. Tariff clawback, penalty exposure, labor-content gap—total annual cost, not capex. That's what tells me if $620K nearshoring is a one-year payback or a gamble.

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Political-risk insurer's 2026 USMCA review exposure quantification ($2-5M clawback, 120-150 bps on capex) closes a critical prospective risk bucket. The cross-functional challenge from auto strategy, supplier, compliance lawyer, trade credit underwriter, supply chain consultant, and CFO forces operationalization of timeline assumptions, security positions, enforcement mechanics, and annual bleed costs—transforming vague labels into concrete underwriting factors and decision triggers. This completes the Policy-to-Supply-Chain Risk Map.  
>   side-effects: political_risk_exposure:+5.0; risk_map_completeness:+5.0; underwriting_discipline:+5.0; rules_of_origin_burden:+3.0; risk_map_completeness:+1; risk_map_completeness:+1


_— R5 end [TERMINATED] | political_risk_exposure=43, risk_map_completeness=69, rules_of_origin_burden=41, supplier_relocation_exposure=40, trade_credit_risk=38, underwriting_discipline=63 —_

