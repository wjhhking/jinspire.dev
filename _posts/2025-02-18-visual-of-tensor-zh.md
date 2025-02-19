---
layout: post
title: "图解大模型生成过程"
date: 2025-02-18
lang: zh
---

# 让我们先看矩阵乘法

注意两个矩阵的维度是如何匹配的，这种模式在transformer中被广泛使用。

![mat_mul]({{ '/assets/images/posts/mat_mul.png' | relative_url }})

# 图例说明

我们将使用蓝色表示输入数据，灰色表示模型权重，蓝色再次表示输出数据。

![legend_of_tensors]({{ '/assets/images/posts/legend_of_tensors.png' | relative_url }})

# 嵌入层

我们选择GPT-2作为分析对象，它是一个很好的示例模型。

![embedding_layer]({{ '/assets/images/posts/embedding_layer.png' | relative_url }})

# Transformer块

![transformer_block]({{ '/assets/images/posts/transformer_block.png' | relative_url }})

# 整个过程

![transformer_tensors]({{ '/assets/images/posts/transformer_tensors.png' | relative_url }})

# 模型参数

所有的transformer模型都有类似的结构，只是层数、d_model、d_head等参数不同。（最新的研究致力于使用不同的注意力机制（如MLA）来减少参数总数，这不是本文的重点。）

注意：以下参数是由AI辅助生成，尚未经过仔细的人工验证。

# Llama系列
![llama_parameters]({{ '/assets/images/posts/llama_parameters.png' | relative_url }})

# Qwen系列
![qwen_parameters]({{ '/assets/images/posts/qwen_parameters.png' | relative_url }})

# DeepSeek系列
![deepseek_parameters]({{ '/assets/images/posts/deepseek_parameters.png' | relative_url }})

# ChatGPT系列
![chatgpt_parameters]({{ '/assets/images/posts/chatgpt_parameters.png' | relative_url }})

# 其他
鉴于Claude和Gemini是闭源的，仅展示对其参数的猜测并没有太大价值。同样地，对于刚刚发布的Grok-3，让我们拭目以待！

