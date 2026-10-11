# Submission checks

Read current upstream instructions before choosing a channel.
A GitHub mirror can accept only mailing-list patches or problem reports.
Use a topic branch and a fork when upstream branch access is absent.
Inspect remotes without exposing embedded credentials.
Preserve unrelated changes, authorship, licenses, and private material.

Retain a failing-before and passing-after regression for a code repair.
A port needs build, installed-consumer, and runtime evidence.
A package claim also needs install, remove, and reinstall checks.
Documentation needs command and link checks.
Record unavailable validation separately from failures.
Use drafts only when the target permits them.

Lead the description with the problem and resulting behavior.
Use the repository template.
Include tested revision, platform, tools, commands, results, limits, and provenance.
Address reviews in the same contribution.
Report prepared, submitted, reviewed, merged, or released state accurately.

Keep EmberBSD integration in the project change.
Prepare a minimal upstream patch against upstream's accepted base.
Test that patch separately.
Cross-link authorized submissions.
Use an authorized issue for a reproduced bug without a fix.

Read current [pkgsrc submission rules](https://www.netbsd.org/docs/pkgsrc/submit.html).
Read the [NetBSD AI policy](https://www.netbsd.org/developers/commit-guidelines.html) before submission.
The 2026-10-06 policy required prior written core approval for committing LLM-generated code.
Recheck that rule.
Disclose assistance.
Tests do not replace the accepting project's approval.
