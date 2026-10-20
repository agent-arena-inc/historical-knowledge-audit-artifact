# node3_run_005


## ▶ Stage 0: translate_exposures (0 facts injected)


**[R1] auto_strategy** (pass 1): When we map a plant that falls short on RVC — say we're 3-4 points below the 75% threshold — what's the cost assumption tied to that in your supplier-relocation exposure number? Are we pricing nearshoring, or just flagging it?

**[R1] supplier** (pass 1): Right — and that's exactly the problem. We're flagging nearshoring, but we're not saying *which tier-2 suppliers in Mexico or Canada can't absorb $2–5M capex in 18 months without going under*. Until we name them and tag the insolvency risk, the map stays soft. Who owns the supplier financial health piece?

**[R1] compliance_lawyer** (pass 1): Who's mapping tier-2 supplier balance sheets against the 18-month capex window? Because if a plant falls 3-4 RVC points short and we're forcing nearshoring, I need to know which suppliers can't fund it — that's not just a relocation flag, that's a certification audit trigger the moment they go under mid-transition.

**[R1] supplier** ⚡reply: Nobody's doing it yet — that's the gap. I need compliance to pull tier-2 balance sheets this week, cross-walk them against the 18-month capex timeline, and flag which suppliers hit insolvency risk *before* we force the nearshoring call. Otherwise we're pricing relocation exposure at 25 when it should be 50-plus once we account for supply-chain collapse.

**[R1] trade_credit_underwriter** (pass 1): Compliance, when you pull those tier-2 sheets, what's your working definition of insolvency for a mid-sized nearshoring supplier — debt-to-EBITDA ratio, working-capital runway, ability to service new capex lines? Because I need to tag which ones can't fund the move and price their default risk as a hard underwriting factor, not a flag.

**[R1] compliance_lawyer** ⚡reply: For nearshoring suppliers, I'm using debt-to-EBITDA >3.5x as the hard insolvency trigger — anything above that can't service new capex lines during a transition. I'll pull tier-2 balance sheets by end of day and cross-walk them against the 18-month timeline; once I flag which suppliers hit that ratio, you can price default risk as a named underwriting factor, not a soft exposure.

**[R1] auto_strategy** [speech]: When we map a plant that falls short on RVC — say we're 3-4 points below the 75% threshold — what's the cost assumption tied to that in your supplier-relocation exposure number? Are we pricing nearshoring, or just flagging it?

**[R1] supplier** [speech]: Right — and that's exactly the problem. We're flagging nearshoring, but we're not saying *which tier-2 suppliers in Mexico or Canada can't absorb $2–5M capex in 18 months without going under*. Until we name them and tag the insolvency risk, the map stays soft. Who owns the supplier financial health piece?

**[R1] compliance_lawyer** [speech]: Who's mapping tier-2 supplier balance sheets against the 18-month capex window? Because if a plant falls 3-4 RVC points short and we're forcing nearshoring, I need to know which suppliers can't fund it — that's not just a relocation flag, that's a certification audit trigger the moment they go under mid-transition.

**[R1] trade_credit_underwriter** [speech]: Compliance, when you pull those tier-2 sheets, what's your working definition of insolvency for a mid-sized nearshoring supplier — debt-to-EBITDA ratio, working-capital runway, ability to service new capex lines? Because I need to tag which ones can't fund the move and price their default risk as a hard underwriting factor, not a flag.

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Insurer defines RVC-audit-failure trigger sequence: 90-day cert hold → credit-line freeze → 60-day insolvency window.  
>   side-effects: political_risk_exposure:+4.0; underwriting_discipline:+4; trade_credit_risk:+3.0; risk_map_completeness:+3.0; rules_of_origin_burden:-2.0; risk_map_completeness:+1

> _GM ⟶ supply_chain_consultant (PROPOSAL, approved)_: Consultant builds three-tier relocation matrix: self-fund / credit-support / co-invest-or-exit, converting exposure into named client actions.  
>   side-effects: supplier_relocation_exposure:+4.0; underwriting_discipline:+5; risk_map_completeness:+4.0; trade_credit_risk:+3.0; risk_map_completeness:+1; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: CFO demands EOD consolidated map: supplier name, insolvency flag, relocation tier, credit need, priced add-ons — assigns synthesis ownership.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+4; political_risk_exposure:+2.0; trade_credit_risk:+2.0; supplier_relocation_exposure:-3.0; risk_map_completeness:+1


