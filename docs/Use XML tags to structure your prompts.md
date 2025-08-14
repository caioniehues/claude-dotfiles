---
title: "Use XML tags to structure your prompts"
source: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags"
author:
  - "[[Anthropic]]"
published:
created: 2025-08-14
description:
tags:
  - "clippings"
---
While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).

When your prompts involve multiple components like context, instructions, and examples, XML tags can be a game-changer. They help Claude parse your prompts more accurately, leading to higher-quality outputs.

**XML tip**: Use tags like `<instructions>`, `<example>`, and `<formatting>` to clearly separate different parts of your prompt. This prevents Claude from mixing up instructions with examples or context.

## Why use XML tags?

- **Clarity:** Clearly separate different parts of your prompt and ensure your prompt is well structured.
- **Accuracy:** Reduce errors caused by Claude misinterpreting parts of your prompt.
- **Flexibility:** Easily find, add, remove, or modify parts of your prompt without rewriting everything.
- **Parseability:** Having Claude use XML tags in its output makes it easier to extract specific parts of its response by post-processing.

There are no canonical “best” XML tags that Claude has been trained with in particular, although we recommend that your tag names make sense with the information they surround.

---

## Tagging best practices

1. **Be consistent**: Use the same tag names throughout your prompts, and refer to those tag names when talking about the content (e.g, `Using the contract in <contract> tags...`).
2. **Nest tags**: You should nest tags `<outer><inner></inner></outer>` for hierarchical content.

**Power user tip**: Combine XML tags with other techniques like multishot prompting (`<examples>`) or chain of thought (`<thinking>`, `<answer>`). This creates super-structured, high-performance prompts.

### Examples

---## [Prompt library](https://docs.anthropic.com/en/resources/prompt-library/library)

[

Get inspired by a curated selection of prompts for various tasks and use cases.

](https://docs.anthropic.com/en/resources/prompt-library/library)GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

[View original](https://github.com/anthropics/prompt-eng-interactive-tutorial)Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

[View original](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)