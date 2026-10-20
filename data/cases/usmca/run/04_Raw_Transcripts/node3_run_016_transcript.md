# node3_run_016


## ▶ Stage 0: translate_exposures (0 facts injected)


**[R1] auto_strategy** (pass 1): Here's what I need: which three supplier categories hit the wage-floor threshold first, and what's the insolvency window if we force nearshoring without buydown? Right now we're saying "labor-content risk exists" — I need the 90-day cost to ramp compliance at each plant.

**[R1] supplier** (pass 1): Electronics and wiring harness suppliers hit the floor first — they're lowest-margin, tightest lead times. Stamped-metal comes second. If we force nearshoring without subsidy, you're looking at 60–90 days before the smaller Tier 2 shops start defaulting on tooling capex. I can map the cost-to-ramp per plant, but I need you to tell me: are we pricing subsidy buydown, or are we pricing supplier churn as the baseline scenario?

**[R1] auto_strategy** ⚡reply: We price supplier churn as baseline — that's the compliance cost we own. But I need the 90-day ramp cost per plant *and* the insolvency trigger points by supplier tier so I can model which models go non-compliant first. Give me the numbers, and I'll tell you where we need to negotiate buydown versus absorb the hit.

**[R1] compliance_lawyer** (pass 1): When you model which models go non-compliant first — are you assuming CBP initiates verification audits on the nearshored suppliers immediately, or is there a grace window? Because if we're absorbing supplier churn as baseline, I need to know if we're *also* absorbing audit penalties on the borderline-compliant units that ship in that ramp window.

**[R1] political_risk_insurer** (pass 1): Okay, so here's what I need to price this: what's CBP's *actual* enforcement posture on nearshored Tier 2 shops in the first 90 days — are we looking at spot audits, or is there a documented grace period? Because if there's no grace, I'm adding audit-penalty exposure as a *separate* line item, and that changes what we can insure versus what auto_strategy absorbs as cost-of-business.

**[R1] compliance_lawyer** ⚡reply: CBP has no published grace period — they audit on risk profile, not calendar. If a nearshored supplier shows low labor-content documentation or inconsistent recordkeeping, verification can trigger within 30 days of first shipment. So you're pricing audit-penalty exposure as *separate* from supplier-churn cost: non-compliant units in that ramp window face duty assessments plus potential 20% penalties on the entered value, *and* we need certified labor-cost data from day one or we're exposing every SKU.

**[R1] trade_credit_underwriter** (pass 1): When you absorb supplier churn as baseline cost, are you also absorbing the receivables hit — meaning we're holding inventory risk on units from suppliers who go insolvent mid-ramp, or are we pre-paying those tiers to lock in cash flow? Because if it's the former, that's a trade-credit variable I need to price separately.

**[R1] supplier** [speech]: Electronics and wiring harness suppliers hit the floor first — they're lowest-margin, tightest lead times. Stamped-metal comes second. If we force nearshoring without subsidy, you're looking at 60–90 days before the smaller Tier 2 shops start defaulting on tooling capex. I can map the cost-to-ramp per plant, but I need you to tell me: are we pricing subsidy buydown, or are we pricing supplier churn as the baseline scenario?

**[R1] auto_strategy** [speech]: Here's what I need: which three supplier categories hit the wage-floor threshold first, and what's the insolvency window if we force nearshoring without buydown? Right now we're saying "labor-content risk exists" — I need the 90-day cost to ramp compliance at each plant.

**[R1] compliance_lawyer** [speech]: When you model which models go non-compliant first — are you assuming CBP initiates verification audits on the nearshored suppliers immediately, or is there a grace window? Because if we're absorbing supplier churn as baseline, I need to know if we're *also* absorbing audit penalties on the borderline-compliant units that ship in that ramp window.

