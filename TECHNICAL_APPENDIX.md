## Technical Appendix — Persistence-Gated Structure Detection

### Problem Framing

Given a high-entropy visual signal \( V_t \) (e.g. smoke, fire, water),
most spatial features are transient.

VeilSight does not attempt object detection or semantic classification.
Instead, it searches for **structures that persist under entropy**.

---

### Definitions

Let:

- \( F_t \) be the frame at time \( t \)
- \( E(F_t) \) be an entropy-preserving transformation
- \( G_t \) be a candidate glyph extracted from \( F_t \)

A glyph \( G \) is defined as **persistent** if:

\[
P(G) = \sum_{t = 1}^{T} \mathbb{1}[G \in F_t] \geq \tau
\]

Where:
- \( T \) is the observation window
- \( \tau \) is the persistence threshold
- \( \mathbb{1} \) is the indicator function

---

### Persistence Gating

The extraction pipeline enforces:

1. **Spatial consistency** across frames
2. **Topological similarity** under entropy fluctuation
3. **Temporal survival** across \( \tau \) frames

Features that do not meet persistence constraints are discarded.

This prevents:
- Single-frame noise artifacts
- Random high-contrast edges
- Pareidolic hallucinations

---

### Empirical Behavior

Observed behavior across multiple entropy sources:

- Lower \( \tau \): high glyph count, low stability
- Higher \( \tau \): low glyph count, high stability

This monotonic tradeoff confirms that glyphs are gated by persistence,
not appearance.

---

### Key Insight

If a structure:

- Reappears under stochastic variation
- Survives entropy-preserving transforms
- Maintains spatial coherence over time

Then it is **not random noise**.

VeilSight isolates this class of structure.

---

### Implications

This framing positions the system as:

- A pre-semantic signal extractor
- An entropy-resistant structure detector
- A substrate for security, authentication, or adversarial ML research

No linguistic, cultural, or semantic priors are assumed.