_— R1 end | political_risk_exposure=32, risk_map_completeness=35, rules_of_origin_burden=30, supplier_relocation_exposure=26, trade_credit_risk=33, underwriting_discipline=43 —_



## ▶ Stage 1: operationalize_and_consolidate (1 facts injected)


**[R2] auto_strategy** (pass 1): CFO, compliance's pulling those tier-2 sheets by EOD — but do we have a hard list of which plants are actually RVC-short right now? Because I can't cost nearshoring pressure until I know which suppliers are on the hook and how deep their debt is.

**[R2] cfo_erm** ⚡reply: I've got compliance pulling the balance sheets today, but here's the hard truth — we don't have the RVC shortfall mapped against those sheets yet. I need supply chain to cross-walk plant-level RVC scores against the 18-month capex timeline *this week*, then I'm flagging any supplier that can't self-fund the move. That's the only way we price nearshoring as a real underwriting factor instead of a soft exposure.

**[R2] supplier** (pass 1): Compliance, when you pull those tier-2 sheets by EOD, are you cross-walking them against plant-level RVC scores, or is that supply chain's piece? Because right now it sounds like both of you are waiting for the other to connect the dots.

**[R2] compliance_lawyer** ⚡reply: Compliance owns the balance-sheet pull and insolvency flagging by EOD today — I'm defining insolvency as debt-to-EBITDA above 3.5x or working-capital runway under 6 months given the capex load. Supply chain cross-walks those sheets against plant RVC scores this week and tags which suppliers fall short on both fronts; that's the trigger for the audit-failure sequence the insurer flagged.

**[R2] compliance_lawyer** (pass 1): You've got the 90-day cert hold → credit freeze → 60-day insolvency sequence nailed. But what's the actual cost to the supplier when that RVC audit fails — lost revenue during the hold, financing premium on emergency credit, or full working-capital gap? I need a number to price against the relocation capex, or this stays a trigger without teeth.

**[R2] political_risk_insurer** ⚡reply: The cost hits in three places — revenue loss during the 90-day cert hold runs 15–25% of monthly EBITDA for affected SKUs, emergency credit lines jump 300–500 bps over normal rates, and the working-capital gap to fund nearshoring capex balloons by $2–5M depending on plant size. I'm pricing that as a hard underwriting factor: any supplier hitting the audit-failure sequence gets marked uninsurable for trade-credit cover until they've relocated and re-certified, which means their financing costs spike and their nearshoring timeline compresses — that's the leverage point to force the move or trigger default.

**[R2] supplier** ⚡reply: I need the supplier names and RVC scores from supply chain *right now* — compliance's balance sheets alone don't tell me which plants are actually short. Once I have both, I'm mapping the capex load against each supplier's working capital and flagging anyone who can't self-fund; that goes straight into the consolidated map as a priced add-on with the insurer's 400-bps surcharge attached. Supply chain, you own the plant-level RVC cross-walk this week — but I need the preliminary list by end of day tomorrow so CFO can cost it.

**[R2] trade_credit_underwriter** (pass 1): Compliance, when you pull those sheets by EOD today, are you filtering for the RVC-short plants supply chain flagged, or pulling the whole tier-2 universe and letting supply chain sort it tomorrow? Because if it's the latter, I'm pricing blind until Friday. I need the high-leverage + RVC-short overlap *named* by EOD tomorrow so I can lock in the 400-bps rule and cost the map.

**[R2] supply_chain_consultant** (pass 1): CFO, when you slot suppliers into those three tiers tomorrow, are you attaching a relocation timeline to each tier — like tier 2 gets 12 months, tier 3 gets 18+ months? Because if a tier-3 supplier is 60 days from insolvency after the audit hold, we can't actually execute a 24-month nearshoring plan. That gap is a hard cost or an exit call — need to know which one you're pricing.

**[R2] auto_strategy** [speech]: CFO, compliance's pulling those tier-2 sheets by EOD — but do we have a hard list of which plants are actually RVC-short right now? Because I can't cost nearshoring pressure until I know which suppliers are on the hook and how deep their debt is.

