---
name: address-review
description: >
  Work through the unresolved review threads of a GitHub pull request. As the
  PR author: for each finding, fix it, defer it to a backlog issue, or decline
  it with a reason. As a reviewer: check the author's replies against the code,
  then resolve verified threads, push back on the rest, and move leftover
  findings to the backlog. Either way it replies on and resolves threads and
  posts a summary. Use when the user asks to address, handle, triage, follow up
  on or respond to review comments on a PR, or to move review findings to the
  backlog.
---

# Address review

Go through a PR's open review threads with the user. The user decides what
happens to each finding; this skill carries it out and leaves a record on the
PR. Nothing is posted, pushed or created on GitHub until the user approves
the plan.

There are two modes, picked in step 1:
- **Author mode** (steps 2-7): the user wrote the PR and answers findings
  from reviewers.
- **Reviewer mode** (section "Reviewer mode" at the end): the user reviewed
  the PR and follows up on the author's answers to their own threads.

Argument: a PR number or URL. With none, use the PR of the current branch.

## 1. Collect PR context and settings

```bash
gh pr view <N> --json number,title,url,author,headRefName,headRefOid,state
gh repo view --json nameWithOwner
gh api user --jq .login
git branch --show-current
git status --porcelain
```

- Pick the mode. If the current user is the PR author, use author mode. If
  not, use reviewer mode and say so in one line ("You're the reviewer on
  #<N>, so I'll check the author's replies to your threads."). If the user
  asked for the other mode explicitly, use that one.
- If the current branch is not the PR's head branch, ask before switching
  (`gh pr checkout <N>`). If the working tree has changes, stop and ask. In
  reviewer mode, `git fetch` and read the code at `headRefOid`
  (`git show <headRefOid>:<path>`) instead of switching, if the user prefers
  to stay on their branch.
- Read the backlog settings. Look in `AGENTS.md`, then `CLAUDE.md`, for lines
  like these (case does not matter):

  ```
  review-backlog-label: review-backlog
  review-backlog-issues: per-pr | per-finding | grouped
  ```

  Defaults: label `review-backlog`, issues `per-pr`.

## 2. Fetch unresolved threads

```bash
gh api graphql -F owner=<owner> -F repo=<repo> -F pr=<N> -f query='
query($owner:String!,$repo:String!,$pr:Int!,$after:String){
  repository(owner:$owner,name:$repo){
    pullRequest(number:$pr){
      reviewThreads(first:100,after:$after){
        pageInfo{hasNextPage endCursor}
        nodes{
          id isResolved isOutdated path line originalLine
          comments(first:50){nodes{databaseId body url author{login} createdAt}}
        }}}}}'
```

Page with `-F after=<endCursor>` while `hasNextPage` is true. Keep threads
with `isResolved == false`. Also read the latest pr-review summary in the PR's
reviews (`gh api repos/<owner>/<repo>/pulls/<N>/reviews`) for "Findings
outside the diff", which have no thread; treat each as a finding without a
thread id.

For each finding record: thread id, first comment's author and URL, path,
line (`line`, or `originalLine` when outdated), summary, and severity. Take
the severity from the `<!-- pr-review: id=.. severity=.. -->` marker. For
threads without a marker (human reviewers), set severity to `unknown` and
read later comments in the thread too, since the discussion may have changed
what is asked.

If there are no unresolved findings, say so and stop.

## 3. Propose a decision for each finding

Read the code each finding points to before proposing anything. Propose:

- **fix**: blocking findings; small, low-risk nits in code this PR touches.
- **defer**: pre-existing bugs; nits that need a design change or touch code
  outside the PR's scope.
- **won't fix**: only when you can show the finding is wrong; give the reason.

Show one table:

| # | Severity | Reviewer | File:line | Summary | Proposed | Why |

Then let the author change it. With more than four findings, ask them to
reply in free text ("fix 2, 5; defer the rest; won't fix 4 because ...");
with four or fewer, AskUserQuestion with one question per finding is fine.

Rules:
- A `blocking` finding can be deferred or declined only with a reason from
  the author. Ask for it if missing.
- Every won't-fix needs a reason, as it goes in the reply.
- The author can always overrule your proposal.

## 4. Plan the backlog issues (only if something is deferred)

Ask once (AskUserQuestion), with the configured default first and marked
(Recommended):
- One issue for this PR: a checklist of all deferred findings
- One issue per finding
- Grouped: you propose groups (by file or theme) and the author edits them

The author can also pull a single finding into its own issue while the rest
stay grouped.

Look for duplicates before planning new issues:

```bash
gh issue list --label <label> --state open --json number,title,body --limit 100
```

If an open issue covers the same file and problem, propose adding to it (a
comment, or a new checklist item) instead of opening a new one.

## 5. Show the full plan and get one approval

Show, in one message:
- the fixes: what changes in which file, and the checks you will run
- the issues: the title of each, which findings go in it, or which existing
  issue gets a comment
- the replies: the text you will post on each thread, and which threads you
  will resolve
- that you will commit, push the PR branch, and post a summary comment

Ask: proceed / edit / stop. Do nothing outward-facing without "proceed".

## 6. Carry it out

In this order, so replies can link to real commits and issues.

**Fixes**
1. Make each fix. Run the repo's checks from `AGENTS.md`/`CLAUDE.md` (tests,
   linters, format checks). If a check fails and you cannot fix it, stop and
   tell the author; do not push.
