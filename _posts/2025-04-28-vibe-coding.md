---
layout: post
title: "Vibe Coding, Prompts, and New Thoughts"
date: 2025-04-28
lang: en
---

It's good to share some thoughts again!

# My Current AI Tools

Have been super busy and efficient these days. I love vibe coding! My current setup is:

- **Coding:** Cursor + Gemini 2.5 (95% of the time). Occasionally use Claude 3.7 + O3 for debugging, but it's more of the case that if Gemini can't debug, the rest can't either.
- **Production, Deployment:** Claude. Even for Google Cloud, which is pretty funny.
- **General Q&A:** ChatGPT (although I just unsubscribed).
- **Deep Research, Deep Thoughts:** Gemini 2.5.

## Overall Comparison

**Gemini 2.5** is currently the best model. It naturally mirrors my coding style.
I've done "vibe coding" using Claude 3.5 and 3.7 — roughly 100k lines of meaningful code — but I much prefer the feel of Gemini 2.5 now.

However, Gemini still has some app-side bugs: sometimes it loses context mid-session, which is very disturbing. That said, it produces the least hallucinations compared to others.

**Claude 3.7** is best at agentic tasks.
For example, when I work with Google Cloud, Claude often generates shell commands and configuration instructions better and faster than Gemini 2.5, especially on the first attempt.

**ChatGPT** still dominates in simple, casual Q&A.
However, I unsubscribed recently because the tone shifted — it became overly "flirty" and non-official, which made me uncomfortable for my use cases. I do like the question-asking style for continuing the conversations. It also seems to use some GPU that are extremley slow that really triggers me.

---

# Prompting — the Art of Letting Go

One of the most helpful rules I set up in Cursor is:

> **"Don't over-engineer. Favor simple logic and common industry solutions."**

This reflects a bigger principle I've observed:
**Less is more** — Simplicity is the ultimate solution for fast iterations and stability, just like all beautiful mathematical equations.

As AI models become stronger, I've noticed that effective prompting often leans toward *minimalism* — or what Andrew Ng calls **Lazy Prompting** ([link](https://x.com/AndrewYNg/status/1907843984158036137)):

> Copy-paste error messages — sometimes pages of them — into an LLM without any extra framing or instructions.

Extending that idea:
For many tasks, copy-paste a large context but a simple instruction is enough. That's usually my first strategy now — *"give less, get more."*

However, when AI behavior starts diverging from your intent (especially in coding or multi-step tasks), you must become hyper-precise.

At that point, **only exact words** — exact descriptions — will reliably get what you want.

Interestingly, I've noticed that word comprehension across different models is starting to converge.

## Do you need to understand the generated code?

One key question to ponder: **Do you need to fully understand the AI-generated code?**

My personal philosophy:

- **High level:** Absolutely yes. You must understand the overall design, flow, architecture, and data structures — otherwise you are flying blind.
- **Low level:** Let go most part. You don't need to micro-read every helper function unless it is part of the **core algorithm**, **agent loop**, or **critical performance path**. Those parts demand deep understanding.

For me, the real art is knowing **when to dive deep** and **when to trust AI**.
I enjoy discussing architecture and data structure design for hours — that's where most of the thinking should happen.
Once the structure is clear, actual implementation often takes far less time.

So, the workflow is usually:

1. **Design** — Discuss ideas with ChatGPT / Gemini, for however long you need.
2. **Code Architecture** — Discuss with Gemini / Claude, for 10-15 minutes.
3. **Implementation** — Let AI write the code, usually fast, maybe 30s to 2 minutes. Unless some unexpected code (which usually is due to my bad instructions).
4. **Debug** — Try paste the error trace into AI first, and if it is a hard bug, open a web page and debug together with Gemini 2.5.
5. Go back to 1 and iterate.

## Can I still code?

I once worried: after relying so heavily on AI for code generation, maybe I couldn't write code independently anymore.

I was wrong.

I can still write good code, with good quality and good performance.

The proof is that I'm taking the Stanford cs336, building LLM from scratch, a extremly coding intensive course, and recommended not to use AI. I've done a fairly good job in doing the assignments.

---

# Thought Experiment

Imagine you are struck by amnesia and consistently lose your recent memory, but maintain your intelligence and language skills. Basically, you don't have a sense of time anymore.

If someone else gave you a task, would you be able to solve it?

This is a good way to think about how to use AI and how to build agents:

- Provide just enough instruction and tooling.
- Keep the logic simple and composable, so losing memory won't cause catastrophic failure.
- Memory management (and context management) is key.

My current key formula of successful agents:

> **Successful Agent = Good Prompting + Simple Loop + Good Memory Management**

---

#AI #Coding #Prompting #AITools #SoftwareEngineering #Programming #TechThoughts #Gemini #Claude #ChatGPT #CursorAI #ArtificialIntelligence