**[R2] supplier** [speech]: Compliance, when you pull those tier-2 sheets by EOD, are you cross-walking them against plant-level RVC scores, or is that supply chain's piece? Because right now it sounds like both of you are waiting for the other to connect the dots.

**[R2] compliance_lawyer** [speech]: You've got the 90-day cert hold → credit freeze → 60-day insolvency sequence nailed. But what's the actual cost to the supplier when that RVC audit fails — lost revenue during the hold, financing premium on emergency credit, or full working-capital gap? I need a number to price against the relocation capex, or this stays a trigger without teeth.

**[R2] trade_credit_underwriter** [speech]: Compliance, when you pull those sheets by EOD today, are you filtering for the RVC-short plants supply chain flagged, or pulling the whole tier-2 universe and letting supply chain sort it tomorrow? Because if it's the latter, I'm pricing blind until Friday. I need the high-leverage + RVC-short overlap *named* by EOD tomorrow so I can lock in the 400-bps rule and cost the map.

**[R2] supply_chain_consultant** [speech]: CFO, when you slot suppliers into those three tiers tomorrow, are you attaching a relocation timeline to each tier — like tier 2 gets 12 months, tier 3 gets 18+ months? Because if a tier-3 supplier is 60 days from insolvency after the audit hold, we can't actually execute a 24-month nearshoring plan. That gap is a hard cost or an exit call — need to know which one you're pricing.

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Underwriting rule locked: RVC-short + debt >3.5x triggers credit pull and 400-bps surcharge retroactive to audit date.  
>   side-effects: underwriting_discipline:+5.0; trade_credit_risk:+5.0; risk_map_completeness:+4.0; supplier_relocation_exposure:+3.0; risk_map_completeness:+1; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: Consolidated sheet deadline locked: compliance EOD today, supply chain 6 PM tomorrow, CFO gets full map EOD tomorrow.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+5.0; rules_of_origin_burden:+3.0; trade_credit_risk:+2.0; stress:+4.0; stress:+1.0; risk_map_completeness:+1


_— R2 end | political_risk_exposure=32, risk_map_completeness=45, rules_of_origin_burden=35, supplier_relocation_exposure=29, trade_credit_risk=40, underwriting_discipline=53 —_


**[R3] auto_strategy** (pass 1): CFO, compliance pulls balance sheets EOD today, supply chain has RVC scores by 6 PM tomorrow — but who's doing the actual cross-walk to name which suppliers hit both triggers at the same time? Because if that's a third step happening Friday, I can't model capex costs until I see the full list.

**[R3] cfo_erm** ⚡reply: I'm owning the cross-walk — compliance hands me the sheets EOD today, supply chain feeds me RVC scores by 6 PM tomorrow, and I'm naming the RVC-short + high-leverage overlap by 9 AM Friday so you can price capex against actual insolvency risk, not a flag. That's the blocking dependency for the consolidated map, and it gets locked before close of business Friday.

**[R3] supplier** (pass 1): CFO, when you hand me that overlap list Friday morning — RVC-short plus debt >3.5x — are you flagging just the supplier names, or am I also getting their current capex headroom and the 18-month nearshoring cost estimate attached? Because if I'm hunting for those numbers separately, we lose a day.

**[R3] compliance_lawyer** (pass 1): CFO, when you hand over that RVC-short plus debt >3.5x list Friday morning, are you attaching each supplier's available capex headroom and the 18-month nearshoring cost estimate, or is supply chain pulling those separately? Because if it's the latter, the consolidated map doesn't close until Saturday — and I need it defensible by Friday EOD for the underwriting rule to stick.

**[R3] supplier** ⚡reply: Supply chain owns the nearshoring cost estimates — I'm pulling capex headroom straight from the balance sheets compliance hands me today, so both columns hit your list Friday 9 AM. You want me to lock supply chain into appending their 18-month numbers to my overlap sheet, or do you take that dependency yourself?

**[R3] trade_credit_underwriter** (pass 1): Supply chain — the CFO's Friday list gets capex headroom from compliance's balance sheets. Are you appending your 18-month nearshoring cost estimates to that same list by 9 AM Friday, or do I have to hunt for those separately? Because if they're not on the overlap sheet, I can't price the trade-credit variable — I'm just flagging suppliers without pricing their actual default risk against the relocation cost.

