# VeilSight — Persistence-Gated Glyph Extraction from Visual Entropy

VeilSight is a research prototype for detecting **persistent symbolic structures (“glyphs”)**
that emerge from high-entropy natural video (smoke, fire, water, clouds).

Unlike conventional vision pipelines, VeilSight does **not** classify objects.
It detects **stable structure inside visual chaos** using persistence constraints.

This repository contains:
- The **extraction method**
- Stability / persistence instrumentation
- Reproducible scripts (no dataset included)

The underlying dataset and trained models are **not public**.

---

## Why This Exists

Most vision models learn shortcuts.
VeilSight explores the opposite question:

> *What structures remain when appearance is unstable but persistence is enforced?*

Observed behavior:
- Lower persistence → higher yield, low coherence
- Higher persistence → low yield, high structural stability
- Glyph emergence collapses outside narrow stability windows

---

## Core Definition

A glyph is a visual structure that:

1. Appears in high-entropy regions
2. Survives across N consecutive frames
3. Maintains edge stability below a threshold
4. Passes a learned structural filter

Persistence acts as a **semantic pressure**, not a classifier.

---

## Pipeline Overview

```
Video
  ↓
Frame Sampling
  ↓
Entropy Filtering
  ↓
Edge Stability Comparison
  ↓
Persistence Gate (N frames)
  ↓
Glyph Prediction Model
  ↓
Glyph Artifact
```

---

## Key Parameters

| Parameter           | Description                            |
|--------------------|----------------------------------------|
| FRAME_STEP          | Frame sampling interval                |
| ENTROPY_THRESHOLD   | Rejects low-entropy frames             |
| STABILITY_FRAMES    | Required persistence window            |
| EDGE_DIFF_THRESHOLD | Edge stability tolerance               |

---

## Observed Yield vs Persistence

| Persistence Frames | Glyphs Extracted |
|--------------------|------------------|
| 4                  | ~70              |
| 6–12               | ~215             |
| 15                 | ~13              |

Yield increases with lower persistence, but structure degrades.
Higher persistence sharply reduces yield while stabilizing form.

---

## What This Is NOT

- Object detection
- OCR or symbolic labeling
- Artistic rendering
- Cryptographic primitives

VeilSight extracts **structure**, not meaning.

---

## Dataset & Access

The dataset and trained models are proprietary.

Evaluation access may be granted for:
- Research validation
- Robustness testing
- Security experiments

Contact information to be added.

---

## Status

Active research.

VeilSight is evaluated by behavioral invariants, not accuracy metrics.


Interfaces and parameters may change.

Initial README describing persistence-gated glyph extraction
