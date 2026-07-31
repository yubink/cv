#!/usr/bin/env python3
"""Regenerate skills_evidence_matrix in bullet-library.yaml from bullets + publications.
Run from resume-system root after editing any skills[] field."""
import yaml, re

bl = yaml.safe_load(open('bullet-library.yaml'))
pl = yaml.safe_load(open('publication-library.yaml'))

matrix = {}
for b in bl['bullets']:
    for s in b['skills']:
        matrix.setdefault(s, {'bullets': [], 'publications': []})['bullets'].append(b['id'])
for p in pl['publications']:
    for s in p['skills']:
        matrix.setdefault(s, {'bullets': [], 'publications': []})['publications'].append(p['id'])

lines = ["", "# ---- GENERATED: skills_evidence_matrix (regenerate via TODO.md §1 script; do not hand-edit) ----",
         "# Skills with only publication evidence are still valid (publications count regardless of age),",
         "# but check whether an experience bullet would strengthen them.",
         "skills_evidence_matrix:"]
for s in sorted(matrix):
    e = matrix[s]
    lines.append(f"  {s}:")
    lines.append(f"    bullets: {e['bullets']}")
    lines.append(f"    publications: {e['publications']}")

src = open('bullet-library.yaml').read()
src = re.sub(r"\n# ---- GENERATED: skills_evidence_matrix.*", "", src, flags=re.S)
open('bullet-library.yaml','w').write(src.rstrip() + "\n" + "\n".join(lines) + "\n")

pub_only = [s for s,e in sorted(matrix.items()) if not e['bullets']]
print(f"skills: {len(matrix)} | bullets: {len(bl['bullets'])} | pubs: {len(pl['publications'])}")
print("publication-only skills:", pub_only)
