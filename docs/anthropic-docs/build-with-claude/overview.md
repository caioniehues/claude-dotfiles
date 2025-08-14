# Build with Claude - Overview

**Source:** https://docs.anthropic.com/en/docs/build-with-claude/overview
**Scraped on:** 2025-08-14

## Core capabilities

These features enhance Claude's fundamental abilities for processing, analyzing, and generating content across various formats and use cases.

| Feature | Description | Availability |
| --- | --- | --- |
| [1M token context window](https://docs.anthropic.com/en/docs/build-with-claude/context-windows#1m-token-context-window) | An extended context window that allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases. | Anthropic API (Beta)<br>Amazon Bedrock (Beta) |
| [Batch processing](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing) | Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls costs 50% less than standard API calls. | Anthropic API<br>Amazon Bedrock<br>Google Cloud's Vertex AI |
| [Citations](https://docs.anthropic.com/en/docs/build-with-claude/citations) | Ground Claude's responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. | Anthropic API<br>Amazon Bedrock<br>Google Cloud's Vertex AI |
| [Extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) | Enhanced reasoning capabilities for complex tasks, providing transparency into Claude's step-by-step thought process before delivering its final answer. | Anthropic API<br>Amazon Bedrock<br>Google Cloud's Vertex AI |
| [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files) | Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files. | Anthropic API (Beta) |
| [PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support) | Process and analyze text and visual content from PDF documents. | Anthropic API<br>Amazon Bedrock<br>Google Cloud's Vertex AI |
| [Prompt caching (5m)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) | Provide Claude with more background knowledge and example outputs to reduce costs and latency. | Anthropic API<br>Amazon Bedrock<br>Google Cloud's Vertex AI |
| [Prompt caching (1hr)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration) | Extended 1-hour cache duration for less frequently accessed but important context, complementing the standard 5-minute cache. | Anthropic API |
| [Search results](https://docs.anthropic.com/en/docs/build-with-claude/search-results) | Enable natural citations for RAG applications by providing search results with proper source attribution. Achieve web search-quality citations for custom knowledge bases and tools. | Anthropic API<br>Google Cloud's Vertex AI |
| [Token counting](https://docs.anthropic.com/en/api/messages-count-tokens) | Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. | Anthropic API<br>Google Cloud's Vertex AI |
| [Tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) | Enable Claude to interact with external tools and APIs to perform a wider variety of tasks. For a list of supported tools, see [the Tools table](https://docs.anthropic.com/en/docs/build-with-claude/overview#tools). | Anthropic API<br>Amazon Bedrock<br>Google Cloud's Vertex AI |

## Tools

These features enable Claude to interact with external systems, execute code, and perform automated tasks through various tool interfaces.

| Feature | Description | Availability |
| --- | --- | --- |
| [Bash](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/bash-tool) | Execute bash commands and scripts to interact with the system shell and perform command-line operations. | Anthropic API<br>Amazon Bedrock<br>Google Cloud's Vertex AI |
| [Code execution](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool) | Run Python code in a sandboxed environment for advanced data analysis. | Anthropic API (Beta) |
| [Computer use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use-tool) | Control computer interfaces by taking screenshots and issuing mouse and keyboard commands. | Anthropic API (Beta)<br>Amazon Bedrock (Beta)<br>Google Cloud's Vertex AI (Beta) |
| [Fine-grained tool streaming](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming) | Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters. | Anthropic API<br>Google Cloud's Vertex AI |
| [MCP connector](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector) | Connect to remote [MCP](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) servers directly from the Messages API without a separate MCP client. | Anthropic API (Beta) |
| [Text editor](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool) | Create and edit text files with a built-in text editor interface for file manipulation tasks. | Anthropic API<br>Amazon Bedrock<br>Google Cloud's Vertex AI |
| [Web search](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool) | Augment Claude's comprehensive knowledge with current, real-world data from across the web. | Anthropic API |

Was this page helpful?

YesNo

[Building with Claude](https://docs.anthropic.com/en/docs/overview) [Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)