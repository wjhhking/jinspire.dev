---
layout: post
title: "Visualize Generation in LLM"
date: 2025-02-18
lang: en
---

# Visualize Matrix Multiplication

Let's visualize matrix multiplication first. Note how the dimensions of the two matrixs are matched, and similar patterns are used in the transformer. 

![mat_mul]({{ '/assets/images/posts/mat_mul.png' | relative_url }})

# Legend

We will use blue to represent the input data, grey to represent the model weight, and blue again to represent the output data.

![legend_of_tensors]({{ '/assets/images/posts/legend_of_tensors.png' | relative_url }})

# Embedding Layer

Still GPT-2 small, which is a good model to do analysis.

![embedding_layer]({{ '/assets/images/posts/embedding_layer.png' | relative_url }})


# Transformer Block

![transformer_block]({{ '/assets/images/posts/transformer_block.png' | relative_url }})

# The Whole Process

![transformer_tensors]({{ '/assets/images/posts/transformer_tensors.png' | relative_url }})


# Parameters of Models

All the transformer models have a similar structure, just different number of layers, d_model, d_head, etc. Latest research aims to reduce the total number of parameters using different attention mechanisms (e.g., MLA), which is not the focus of this article.

*Note below tables are assisted by AI, and not manually verified carefully.*

# Llama Family
![llama_parameters]({{ '/assets/images/posts/llama_parameters.png' | relative_url }})

# Qwen Family
![qwen_parameters]({{ '/assets/images/posts/qwen_parameters.png' | relative_url }})

# DeepSeek Family
![deepseek_parameters]({{ '/assets/images/posts/deepseek_parameters.png' | relative_url }})


# ChatGPT Family
![chatgpt_parameters]({{ '/assets/images/posts/chatgpt_parameters.png' | relative_url }})

# Other
Given Claude and Gemini are closed source, it does not provide much value just showing the guesses. Same for Grok, Grok-3 just got released. Let's wait and see!

