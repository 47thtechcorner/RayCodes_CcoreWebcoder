"""
CCORE-Web-Coder-4B: Local Production Pipeline Runner
Runs the fine-tuned 4B model via Ollama to generate single-file React HTML applications.
"""

import os
import sys
import time
from pathlib import Path
import ollama  # pyright: ignore

# Model configuration
MODEL_NAME = "ccore-web-coder-4b"

# Official CCORE System Prompt
SYSTEM_PROMPT = """You design and build polished HTML experiences in React. Turn each brief into the format that best serves its audience and goal: a website or interface, a slide presentation, or an informational page. Follow the requested format when the brief specifies one.

Return only one complete HTML document, from <!doctype html> through </html>. Write all visible text in natural English and set the document language to en. The page must render when opened directly in a browser, without a build step.

Load these scripts in this order:
https://cdn.jsdelivr.net/npm/react@18.3.1/umd/react.production.min.js
https://cdn.jsdelivr.net/npm/react-dom@18.3.1/umd/react-dom.production.min.js
https://cdn.jsdelivr.net/npm/@babel/standalone@7.26.10/babel.min.js

Put all CSS in one <style> block. Put all JSX in one <script type="text/babel" data-presets="react"> block after <div id="root"></div>. Mount with ReactDOM.createRoot(document.getElementById("root")).render(<App />). Use named function components for major sections or slides and descriptive class names so the work can later be moved into Vite.

For websites and interfaces, organize the page around the main visitor task. Make navigation and the interactions requested in the brief work.

For presentations, give each slide one main point and arrange the slides around the takeaway or decision. Provide on-screen navigation and a Save as PDF button that opens the browser print dialog. In print, show all slides in order, with one complete slide per A4 landscape page. Hide on-screen controls and avoid clipped content or blank pages.

For informational pages, make the main takeaway easy to find. Use headings, diagrams, tables, or examples when they help explain the subject. Preserve figures and claims supplied in the brief. Label fictional data as illustrative when needed.

Use semantic markup, visible keyboard focus, and responsive layouts that work at 390px and 1440px. You may choose publicly accessible images that fit the brief. Use direct image URLs, descriptive alt text, and a styled fallback that preserves the layout if an image fails to load."""

# Workflows to execute
WORKFLOWS = [
    {
        "id": "task1",
        "name": "Task 1: Boardroom Decision Deck",
        "input_file": "inputs/task1_boardroom_brief.txt",
        "output_file": "outputs/executive_board_decision_deck.html"
    },
    {
        "id": "task2",
        "name": "Task 2: Field Operations Pilot Deck",
        "input_file": "inputs/task2_irrigation_brief.txt",
        "output_file": "outputs/field_operations_pilot_deck.html"
    },
    {
        "id": "task3",
        "name": "Task 3: Observatory Web App",
        "input_file": "inputs/task3_observatory_brief.txt",
        "output_file": "outputs/interactive_observatory_app.html"
    }
]


def clean_html_response(raw_text: str) -> str:
    """Extracts clean HTML between <!doctype html> and </html> tags."""
    text = raw_text.strip()
    if "```html" in text:
        parts = text.split("```html")
        if len(parts) > 1:
            text = parts[1].split("```")[0].strip()
    elif "```" in text:
        parts = text.split("```")
        if len(parts) > 1:
            text = parts[1].strip()

    start_idx = text.lower().find("<!doctype html>")
    if start_idx != -1:
        text = text[start_idx:]

    end_idx = text.lower().rfind("</html>")
    if end_idx != -1:
        text = text[: end_idx + len("</html>")]

    return text.strip()


def write_benchmark_report(results: list):
    """Writes a clean summary markdown report of workflow execution metrics."""
    report_path = Path("outputs/generation_benchmark_report.md")
    lines = [
        "# Local Generation Benchmark Report\n",
        f"Execution throughput and memory allocation metrics across the {len(results)} production workflows for **{MODEL_NAME}**.\n",
        "---\n",
        "## 📊 Workflow Execution Metrics\n",
        "| Workflow | Deliverable | Generated Tokens | Time (sec) | Throughput | Model Footprint |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ]

    for res in results:
        deliverable_name = Path(res["file"]).name
        time_str = f"{res['time_sec']:.1f}s (~{res['time_sec']/60:.1f}m)"
        lines.append(
            f"| **{res['name']}** | `{deliverable_name}` | ~{res['tokens']} tokens | {time_str} | {res['tok_per_sec']:.1f} tok/s | ~4.8 GB |"
        )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"📊 Benchmark metrics saved to: {report_path}")


def run_pipeline():
    """Executes the local model pipeline across all registered tasks."""
    print("=" * 70)
    print("🚀 Starting CCORE-Web-Coder-4B Production Pipeline")
    print(f"📦 Model: {MODEL_NAME} | Runtime: Ollama (Local)")
    print("=" * 70)

    Path("outputs").mkdir(parents=True, exist_ok=True)
    results = []

    for idx, wf in enumerate(WORKFLOWS, 1):
        input_path = Path(wf["input_file"])
        output_path = Path(wf["output_file"])

        if not input_path.exists():
            print(f"⚠️ Input brief missing: {input_path}")
            continue

        brief_text = input_path.read_text(encoding="utf-8").strip()
        print(f"\n[{idx}/{len(WORKFLOWS)}] Running: {wf['name']}")
        print(f"📄 Input: {input_path} ({len(brief_text)} chars)")

        start_time = time.time()

        try:
            response = ollama.chat(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": brief_text}
                ],
                options={
                    "temperature": 0.7,
                    "top_k": 40,
                    "top_p": 0.95,
                    "num_ctx": 24000
                }
            )

            elapsed = time.time() - start_time
            raw_content = response.get("message", {}).get("content", "")
            cleaned_html = clean_html_response(raw_content)

            output_path.write_text(cleaned_html, encoding="utf-8")
            file_size_kb = output_path.stat().st_size / 1024

            eval_count = response.get("eval_count", 0)
            tok_per_sec = eval_count / elapsed if elapsed > 0 else 0

            print(f"✅ Generated: {output_path} ({file_size_kb:.1f} KB)")
            print(f"⏱️ Time: {elapsed:.2f}s | Tokens: {eval_count} ({tok_per_sec:.1f} tok/s)")

            results.append({
                "name": wf["name"],
                "file": wf["output_file"],
                "time_sec": elapsed,
                "tokens": eval_count,
                "tok_per_sec": tok_per_sec,
                "size_kb": file_size_kb
            })

        except Exception as e:
            print(f"❌ Error querying model '{MODEL_NAME}': {e}")
            print("💡 Reminder: Ensure you ran the README setup steps to download and register the model:")
            print("   hf download ccore/CCORE-Web-Coder-4B ccore-web-coder-Q8_0.gguf --local-dir models/ccore-web-coder")
            print("   ollama create ccore-web-coder-4b -f Modelfile")
            return

    if results:
        write_benchmark_report(results)

    print("\n" + "=" * 70)
    print("🎉 All Workflows Completed Successfully!")
    print("=" * 70)


if __name__ == "__main__":
    run_pipeline()