**[R3] supply_chain_consultant** ⚡reply: Yes — supply chain appends the 18-month nearshoring cost estimates to your overlap sheet by 9 AM Friday, same doc, same rows as the names and capex headroom. That's locked. Once you've got all three columns, you price the default-risk variable against relocation capex for each supplier — that's how the map moves from flags to priceable underwriting factors.

**[R3] supply_chain_consultant** (pass 1): CFO, when supply chain locks those 18-month nearshoring cost estimates Friday morning — are those built on the assumption the RVC threshold stays at 75%, or are we pricing in the risk that the 2026 review tightens it to 78–80%? Because if we're relocating tier-2 suppliers today on a 75% baseline and the review hits 80%, we're right back in shortfall in 18 months.

**[R3] cfo_erm** (pass 1): Supply chain — when you lock those 18-month nearshoring cost estimates Friday morning, are you building in a buffer for 2026 RVC tightening, or are we pricing on the assumption the 75% threshold holds? Because if we're not hedging that, I'm pricing a relocation capex that might not even solve the problem 18 months from now. What's the cost delta if we design for 78–80% compliance instead?

**[R3] auto_strategy** [speech]: CFO, compliance pulls balance sheets EOD today, supply chain has RVC scores by 6 PM tomorrow — but who's doing the actual cross-walk to name which suppliers hit both triggers at the same time? Because if that's a third step happening Friday, I can't model capex costs until I see the full list.

**[R3] supplier** [speech]: CFO, when you hand me that overlap list Friday morning — RVC-short plus debt >3.5x — are you flagging just the supplier names, or am I also getting their current capex headroom and the 18-month nearshoring cost estimate attached? Because if I'm hunting for those numbers separately, we lose a day.

**[R3] compliance_lawyer** [speech]: CFO, when you hand over that RVC-short plus debt >3.5x list Friday morning, are you attaching each supplier's available capex headroom and the 18-month nearshoring cost estimate, or is supply chain pulling those separately? Because if it's the latter, the consolidated map doesn't close until Saturday — and I need it defensible by Friday EOD for the underwriting rule to stick.

**[R3] trade_credit_underwriter** [speech]: Supply chain — the CFO's Friday list gets capex headroom from compliance's balance sheets. Are you appending your 18-month nearshoring cost estimates to that same list by 9 AM Friday, or do I have to hunt for those separately? Because if they're not on the overlap sheet, I can't price the trade-credit variable — I'm just flagging suppliers without pricing their actual default risk against the relocation cost.

**[R3] supply_chain_consultant** [speech]: CFO, when supply chain locks those 18-month nearshoring cost estimates Friday morning — are those built on the assumption the RVC threshold stays at 75%, or are we pricing in the risk that the 2026 review tightens it to 78–80%? Because if we're relocating tier-2 suppliers today on a 75% baseline and the review hits 80%, we're right back in shortfall in 18 months.

**[R3] cfo_erm** [speech]: Supply chain — when you lock those 18-month nearshoring cost estimates Friday morning, are you building in a buffer for 2026 RVC tightening, or are we pricing on the assumption the 75% threshold holds? Because if we're not hedging that, I'm pricing a relocation capex that might not even solve the problem 18 months from now. What's the cost delta if we design for 78–80% compliance instead?

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: The CFO commits to delivering a single consolidated overlap list Friday morning with three columns: supplier name, current capex headroom (from compliance balance sheets), and 18-month nearshoring cost estimates (from supply chain). Supply chain agrees to append nearshoring costs built on 75% RVC baseline with a documented sensitivity range for 78-80% tightening scenarios.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+4.0; supplier_relocation_exposure:+2.0; political_risk_exposure:+1.0; risk_map_completeness:+1


_— R3 end | political_risk_exposure=33, risk_map_completeness=51, rules_of_origin_burden=37, supplier_relocation_exposure=31, trade_credit_risk=40, underwriting_discipline=57 —_


**[R4] auto_strategy** (pass 1): Supply chain, when you lock those nearshoring estimates Friday — what's the cost delta if we design for 78–80% RVC instead of 75%? Because if tier-2 suppliers are relocating on a baseline that tightens in 18 months, we're pricing relocation capex that doesn't stick. I need that sensitivity range to know which plants are actually recoverable.

