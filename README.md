# Flood_Forecast_Resolve 🌊

## 🌟 Project Objective

The primary objective of **Flood\_Forecast\_Resolve** is to save lives by developing a proactive, end-to-end disaster management intelligence system focused on **flood and fire prediction and dynamic safety path generation**.

This multi-agentic system leverages advanced satellite imagery analysis and machine learning to provide accurate, timely forecasts and translates that intelligence directly into actionable, life-saving guidance for citizens and disaster management organizations (DMOs).

## 💡 Challenges Addressed

This project tackles critical issues in traditional disaster response by aiming to bridge the gap between scientific prediction and practical, on-the-ground response:

1.  **Late Warning & Response:**
    * **Solution:** Providing significant **lead time** (hours to days) before an event by continuously monitoring precipitation, soil saturation, water bodies (for floods), and temperature/vegetation indices (for fires) using satellite data.
2.  **Lack of Actionable Guidance:**
    * **Solution:** Moving beyond simple "danger zone" maps to generate **dynamic, customized "Paths to Safety."** These routes are calculated in real-time to avoid roads that are already cut off or are projected to be impassable, guiding people to designated safe, elevated shelters.
3.  **Inefficient Resource Allocation:**
    * **Solution:** Delivering a **Common Operating Picture (COP)** to DMOs, showing real-time hazard extent, population density in affected areas, and critical infrastructure vulnerability, enabling strategic resource pre-positioning.

---

## 🤖 Multi-Agentic System Architecture

The **Flood\_Forecast\_Resolve** solution operates as a **Multi-Agentic System**, where specialized, independent software agents work in concert to predict threats, communicate warnings, and provide tailored resolutions.

### 1. The Alert Agent (Live Public Communication)

This agent is responsible for **immediate and widespread dissemination** of time-critical information and warnings directly to the public through common platforms.

* **Function:** Delivers **live, geo-targeted alerts** and mandatory evacuation notices.
* **Channels:** Integrates with platforms like **Social Media, WhatsApp, Email/Gmail, and SMS** gateways to ensure maximum reach, especially to high-risk populations.
* **Goal:** Maximize citizen awareness and minimize time-to-action during an escalating event.

### 2. The Information Agent (User Reports & Q\&A)

This agent serves as the primary interface for personalized information requests and detailed local reporting.

* **Function:** Operates as a **conversational chatbot** or automated service where users can input their precise location (e.g., "My home address is X") and ask for **localized reports** on the current hazard status, proximity to danger, and general safety tips.
* **Goal:** Reduce panic by providing trustworthy, on-demand, and tailored information about their immediate surroundings.

### 3. The Core Prediction & Resolution Agent (The Engine)

This is the central engine of the system, responsible for the high-level computation, modeling, and output of the life-saving guidance.

* **Function:**
    * **Forecasting:** Ingests and processes **Satellite Imagery** (Sentinel, Landsat) and sensor data to run **Deep Learning/Machine Learning models** that predict the precise location and timing of the flood or fire event.
    * **Safe Route Generation:** Utilizes **GIS and Routing Algorithms** alongside **Digital Elevation Models (DEMs)** to calculate the **fastest, safest, and most viable path** from a threatened location to the nearest safe zone.
* **Goal:** Provide the core intelligence (maps, boundaries, and routes) that powers the Alert and Information agents, and directly supports Disaster Management Organizations.












Technical Requirements:
1) use Python: 3.12
2) Environment Management: Conda
3) Dependencies: Listed in requirements.txt
4) get groq api key from https://console.groq.com/keys