2. Commit, one commit per finding unless several are one-line changes to the
   same file. Message: `fix(<area>): <summary> (review R<id>)`, with the
   commit attribution lines from the system reminders.
3. `git push`. Record each finding's commit SHA.

**Deferred findings**
1. Make sure the label exists:
   `gh label create <label> --color FBCA04 --description "Deferred from PR review" 2>/dev/null || true`
2. Create the issues with `gh issue create --label <label> --title ... --body-file <scratchpad file>`.
   Permalinks point at the PR head commit from step 1, so they stay correct
   after more commits:
   `https://github.com/<owner>/<repo>/blob/<headRefOid>/<path>#L<line>`

   Line numbers in a finding can be stale (the code moved after the review,
   or the reviewer got them wrong). Before writing a permalink, find the
   function or statement the finding names in the file at `headRefOid` and
   use its real line range.

   One-issue-per-PR body:
   ```
   Findings deferred from the review of #<N> (<PR title>).

   - [ ] **[nit] <summary>** — [<path>:<line>](<permalink>) · [thread](<comment url>)
     <what is wrong; when it goes wrong; suggested fix>
     Deferred because: <author's reason, if given>
   - [ ] ...
   ```
   Title: `Review backlog from #<N>: <PR title>`.

   One-per-finding body: the same fields as one checklist item, written out
   as sections. Title: the finding's summary.
3. Record the issue URL for each finding.

**Replies and resolving**

Reply on each thread:

```bash
gh api graphql -f query='mutation($id:ID!,$body:String!){
  addPullRequestReviewThreadReply(input:{pullRequestReviewThreadId:$id,body:$body}){comment{url}}}' \
  -f id=<thread id> -f body=<text>
```

- fix: `Fixed in <sha>.` plus one line on what changed if not obvious.
- defer: `Deferred to #<issue>: <reason>.`
- won't fix: `Not changing this: <reason>.`

Resolve the thread:

```bash
gh api graphql -f query='mutation($id:ID!){resolveReviewThread(input:{threadId:$id}){thread{isResolved}}}' -f id=<thread id>
```

Resolve every thread opened by pr-review (has the marker) or by the current
user. For threads opened by other people, resolve fixed and deferred ones,
but leave won't-fix threads open so the reviewer can answer.

**Summary comment**

```bash
gh pr comment <N> --body-file <scratchpad file>
```

```
Review addressed:
- Fixed (<n>): R1 (<sha>), R3 (<sha>)
- Deferred (<n>): R2, R4 → #<issue>
- Won't fix (<n>): R5 — <reason>
```

