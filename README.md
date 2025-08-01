![Project Status](https://img.shields.io/badge/Status-Alpha-orange)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Java](https://img.shields.io/badge/Java-17-red?logo=java)
![React](https://img.shields.io/badge/React-Frontend-blue?logo=react)
![Docker Image Version](https://img.shields.io/badge/Docker%20Image-latest-blue?logo=docker)
![CI](https://github.com/abhishekmaity/BhashaMind/actions/workflows/test.yml/badge.svg)
![License](https://img.shields.io/github/license/abhishekmaity/BhashaMind)
![Language](https://img.shields.io/badge/Language-Bengali-yellowgreen)
![Model](https://img.shields.io/badge/Model-LLM%2FTransformers-9cf?logo=huggingface)
![Tasks](https://img.shields.io/badge/NLP-Summarization%20%7C%20Classification-purple)
![Zero-Shot](https://img.shields.io/badge/Inference-Zero--Shot%20Enabled-ff69b4)
![Architecture](https://img.shields.io/badge/Architecture-Microservices-informational?logo=springboot)

# *Bhasha*Mind: A Bengali Language Intelligence Platform

![BhashaMind Banner](docs/banner-short.png)

BhashaMind (ভাষাMind) is an open-source Bengali language processing prototype focused on **text summarization** and **zero-shot classification** using state-of-the-art deep learning and LLM technologies. It integrates a full-stack application built with **FastAPI**, **Spring Boot**, and **React**, designed for real-world applications.

## 🌟 Project Highlights

- 🔤 **Low-Resource Bengali NLP**: Tailored for Bengali, one of the least-resourced languages in NLP.
- 🧠 **Transformer-powered**: Uses multilingual LLMs like `xlm-roberta` and optionally fine-tuned `BanglaT5`.
- 🧩 **Microservices Architecture**: Spring Boot API gateway + FastAPI backend + React frontend.
- 🧪 **Full-stack Pipeline**: Data ingestion → Summarization/Classification → Evaluation → UI interaction.

## 🏗️ Architecture

![Architecture](docs/sys-architecture.png)

- **Frontend:** ReactJS + TailwindCSS
- **API Gateway:** Java Spring Boot
- **NLP Backend:** Python FastAPI with HuggingFace Transformers
- **Model Training:** PyTorch-based scripts for fine-tuning
- **Dataset:** Placeholder Bengali datasets (summarization/classification)
<small>

## 🧪 Sample Usage

### 🔹 Summarization API
**Request** (`POST /api/summarize`):
```json
{
  "text": "জাতিসংঘের মহাসচিব আন্তোনিও গুতেরেস বলেছেন, জলবায়ু পরিবর্তনের প্রভাব এখন বৈশ্বিক সংকটের রূপ নিয়েছে। আফ্রিকা, এশিয়া ও লাতিন আমেরিকার বহু দেশ ভয়াবহ খরার সম্মুখীন হচ্ছে, যেখানে খাদ্য ও পানির তীব্র সংকট দেখা দিয়েছে। গুতেরেস উন্নত দেশগুলোকে কার্বন নিঃসরণ কমাতে জরুরি পদক্ষেপ নেওয়ার আহ্বান জানান।"
}
```
**Response**:
```json
{
  "summary": "জাতিসংঘ মহাসচিব গুতেরেস জানান, জলবায়ু পরিবর্তন বৈশ্বিক সংকটের রূপ নিয়েছে এবং উন্নত দেশগুলোকে কার্বন নিঃসরণ কমাতে হবে।"
}
```

### 🔹 Classification API
**Request** (`POST /api/classify`):
```json
{
  "text": "বিশ্বব্যাপী অর্থনৈতিক প্রবৃদ্ধি ধীর হয়ে পড়েছে। আন্তর্জাতিক মুদ্রা তহবিল (IMF) জানিয়েছে যে মুদ্রাস্ফীতি, উচ্চ সুদের হার এবং রাশিয়া-ইউক্রেন যুদ্ধের প্রভাব বৈশ্বিক অর্থনীতিতে দীর্ঘমেয়াদি নেতিবাচক প্রভাব ফেলছে। উন্নয়নশীল দেশগুলোতে খাদ্য ও জ্বালানির দাম বেড়ে যাওয়ায় সাধারণ মানুষের উপর চাপ বৃদ্ধি পাচ্ছে।"
}
```
**Response**:
```json
{
  "label": "economy"
}
```
</small>

## 🤖 Models Used
| Task           | Model Name                               | Reference/Link                              |
|----------------|------------------------------------------|---------------------------------------------|
| Summarization  | `csebuetnlp/banglat5-small`              | [BanglaT5 - Hugging Face](https://huggingface.co/csebuetnlp/banglat5_small) |
| Classification | `joeddav/xlm-roberta-large-xnli`         | [XLM-RoBERTa - Hugging Face](https://huggingface.co/joeddav/xlm-roberta-large-xnli) |

> **Note:** Bengali is supported by XLM-R via multilingual training and subword tokenization.

## 📚 References & Resources
- [FastAPI](https://fastapi.tiangolo.com)
- [Transformers by HuggingFace](https://huggingface.co/transformers)
- [XLM-RoBERTa](https://arxiv.org/abs/1911.02116)
- [BanglaT5](https://aclanthology.org/2023.findings-eacl.54.pdf)

## 📜 Citing

If you use this, please include the following citation:

Maity, A. (2025) *“A Low-Resource Bengali Language Intelligence Platform for Summarization and Zero-Shot Classification”*. **Zenodo**. DOI:[10.5281/zenodo.16434434](https://doi.org/10.5281/zenodo.16434434)

```
@misc{maity2025bhashamind,
  author       = {Maity, Abhishek},
  title        = {A Low-Resource Bengali Language Intelligence Platform for Summarization and Zero-Shot Classification},
  year         = {2025},
  publisher    = {Zenodo and {CERN}},
  doi          = {10.5281/zenodo.16434434},
  url          = {https://doi.org/10.5281/zenodo.16434434},
  language     = {en}
}
```

## 📄 License
This project is licensed under the **MIT License**.

## Disclaimer

<img src="https://avatars.githubusercontent.com/in/842251?v=4&size=30"> **Google Jules** was used for fixing errors in the Continuous Integration (CI) workflow of this repository.

---

> Made with ❤️ and code.
