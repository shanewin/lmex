# LMeX: Learning Management Exchange 🎓🚀

> **A Next-Gen Financial Literacy Platform for Student Communities**  
> *Gamified Social Learning • Web3 Identity • Biometric Verification*

![Status](https://img.shields.io/badge/Status-Prototype-success) ![Stack](https://img.shields.io/badge/Stack-Django%20%7C%20Web3%20%7C%20Biometrics-blue)

**LMeX** is a gamified, Blockchain-based Learning Management System with specialization towards alternative K12 educational programs, such as afterschool and adult learner programs. It leverages **Biometrics** for secure attendance and **Web3** for a tokenized internal economy with NFTs and bespoke ERC-20 reward tokens to incentivize students to engage in learning activities and serve as evergreen records of student achievement. 

---

## Project Context

Built as technical lead for a Web3 EdTech startup's enterprise pilot program. Deployed to 3 different educational programs Flint, Chicago, and Seattle with customized curriculums.

**Status:** Archived pilot project (2022-2023). Code demonstrates production Django architecture, Web3 integration patterns, and complex feature development.

| **LMS Class Feed** | **Student Dashboard** |
|:---:|:---:|
| ![LMS](screenshots/lms-student.png) | ![Profile](screenshots/profile_dashboard.png) |
| *Instructor Moderated Message Board* | *Wallet, Identity & Leaderboard* |
| **Biometric Verification** | **NFT Class Identity** |
| ![Biometrics](screenshots/facial_recognition.png) | ![Mint NFT](screenshots/mint_nft.png) |
| *Login & Attendance Verification* | *Minting NFT for Authentication* |

---

## 🛠 Modular Architecture

- **`users/`:** 
  - Manages Custom User Models, Auth, and Wallet integration.
  - Generates verifiable "Web3 ID" Cards (NFTs) which serve as student profile. 
  
- **`lms/`:**
  - The "Learning Management System" engine.
  - Class/Curriculum/Program set up with custom ERC-20 smart contract for tokenization and verifiability on the blockchain.
  - Handles Posts, Units, Replies, and the "Token Gating" logic (pay-to-view).
  - Game mechanics for contributions with rewards from fellow students and instructors for quality class contributions. 
  
- **`biometrics/`:**
  - Handles webcam sessions for secure login and class attendance verification.


---

## 🚀 Quick Start (Docker)

The recommended way to run LMeX is via Docker to handle complex dependencies (`psycopg2`, `dlib`) automatically.

### 1. Clone & Configure
```bash
git clone https://github.com/your-repo/lmex.git
cd lmex
cp .env.example .env
```
*Tip: The `.env.example` comes pre-configured for local dev.*

### 2. Launch
```bash
docker-compose up --build
```
The app will launch at `http://localhost:8000`.

---

## 💻 Manual Setup (Local Dev)

If you prefer running without Docker (e.g., for rapid frontend iteration):

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: This installs all "Safe" dependencies. ML libraries are optional.*

2. **Run Migrations & Server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

3. **Mock Mode (Automatic)**
   If `face_recognition` or `Web3` libraries are missing, the app automatically enters **Mock Mode**:
   - Biometric scans simulates "Success."
   - Wallet balances show dummy ETH/Tokens.
   - *No crashes, perfect for UI development/Demoing.*

---

## 🔒 Security Highlights
- **No Private Keys:** Migration `0048` permanently removed all private key storage.
- **Environment config:** All secrets (Infura, Django Secret) are loaded from `.env`.
- **Mock Fallbacks:** Critical user paths gracefully degrade if external services are offline.

---

   ## Modernization (2025)
   
   This codebase was refactored for simple demonstration purposes:
   
   - **Architecture:** Restructured into domain-driven modules (core, lms, biometrics)
   - **DevOps:** Dockerized for consistent deployment
   - **Developer Experience:** Mock mode enables rapid development without ML dependencies

