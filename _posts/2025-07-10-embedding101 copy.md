---
layout: post
title: "What I learned from 100 hours into embedding search"
date: 2025-07-10
lang: en
published: false
---

I spend 100 hours into embedding search - the goal was to build an semantic search engine, but I ended up learning much more. I want to share what I learned, to save you some time when you are learning embedding. I'll bring cover the history of it, and then share the **best engineering suggestions and practices** I learned.


## Brief History of Embedding


![History of Major Milestones in Embedding]({{ '/assets/images/posts/embedding101_history.jpg' | relative_url }})


It's crucial to brief the history of embedding milestones concisely. I divided the history into x parts:



A Focused History of Embedding Search & RAG
Era 1: The Keyword Tyranny (Pre-2013)
This era serves as the baseline—what embedding search replaced.

The Technology: Traditional search engines relied on lexical search. They used inverted indexes, TF-IDF (Term Frequency-Inverse Document Frequency), and algorithms like BM25.

The Experience: You had to guess the exact keywords the document might contain. Searching for "how to fix a wobbly chair" would fail if the guide was titled "tightening the legs on your furniture." The search engine didn't understand that these meant the same thing. It was a system of matching strings, not concepts.

Era 2: The Semantic Dawn (c. 2013 - 2017)
This is when the core idea of modern search was born, directly thanks to the word embedding revolution.

The Milestone: The "Aha!" Moment with word2vec. After word2vec (2013) demonstrated that embeddings could capture meaning, researchers and engineers realized they could do more than just analyze words—they could search with them. By converting both the user's query and all the documents into embedding vectors, a search engine could find documents that were semantically similar, even if they didn't share any keywords.

The Challenge: This was computationally brutal. Calculating the distance between a query vector and millions of document vectors one-by-one (a "brute-force" or "k-nearest neighbor" search) was far too slow for real-time applications. The concept was there, but the technology wasn't ready to scale. Early semantic search was mostly confined to academic papers and small-scale tech demos.

Era 3: The Scaling Revolution (c. 2017 - 2021)
This era was all about solving the speed problem. This is when semantic search became a practical reality for large tech companies.

The Milestone: Approximate Nearest Neighbor (ANN) Search. The breakthrough was the popularization of algorithms that didn't find the perfect matches, but found extremely close matches with incredible speed. They trade a tiny amount of accuracy for a massive gain in performance.

The Tools that Built the Era:

Facebook AI Similarity Search (FAISS) (2017): When Facebook open-sourced FAISS, it was a game-changer. It provided a powerful, optimized library for high-speed ANN search that any skilled engineer could implement. Suddenly, you didn't need to be a Ph.D. in algorithms to build a vector search engine.

The Rise of "Two-Tower" Models: This neural network architecture became standard for retrieval. One "tower" (a neural network) encodes the user's query into an embedding. The other tower encodes the documents. The system is trained to make the embeddings for relevant query-document pairs as close as possible. This is the core architecture behind recommendations at YouTube and search at Google.

Era 4: The Democratization & "Vector Database" Era (c. 2021 - Present)
This era is about making large-scale retrieval accessible to everyone, not just a few tech giants.

The Milestone: The Rise of the Managed Vector Database. Companies like Pinecone, Weaviate, and Milvus emerged, offering vector search as a managed cloud service. This abstracted away the complexity of managing ANN indexes, scaling infrastructure, and filtering metadata. A developer could now add powerful semantic search to their application via a simple API call, dramatically lowering the barrier to entry.

The Impact: Startups and smaller companies could now easily build applications that were previously the exclusive domain of Big Tech: semantic product search, image similarity finders, music recommendations, and more.

Era 5: The LLM Fusion - The RAG Revolution (c. 2022 - Present)
This is the current, cutting-edge era where retrieval is no longer just the final answer; it's a critical component of a larger reasoning process.

The Problem: Large Language Models (LLMs) like GPT are amazing, but they have critical flaws: they hallucinate facts and their knowledge is frozen at the time of their training. They don't know about current events or your company's private data.

The Milestone: Retrieval-Augmented Generation (RAG). RAG was proposed as a concept earlier, but it became the definitive architecture for applied AI in 2022-2023. It's a simple but brilliant process:

Retrieve: When a user asks a question, don't send it directly to the LLM. Instead, use the question as a query for an embedding search over a database of trusted, up-to-date information (e.g., company docs, recent news, product manuals).

Augment: Take the top 3-5 most relevant documents from that search.

Generate: Prepend those documents to the user's original query as context, and then send the entire bundle to the LLM. The prompt now effectively says: "Using only the following information, answer this question: [user's question]."

The Impact: RAG is a revolution. It makes LLMs more factual, auditable (you can see the sources), and capable of using current information. It is the single most important architectural pattern for building reliable, enterprise-grade applications with generative AI today. It represents the perfect marriage of retrieval's ability to find and generation's ability to synthesize.

## Model Selection

## Vector Databases  vs Chunking

## Two-Stage Retrieval Process - Recall + Rerank