**[R1] political_risk_insurer** [speech]: Okay, so here's what I need to price this: what's CBP's *actual* enforcement posture on nearshored Tier 2 shops in the first 90 days — are we looking at spot audits, or is there a documented grace period? Because if there's no grace, I'm adding audit-penalty exposure as a *separate* line item, and that changes what we can insure versus what auto_strategy absorbs as cost-of-business.

**[R1] trade_credit_underwriter** [speech]: When you absorb supplier churn as baseline cost, are you also absorbing the receivables hit — meaning we're holding inventory risk on units from suppliers who go insolvent mid-ramp, or are we pre-paying those tiers to lock in cash flow? Because if it's the former, that's a trade-credit variable I need to price separately.

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Pre-positioning plan approved; capex classification deferred to CFO-strategy alignment.  
>   side-effects: risk_map_completeness:+4.0; underwriting_discipline:+3.0; trade_credit_risk:-2.0; supplier_relocation_exposure:+2.0

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: CFO frames binary choice; awaits auto-strategy decision to consolidate risk map.  
>   side-effects: risk_map_completeness:+3.0; underwriting_discipline:+4.0; political_risk_exposure:+1.0; risk_map_completeness:+1


_— R1 end | political_risk_exposure=27, risk_map_completeness=27, rules_of_origin_burden=32, supplier_relocation_exposure=27, trade_credit_risk=23, underwriting_discipline=37 —_


**[R2] supplier** ⚡reply: I can build the matrix right now — electronics and harness hit wage-floor first, 60–90 days before Tier 2 defaults if we force nearshoring without subsidy; stamped-metal follows. But I need CFO to commit: are we pre-paying those tiers to lock cash flow, or are we absorbing receivables risk on inventory from suppliers who go insolvent mid-ramp? That answer changes the matrix rows.

**[R2] supplier** (pass 1): CFO, I hear the binary—pre-pay or churn. But which one are you modeling for capex this round? Because if pre-pay, I need the bucket locked *now* so I can cost the 90-day ramp per plant and show you the supplier survival numbers. If churn, I'm holding inventory from three tiers that go insolvent in 60–90 days—that's a receivables line item I can't price until you confirm we're absorbing it.

**[R2] cfo_erm** ⚡reply: We pre-pay the three highest-risk tiers—electronics, harness, stamped-metal—capex bucket locked now. That's my call. Build the matrix with 90-day ramp costs per plant and the insolvency trigger for each tier if subsidy fails; I'll reconcile the audit-penalty exposure separately once we know CBP's enforcement posture on the nearshore window.

**[R2] compliance_lawyer** (pass 1): CFO, when you reconcile audit-penalty exposure—are we assuming CBP targets the certification gaps on nearshored intake, or labor-content documentation failures during the 90-day ramp? Because those hit different penalty brackets, and if the pre-pay covers tooling but not certification remediation, that's a separate line-item cost I need to isolate for the matrix.

**[R2] political_risk_insurer** (pass 1): Compliance, I need specifics: what's CBP's documented penalty bracket for certification gaps on nearshored intake versus labor-content shortfalls during the ramp window? Because if those penalties hit different thresholds, that's two separate political-risk lines I'm pricing — one at intake, one at audit. And if pre-pay doesn't cover remediation, that gap becomes *my* insurable layer. Give me the numbers now.

**[R2] compliance_lawyer** ⚡reply: CBP's intake certification gaps run 5–15% of landed value as civil penalties, auditable within 30 days of entry; labor-content shortfalls during ramp hit 20–25% if documented non-compliance is found post-audit, typically triggered 60–120 days in. Pre-pay covers nearshore tooling capex, not certification remediation—that's a separate $200–400K per supplier tier exposure I'm flagging as uninsurable under standard trade-credit policies, so the matrix needs a standalone "compliance remediation reserve" line.

**[R2] trade_credit_underwriter** (pass 1): CFO, when does pre-pay settle relative to shipment — are we funding before PO commitment, or after goods leave the nearshore plant? Because if there's a window where inventory ships but cash hasn't cleared, I'm holding a receivables position on suppliers who default mid-ramp, and that changes what I price as baseline supplier-default cost versus what becomes an insurable layer.