## 7. Report

Tell the author what was fixed (with commits), which issues were created or
updated (with links), which threads are still open and why, and any check
that failed. If anything failed partway (a push rejected, an API error), say
exactly which steps were done and which were not, so nothing is posted twice
on a rerun.

## Reviewer mode

Use steps 1 and 2 as above, then these steps instead of 3-7. In this mode
you do not change the PR's code, commit or push: the branch belongs to the
author. If the user wants a fix made on their behalf, say that is author
work and ask before doing it.

### R1. Sort the threads

Keep the unresolved threads whose first comment is by the current user.
List other people's threads in one line ("3 threads from <login> are left
alone") and do not touch them.

Read every comment after the first one in each thread and put the thread in
one of these states:

- **claims fixed**: the author says it is fixed, often naming a commit or a
  test.
- **declined**: the author explains why they will not change it, or that the
  finding was wrong.
- **question**: the author asks something or the discussion is open.
- **no reply**: nothing after the first comment.

### R2. Check the claims against the code

For each **claims fixed** thread, check the claim at `headRefOid`, not on
trust:
- the named commits exist (`git log -1 <sha>`) and are in the PR
  (`git merge-base --is-ancestor <sha> <headRefOid>`);
- the code now does what the reply says (read the function, not only grep);
- the named tests exist; run them if the repo's test command works here, and
  say so if it doesn't (missing tool, needs a license) rather than claiming
  they pass;
- for documentation changes, the docs say what the reply says.

Mark each one **verified**, **partly fixed** (say what is missing) or **not
found**.

For each **declined** thread, read the reason and the code, and say whether
the reason holds up. The user decides; you only advise.

### R3. Propose and let the user decide

Show one table:

| # | State | File:line | Finding | Check result | Proposed |

Proposals:
- verified: **resolve**, with reply `Verified in <short head sha>, thanks.`
- partly fixed or not found: **reply, leave open**, saying exactly what is
  still missing.
- declined, reason holds: **accept and resolve**, reply `OK, agreed.` or
  similar.
- declined, reason doesn't hold: **push back, leave open**, with the
  counter-argument.
- question: **answer, leave open**, with a drafted answer for the user to
  edit.
- no reply: **leave**; offer a nudge (`@<author> any update on this one?`)
  only if the user wants it.
- out of scope after discussion: **defer**, as in author mode step 4.

If the user also has findings that were never posted (for example from a
`/code-review` run earlier in the conversation), list them under the table
and ask what to do with them: put them in a backlog issue, post them on the
PR with the pr-review skill, or drop them.

Use AskUserQuestion with a recommended option when the choices are uniform
(for example "all 10 verified: reply and resolve?"); otherwise ask for free
text as in step 3.

### R4. Show the plan and get one approval

Same as step 5: the replies with their text, which threads get resolved and
which stay open, the backlog issues and what goes in each, and the summary
comment. Do nothing on GitHub without "proceed". An answer to an
AskUserQuestion in R3 that names the action ("Reply and resolve") counts as
that approval, as long as you then do only what the option said.

### R5. Carry it out

In this order:
1. Backlog issues, as in step 6 "Deferred findings" (label, duplicate check,
   permalinks at `headRefOid` with checked line numbers).
2. Replies and resolving, with the step 6 mutations. Resolve only the
   threads the plan says; leave the rest open with their replies.
3. One summary comment on the PR:

   ```
   Review follow-up:
   - Verified and resolved (<n>): <short list or "all earlier threads">; the fixes are in <sha>.
   - Still open (<n>): <thread links>, see replies.
   - Deferred (<n>): <what>, in #<issue>. Not needed for this PR.
   ```

   Leave out lines with nothing in them.

### R6. Report

Say which threads were resolved, which are still open and why, the issues
created (with links), what you could not check (for example tests you could
not run), and any line numbers you corrected. If something failed partway,
say exactly which replies and resolves went through, so a rerun does not
post twice.