**[R4] supply_chain_consultant** ⚡reply: The 78–80% RVC tightening adds 12–18% to nearshoring capex per plant — that's the delta I'm building into Friday's list, tiered by supplier debt capacity. Tier 1 self-funds the uplift; tier 2 needs credit support to absorb it; tier 3 hits the co-invest-or-exit threshold. I'm attaching that sensitivity to the consolidated map so you price the relocation cost *and* the 2026 review risk as one underwriting variable, not two separate bets.

**[R4] supplier** (pass 1): CFO, on that tier-3 co-invest-or-exit bucket—when you hand me the names Friday, are you flagging which ones we're actually trying to keep vs. which are exit candidates? Because I can't build relocation timelines or start re-qualification for replacement suppliers until I know which ones you're betting on.

**[R4] cfo_erm** ⚡reply: Tier-3 flagging goes on the Friday sheet—I'm marking each one with a "keep/exit" call based on whether their capex headroom covers the 78–80% uplift plus 18-month relocation timeline. If they can't fund it and we're not co-investing, that's an exit candidate; you start replacement qualification immediately. I'll have the names and the funding gap dollar amount so you know exactly what you're pricing into the relocation plan.

**[R4] compliance_lawyer** (pass 1): Before Friday's list lands, I need compliance to flag which tier-2 suppliers have active RVC audits in flight right now—audit start date, expected completion. Because if we're applying the 400-bps surcharge retroactive to the audit date and a supplier's already 60 days into a review, that's a different cost than pricing it forward from Friday. What's the audit-status snapshot on the RVC-short list?

**[R4] trade_credit_underwriter** (pass 1): CFO, on that Friday list—when you flag tier-2 suppliers as RVC-short plus leveraged, are you also showing me their working-capital runway *given the audit hold revenue loss*? Because I'm pricing default risk during the 90-day hold, not 18 months out. If a supplier's got 4 months of runway and we're holding certification for 90 days, that's a 60-day insolvency window I need to quantify per supplier, not just flag as risk.

**[R4] supply_chain_consultant** (pass 1): CFO, on that Friday sheet — when you're flagging tier-3 co-invest-or-exit, are you also calculating days-to-insolvency *from the audit-hold start date*, not from today? Because if a supplier's got 90 days of runway and the cert hold eats 60 days of revenue, we're executing relocation on a 30-day clock, not 18 months. That changes which ones we're actually keeping.

**[R4] auto_strategy** [speech]: Supply chain, when you lock those nearshoring estimates Friday — what's the cost delta if we design for 78–80% RVC instead of 75%? Because if tier-2 suppliers are relocating on a baseline that tightens in 18 months, we're pricing relocation capex that doesn't stick. I need that sensitivity range to know which plants are actually recoverable.

**[R4] supplier** [speech]: CFO, on that tier-3 co-invest-or-exit bucket—when you hand me the names Friday, are you flagging which ones we're actually trying to keep vs. which are exit candidates? Because I can't build relocation timelines or start re-qualification for replacement suppliers until I know which ones you're betting on.

**[R4] compliance_lawyer** [speech]: Before Friday's list lands, I need compliance to flag which tier-2 suppliers have active RVC audits in flight right now—audit start date, expected completion. Because if we're applying the 400-bps surcharge retroactive to the audit date and a supplier's already 60 days into a review, that's a different cost than pricing it forward from Friday. What's the audit-status snapshot on the RVC-short list?

**[R4] trade_credit_underwriter** [speech]: CFO, on that Friday list—when you flag tier-2 suppliers as RVC-short plus leveraged, are you also showing me their working-capital runway *given the audit hold revenue loss*? Because I'm pricing default risk during the 90-day hold, not 18 months out. If a supplier's got 4 months of runway and we're holding certification for 90 days, that's a 60-day insolvency window I need to quantify per supplier, not just flag as risk.

**[R4] supply_chain_consultant** [speech]: CFO, on that Friday sheet — when you're flagging tier-3 co-invest-or-exit, are you also calculating days-to-insolvency *from the audit-hold start date*, not from today? Because if a supplier's got 90 days of runway and the cert hold eats 60 days of revenue, we're executing relocation on a 30-day clock, not 18 months. That changes which ones we're actually keeping.