**[R2] supply_chain_consultant** (pass 1): CFO, quick clarification before we hand this off to auto_strategy: when you pre-pay those three tiers, does cash clear *before* PO commitment, or after goods physically ship from the nearshore plant? Because if it's the latter, we're still holding inventory receivables during the 60–90 day ramp window—and that changes whether supplier churn is our baseline or trade-credit's problem.

**[R2] cfo_erm** (pass 1): Supply chain, I need one hard answer: does pre-pay settle *before* we commit the PO, or after goods physically leave the nearshore plant? That gap—if it exists—is where receivables risk lives, and it changes whether this is a capex play or we're still absorbing trade-credit exposure on a supplier that goes insolvent mid-ramp. Give me the timeline.

**[R2] supply_chain_consultant** ⚡reply: Pre-pay settles *before* PO commitment—cash clears to the nearshore plant within 5 days of capex bucket release, tooling starts immediately, first units ship 45–60 days in. That locks cash flow and kills the receivables window you're worried about.

**[R2] supplier** [speech]: CFO, I hear the binary—pre-pay or churn. But which one are you modeling for capex this round? Because if pre-pay, I need the bucket locked *now* so I can cost the 90-day ramp per plant and show you the supplier survival numbers. If churn, I'm holding inventory from three tiers that go insolvent in 60–90 days—that's a receivables line item I can't price until you confirm we're absorbing it.

**[R2] compliance_lawyer** [speech]: CFO, when you reconcile audit-penalty exposure—are we assuming CBP targets the certification gaps on nearshored intake, or labor-content documentation failures during the 90-day ramp? Because those hit different penalty brackets, and if the pre-pay covers tooling but not certification remediation, that's a separate line-item cost I need to isolate for the matrix.

**[R2] political_risk_insurer** [speech]: Compliance, I need specifics: what's CBP's documented penalty bracket for certification gaps on nearshored intake versus labor-content shortfalls during the ramp window? Because if those penalties hit different thresholds, that's two separate political-risk lines I'm pricing — one at intake, one at audit. And if pre-pay doesn't cover remediation, that gap becomes *my* insurable layer. Give me the numbers now.

**[R2] trade_credit_underwriter** [speech]: CFO, when does pre-pay settle relative to shipment — are we funding before PO commitment, or after goods leave the nearshore plant? Because if there's a window where inventory ships but cash hasn't cleared, I'm holding a receivables position on suppliers who default mid-ramp, and that changes what I price as baseline supplier-default cost versus what becomes an insurable layer.

**[R2] supply_chain_consultant** [speech]: CFO, quick clarification before we hand this off to auto_strategy: when you pre-pay those three tiers, does cash clear *before* PO commitment, or after goods physically ship from the nearshore plant? Because if it's the latter, we're still holding inventory receivables during the 60–90 day ramp window—and that changes whether supplier churn is our baseline or trade-credit's problem.

**[R2] cfo_erm** [speech]: Supply chain, I need one hard answer: does pre-pay settle *before* we commit the PO, or after goods physically leave the nearshore plant? That gap—if it exists—is where receivables risk lives, and it changes whether this is a capex play or we're still absorbing trade-credit exposure on a supplier that goes insolvent mid-ramp. Give me the timeline.

> _GM ⟶ auto_strategy (PROPOSAL, denied)_: The proposal is denied—not because it's invalid, but because it's a request for information, not an executable action. Auto_strategy is asking supply_chain to build a matrix, but supply_chain has already kicked the decision back to CFO (pre-pay timing). This creates a circular dependency with no present-tense action to rule on.  
>   side-effects: —


_— R2 end | political_risk_exposure=28, risk_map_completeness=27, rules_of_origin_burden=34, supplier_relocation_exposure=27, trade_credit_risk=23, underwriting_discipline=37 —_


