---
name: pr-review
description: >
  Review a GitHub pull request and post the findings as inline review comments,
  each tagged with a severity (blocking, nit, pre-existing) and a machine-readable
  marker that the address-review skill reads later. Use when the user asks to
  review a PR and post or leave the review on GitHub, e.g. "review PR 36 and
  comment", "post a review on this PR". For a review the user only wants to read
  in the terminal, use /code-review instead.
---

# PR review

Review a pull request, show the findings to the user, and after they approve,
post them as one GitHub review with one inline comment per finding.

Argument: a PR number or URL. With none, use the PR of the current branch
(`gh pr view --json number,url`). If there is none, stop and say so.

## 1. Collect PR context

```bash
gh pr view <N> --json number,title,url,author,headRefOid,baseRefName,headRefName,isDraft,state
gh repo view --json nameWithOwner
gh api user --jq .login
```

Keep `headRefOid` (the commit the comments attach to), `nameWithOwner` and
whether the PR author is the current user (GitHub rejects REQUEST_CHANGES and
APPROVE on your own PR). If the PR is closed or merged, ask before continuing.

Read the repo's review rules if present: `AGENTS.md`, `CLAUDE.md`,
`CONTRIBUTING.md`, `.github/pull_request_template.md`.

## 2. Review

Invoke the `code-review` skill with the PR URL as the target, without
`--comment` (this skill posts the comments itself). Pass an effort level only
if the user gave one. Wait for its findings.

If `code-review` is not available, review the diff yourself
(`gh pr diff <N>`, and read the changed files at the PR head for context).
Look for correctness bugs, broken repo rules and missing tests. Report only
findings you can tie to a concrete failure.

Map each finding to a severity:

| code-review severity | posted severity | meaning |
|---|---|---|
| `important` | `blocking` | a bug the PR adds or makes worse; should be fixed before merge |
| `nit` | `nit` | minor; fine to fix later |
| `pre_existing` | `pre-existing` | a bug already there before the PR; usually out of scope |

Number the findings R1, R2, ... in order of severity.

## 3. Check each finding can be anchored

An inline comment must point to a line that is part of the diff on the
right-hand side. Get the changed line ranges with `gh pr diff <N>` and check
each finding's `path` and `line`:

- line is in a hunk on the new side: inline comment, `side: "RIGHT"`.
- otherwise: move the finding into the review body, under "Findings outside
  the diff", with a permalink
  `https://github.com/<owner>/<repo>/blob/<headRefOid>/<path>#L<line>`.

## 4. Show the plan and ask before posting

Posting is visible to everyone on the PR. Show the user a table:

| ID | Severity | File:line | Summary | Placement |

Then ask (AskUserQuestion) whether to post, with these options:
- Post as a comment review (Recommended)
- Post as "Request changes" (offer only when there is a `blocking` finding and
  the PR author is not the current user)
- Edit first (the user says which findings to drop or reword)
- Don't post

Do not post without an explicit yes in this step.

## 5. Post one review

Write the payload to a file in the scratchpad and post it in one call, so the
PR gets one notification, not one per comment:

```bash
gh api repos/<owner>/<repo>/pulls/<N>/reviews -X POST --input <scratchpad>/review.json
```

```json
{
  "commit_id": "<headRefOid>",
  "event": "COMMENT",
  "body": "<review body>",
  "comments": [
    {"path": "scripts/x.py", "line": 187, "side": "RIGHT", "body": "<comment body>"}
  ]
}
```

Each comment body:

```
**[nit] R2: <one-line summary>**

<what is wrong, in two to four sentences>

**When it goes wrong:** <concrete inputs or state, and the wrong result>

**Suggested fix:** <the change, with a short code snippet if it helps>

<!-- pr-review: id=R2 severity=nit -->
```

Write every comment so it still makes sense when copied into an issue on its
own: name the function and file, do not say "see above".

Review body:

```
Automated review: <n> findings (<b> blocking, <k> nit, <p> pre-existing).

<one or two sentences on overall impression>

<"Findings outside the diff" section, if any, in the same format as comments>

Reply to each thread, or run the address-review skill to fix, defer to the
backlog, or decline each finding.

<!-- pr-review: summary head=<headRefOid> -->
```

If the API rejects a comment's line (HTTP 422 "line could not be resolved"),
move that finding into the body and post again. Do not drop it.

## 6. Report

Give the user the review URL (from the response's `html_url`) and the
counts by severity. Do not repeat the full findings in the terminal; they
are on the PR.
