# LLM Interview Question Bank

An original, community-driven repository of interview questions for modern LLM engineering.
It is designed for realistic hiring loops and technical screen preparation.
The source of truth is `QUESTION_BANK.md`, while `README.md` is generated for discoverability.
Questions emphasize tradeoffs, debugging strategy, production constraints, and safety thinking.
Contributors are expected to add fully original content using the required strict template.
Automated checks in CI enforce formatting consistency and structural correctness.

An original, community-driven collection of interview questions focused on practical Large Language Model engineering.

## Table of Contents

- [Foundations of LLMs](#foundations-of-llms)
- [Training & Alignment](#training--alignment)
- [Inference & Systems Engineering](#inference--systems-engineering)
- [Retrieval, Agents & Tool Use](#retrieval-agents--tool-use)
- [Evaluation & Safety](#evaluation--safety)
- [Real-World Engineering & Debugging](#real-world-engineering--debugging)
- [System Design Scenarios](#system-design-scenarios)

## Foundations of LLMs

### Q: Why can next-token prediction still produce useful reasoning behavior?

**Difficulty:** Medium  
**Tags:** objectives,emergence,reasoning  
**Question:** Explain why training to predict tokens can yield behaviors that look like planning, and where this breaks in interviews.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How would you explain the role of tokenization in model quality to a product manager?

**Difficulty:** Easy  
**Tags:** tokenization,product,tradeoffs  
**Question:** You inherit a multilingual chatbot with uneven quality across languages; walk through how tokenization may be part of the root cause.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: When does scaling model size stop being the best lever?

**Difficulty:** Medium  
**Tags:** scaling-laws,cost,optimization  
**Question:** A team wants to jump from 7B to 70B parameters; discuss when data quality, retrieval, or prompting might give better returns.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What is the practical difference between pretraining data diversity and data cleanliness?

**Difficulty:** Medium  
**Tags:** data-quality,pretraining,tradeoffs  
**Question:** You can either add noisy web data or spend effort cleaning current corpora; discuss expected impact.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do attention heads specialize, and why should engineers care?

**Difficulty:** Hard  
**Tags:** attention,interpretability,debugging  
**Question:** A model fails on long legal references; discuss how attention behavior can inform debugging without claiming full interpretability.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Why do context windows create both capability and risk?

**Difficulty:** Easy  
**Tags:** context-window,reliability,safety  
**Question:** Describe how longer context helps tasks while introducing distraction, latency, and prompt-injection exposure.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What would you check before claiming a model "understands" domain concepts?

**Difficulty:** Medium  
**Tags:** evaluation,epistemics,robustness  
**Question:** An internal demo looks impressive on curated prompts; explain what evidence is still missing.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do instruction tuning and base-model behavior differ in failure modes?

**Difficulty:** Medium  
**Tags:** instruction-tuning,alignment,failure-analysis  
**Question:** Compare a base model and instruction-tuned model answering ambiguous requests in production.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Why do small models sometimes outperform larger ones on specific workflows?

**Difficulty:** Medium  
**Tags:** small-models,specialization,latency  
**Question:** Your support workflow gets better results from a smaller distilled model; explain plausible reasons.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you reason about memorization versus generalization in interviews?

**Difficulty:** Hard  
**Tags:** memorization,privacy,testing  
**Question:** A candidate claims good benchmark scores prove generalization; probe the limits of that claim.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What are practical signs of distribution shift for LLM products?

**Difficulty:** Easy  
**Tags:** distribution-shift,monitoring,operations  
**Question:** After a pricing-policy change, response quality drops; describe what shift indicators you would monitor.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you compare dense and sparse architectures for product deployment?

**Difficulty:** Hard  
**Tags:** architecture,moe,inference-cost  
**Question:** Discuss deployment implications when choosing dense models versus mixture-of-experts under fixed budget.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

## Training & Alignment

### Q: How would you design a high-signal supervised fine-tuning dataset?

**Difficulty:** Medium  
**Tags:** sft,data-pipeline,quality  
**Question:** You have 20k candidate conversations from support logs; explain filtering and annotation strategy.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What tradeoffs exist between RLHF, RLAIF, and direct preference optimization?

**Difficulty:** Hard  
**Tags:** alignment,rlhf,dpo  
**Question:** The team must pick an alignment method with limited human-labeling budget; compare options.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How can reward hacking appear in language model alignment?

**Difficulty:** Hard  
**Tags:** reward-models,alignment,failures  
**Question:** A model starts writing verbose but unhelpful answers after preference training; explain why.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What does over-alignment look like in enterprise settings?

**Difficulty:** Medium  
**Tags:** policy,alignment,ux  
**Question:** Safety tuning reduced harmful outputs but now blocks harmless policy analysis requests; diagnose.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How would you calibrate refusal behavior instead of maximizing it?

**Difficulty:** Hard  
**Tags:** safety,calibration,policy  
**Question:** You need nuanced refusal boundaries for healthcare admin tasks; describe a calibration approach.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Why does data mixture matter more than raw token count in continued pretraining?

**Difficulty:** Medium  
**Tags:** continued-pretraining,data-mixture,domain-adaptation  
**Question:** A domain adaptation run added many tokens but quality barely improved; explain possible causes.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you detect catastrophic forgetting after domain fine-tuning?

**Difficulty:** Medium  
**Tags:** fine-tuning,catastrophic-forgetting,evaluation  
**Question:** A legal assistant improves on legal tasks but worsens on general writing; propose checks.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What should be in an alignment evaluation set beyond harmful prompts?

**Difficulty:** Easy  
**Tags:** alignment-eval,policy,coverage  
**Question:** Create an eval suite that captures tone, fairness, uncertainty, and instruction-following reliability.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How can synthetic data help and hurt post-training?

**Difficulty:** Medium  
**Tags:** synthetic-data,quality-control,feedback-loops  
**Question:** Your team proposes scaling with model-generated training data; assess upside and risks.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: When should you freeze layers during fine-tuning?

**Difficulty:** Hard  
**Tags:** fine-tuning,optimization,stability  
**Question:** Compute is limited and you need stable adaptation; explain criteria for freezing or unfreezing layers.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you estimate alignment regressions before launch?

**Difficulty:** Medium  
**Tags:** release-process,gating,alignment  
**Question:** A new checkpoint improves benchmark score by 3 points; discuss what pre-launch checks are still required.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What governance controls should exist around training data provenance?

**Difficulty:** Easy  
**Tags:** governance,compliance,data-provenance  
**Question:** Design practical controls that engineering teams can adopt without blocking delivery.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

## Inference & Systems Engineering

### Q: How do you choose between batching for throughput and low tail latency?

**Difficulty:** Medium  
**Tags:** inference,latency,throughput  
**Question:** Design serving behavior for a mixed workload of chat and background summarization.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What causes KV-cache memory pressure and how can you mitigate it?

**Difficulty:** Hard  
**Tags:** kv-cache,memory,performance  
**Question:** Latency spikes occur during long conversations; explain mitigation options.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How would you reason about quantization levels for production quality targets?

**Difficulty:** Medium  
**Tags:** quantization,quality,cost  
**Question:** You can cut cost with 4-bit quantization but fear quality drops on reasoning tasks.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What is speculative decoding and when is it a bad idea?

**Difficulty:** Hard  
**Tags:** decoding,optimization,inference  
**Question:** A team wants speculative decoding everywhere; discuss where overhead can outweigh gains.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you debug nondeterministic output changes across deployments?

**Difficulty:** Medium  
**Tags:** reproducibility,debugging,serving  
**Question:** Two replicas produce different responses for the same prompt; outline an investigation path.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What are practical streaming-response failure modes?

**Difficulty:** Easy  
**Tags:** streaming,api,ux  
**Question:** Users report truncated or repeated chunks in streamed responses; explain likely causes.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you set max tokens and stop criteria for reliability?

**Difficulty:** Medium  
**Tags:** generation-controls,reliability,api  
**Question:** A report-generation endpoint sometimes cuts off conclusions; describe control strategy.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: When do CPU inference paths make sense for LLM applications?

**Difficulty:** Medium  
**Tags:** deployment,cpu-inference,edge  
**Question:** You need low-volume private deployments in regulated environments; assess CPU viability.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How would you design canary rollout for model version updates?

**Difficulty:** Easy  
**Tags:** rollout,observability,risk  
**Question:** Outline traffic-splitting, rollback triggers, and metrics for safe checkpoint upgrades.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How can tokenizer mismatches break production even with the same model weights?

**Difficulty:** Hard  
**Tags:** tokenizer,compatibility,ops  
**Question:** A migrated service shows silent quality regressions; explain tokenizer-related pitfalls.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What metrics matter for inference SLOs besides average latency?

**Difficulty:** Easy  
**Tags:** slo,monitoring,reliability  
**Question:** Define an SLO dashboard for an LLM assistant used by customer support agents.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you harden model-serving pipelines against prompt-level denial-of-service patterns?

**Difficulty:** Hard  
**Tags:** security,abuse-prevention,serving  
**Question:** An attacker sends huge prompts to exhaust resources; propose layered defenses.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

## Retrieval, Agents & Tool Use

### Q: How do you decide whether a feature needs RAG at all?

**Difficulty:** Medium  
**Tags:** rag,product-scope,architecture  
**Question:** A stakeholder requests vector search for every assistant flow; evaluate necessity.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What chunking strategy would you use for policy documents with cross-references?

**Difficulty:** Medium  
**Tags:** chunking,rag,document-design  
**Question:** Answer quality drops when citations span sections; explain chunking choices.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you measure retrieval quality separately from generation quality?

**Difficulty:** Hard  
**Tags:** evaluation,rag,diagnostics  
**Question:** A RAG assistant fails, but it is unclear whether retrieval or synthesis is at fault.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Why can higher recall retrieval still reduce final answer quality?

**Difficulty:** Medium  
**Tags:** retrieval,precision-noise,tradeoffs  
**Question:** A team increased top-k and sees more hallucinations; discuss the mechanism.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How should an agent decide when to call a tool versus answer directly?

**Difficulty:** Hard  
**Tags:** agents,tool-selection,policy  
**Question:** Design decision logic for a finance assistant with calculator and SQL tools.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What safety checks belong between agent planning and tool execution?

**Difficulty:** Hard  
**Tags:** agent-safety,guardrails,tool-use  
**Question:** An agent can trigger irreversible actions; define pre-execution controls.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you prevent stale embeddings from silently degrading answers?

**Difficulty:** Medium  
**Tags:** embeddings,data-freshness,ops  
**Question:** Knowledge base updates weekly but retrieval quality drifts; propose safeguards.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What are reliable citation strategies for RAG responses?

**Difficulty:** Easy  
**Tags:** citations,trust,ux  
**Question:** Users need verifiable answers for compliance workflows; outline citation design.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you design fallback behavior when retrieval returns low-confidence matches?

**Difficulty:** Medium  
**Tags:** fallbacks,retrieval-confidence,ux  
**Question:** Describe response strategies that avoid confident hallucination.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: When does multi-agent architecture help, and when is it unnecessary complexity?

**Difficulty:** Hard  
**Tags:** multi-agent,architecture,maintenance  
**Question:** Evaluate a proposal to split planner, researcher, and writer agents for support tasks.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How can tool output schemas reduce downstream hallucination?

**Difficulty:** Medium  
**Tags:** structured-output,tools,reliability  
**Question:** Explain why strict schema contracts improve end-to-end correctness.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you monitor agent loops and runaway tool-calling?

**Difficulty:** Easy  
**Tags:** agents,monitoring,cost-control  
**Question:** Design telemetry and guardrails for loops causing cost spikes.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

## Evaluation & Safety

### Q: How would you build an evaluation ladder from unit tests to live traffic probes?

**Difficulty:** Medium  
**Tags:** evaluation,strategy,release  
**Question:** Define staged evaluation before promoting a model to production.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Why are benchmark leaderboards insufficient for hiring decisions about model quality?

**Difficulty:** Easy  
**Tags:** benchmarks,validity,interview  
**Question:** A candidate cites leaderboard rank as proof of readiness; probe deeper.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you evaluate factuality when ground truth is ambiguous or evolving?

**Difficulty:** Hard  
**Tags:** factuality,uncertainty,evaluation  
**Question:** Regulatory guidance changes over time; explain evaluation approach.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What is a practical red-team process for an internal assistant?

**Difficulty:** Medium  
**Tags:** red-teaming,safety,operations  
**Question:** Design a repeatable process with prioritization and remediation tracking.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you detect and quantify hallucination in production?

**Difficulty:** Medium  
**Tags:** hallucination,monitoring,qa  
**Question:** You need ongoing hallucination estimates without manually reading all outputs.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What is calibration and why does confidence wording matter?

**Difficulty:** Easy  
**Tags:** calibration,ux,trust  
**Question:** A model sounds certain even when unsure; discuss mitigation.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you evaluate bias without reducing it to one metric?

**Difficulty:** Hard  
**Tags:** bias,evaluation,multidimensional  
**Question:** Create an evaluation plan across demographic, linguistic, and contextual factors.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How can safety filters create hidden product regressions?

**Difficulty:** Medium  
**Tags:** safety-filters,false-positives,product  
**Question:** A new filter improves policy compliance but hurts task completion rates.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What abuse scenarios should be in threat modeling for LLM APIs?

**Difficulty:** Medium  
**Tags:** threat-modeling,security,api  
**Question:** List realistic misuse paths and corresponding mitigations.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you set go/no-go thresholds for model release?

**Difficulty:** Hard  
**Tags:** release-gates,risk-management,metrics  
**Question:** Define release criteria balancing quality, safety, and business timelines.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: When should you require human-in-the-loop review?

**Difficulty:** Easy  
**Tags:** human-in-the-loop,risk,workflow  
**Question:** Identify use cases where automated output should not be final.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you design post-incident analysis for harmful model outputs?

**Difficulty:** Medium  
**Tags:** incident-response,learning,safety  
**Question:** Outline a blameless process that still drives concrete fixes.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

## Real-World Engineering & Debugging

### Q: A model suddenly becomes verbose overnight—how do you triage quickly?

**Difficulty:** Medium  
**Tags:** debugging,ops,prompting  
**Question:** Explain a step-by-step production triage process for unexpected verbosity.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you separate prompt regression from model regression?

**Difficulty:** Hard  
**Tags:** regression-analysis,prompts,model-ops  
**Question:** A new release changed prompts and checkpoint simultaneously; design isolation tests.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What logs are essential for debugging low-quality responses while respecting privacy?

**Difficulty:** Medium  
**Tags:** observability,privacy,debugging  
**Question:** Design a logging policy that supports root-cause analysis.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you diagnose sudden cost increases in an LLM pipeline?

**Difficulty:** Easy  
**Tags:** cost,monitoring,capacity  
**Question:** Token usage doubled week-over-week; describe an investigation framework.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What are common failure patterns in function-calling integrations?

**Difficulty:** Medium  
**Tags:** function-calling,integration,errors  
**Question:** API calls succeed but returned answers are wrong; explain likely weak points.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you recover gracefully when an upstream model provider degrades?

**Difficulty:** Hard  
**Tags:** resilience,multi-provider,sre  
**Question:** Design fallback and degradation strategy for provider outages.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Why do prompt templates rot over time, and how do you maintain them?

**Difficulty:** Medium  
**Tags:** prompt-management,maintenance,qa  
**Question:** A once-reliable template now fails on new customer intents; propose maintenance process.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How would you test concurrency bugs in tool-augmented chat systems?

**Difficulty:** Hard  
**Tags:** concurrency,testing,agents  
**Question:** Interleaved sessions leak context; outline a reproducible test strategy.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What rollback plan should exist for bad model launches?

**Difficulty:** Easy  
**Tags:** rollback,release,incident  
**Question:** Describe rollback mechanics, communication, and data capture during incident.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How can caching improve performance while causing correctness bugs?

**Difficulty:** Medium  
**Tags:** caching,correctness,tradeoffs  
**Question:** A response cache boosts speed but returns stale personalized results.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: How do you design prompts for multilingual support without creating translation artifacts?

**Difficulty:** Medium  
**Tags:** multilingual,prompt-design,quality  
**Question:** Support responses in mixed-language chats feel unnatural; explain improvements.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: What do you do when eval metrics improve but user satisfaction drops?

**Difficulty:** Hard  
**Tags:** product-metrics,evaluation,gap-analysis  
**Question:** Discuss how to investigate metric-product mismatch and recalibrate goals.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

## System Design Scenarios

### Q: Design an internal knowledge assistant for 10,000 employees across regions

**Difficulty:** Hard  
**Tags:** system-design,enterprise,rag  
**Question:** Discuss architecture, auth boundaries, latency targets, and rollout phases.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design a customer-support copilot with strict auditability requirements

**Difficulty:** Hard  
**Tags:** system-design,auditability,compliance  
**Question:** Explain how responses, sources, and agent actions should be traceable.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design a low-latency voice assistant backed by an LLM

**Difficulty:** Hard  
**Tags:** system-design,voice,latency  
**Question:** Cover streaming ASR/TTS integration, interruption handling, and fallback logic.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design an offline-capable on-prem LLM assistant for regulated environments

**Difficulty:** Hard  
**Tags:** system-design,on-prem,security  
**Question:** Describe model selection, update channel, and operational constraints.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design an evaluation platform shared by multiple LLM product teams

**Difficulty:** Medium  
**Tags:** system-design,evaluation,platform  
**Question:** Define dataset versioning, metric governance, and CI integration.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design a safe tool-using agent that can execute database queries

**Difficulty:** Hard  
**Tags:** system-design,agents,database-safety  
**Question:** Specify permissions model, query validation, and incident containment.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design a migration plan from one model provider to a hybrid multi-provider stack

**Difficulty:** Medium  
**Tags:** system-design,migration,resilience  
**Question:** Discuss abstraction layers, capability gaps, and risk mitigation.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design a cost-aware routing layer across small and large models

**Difficulty:** Medium  
**Tags:** system-design,routing,cost-optimization  
**Question:** Explain routing policies, quality safeguards, and feedback loops.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design a personalization system that preserves user privacy

**Difficulty:** Hard  
**Tags:** system-design,personalization,privacy  
**Question:** Balance user-level adaptation with data minimization and policy compliance.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design a real-time moderation system for user-generated prompts and outputs

**Difficulty:** Medium  
**Tags:** system-design,moderation,safety  
**Question:** Include latency budget, escalation paths, and false-positive handling.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design an LLM-powered analytics assistant that generates SQL and charts

**Difficulty:** Hard  
**Tags:** system-design,analytics,tool-use  
**Question:** Address schema grounding, query validation, and user trust mechanisms.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.

### Q: Design a postmortem and reliability loop for LLM incidents at scale

**Difficulty:** Medium  
**Tags:** system-design,reliability,incident-management  
**Question:** Define ownership, telemetry, and preventive engineering feedback loops.  
**What a strong answer includes:**

- Clear assumptions and problem framing.
- Tradeoff analysis tied to realistic constraints.
- Concrete validation or monitoring approach.
**Common pitfalls:**

- Giving generic definitions without operational detail.
- Ignoring failure modes, costs, or stakeholder constraints.