**[R3] compliance_lawyer** ⚡reply: Electronics and harness plants hit 20–25% penalty exposure first because they're lowest-margin—if labor docs slip during ramp, you're looking at $2.8–$3.4M in CBP civil penalties across those two tiers against the pre-pay capex bucket. That penalty bracket only clears if we lock certification protocols *before* PO commitment, not after goods leave the nearshore plant—so we need the audit timeline from CBP intake forward, today, or that penalty risk stays unpriced in your matrix.

**[R3] supplier** (pass 1): Compliance, I need the CBP audit timeline from nearshore intake forward — when does verification actually kick off on these Tier 2 shops, and does locking labor-doc certifications 5 days *before* PO commitment get us ahead of that window? Because if audits hit in 30 days and we're still building docs, my suppliers are dead weight. Give me the sequence.

**[R3] compliance_lawyer** (pass 1): Supplier, here's the real question: if we lock labor-content certifications 5 days *before* PO commitment, does CBP verification on nearshore intake start from that locked date, or from shipment? Because that gap—certification date versus audit start—is where compliance either holds or collapses. I need the sequence.

**[R3] supplier** ⚡reply: CBP verification starts from *shipment date*, not certification lock—that's the audit window we're up against. So if you lock docs 5 days before PO but goods don't ship for 45 days, you've bought zero audit buffer; verification kicks off when those nearshored units hit the border, and if labor docs have drifted in production, penalties hit the full bracket. Lock the certification *and* the production schedule together, or the 5-day cushion evaporates.

**[R3] trade_credit_underwriter** (pass 1): Compliance, skip the audit timeline for a second—I need to know: if labor docs lock 5 days before PO but production specs *don't* lock until 30 days in, and a nearshore Tier 2 shop cuts corners on wage compliance to hit the ramp, do *they* default on tooling payback before CBP even audits? That's the receivables hit pre-pay doesn't cover. What's your read on supplier survival if we lock docs but *not* production discipline?

**[R3] supplier** [speech]: Compliance, I need the CBP audit timeline from nearshore intake forward — when does verification actually kick off on these Tier 2 shops, and does locking labor-doc certifications 5 days *before* PO commitment get us ahead of that window? Because if audits hit in 30 days and we're still building docs, my suppliers are dead weight. Give me the sequence.

**[R3] compliance_lawyer** [speech]: Supplier, here's the real question: if we lock labor-content certifications 5 days *before* PO commitment, does CBP verification on nearshore intake start from that locked date, or from shipment? Because that gap—certification date versus audit start—is where compliance either holds or collapses. I need the sequence.

**[R3] trade_credit_underwriter** [speech]: Compliance, skip the audit timeline for a second—I need to know: if labor docs lock 5 days before PO but production specs *don't* lock until 30 days in, and a nearshore Tier 2 shop cuts corners on wage compliance to hit the ramp, do *they* default on tooling payback before CBP even audits? That's the receivables hit pre-pay doesn't cover. What's your read on supplier survival if we lock docs but *not* production discipline?

> _GM ⟶ auto_strategy (PROPOSAL, approved)_: Strategy lead demands CBP penalty matrix with plant-level ramp thresholds—critical for compliance planning.  
>   side-effects: rules_of_origin_burden:+4.0; risk_map_completeness:+3; underwriting_discipline:+3; trade_credit_risk:+2.0; risk_map_completeness:+1

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Insurer defines 90-day CBP audit window from shipment—creates insurable gap if production schedules lock.  
>   side-effects: political_risk_exposure:+3.0; underwriting_discipline:+3; risk_map_completeness:+2

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Consultant proposes three-lock matrix: labor docs, production schedule, 90-day ramp budget—kills audit drift.  
>   side-effects: risk_map_completeness:+4; underwriting_discipline:+3; supplier_relocation_exposure:+3.0; trade_credit_risk:-2.0

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: CFO locks penalty exposure matrix with supplier-survival thresholds—pre-pay covers tooling, not remediation.  
>   side-effects: risk_map_completeness:+4; underwriting_discipline:+4; political_risk_exposure:+2.0; trade_credit_risk:-3.0; rules_of_origin_burden:+3.0; risk_map_completeness:+1


