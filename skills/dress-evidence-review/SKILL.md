---
name: dress-evidence-review
description: Organize wedding dress fitting photos, paired sketches and handwritten opinions, then compare sourced Instagram or blog candidates with explicit evidence and review coverage. Use for dress-tour comparison archives and their existing websites.
---

# Dress evidence review

Create a traceable comparison of fittings, personal notes and external candidates. Preserve the user's shop names, ordering, chosen site and current classification system. Do not infer a purchase decision or expand a photo comparison into exhaustive social-account collection unless requested.

## Establish the record

- Ask only for missing facts that block identification. Apply explicit user corrections ahead of a printed sheet heading or earlier interpretation. Record the correction rather than silently retaining both assignments.
- Assign stable fitting IDs per shop and fitting number. Multiple views of one dress and two people's sketches of it are not separate dresses. Keep media IDs separate from fitting IDs; external photos may have unknown product identity.
- Link both full sheets and per-dress excerpts. Keep full-sheet context accessible when comments cross column boundaries. Avoid exposing unrelated printed information when preparing excerpts for sharing.
- Transcribe each author's opinions separately, distinguishing observed design notes from personal preferences. Use neutral record labels if author identity is unknown. Mark illegible text rather than completing it from context. A comparison summary must not erase disagreement.

## Compare visible evidence

- Record silhouette, neckline, bodice seams, drape direction, waist position, skirt volume, train and accessories separately. Treat covered areas as unobserved.
- Separate source-described material from visible finish. Silk, satin and mikado are not mutually exclusive fiber categories. Do not infer composition from sheen. Keep uncertain tags explicit; do not copy representative-photo tags to unseen slides.
- For a veil search, compare length, tiering, motif shape, spacing, density and border placement. Distinguish flat embroidery from raised appliqué. Check dress versus veil decoration and flower bouquets.
- Use match states: `confirmed`, `strong_candidate`, `partial_candidate`, `excluded`, `unresolved`. Confirmation requires a source/model identifier or explicit user/vendor confirmation, not resemblance alone. Matching a veil does not confirm a dress; inspect the dress in the same source separately.
- For each candidate retain source URL, observed image, matching details, conflicting details and unobserved areas. Do not fabricate a better candidate when the search yields none.

## Collect and review

Read [references/review-records.md](references/review-records.md) before collecting more than a handful of posts or merging parallel work.

- Use available approved connectors/browser tools. Work from actual visible links and observed media addresses. Do not invent API endpoints, bypass access restrictions or reuse private session credentials outside their intended tool.
- Distinguish URL discovery, file download, visual review, classification and site publication. Log separate statuses and concrete blockers.
- Carousel: visit all reachable slides and verify visible content. Navigation can return the prior slide during animation; compare collected unique media keys with observed slide positions. An animated or video slide may not appear in an image-only selector. Do not conclude completion solely from a click count or DOM preload.
- Reel: inspect whether the player is visible and playing, dismiss optional overlays, record duration and actual sampled timestamps. Cover beginning, end and scene changes; enlarge relevant frames. Report time-sampled review as such, never all-frame inspection. A cropped view may leave the veil unjudgeable.
- Preserve original observed URLs but derive media identity from stable identifiers or content hashes, not rotating query signatures. Different encodings can represent the same photograph; inspect suspected duplicates. When source identity changes, an existing destination file is not proof it is current.
- Contact sheets accelerate screening; enlarge potential matches and small/ambiguous details. Failure to download is not a negative match. Use existing verified assets or accessible UI, otherwise report the blocked subset.

## Delegate and merge when authorized

Split disjoint shop/post ranges or media types. Give each worker the target reference, exact range, completion criteria and an independent output path. Workers should not write one shared manifest or edit the site concurrently. One owner merges by stable keys, validates coverage and resolves conflicts. Reload disk state before a merge; stale in-memory state must not replace newer work.

The validator checks bookkeeping, not visual correctness:

```sh
python scripts/check_review.py review.json
```

## Present and finish

- For the user's requested layout, prioritize actual fitting evidence and both records; put external candidates below with explicit status. Preserve requested collapsed sections and offer full-sheet viewing. Do not impose this layout on a different requested design.
- Add photos to an existing archive without renumbering existing items or losing tags, saved-item keys and personal notes. Preserve source links. Distinguish post totals, photo totals and confirmed product totals.
- Use the site's supported workflow if available; keep its identity and audience. Existing publication permission is scoped to that site, not a separate blog or public photo pack. A missing publishing tool should produce a local artifact and an explicit deployment limitation, not a false completion claim.
- Verify both record viewers, image loading, ordering, filters and candidate disclosures affected by the change. Report new photos and remaining blockers accurately. If no same-veil candidate is found, say so and do not add an unverified match merely to produce a site change.
- For a shareable skill or process article, use synthetic examples instead of personal photos, local account paths or expiring CDN links. Attribute original public images if included in a separate authorized deliverable.
