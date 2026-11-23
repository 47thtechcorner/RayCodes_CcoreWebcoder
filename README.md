<div align="center">
  <a href="https://youtu.be/GaZ4j-Ww2-A">
    <img src="https://img.youtube.com/vi/GaZ4j-Ww2-A/maxresdefault.jpg" alt="Qwen WebCoder 4B: This Tiny AI Builds Complete React Apps in 1-Shot!">
  </a>
  <h3>📺 <a href="https://youtu.be/GaZ4j-Ww2-A">Watch the full video on YouTube</a></h3>
</div>

# CCORE-Web-Coder-4B: Zero-Build React & Single-File Web Generator

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Architecture: Qwen3.5-4B](https://img.shields.io/badge/Architecture-Qwen3.5--4B--Base-purple.svg)](https://huggingface.co/Qwen/Qwen3.5-4B-Base)
[![Format: GGUF Q8_0](https://img.shields.io/badge/Format-GGUF%20Q8__0%20(4.48%20GB)-emerald.svg)](https://huggingface.co/ccore/CCORE-Web-Coder-4B)
[![Local Footprint](https://img.shields.io/badge/Local%20VRAM-6GB--8GB-orange.svg)](#quick-start-windows-powershell)

> "CCORE-Web-Coder-4B turns raw conversational briefs into complete, browser-ready single-file React web applications, interactive slide decks with native A4 print-to-PDF formatting, and structured reports in a single inference pass—without any build steps or npm bundling."

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
| :--- | :--- | :--- | :--- |
| **Boardroom Decision Deck** | Multi-slide deck with A4 print-to-PDF rules | Fleet costs and route delay notes | Board deck with split decision cards |
| **Field Operations Pilot Deck** | Strict numerical accuracy with visual telemetry bars | Sensor notes and 60-person survey data | Operational deck with comparison bars |
| **Observatory Web App** | Single-file React app with interactive state and modal | Stargazing event and telescope brief | Responsive celestial web app with star map |

---

## ⚡ Quick Start (Windows PowerShell)

### Step 1: Setup Environment, Download Weights & Register Runtime

Run this combined setup block to create your environment, download the official 4.48 GB Q8_0 GGUF weights, and register the model with your local runtime:

```powershell
# 1. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install ollama huggingface_hub

# 3. Download official CCORE-Web-Coder-4B Q8_0 GGUF weights
hf download ccore/CCORE-Web-Coder-4B ccore-web-coder-Q8_0.gguf --local-dir models/ccore-web-coder

# 4. Register local model in Ollama
ollama create ccore-web-coder-4b -f Modelfile
```

### Step 2: Run Production Pipeline

Execute the full generation pipeline across your local test cases:

```powershell
python main.py
```

---

## 🎯 Practical Use Cases

- ⚡ **Instant Client Prototyping**: Turn one-sentence client briefs into fully functioning, clickable React web applications during live client discovery sessions.
- 📑 **Offline Board Presentation Decks**: Generate confidential executive slide decks with built-in A4 landscape pagination and print-to-PDF export without exposing private company numbers to cloud APIs.
- 📊 **Telemetry & Operations Dashboards**: Convert messy sensor logs or internal metrics into styled single-file status dashboards that run in any modern browser without web servers.
- 🌐 **Zero-Build Micro-Sites**: Create standalone landing pages, event micro-portals, or interactive surveys ready for instant distribution over local networks or USB drives.
- 🛡️ **Air-Gapped Developer Workstations**: Deliver full-stack prototyping capabilities to air-gapped defense, healthcare, and enterprise banking environments without external package dependencies.

---

## 🔮 Future Feature Roadmap

- 🚀 **Multi-Page Site Stitching**: Generate linked multi-page HTML architectures with client-side hash routing in a single cohesive pass.
- 🎨 **Direct Tailwind & CSS Variable Themes**: Add configurable color palettes and design token bridges for instant company re-skinning.
- 🧩 **Native Data Visualization Components**: Expand built-in SVG and Canvas interactive charting primitives for complex financial time series.
- 🔍 **Interactive Code Inspector Overlay**: Embed a collapsible drawer showing JSX component hierarchy and Vite migration helpers directly inside generated pages.
- ⚡ **Automated VRAM Benchmark Profiler**: Measure per-token latency and memory headroom across different consumer GPU quantization tiers.
---

## 🏷️ Search Tags
`ccore web coder`, `ccore-web-coder-4b`, `ccore coder`, `ccore 4b`, `ccore ai`, `qwen 3.5 4b`, `qwen 4b coder`, `qwen gguf`, `ccore qwen3.5`, `qwen3.5 gguf`, `qwen3.5 ollama`, `qwen3.5 4b finetune`, `ccore qwen`, `qwen ollama`, `qwen3.5 antigravity`, `qwen3.5 local`, `qwen3.5 4b`, `qwen coder local`, `qwen3.5 coder`, `qwen coder`, `qwen 4b`, `ai website generator`, `bolt alternative`, `local lovable`, `lovable alternative`, `react website ai`, `ai website builder`, `ai app builder`, `react ai`, `build website with ai`
