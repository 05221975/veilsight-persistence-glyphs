## Empirical Results (Summary)

VeilSight has been evaluated on entropy-rich natural video
(smoke, fire, water, cloud formations).

The system does not classify objects.
It detects *persistent structure* under visual instability.

### Observed Behavior

Across multiple videos and parameter sweeps:

| Stability Frames | Glyph Yield | Notes |
|------------------|------------|------|
| 4                | High        | Dense extraction, low persistence |
| 8                | Medium      | Balanced signal/noise |
| 12               | Low         | High persistence structures only |

Increasing the persistence window reduces glyph count
while increasing structural stability.

### Key Property

Glyphs extracted at higher persistence thresholds:

- Reappear across frame windows
- Survive entropy fluctuations
- Are resistant to frame-level perturbations

This behavior is consistent across multiple natural phenomena.

### Reproducibility

All measurements shown here were generated using
the public persistence-gated extraction logic.

The dataset and trained models are intentionally withheld.