_— R3 end | political_risk_exposure=34, risk_map_completeness=41, rules_of_origin_burden=43, supplier_relocation_exposure=30, trade_credit_risk=20, underwriting_discipline=50 —_



## ▶ Stage 1: operationalize_and_consolidate (1 facts injected)


**[R4] auto_strategy** (pass 1): Supply chain, I've got the penalty numbers and the lock timeline, but I need the plant execution sequence mapped: which models ship first in that 45–60 day window, and if CBP spots a labor-doc gap on the first batch, does that hold the whole line or just that model? That's where the compliance cost either stays theoretical or becomes a production crisis.

**[R4] supply_chain_consultant** ⚡reply: Electronics and harness hit the line first—days 45–52—lowest margin, highest audit risk. If CBP flags labor docs on that first batch, it's a model-level hold, not a full stoppage, but here's the real problem: those two plants survive the penalty hit only if we've pre-paid their tooling before PO commitment. After that window closes, we're absorbing supplier churn as baseline cost, and I need your call on whether we're also holding inventory receivables during the ramp or if pre-pay clears *before* those units ship.

**[R4] supplier** (pass 1): Auto, you've got the penalty matrix locked—good. But pre-pay only covers electronics, harness, and stamped-metal. What's your plan for the Tier 2 and Tier 3 shops that don't make the pre-pay cut? Are they expected to absorb the wage-floor hit on their own capex, or are we assuming they relocate into Mexico? Because if it's the latter, that's a *supplier relocation exposure* number I need to quantify for the risk map, not a compliance variable.

**[R4] auto_strategy** ⚡reply: The Tier 2 and 3 shops that miss pre-pay are absorbing the wage-floor hit themselves or relocating—that's their survival call, not ours to subsidize. But here's what I need locked right now: if pre-pay settles *before* PO commitment, we kill receivables risk on those three plants and I can model supplier survival. If it settles *after* shipment, we're holding 60–90 days of inventory on units from suppliers who go insolvent mid-ramp, and that's a separate trade-credit line I price at cost-of-capital plus default premium. Which one are we running?

**[R4] compliance_lawyer** (pass 1): Auto, pre-pay before PO—that's clean on receivables. But on your Tier 2 and 3 call: are we pricing relocation as "they fund their own wage-floor compliance" or "they exit the US supply chain"? Because if it's relocation, that's a nearshoring concentration risk I need to isolate in the map—different CBP posture, different penalty brackets. Which scenario do you want me to model for political risk?

**[R4] political_risk_insurer** (pass 1): Compliance, one hard clarification: when CBP audits a nearshored Tier 2 plant in that first 90 days post-shipment, do they lead with intake certification completeness or go straight to labor-content documentation during the ramp? Because those are different penalty brackets and different risk profiles for me to price—I need to know which one actually moves the needle for CBP's enforcement strategy on nearshoring.

**[R4] compliance_lawyer** ⚡reply: CBP leads with intake certification—that's the gate. If labor docs are incomplete at intake, the shipment gets flagged before it even clears the port; if docs are clean at intake but labor content fails during the 90-day window, that's a separate audit trigger and a lower-priority penalty bracket. The first one kills your timeline; the second one is remediation-adjacent and insurable. You're pricing two different risk layers.

**[R4] trade_credit_underwriter** (pass 1): Auto, on your Tier 2 and 3 call — if those shops relocate into Mexico, are we replacing them with new nearshore suppliers we've already vetted, or are we eating the supply gap and absorbing their default as cost-of-business? Because if it's replacement, that's a whole new receivables base I need to price, and I need to know their margin and lead-time profile *now* before we model them into the ramp.