> _GM ⟶ political_risk_insurer (PROPOSAL, approved)_: Insurer embeds 2026 review probability scoring into Friday's risk map with retroactive surcharge trigger.  
>   side-effects: political_risk_exposure:+4.0; underwriting_discipline:+5.0; risk_map_completeness:+5.0; trade_credit_risk:+3.0; risk_map_completeness:+1

> _GM ⟶ cfo_erm (PROPOSAL, denied)_: Denied: days-to-insolvency column already covered by political_risk_insurer's proposal 1 this round.  
>   side-effects: —


_— R4 end | political_risk_exposure=37, risk_map_completeness=56, rules_of_origin_burden=39, supplier_relocation_exposure=31, trade_credit_risk=43, underwriting_discipline=62 —_


**[R5] auto_strategy** (pass 1): Compliance, on Friday's sheet you're flagging RVC-short suppliers and their relocation cost — but what's the actual *compliance spend* to bring each plant to 75% RVC in-house, before we even talk nearshoring? Because if a plant's 4 points short and it costs $8M to reshore the inputs versus $3M to relocate the supplier, that changes the whole tier-1/tier-2 split.

**[R5] compliance_lawyer** ⚡reply: We're pulling balance-sheet capex headroom EOD today, but that's *available* capital, not the actual compliance-to-75% retrofit cost per plant—that's a supply-chain engineering call, not a compliance number. I need supply chain to hand me plant-by-plant RVC-gap analysis with retrofit capex attached by 6 PM tomorrow so I can slot suppliers into tiers with *actual* make-versus-relocate costs, not just debt ratios. Right now I'm flagging RVC-short; I can't price the compliance spend until supply chain gives me the engineering.

**[R5] supplier** (pass 1): Supply chain—when you hand me the RVC cross-walk by 6 PM tomorrow, I need one more column: plant-by-plant retrofit capex to hit 75% in-house, not just the shortfall score. That's the make-versus-relocate call I'm pricing on Friday—if reshoring costs $8M and relocating costs $3M, that supplier moves tiers. Can you lock that into the 6 PM delivery?

**[R5] supply_chain_consultant** ⚡reply: Retrofit capex per plant is locked into the 6 PM delivery—I'm pulling engineering estimates right now, and that column goes on the cross-walk. But I need compliance to flag which plants are already mid-audit so I don't price retrofit costs for suppliers we're exiting anyway during the 90-day hold. Give me the audit-status snapshot and I'll have make-versus-relocate costs defensible by tomorrow night.

**[R5] compliance_lawyer** (pass 1): Supply chain, you're pulling retrofit capex estimates right now—when you hand me the cross-walk tomorrow at 6 PM, I need that column flagged by audit status too. If a plant's already 60 days into RVC review, I'm not pricing retrofit; I'm pricing exit-cost or emergency nearshoring instead. Give me both: retrofit capex *and* which suppliers are mid-audit, and the tier call becomes defensible.

**[R5] political_risk_insurer** (pass 1): Compliance, I need the audit-status snapshot right now—which tier-2 suppliers have active RVC audits in flight, audit start date, expected completion. If we're applying that 400-bps surcharge retroactive to the audit date, I can't price it until I know who's already 30, 60, 90 days in. Hand that to supply chain *today* so they lock retrofit capex and exit-cost columns by 6 PM tomorrow, and Friday's sheet closes on time.

**[R5] trade_credit_underwriter** (pass 1): Look, we've got the trigger sequence locked—audit hold, credit freeze, insolvency window. But I need a number: when a tier-2 supplier loses 15–25% EBITDA during that 90-day hold *plus* pays 400 bps on emergency credit, what's the total cost-to-supplier? Revenue loss plus financing premium—give me a range per supplier so I can price receivables risk against their relocation capex and know which ones actually default versus which ones we can carry.

**[R5] political_risk_insurer** ⚡reply: Revenue loss during hold runs 15–25% EBITDA, financing premium on emergency credit is 400–600 bps over base—call it $2–4M per mid-sized supplier depending on leverage and cash position. I'll pull actual EBITDA and debt figures from the balance sheets compliance's running EOD today so I can hand you per-supplier default-cost numbers by tomorrow morning, tied to relocation capex so Friday's tier call prices the full insolvency risk, not just the trigger.

