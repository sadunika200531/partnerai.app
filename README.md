# AI Personal Server & Dev Monitor

A self-hosted monitoring system for personal infrastructure.

## Backend Setup
1. Navigate to `backend/` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run with Docker: `docker-compose up --build`

## Server Agent Setup
1. Copy `agent/` folder to target server.
2. Run `chmod +x install_agent.sh && ./install_agent.sh`

## Android Build Instructions
1. Ensure Java 17 is installed.
2. Navigate to `android/` directory.
3. Build APK: `./gradlew assembleDebug`
4. Find APK in `android/app/build/outputs/apk/debug/`.