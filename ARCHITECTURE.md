# System Architecture

## Overview
This document outlines the architecture of the `lmex` Django application, including its data models, URL routing, and deployment infrastructure.

## Infrastructure

The application is containerized for consistent deployment and dependency management.

### Containers
- **Web (`lmex-web`):**
    - **Base Image:** `python:3.11-slim`
    - **Port:** `8000`
    - **Dependencies:** Listed in `requirements.txt` (Core) + System libs (`libpq-dev`, `build-essential`).
    - **Command:** `gunicorn` or `runserver` via `entrypoint.sh`.
- **Database (`lmex-db`):**
    - **Image:** `postgres:15`
    - **Persistence:** Docker Volume `postgres_data`

### Environment
- Driven by `.env` file (see `.env.example`).
- `DEBUG` and `ALLOWED_HOSTS` are configurable.
- `SECRET_KEY` is externalized.

## Data Models (Schema)

### Core App (Users)
| Model | Description | Key Fields |
| :--- | :--- | :--- |
| `PersonalProfile` | Extended user profile. | `user` (OneToOne), `grade_level`, `school`, `mobile`, `p_color` |
| `NFT` | NFT ownership details. | `user` (OneToOne), `contract_address`, `token_id`, `image_ipfs_uri` |
| `Wallet` | User crypto wallet. | `user` (OneToOne), `wallet_address` |
| `WebCamUser` | Facial recognition data. | `user` (FK), `webcam_image`, `verified` (Bool) |
| `UserFaceEncoding` | Binary face encodings. | `user` (OneToOne), `face_encoding` (Binary) |
| `QRCode` / `QRScanEvent` | QR tracking. | `qrcode` (Image), `scan_timestamp`, `ip_address`, `city` |

### LMS App (Learning Management System)
| Model | Description | Key Fields |
| :--- | :--- | :--- |
| `Post` | User posts. | `user`, `content`, `image`, `video`, `unit` (Course Unit), `content_cost` (Token Gating) |
| `Reply` | Replies to posts. | `user`, `post`, `content` |
| `Unit` | Educational units. | `name` |
| `UserDebt` | Token economy. | `user`, `debt_amount` |

## Route Map (URLs)

### Core (`user_management/urls.py`)
- `/admin/` -> Django Admin
- `/` -> `users.urls` (Home, Auth)
- `/social/` -> `lms.urls`
- `/attendance/` -> `biometrics.urls`
- `/mint-nft/` -> NFT Minting View

### Critical Endpoints
- **Auth:** `/register/`, `/login/`, `/logout/`
- **NFT:** `/mint-nft/` (Requires `web3` libs - currently optional)
- **Webcam:** `/attendance/webcam_recognition/` (Requires `face_recognition` libs - currently optional)