**[R5] supply_chain_consultant** (pass 1): CFO, when you mark tier-3 as keep-versus-exit Friday morning, are you pricing that decision *after* the $2–4M audit-hold revenue loss and emergency financing premium hit their balance sheet? Because if tier-3 headroom doesn't cover relocation capex *plus* that cost, the keep call doesn't stick—that's an exit with a managed wind-down, not a relocation bet.

**[R5] cfo_erm** ⚡reply: Yes—Friday's tier-3 keep-versus-exit call prices the full hit: available capex headroom minus the $2–4M audit-hold cost, then what's left against the 18-month nearshoring capex. If headroom doesn't cover both, it's exit, not keep. I'm locking that math into the Friday sheet so the tier call is defensible, not a hope.

**[R5] auto_strategy** [speech]: Compliance, on Friday's sheet you're flagging RVC-short suppliers and their relocation cost — but what's the actual *compliance spend* to bring each plant to 75% RVC in-house, before we even talk nearshoring? Because if a plant's 4 points short and it costs $8M to reshore the inputs versus $3M to relocate the supplier, that changes the whole tier-1/tier-2 split.

**[R5] supplier** [speech]: Supply chain—when you hand me the RVC cross-walk by 6 PM tomorrow, I need one more column: plant-by-plant retrofit capex to hit 75% in-house, not just the shortfall score. That's the make-versus-relocate call I'm pricing on Friday—if reshoring costs $8M and relocating costs $3M, that supplier moves tiers. Can you lock that into the 6 PM delivery?

**[R5] compliance_lawyer** [speech]: Supply chain, you're pulling retrofit capex estimates right now—when you hand me the cross-walk tomorrow at 6 PM, I need that column flagged by audit status too. If a plant's already 60 days into RVC review, I'm not pricing retrofit; I'm pricing exit-cost or emergency nearshoring instead. Give me both: retrofit capex *and* which suppliers are mid-audit, and the tier call becomes defensible.

**[R5] political_risk_insurer** [speech]: Compliance, I need the audit-status snapshot right now—which tier-2 suppliers have active RVC audits in flight, audit start date, expected completion. If we're applying that 400-bps surcharge retroactive to the audit date, I can't price it until I know who's already 30, 60, 90 days in. Hand that to supply chain *today* so they lock retrofit capex and exit-cost columns by 6 PM tomorrow, and Friday's sheet closes on time.

**[R5] trade_credit_underwriter** [speech]: Look, we've got the trigger sequence locked—audit hold, credit freeze, insolvency window. But I need a number: when a tier-2 supplier loses 15–25% EBITDA during that 90-day hold *plus* pays 400 bps on emergency credit, what's the total cost-to-supplier? Revenue loss plus financing premium—give me a range per supplier so I can price receivables risk against their relocation capex and know which ones actually default versus which ones we can carry.

**[R5] supply_chain_consultant** [speech]: CFO, when you mark tier-3 as keep-versus-exit Friday morning, are you pricing that decision *after* the $2–4M audit-hold revenue loss and emergency financing premium hit their balance sheet? Because if tier-3 headroom doesn't cover relocation capex *plus* that cost, the keep call doesn't stick—that's an exit with a managed wind-down, not a relocation bet.

> _GM ⟶ cfo_erm (PROPOSAL, approved)_: The CFO's decision-logic column request crystallizes the keep-versus-exit framework into executable math, integrating audit-hold costs, capex headroom, and nearshoring thresholds. The cross-functional alignment on retrofit-versus-relocate calculations, audit-status flags, and supplier-level cost modeling transforms fragmented risk assessments into a unified, operationalized decision matrix ready for Friday's tier-classification session.  
>   side-effects: risk_map_completeness:+5.0; underwriting_discipline:+5.0; supplier_relocation_exposure:+3.0; trade_credit_risk:+2.0; risk_map_completeness:+1


_— R5 end [TERMINATED] | political_risk_exposure=38, risk_map_completeness=61, rules_of_origin_burden=41, supplier_relocation_exposure=34, trade_credit_risk=45, underwriting_discipline=67 —_

