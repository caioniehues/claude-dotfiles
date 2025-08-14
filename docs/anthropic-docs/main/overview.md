# Building with Claude

Source: https://docs.anthropic.com/en/docs/overview  
Scraped: 2025-08-14

This guide introduces Claude's enterprise capabilities, the end-to-end flow for developing with Claude, and how to start building.

## What you can do with Claude

Claude is designed to empower enterprises at scale with strong performance across benchmark evaluations for reasoning, math, coding, and fluency in English and non-English languages.

Here's a non-exhaustive list of Claude's capabilities and common uses.

| Capability | Enables you to… |
| --- | --- |
| Text and code generation | - Adhere to brand voice for excellent customer-facing experiences such as copywriting and chatbots<br>- Create production-level code and operate (in-line code generation, debugging, and conversational querying) within complex codebases<br>- Build automatic translation features between languages<br>- Conduct complex financial forecasts<br>- Support legal use cases that require high-quality technical analysis, long context windows for processing detailed documents, and fast outputs |
| Vision | - Process and analyze visual input, such as extracting insights from charts and graphs<br>- Generate code from images with code snippets or templates based on diagrams<br>- Describe an image for a user with low vision |
| Tool use | - Interact with external client-side tools and functions, allowing Claude to reason, plan, and execute actions by generating structured outputs through API calls |

## Enterprise considerations

Along with an extensive set of features, tools, and capabilities, Claude is also built to be secure, trustworthy, and scalable for wide-reaching enterprise needs.

| Feature | Description |
| --- | --- |
| **Secure** | - Enterprise-grade security and data handling for API<br>- SOC II Type 2 certified, HIPAA compliance options for API<br>- Accessible through AWS (GA) and GCP (in private preview) |
| **Trustworthy** | - Resistant to jailbreaks and misuse. We continuously monitor prompts and outputs for harmful, malicious use cases that violate our AUP.<br>- Copyright indemnity protections for paid commercial services<br>- Uniquely positioned to serve high trust industries that process large volumes of sensitive user data |
| **Capable** | - 200K token context window for expanded use cases, with future support for 1M<br>- Tool use, also known as function calling, which allows seamless integration of Claude into specialized applications and custom workflows<br>- Multimodal input capabilities with text output, allowing you to upload images (such as tables, graphs, and photos) along with text prompts for richer context and complex use cases<br>- Developer Console with Workbench and prompt generation tool for easier, more powerful prompting and experimentation<br>- SDKs and APIs to expedite and enhance development |
| **Reliable** | - Very low hallucination rates<br>- Accurate over long documents |
| **Global** | - Great for coding tasks and fluency in English and non-English languages like Spanish and Japanese<br>- Enables use cases like translation services and broader global utility |
| **Cost conscious** | - Family of models balances cost, performance, and intelligence |

## Implementing Claude

1. **Scope your use case**
   - Identify a problem to solve or tasks to automate with Claude.
   - Define requirements: features, performance, and cost.

2. **Design your integration**
   - Select Claude's capabilities (e.g., vision, tool use) and models (Opus, Sonnet, Haiku) based on needs.
   - Choose a deployment method, such as the Anthropic API, AWS Bedrock, or Vertex AI.

3. **Prepare your data**
   - Identify and clean relevant data (databases, code repos, knowledge bases) for Claude's context.

4. **Develop your prompts**
   - Use Workbench to create evals, draft prompts, and iteratively refine based on test results.
   - Deploy polished prompts and monitor real-world performance for further refinement.

5. **Implement Claude**
   - Set up your environment, integrate Claude with your systems (APIs, databases, UIs), and define human-in-the-loop requirements.

6. **Test your system**
   - Conduct red teaming for potential misuse and A/B test improvements.

7. **Deploy to production**
   - Once your application runs smoothly end-to-end, deploy to production.

8. **Monitor and improve**
   - Monitor performance and effectiveness to make ongoing improvements.

## Start building with Claude

When you're ready, start building with Claude:

- Follow the Quickstart to make your first API call
- Check out the API Reference
- Explore the Prompt Library for example prompts
- Experiment and start building with the Workbench
- Check out the Anthropic Cookbook for working code examples