**[R4] supply_chain_consultant** (pass 1): Auto, you said Tier 2 and 3 absorb the hit or relocate — but do we have intel on which shops are actually choosing relocation versus staying and tightening margins? Because if half of them are moving production south, that's a different nearshoring footprint and a different CBP posture I need to price. What's your baseline assumption there?

**[R4] auto_strategy** [speech]: Supply chain, I've got the penalty numbers and the lock timeline, but I need the plant execution sequence mapped: which models ship first in that 45–60 day window, and if CBP spots a labor-doc gap on the first batch, does that hold the whole line or just that model? That's where the compliance cost either stays theoretical or becomes a production crisis.

**[R4] supplier** [speech]: Auto, you've got the penalty matrix locked—good. But pre-pay only covers electronics, harness, and stamped-metal. What's your plan for the Tier 2 and Tier 3 shops that don't make the pre-pay cut? Are they expected to absorb the wage-floor hit on their own capex, or are we assuming they relocate into Mexico? Because if it's the latter, that's a *supplier relocation exposure* number I need to quantify for the risk map, not a compliance variable.

**[R4] compliance_lawyer** [speech]: Auto, pre-pay before PO—that's clean on receivables. But on your Tier 2 and 3 call: are we pricing relocation as "they fund their own wage-floor compliance" or "they exit the US supply chain"? Because if it's relocation, that's a nearshoring concentration risk I need to isolate in the map—different CBP posture, different penalty brackets. Which scenario do you want me to model for political risk?

**[R4] political_risk_insurer** [speech]: Compliance, one hard clarification: when CBP audits a nearshored Tier 2 plant in that first 90 days post-shipment, do they lead with intake certification completeness or go straight to labor-content documentation during the ramp? Because those are different penalty brackets and different risk profiles for me to price—I need to know which one actually moves the needle for CBP's enforcement strategy on nearshoring.

**[R4] trade_credit_underwriter** [speech]: Auto, on your Tier 2 and 3 call — if those shops relocate into Mexico, are we replacing them with new nearshore suppliers we've already vetted, or are we eating the supply gap and absorbing their default as cost-of-business? Because if it's replacement, that's a whole new receivables base I need to price, and I need to know their margin and lead-time profile *now* before we model them into the ramp.

**[R4] supply_chain_consultant** [speech]: Auto, you said Tier 2 and 3 absorb the hit or relocate — but do we have intel on which shops are actually choosing relocation versus staying and tightening margins? Because if half of them are moving production south, that's a different nearshoring footprint and a different CBP posture I need to price. What's your baseline assumption there?

> _GM ⟶ cfo_erm (PROPOSAL, denied)_: The CFO's demand for a single baseline assumption on Tier 2/3 supplier location is premature — five other specialists have just surfaced that this binary (domestic vs. nearshore) splits into multiple distinct risk profiles that each require separate modeling. Forcing a single number now would collapse critical distinctions the team needs to price accurately.  
>   side-effects: —


_— R4 end | political_risk_exposure=34, risk_map_completeness=41, rules_of_origin_burden=43, supplier_relocation_exposure=30, trade_credit_risk=20, underwriting_discipline=50 —_


**[R5] auto_strategy** (pass 1): Supply chain, forget the binary for a second—give me real data: of the Tier 2/3 shops we pre-qualify, how many have already signaled Mexico relocation, how many are self-funding wage-floor capex, and what's the timeline on both? Because that's the *actual* relocation exposure I need to price into the map.

**[R5] supply_chain_consultant** ⚡reply: We don't have that baseline intel yet—that's the gap blocking the risk map. I'm pulling relocation signals from our Tier 2/3 pre-qual cohort *this week*, but I need auto_strategy and CFO to decide *now* whether we're modeling relocation as a nearshoring opportunity we fund, or a supplier-churn scenario they self-fund. Which one do you want me to cost out first?

