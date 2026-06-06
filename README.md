# OpenVetCausal: Open-Source Causal AI Framework for Veterinary Medicine

OpenVetCausal is a local-first clinical assistant and research framework designed to apply **Causal AI** and inference models to veterinary medicine, specifically targeting dairy cattle reproductive health and metabolic management.

## Key Features (Under Development)
- **Causal Discovery & Intervention:** Moving beyond correlation to simulate counterfactuals (e.g., predicting the exact impact of nutritional changes on herd conception rates).
- **Local-First Privacy:** Tailored for agricultural enterprises and field clinics where data privacy and offline functionality are vital.
- **AI Scribe Integration:** Hands-free clinical note-taking via optimized local automatic speech recognition (ASR).

## Tech Stack
- **Causal Inference:** `DoWhy`, `CausalNex`
- **Speech Processing:** `Faster-Whisper` (Local Offline Transcription)
- **Interface:** `Streamlit` (Interactive Causal Graph Visualizer)

## Project Structure
- `app/causal_engine.py`: Defines the Structural Causal Model (SCM) for veterinary parameters.
- `app/audio_scribe.py`: Speech-to-text pipeline for unstructured clinical voice notes.
