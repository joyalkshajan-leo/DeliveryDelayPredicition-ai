# Smart Supply Chain Oracle


## Problem Statement
Logistics operations are highly susceptible to disruptions caused by traffic congestion, adverse weather, and inefficient route planning. These unpredictable challenges often result in delayed deliveries, increased operational costs, and severely reduced customer satisfaction. Existing logistics dashboards are reactive—they report delays after they occur rather than predicting and circumventing them.

## Project Description
The **Smart Supply Chain Oracle** is an AI-powered logistics optimization system that provides real-time, dynamic insights to supply chain managers. Simply by inputting source and destination locations, weather conditions, and live traffic levels, the system leverages a Machine Learning predictive model (Random Forest) to instantly forecast delivery delays and assign a risk confidence score. 

It features an intelligent routing backend that integrates open-source mapping APIs (Nominatim & OSRM) supplemented with custom geometric fallback heuristics (Haversine formula). This allows it to automatically calculate real-world driving distances, render live interactive route maps, and recommend smarter alternative shipments securely through a modern, responsive Glass-morphism UI dashboard.

## Google AI Usage
### Tools / Models Used
- **Google DeepMind / Gemini (AI Agentic Assistant):** Used extensively as an advanced autonomous pair-programmer.

### How Google AI Was Used
Google's advanced Agentic AI models were utilized to rapidly architect the structural foundation of the Flask backend, engineer the complex geometric fallback calculations for routing edge-cases, and dynamically design the aesthetic frontend user interface. The AI agent actively diagnosed pipeline errors, integrated third-party mapping APIs directly into the codebase, and fully automated the deployment staging for this hackathon prototype.

## Proof of Google AI Usage
*Screenshots of the AI's autonomous architectural generation and collaborative problem-solving are stored in the `/proof` folder.*
- [AI Assistant Workspace Proof](proof/ai-workspace.png)

## Screenshots
*(Make sure to upload actual images to your repository and link them here)*
---<img width="1362" height="927" alt="1" src="https://github.com/user-attachments/assets/6c590248-0d79-4e4c-bffb-3e5c09da8379" />
<img width="1291" height="909" alt="2" src="https://github.com/user-attachments/assets/b2c1de84-c82d-481f-8f88-21ed507d6aaa" />
<img width="909" height="624" alt="4" src="https://github.com/user-attachments/assets/fc7ad434-67f4-4a91-9c75-b43c0da860fe" />

<img width="1383" height="939" alt="send" src="https://github.com/user-attachments/assets/ce60abb6-42a2-4589-b5f8-615a36b19170" />
## Demo Video
Watch the full project walkthrough and live demonstration here (Under 3 minutes):






## Installation Steps


> **Note:** This project is built u
tilizing a Python backend (Flask), so the core dependencies are managed via `pip` instead of `npm`.

```bash
# Clone the repository
git clone <your-repo-link>

# Go to project folder
cd "our project"

# 1. Create a virtual environment (Optional but highly recommended)
python -m venv venv

# 2. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
# source venv/bin/activate

# 3. Install the required Python dependencies
pip install -r requirements.txt

# 4. Run the development server
python app.py
```

*Once running, open your web browser and navigate to `http://127.0.0.1:5000` to interact with the UI.*