**[R5] political_risk_insurer** ⚡reply: I need both scenarios priced by Friday—but Scenario B (they relocate, we absorb the gap) is my baseline for political-risk scoring, because that's where the nearshoring footprint shifts and CBP's enforcement posture changes. Run A second, but flag every supplier in your cohort that's already signaled Mexico movement; that's my insurable exposure right there.

**[R5] compliance_lawyer** (pass 1): Supply chain, skip the scenario modeling for now — focus on this: of your pre-qual cohort, which shops have *already locked* Mexico relocation timelines, and when do their first nearshore units clear the port? Because that's when CBP intake audits start, and I need to know if we're absorbing one batch or a flood.

**[R5] political_risk_insurer** (pass 1): Supply chain, skip the full cohort analysis—give me three hard numbers right now: how many Tier 2/3 shops have *already signaled* Mexico movement, when do their first units ship nearshore, and what's the intake certification gap if we're absorbing supply churn? That's my baseline for pricing Scenario B.

**[R5] trade_credit_underwriter** (pass 1): Supply chain, cut to it: of your pre-qual Tier 2/3 cohort, how many have *already signaled* Mexico movement, and what's their current margin on nearshore-comparable tooling? Because if it's more than 20–30%, I can price them as default risk and lock that into the receivables base. If it's lower, they're staying domestic and absorbing wage pressure—different underwriting profile entirely. Give me the number now, not the scenario.

**[R5] auto_strategy** [speech]: Supply chain, forget the binary for a second—give me real data: of the Tier 2/3 shops we pre-qualify, how many have already signaled Mexico relocation, how many are self-funding wage-floor capex, and what's the timeline on both? Because that's the *actual* relocation exposure I need to price into the map.

**[R5] compliance_lawyer** [speech]: Supply chain, skip the scenario modeling for now — focus on this: of your pre-qual cohort, which shops have *already locked* Mexico relocation timelines, and when do their first nearshore units clear the port? Because that's when CBP intake audits start, and I need to know if we're absorbing one batch or a flood.

**[R5] political_risk_insurer** [speech]: Supply chain, skip the full cohort analysis—give me three hard numbers right now: how many Tier 2/3 shops have *already signaled* Mexico movement, when do their first units ship nearshore, and what's the intake certification gap if we're absorbing supply churn? That's my baseline for pricing Scenario B.

**[R5] trade_credit_underwriter** [speech]: Supply chain, cut to it: of your pre-qual Tier 2/3 cohort, how many have *already signaled* Mexico movement, and what's their current margin on nearshore-comparable tooling? Because if it's more than 20–30%, I can price them as default risk and lock that into the receivables base. If it's lower, they're staying domestic and absorbing wage pressure—different underwriting profile entirely. Give me the number now, not the scenario.

> _GM ⟶ supplier (PROPOSAL, approved)_: Supplier commits to dual-path costing framework with Friday pre-qual data deadline.  
>   side-effects: supplier_relocation_exposure:+3.0; risk_map_completeness:+4.0; underwriting_discipline:+2.0; stress:+2.0

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Consultant delivers bifurcated nearshoring model with 2026 USMCA review as forward shock layer.  
>   side-effects: supplier_relocation_exposure:+4.0; political_risk_exposure:+3.0; risk_map_completeness:+5.0; underwriting_discipline:+4.0; stress:+3.0; risk_map_completeness:+1; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, denied)_: Denied: semantically identical to consultant's bifurcated model already approved this round.  
>   side-effects: —


_— R5 end | political_risk_exposure=37, risk_map_completeness=52, rules_of_origin_burden=44, supplier_relocation_exposure=37, trade_credit_risk=20, underwriting_discipline=56 —_


