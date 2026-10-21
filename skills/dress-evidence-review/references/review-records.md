# Review records and coverage

Keep these entities distinct:

| Entity | Stable key | Evidence |
|---|---|---|
| Fitting | shop key + user-confirmed fitting number | user corrections, both full sheets, actual views |
| Record | fitting ID + record author label | transcription, uncertain spans, source crop |
| Post | canonical source post ID | source URL, media type, observed ending |
| Media | post ID + stable media key | observed address/file, slide position, visual-review status |
| Candidate | fitting ID + source media key | matching/conflicting details, match state, confirmation source |

Use separate worker files. Merge post records by canonical ID and media by stable key. Retain the original source URL. Do not conflate a count match with a proof of coverage, or consecutive source rows with confirmed unique dresses.

Minimal format accepted by `scripts/check_review.py`:

```json
{
  "expected_post_ids": ["sample-post"],
  "posts": [{
    "id": "sample-post",
    "url": "https://example.org/posts/sample-post",
    "kind": "carousel",
    "collection_complete": true,
    "visual_complete": true,
    "observed_end": true,
    "expected_slides": 2,
    "media": [
      {"key": "photo-a", "position": 1, "reviewed": true},
      {"key": "photo-b", "position": 2, "reviewed": true}
    ],
    "finding": "Different veil pattern; not a confirmed match."
  }]
}
```

For `photo`, require one media record. For `carousel`, record the actual observed count after reaching its end; uncertain collection remains incomplete. A video slide still gets a media record with a stable key, and its visual status requires video review. If platform behavior prevents a reliable count, record a blocker rather than asserting `collection_complete`.

For `reel`, add `duration_seconds`, ordered `sample_times` and `sampling_note`. `observed_end` means playback end was observed. `visual_complete` means the declared time-sampling plan was reviewed, not every frame. Optional media records can hold representative frames. Record whether framing makes the target unjudgeable. Sampling density should follow scene changes and the detail sought, not a universal one-second rule.

The checker rejects duplicate IDs/keys, mismatched carousel positions/counts and unsupported completion claims. Incomplete records are allowed and appear in the summary. A successful check does not establish that a source is authentic, samples cover every scene, notes are accurate, or two dresses match.

For a candidate use `match_status` and `confirmation_evidence` if confirmed. Evidence should identify the model/source statement or user confirmation. Keep manual material tags separate from source specifications. Store detailed transcription outside this compact post record when needed.
