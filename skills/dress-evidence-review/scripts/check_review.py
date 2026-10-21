"""Check review bookkeeping, not visual truth. Python standard library only."""
import json
import sys
from pathlib import Path


def check(data):
    errors = []
    posts = data.get('posts', [])
    ids = [p.get('id') for p in posts]
    if any(not isinstance(i, str) or not i for i in ids):
        errors.append('Every post needs a nonempty string id')
    if len(set(map(str, ids))) != len(ids):
        errors.append('Duplicate post ids')
    expected = data.get('expected_post_ids', [])
    if len(set(expected)) != len(expected):
        errors.append('Duplicate expected post ids')
    if expected and set(ids) != set(expected):
        errors.append('Expected post coverage differs from collected ids')
    for p in posts:
        label = str(p.get('id', '?'))
        def fail(message):
            errors.append(label + ': ' + message)
        if not str(p.get('url', '')).startswith(('https://', 'http://')):
            fail('Missing source URL')
        kind = p.get('kind')
        if kind not in ('photo', 'carousel', 'reel'):
            fail('Unknown media kind')
        media = p.get('media', [])
        keys = [m.get('key') for m in media]
        if any(not isinstance(k, str) or not k for k in keys) or len(set(map(str, keys))) != len(keys):
            fail('Missing or duplicate media keys')
        complete = p.get('collection_complete') is True
        reviewed = p.get('visual_complete') is True
        if reviewed and not complete:
            fail('Visual completion requires completed collection')
        if complete and kind == 'photo' and len(media) != 1:
            fail('Completed photo post needs one media item')
        if complete and kind == 'carousel':
            count = p.get('expected_slides')
            if not isinstance(count, int) or isinstance(count, bool) or count < 2:
                fail('Completed carousel needs an observed slide count >= 2')
            elif len(media) != count or sorted(m.get('position', -1) for m in media) != list(range(1, count + 1)):
                fail('Carousel count or positions do not match')
            if p.get('observed_end') is not True:
                fail('Carousel ending not observed')
        if reviewed and kind in ('photo', 'carousel') and any(m.get('reviewed') is not True for m in media):
            fail('Unreviewed media marked visually complete')
        if reviewed and kind == 'reel':
            duration = p.get('duration_seconds')
            times = p.get('sample_times', [])
            valid_duration = isinstance(duration, (int, float)) and not isinstance(duration, bool) and duration > 0
            if not valid_duration or not times:
                fail('Reel review needs duration and sample times')
            elif any(not isinstance(t, (int, float)) or isinstance(t, bool) or t < 0 or t > duration + .5 for t in times):
                fail('Invalid sample timestamp')
            elif times != sorted(set(times)):
                fail('Sample times must be unique and ordered')
            if p.get('observed_end') is not True or not p.get('sampling_note'):
                fail('Reel needs observed end and sampling limitations')
        if p.get('match_status') == 'confirmed' and not p.get('confirmation_evidence'):
            fail('Confirmed match needs confirmation evidence')
    return errors, {'posts': len(posts), 'collection_complete': sum(p.get('collection_complete') is True for p in posts),
                    'visual_complete': sum(p.get('visual_complete') is True for p in posts)}


def main():
    if len(sys.argv) != 2:
        print('Usage: python check_review.py review.json', file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8-sig'))
        errors, summary = check(data)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(json.dumps({'errors': [str(exc)]}, ensure_ascii=False))
        return 2
    print(json.dumps({'summary': summary, 'errors': errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
