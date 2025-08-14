---
title: "Let Claude think (chain of thought prompting) to increase performance"
source: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought#example-writing-donor-emails-structured-guided-cot"
author:
  - "[[Anthropic]]"
published:
created: 2025-08-14
description:
tags:
  - "clippings"
---
While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).

When faced with complex tasks like research, analysis, or problem-solving, giving Claude space to think can dramatically improve its performance. This technique, known as chain of thought (CoT) prompting, encourages Claude to break down problems step-by-step, leading to more accurate and nuanced outputs.

## Before implementing CoT

### Why let Claude think?

- **Accuracy:** Stepping through problems reduces errors, especially in math, logic, analysis, or generally complex tasks.
- **Coherence:** Structured thinking leads to more cohesive, well-organized responses.
- **Debugging:** Seeing Claude’s thought process helps you pinpoint where prompts may be unclear.

### Why not let Claude think?

- Increased output length may impact latency.
- Not all tasks require in-depth thinking. Use CoT judiciously to ensure the right balance of performance and latency.

Use CoT for tasks that a human would need to think through, like complex math, multi-step analysis, writing complex documents, or decisions with many factors.

---

## How to prompt for thinking

The chain of thought techniques below are **ordered from least to most complex**. Less complex methods take up less space in the context window, but are also generally less powerful.

**CoT tip**: Always have Claude output its thinking. Without outputting its thought process, no thinking occurs!

- **Basic prompt**: Include “Think step-by-step” in your prompt.
	- Lacks guidance on *how* to think (which is especially not ideal if a task is very specific to your app, use case, or organization)
- **Guided prompt**: Outline specific steps for Claude to follow in its thinking process.
	- Lacks structuring to make it easy to strip out and separate the answer from the thinking.
	| Role | Content |
	| --- | --- |
	| User | Draft personalized emails to donors asking for contributions to this year’s Care for Kids program.      Program information:   <program>{{PROGRAM\_DETAILS}}   </program>      Donor information:   <donor>{{DONOR\_DETAILS}}   </donor>      Think before you write the email. First, think through what messaging might appeal to this donor given their donation history and which campaigns they’ve supported in the past. Then, think through what aspects of the Care for Kids program would appeal to them, given their history. Finally, write the personalized donor email using your analysis. |
- **Structured prompt**: Use XML tags like `<thinking>` and `<answer>` to separate reasoning from the final answer.
	| Role | Content |
	| --- | --- |
	| User | Draft personalized emails to donors asking for contributions to this year’s Care for Kids program.      Program information:   <program>{{PROGRAM\_DETAILS}}   </program>      Donor information:   <donor>{{DONOR\_DETAILS}}   </donor>      Think before you write the email in <thinking> tags. First, think through what messaging might appeal to this donor given their donation history and which campaigns they’ve supported in the past. Then, think through what aspects of the Care for Kids program would appeal to them, given their history. Finally, write the personalized donor email in <email> tags, using your analysis. |

### Examples

---## [Prompt library](https://docs.anthropic.com/en/resources/prompt-library/library)

[

Get inspired by a curated selection of prompts for various tasks and use cases.

](https://docs.anthropic.com/en/resources/prompt-library/library)GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

[View original](https://github.com/anthropics/prompt-eng-interactive-tutorial)Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

[View original](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)