**[R6] supplier** (pass 1): Auto, the 50% trigger makes sense—but that's a repricing call, not a supply call. If half my pre-qual cohort moves south in month two, I've already cut POs based on Scenario A tooling. When do I *know* which shops are actually relocating so I can lock their nearshore intake schedule before the signal count hits 50%?

**[R6] auto_strategy** ⚡reply: We pull the relocation signal data *this week*—I'm running a hard yes/no on each pre-qual shop: are they funding Mexico capex or absorbing wage-floor cost domestically, and when does their first nearshore unit clear the port if they move. That gives you the intake schedule 45 days before the 50% trigger even matters, so your PO lock doesn't get blindsided.

**[R6] compliance_lawyer** (pass 1): Auto, the 50% trigger makes sense for repricing—but here's my read: that signal hit *also* needs to flip our intake certification discipline. If half the cohort moves south by month two, their first units are clearing the port in that same window, and CBP's audit clock starts at shipment, not at signal count. So does the 50% call lock an accelerated certification audit *before* PO, or do we stay on the 45–60 day ramp timeline regardless?

**[R6] compliance_lawyer** ⚡reply: CBP's 90-day audit clock doesn't shift—it starts at shipment regardless of volume—but their *sampling intensity* absolutely spikes when nearshore intake jumps. If 50%+ of your cohort clears the port in a compressed 45-day window, you're looking at mandatory first-article inspection on every batch, not statistical sampling. That's where your $600–800K exposure is real: it's not timeline drift, it's audit depth on a locked schedule. Lock the accelerated pre-PO certification now, or eat the compressed ramp penalty.

**[R6] supplier** ⚡reply: Yes, that locks it—but I need one clarification before I price it: in Scenario B, does the $800K reserve cover *both* nearshore shops eating mandatory first-article inspection *and* domestic stayers defaulting on wage-floor capex, or just one cohort? Because if it's both, I'm pricing dual default risk and the reserve splits—that changes my receivables base and which shops I'm actually covering under pre-pay tooling.

**[R6] supplier** [speech]: Auto, the 50% trigger makes sense—but that's a repricing call, not a supply call. If half my pre-qual cohort moves south in month two, I've already cut POs based on Scenario A tooling. When do I *know* which shops are actually relocating so I can lock their nearshore intake schedule before the signal count hits 50%?

**[R6] compliance_lawyer** [speech]: Auto, the 50% trigger makes sense for repricing—but here's my read: that signal hit *also* needs to flip our intake certification discipline. If half the cohort moves south by month two, their first units are clearing the port in that same window, and CBP's audit clock starts at shipment, not at signal count. So does the 50% call lock an accelerated certification audit *before* PO, or do we stay on the 45–60 day ramp timeline regardless?

> _GM ⟶ auto_strategy (PROPOSAL, approved)_: Scenario A baseline locked with 50% trigger rule for Scenario B flip.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+3; political_risk_exposure:+2.0; stress:-2.0

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Policy shock pricing layer locked into underwriting model.  
>   side-effects: political_risk_exposure:+3.0; underwriting_discipline:+2; stress:-1.0

> _GM ⟶ trade_credit_underwriter (PROPOSAL, approved)_: Relocation-driven supplier insolvency factor defined with dual reserves.  
>   side-effects: trade_credit_risk:+4.0; underwriting_discipline:+3; risk_map_completeness:+3.0; stress:-2.0

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Risk cohorts separated cleanly with Friday confirmation protocol.  
>   side-effects: supplier_relocation_exposure:+3.0; underwriting_discipline:+2; stress:-1.0

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: Automatic trigger locked with Friday data commitment for operational handoff.  
>   side-effects: underwriting_discipline:+3; risk_map_completeness:+4.0; supplier_relocation_exposure:+2.0; stress:-3.0


_— R6 end [TERMINATED] | political_risk_exposure=42, risk_map_completeness=63, rules_of_origin_burden=44, supplier_relocation_exposure=42, trade_credit_risk=24, underwriting_discipline=69 —_

