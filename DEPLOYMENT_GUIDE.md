# Deployment Guide for Skincare Web App

Your application has been configured for one-click deployment to **[Render.com](https://render.com/)**, a modern cloud hosting platform. 

## What Was Changed
1. **Frontend API URL**: Changed from `http://127.0.0.1:8000/api` to `/api` so it dynamically connects to the correct domain when online.
2. **Production Web Server**: Added `gunicorn` to `backend/requirements.txt` to run your Python code reliably in production.
3. **Infrastructure Configuration**: Created `render.yaml`, an "Infrastructure as Code" file that tells Render exactly how to build and run your application automatically.

## How to Deploy

### Step 1: Push Your Code to GitHub
To use Render, your code must be on GitHub.
1. Create a free account on [GitHub](https://github.com/) if you don't have one.
2. Create a **New Repository**.
3. Open your terminal or command prompt in your project folder (`c:\Users\SARANYA M\OneDrive\Desktop\skincare_webapp`).
4. Run the following commands to upload your code:
```bash
git init
git add .
git commit -m "Ready for deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```
*(Make sure to replace the GitHub link above with your actual repository link)*

### Step 2: Connect to Render
1. Go to [Render.com](https://render.com/) and sign up using your GitHub account.
2. Once logged in, click on the **"New +"** button in the dashboard and select **"Blueprint"**.
3. Connect your GitHub account and select your new Skincare Web App repository.
4. Render will automatically detect the `render.yaml` file we created and set up your Web Service.
5. Click **"Apply"** or **"Approve"**.

### Step 3: Wait for Build
Render will now build your app and download the libraries in `requirements.txt`. Watch the logs until it says **"Live"**. You can then click the URL provided by Render (e.g., `https://skincare-webapp-abcd.onrender.com`) to view your live site!

> **Note on Free Tier:**
> Since this will use Render's Free tier, the server will "go to sleep" after 15 minutes of inactivity. The first time someone visits your site after it's asleep, it might take 30-50 seconds to wake back up. This is normal.
